"""Build the deployable pages from the design-canvas bundle exports.

Each export in design/canvas/ becomes one page. Media (images, video) leave
the inline manifest and are served from assets/site/, named by content hash
so the immutable cache header on /assets is safe. Fonts and scripts stay
inline. Links between the exports are rewritten to clean URLs.

Usage, from the repo root:
  python3 design/build_site.py
"""
import base64, gzip, hashlib, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVAS = os.path.join(ROOT, 'design', 'canvas')
HERO_H264 = os.path.join(CANVAS, 'hero-loop-h264.mp4')  # H.264 re-encode of the HEVC hero

# Export file -> (output file, clean URL). vercel.json has cleanUrls on.
PAGES = {
    'TBWI-Home.html': ('index.html', '/'),
    'TBWI-Aesthetics.html': ('aesthetics.html', '/aesthetics'),
    'TBWI-Medical-Wellness.html': ('medical-wellness.html', '/medical-wellness'),
    'TBWI-Longevity.html': ('longevity.html', '/longevity'),
    'TBWI-Privacy-Policy.html': ('privacy-policy.html', '/privacy-policy'),
    'TBWI-Medical-Disclaimer.html': ('medical-disclaimer.html', '/medical-disclaimer'),
}

# Appointment requests go to the practice's Jotform. Some exports still carry
# a placeholder for it. Fullscript goes to the Fullscript home page, where
# patients can sign in, until the dispensary link arrives.
JOTFORM_URL = 'https://form.jotform.com/251495476973069'
FULLSCRIPT_URL = 'https://fullscript.com/'

DESC_RE = re.compile(r'<meta name="description" content="([^"]*)">')


def fix(tpl, name):
    """Copy, link and display fixes applied to every page."""
    def sub(old, new, count=None):
        nonlocal tpl
        n = tpl.count(old)
        assert n and (count is None or n == count), (name, old[:60], n)
        tpl = tpl.replace(old, new)

    # Links between pages and placeholder links.
    for src, (_, url) in PAGES.items():
        tpl = tpl.replace('href="%s#' % src, 'href="%s#' % url.rstrip('/') if url != '/' else 'href="/#')
        tpl = tpl.replace('href="%s"' % src, 'href="%s"' % url)
    tpl = tpl.replace('https://form.jotform.com/YOUR-FORM-ID', JOTFORM_URL)
    assert JOTFORM_URL in tpl, name
    # Footer legal links: older exports pointed them at the footer itself.
    tpl = re.sub(r'<a href="#contact"( style="[^"]*">Privacy Policy</a>)', r'<a href="/privacy-policy"\1', tpl)
    tpl = re.sub(r'<a href="#medical-disclaimer"( style="[^"]*">Medical Disclaimer</a>)', r'<a href="/medical-disclaimer"\1', tpl)
    assert re.search(r'href="/privacy-policy"[^>]*>Privacy Policy</a>', tpl) and \
        re.search(r'href="/medical-disclaimer"[^>]*>Medical Disclaimer</a>', tpl), name
    sub('https://us.fullscript.com/welcome/YOUR-DISPENSARY', FULLSCRIPT_URL)
    assert 'TBWI-' not in re.sub(r'<title>.*?</title>', '', tpl).replace('TBWI-logo', ''), name

    # Name style: "Dr." and "DO" together double up the title, so the
    # credentialed form is "Pamela Chapman, DO, DABOM".
    sub('Dr. Pamela Chapman, DO, DABOM', 'Pamela Chapman, DO, DABOM')
    if name == 'TBWI-Home.html':
        sub('>Dr. Pamela Chapman<', '>Pamela Chapman<', 1)  # credentials sit on the line below
    assert 'Dr. Pamela Chapman' not in re.sub(r'/\*.*?\*/', '', tpl, flags=re.S), name  # CSS comments aside

    # Header: no Contact link in the desktop menu or the phone menu. The
    # footer keeps its Contact column.
    tpl, n = re.subn(r'\n[ \t]*<a href="#contact"(?: data-mnav-link="")? style="[^"]*">Contact</a>', '', tpl)
    assert n == 2, (name, n)

    # Phones: the header appointment button is meant to hide (the menu has its
    # own), but the rule looked for href="#book" and the button now goes to the
    # form, so it stayed and pushed the menu button off screen.
    sub('[data-header-inner] > div:last-child > a[href="#book"] { display: none !important; }',
        '[data-header-inner] > div:last-child > a:last-child { display: none !important; }', 1)

    # Footer: no SRQ badge (it scrolls in the homepage logo strip) and no
    # short disclaimer paragraph (the Medical Disclaimer page covers it).
    tpl, n = re.subn(r'\n[ \t]*<div style="display:flex; align-items:center; gap:12px; margin-top:22px">\s*'
                     r'<span[^>]*><img[^>]*alt="2026 SRQ Top Doctors, Peer Review"[^>]*></span>\s*'
                     r'<span[^>]*>Peer-Selected 2026 SRQ Top Doctor, Family Medicine</span>\s*</div>', '', tpl)
    assert n == 1, (name, 'badge', n)
    tpl, n = re.subn(r'\n[ \t]*<p id="medical-disclaimer"[^>]*><strong[^>]*>Medical disclaimer\.</strong>[^<]*</p>', '', tpl)
    assert n == 1, (name, 'disclaimer', n)

    # Internal review tags read as unfinished on a live page. The copy beside
    # them already says these options are only discussed at consultation; the
    # pending-review status is tracked in the PR and in this comment.
    if 'Pending regulatory review' in tpl:
        sub('>Pending regulatory review</span>',
            '><!-- PENDING REGULATORY REVIEW -->Consultation required</span>')

    if name != 'TBWI-Home.html':
        # Phones: the shared "#top { min-height: 100svh }" is for the homepage
        # hero. On the inner pages it stretched the hero to a full screen, so
        # the breadcrumb sat mid-screen with empty space or photo under it.
        sub('      #top[data-screen-label="Hero"] { border-radius: 0 0 22px 22px !important; }\n',
            '      #top[data-screen-label="Hero"] { border-radius: 0 0 22px 22px !important; }\n'
            '      #top { min-height: 0 !important; }\n', 1)

    if name == 'TBWI-Aesthetics.html':
        # Not every option is "placed" (laser, hair restoration), and who
        # performs each treatment varies; the physician designs the plan.
        sub('Each option is selected and placed by a physician, with results that look like you.',
            'Every treatment plan is designed by a physician, with results that look like you.', 1)

    if name == 'TBWI-Longevity.html':
        # Patient Resources: the online shop isn't open yet, so the button
        # goes to the contact details in the footer, with a "coming soon"
        # tag beside it (it wraps below the button on narrow screens).
        sub('          <div style="margin-top:28px">\n'
            '            <a href="%s" target="_blank" rel="noopener" style="text-decoration:none">\n'
            '              <x-import component-from-global-scope="TBWIDesignSystem_4a5da9.Button" variant="gold" size="md" hint-size="auto,44px">Shop Professional-Grade Supplements</x-import>\n'
            '            </a>\n'
            '          </div>\n' % FULLSCRIPT_URL,
            '          <div style="margin-top:28px; display:flex; flex-wrap:wrap; align-items:center; gap:14px 18px">\n'
            '            <a href="#contact" style="text-decoration:none">\n'
            '              <x-import component-from-global-scope="TBWIDesignSystem_4a5da9.Button" variant="gold" size="md" hint-size="auto,44px">Contact Us</x-import>\n'
            '            </a>\n'
            '            <span style="display:inline-flex; align-items:center; gap:9px; max-width:100%; padding:10px 16px; border-radius:999px; '
            'background:rgba(247,244,237,0.08); border:1px solid rgba(247,244,237,0.22)">'
            '<i data-lucide="shopping-bag" style="width:15px; height:15px; flex-shrink:0; color:var(--gold-300)"></i>'
            '<span style="font-weight:500; font-size:11px; line-height:1.4; letter-spacing:0.14em; text-transform:uppercase; '
            'color:rgba(247,244,237,0.9)">Online Shop Coming Soon</span></span>\n'
            '          </div>\n', 1)

    if name == 'TBWI-Home.html':
        # Pins respond to tap as well as hover.
        sub('Hover a pin to see', 'Hover or tap a pin to see', 2)
        # Mobile map: a !important height pinned the 3D plane at 420px inside a
        # 250px box, so the flat map rose over the clinic text while scrolling in.
        sub('      [data-area-plane] { height: 420px !important; }\n', '', 1)
        # Mobile process: the scale meant for decorative rings also shrank the
        # photo shade, leaving a grey box under the step counter.
        sub('      [data-rs="proc"] [data-media] > div:last-child { transform: scale(0.7); }\n', '', 1)
        # Map: Palma Sola is on the mainland across the bay from Bradenton
        # Beach, not south of it by Longboat Pass. Its label opens to the right,
        # away from the island labels.
        sub('data-area-key="palma" data-side="center" data-mside="center" role="button" tabindex="0" aria-label="Palma Sola" '
            'style="position:absolute; left:29%; top:38%;',
            'data-area-key="palma" data-side="right" data-mside="right" role="button" tabindex="0" aria-label="Palma Sola" '
            'style="position:absolute; left:36.5%; top:39%;', 1)
        # Phones: the island labels piled onto each other and the clinic label.
        # Only the clinic and the tapped pin show a name; the rest show the pin.
        sub('      [data-area-map] { height: 250px !important; }\n',
            '      [data-area-map] { height: 250px !important; }\n'
            '      [data-area-pin]:not(.is-on):not([data-area-key="clinic"]) [data-pin-name] { display: none !important; }\n', 1)
        # About photo: no Top Doctor badge on the portrait (it stays in the footer).
        tpl, n = re.subn(r'\n[ \t]*<span data-fig-badge="".*?</span>(?=\n)', '', tpl, count=1, flags=re.S)
        assert n == 1, name
        # "More than a medspa" marquee: affiliation and recognition logos in
        # place of the service tiles.
        tpl, n = re.subn(r'(<div data-marquee="" style="[^"]*">).*?(\n      </div>\n    </div>)',
                         lambda m: m.group(1) + logo_marquee() + m.group(2), tpl, count=1, flags=re.S)
        assert n == 1, name
        # The logo loop is longer than the old tile loop; 56s keeps it at about
        # the old pace (~55px/s) instead of rushing.
        sub('animation:tbwiMarqueeL 32s linear infinite', 'animation:tbwiMarqueeL 56s linear infinite', 1)
        sub('(this.props.marqueeSpeed ?? 32)', '(this.props.marqueeSpeed ?? 56)', 1)
        sub('&quot;default&quot;: 32, &quot;tsType&quot;: &quot;number&quot;, &quot;section&quot;: &quot;Motion&quot;',
            '&quot;default&quot;: 56, &quot;tsType&quot;: &quot;number&quot;, &quot;section&quot;: &quot;Motion&quot;', 1)
        sub('      [data-marq-wrap] { margin-top: 44px !important; }\n',
            '      [data-marq-wrap] { margin-top: 44px !important; --logo-scale: 0.72; }\n', 1)

    if name == 'TBWI-Home.html':
        # Reviews: the four real patient reviews in place of the design's
        # placeholder testimonials. Wording is verbatim apart from one typo
        # ("Chapamn"). No reviewer location or treatment is claimed beyond
        # what the review itself says.
        sub('Kind words from patients in Northwest Bradenton, Anna Maria Island, and beyond. Individual results vary.',
            'Kind words from our patients. Individual results vary.', 1)
        for (old_ini, old_name, old_label, old_title, old_quote), (ini, who, title, quote) in zip(OLD_REVIEWS, REVIEWS):
            sub('>%s</span>' % old_ini, '>%s</span>' % ini, 1)
            sub('>%s</span>' % old_name, '>%s</span>' % who, 1)
            sub('>%s</span>' % old_label, '>TBWI patient</span>', 1)
            sub('>%s</div>' % old_title, '>%s</div>' % e(title), 1)
            sub('>%s</p>' % old_quote, '>“%s”</p>' % e(quote), 1)
        # These reviews run longer than the placeholders; slightly smaller
        # type keeps the fanned cards compact.
        a, b = tpl.index('<section id="reviews"'), tpl.index('</section>', tpl.index('<section id="reviews"'))
        part = tpl[a:b]
        assert part.count('font-size:1.35rem; line-height:1.2') == 4 and part.count('font-size:0.9rem; line-height:1.6') == 4, name
        part = part.replace('font-size:1.35rem; line-height:1.2', 'font-size:1.12rem; line-height:1.25')
        part = part.replace('font-size:0.9rem; line-height:1.6', 'font-size:0.84rem; line-height:1.55')
        tpl = tpl[:a] + part + tpl[b:]
        # Fan spacing: full-length reviews were hidden where the cards
        # overlapped, so the fan opens wider (no overlap on desktop) and tilts
        # less. The script still narrows it on smaller screens.
        for old, new in [('data-rot="-11" data-x="-390" data-y="34"', 'data-rot="-6" data-x="-486" data-y="22"'),
                         ('data-rot="-4" data-x="-130" data-y="6"', 'data-rot="-2" data-x="-162" data-y="4"'),
                         ('data-rot="4" data-x="130" data-y="6"', 'data-rot="2" data-x="162" data-y="4"'),
                         ('data-rot="11" data-x="390" data-y="34"', 'data-rot="6" data-x="486" data-y="22"')]:
            sub(old, new, 1)
        # Narrow the fan so the outer cards (half width 150px, plus tilt) stay
        # on screen: the outer card's offset is scaled to fit the viewport.
        sub('const k = Math.max(0.42, Math.min(1, (w - 300) / 780));',
            'const k = Math.max(0.42, Math.min(1, (window.innerWidth / 2 - 180) / 486));', 1)

    # Footer: the About link is named for the section it opens.
    foot = tpl.index('<footer')
    tail, n = re.subn(r'>Meet Pamela Chapman, DO, DABOM</a>', '>About &amp; Our Philosophy</a>', tpl[foot:])
    assert n == 1, (name, n)
    tpl = tpl[:foot] + tail
    return tpl


from html import escape as e

# Homepage reviews: (initial, name, headline, quote), from the practice's
# published patient reviews.
REVIEWS = [
    ('J', 'Julia', 'Dr. Chapman really takes the time to listen.',
     'Dr. Chapman really takes the time to listen to you and I feel that she really hears what my concerns are. '
     'She offers natural solutions for weight loss and regulating hormones (as well as other issues). I love the '
     'idea that I can feel in control of my health and wellness. I highly recommend Dr. Chapman.'),
    ('D', 'Deardra', 'One of the best doctors that I have seen.',
     'Dr. Chapman is one of the best doctors that I have seen since moving to Florida in 2014. She is patient, '
     'well informed and listens to her patients and their concerns. I have recommended her to several friends.'),
    ('J', 'Jennifer', 'Dr. Chapman has been great.',
     'I’ve gone to her for injectables, advice, and functional medicine. The functional medicine is very thorough. '
     'It takes a while to get going, but once the process starts she really gives her full attention and seems '
     'like she actually cares about trying to “fix” you.'),
    ('A', 'Ashley', 'Highly recommend Dr. Chapman!',
     'She is very comforting & friendly and takes the time to listen to your needs and present recommendations. '
     'I had never received a Botox treatment and she was very conservative with her approach, which I appreciated. '
     'I have been very pleased with the results!'),
]
# The design export's placeholder cards, in fan order.
OLD_REVIEWS = [
    ('SM', 'Sarah M.', 'Aesthetics patient, Anna Maria Island', 'Natural, and finally me.',
     '“She took time to understand the whole picture. My results look natural, and I feel like myself again.”'),
    ('RT', 'Rebecca T.', 'Medical weight management patient', 'Energy I forgot I had.',
     '“The program changed my energy, my sleep, my skin. I only wish I had started sooner.”'),
    ('DK', 'Daniel K.', 'Hormone therapy patient', 'Care that actually listens.',
     '“Every visit feels unhurried. The labs explained things no one else had, and the plan finally made sense.”'),
    ('LP', 'Lauren P.', 'IV wellness patient, Holmes Beach', 'An hour that resets the week.',
     '“Calm, beautiful, and never rushed. The IV lounge has become my favorite reset.”'),
]


# Logos for the homepage marquee, in design/logos/: single-colour renders in
# the section's heading colour (#E7EBDF) with transparent backgrounds, made
# from the supplied artwork without stretching. Heights follow equal visual
# area (height = sqrt(AREA / aspect)), capped so the square badge doesn't tower.
LOGOS = [
    ('aafp.png', 'American Academy of Family Physicians'),
    ('acofp.png', 'American College of Osteopathic Family Physicians'),
    ('ifm.png', 'The Institute for Functional Medicine'),
    ('srq-2026.png', 'Peer-Selected 2026 SRQ Top Doctor, Family Medicine'),
    ('srq-2020.png', 'SRQ Magazine Top Doctors Peer Review 2020 Honoree'),
]
LOGO_AREA, LOGO_MAX_H = 6400, 70


def asset(path):
    b = open(path, 'rb').read()
    name = '%s%s' % (hashlib.sha256(b).hexdigest()[:16], os.path.splitext(path)[1])
    open(os.path.join(ROOT, 'assets', 'site', name), 'wb').write(b)
    return '/assets/site/' + name


def logo_marquee():
    from PIL import Image
    items = []
    for f, alt in LOGOS:
        path = os.path.join(ROOT, 'design', 'logos', f)
        w, h = Image.open(path).size
        height = min(LOGO_MAX_H, round((LOGO_AREA * h / w) ** 0.5))
        items.append((asset(path), alt, height, round(height * w / h)))

    def logo(src, alt, height, width, hidden):
        return ('<img src="%s" alt="%s" width="%d" height="%d" loading="eager" decoding="async" '
                'style="height:calc(%dpx * var(--logo-scale, 1)); width:auto; flex-shrink:0; display:block; opacity:0.92"%s>'
                ) % (src, '' if hidden else alt, width, height, height, ' aria-hidden="true"' if hidden else '')

    # Each half of the loop repeats the five logos three times, so a half is
    # wider than any screen and the -50% loop never shows a gap.
    def half(hidden):
        return ('\n        <div data-logo-set="" style="display:flex; align-items:center; gap:76px; padding-right:76px">%s\n        </div>'
                % ''.join('\n          ' + logo(*it, hidden=hidden or r > 0) for r in range(3) for it in items))
    return half(False) + half(True)


def head(tpl, url):
    """Favicon, theme color, canonical and Open Graph tags from the page's own title and description."""
    title = re.search(r'<title>(.*?)</title>', tpl, re.S).group(1).strip()
    desc = DESC_RE.search(tpl).group(1)
    tags = ('<meta name="theme-color" content="#26302D">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            '<link rel="canonical" href="https://thebeautyandwellnessinstitute.com%s">\n'
            '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n'
            '<meta property="og:description" content="%s">\n') % (url, title, desc)
    return tags, title, desc


def build(src, out, url):
    t = open(os.path.join(CANVAS, src), encoding='utf-8').read()

    def grab(kind):
        m = re.search(r'(<script type="__bundler/%s">\s*)(.*?)(\s*</script>)' % kind, t, re.S)
        return m, json.loads(m.group(2))

    m_man, man = grab('manifest')
    m_tpl, tpl = grab('template')
    tpl = fix(tpl, src)
    tags, title, desc = head(tpl, url)
    tpl = tpl.replace('</title>\n', '</title>\n' + tags, 1) if '</title>\n' in tpl else tpl.replace('</title>', '</title>\n' + tags, 1)

    outdir = os.path.join(ROOT, 'assets', 'site')
    os.makedirs(outdir, exist_ok=True)
    ext = {'image/jpeg': 'jpg', 'image/png': 'png', 'video/mp4': 'mp4'}
    for uuid in list(man):
        e = man[uuid]
        if e['mime'] not in ext:
            continue
        b = base64.b64decode(e['data'])
        if e['compressed']:
            b = gzip.decompress(b)
        if e['mime'] == 'video/mp4':
            b = open(HERO_H264, 'rb').read()
        name = '%s.%s' % (hashlib.sha256(b).hexdigest()[:16], ext[e['mime']])
        if uuid in tpl:  # media the fixes removed (the footer badge) is dropped
            open(os.path.join(outdir, name), 'wb').write(b)
            tpl = tpl.replace(uuid, '/assets/site/' + name)
        del man[uuid]

    def enc(o):
        return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\u002F')

    html = t[:m_man.start(2)] + enc(man) + t[m_man.end(2):m_tpl.start(2)] + enc(tpl) + t[m_tpl.end(2):]
    # The loader page shown before the bundle unpacks gets the same head tags.
    loader_title = re.search(r'<title>.*?</title>', html[:m_man.start(2)], re.S).group(0)
    html = html.replace(loader_title, '%s\n  <meta name="description" content="%s">\n  %s' % (
        loader_title, desc, tags.rstrip('\n').replace('\n', '\n  ')), 1)
    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(html)
    print(out, len(html.encode()), 'bytes; manifest entries left', len(man))


if __name__ == '__main__':
    for src, (out, url) in PAGES.items():
        build(src, out, url)
