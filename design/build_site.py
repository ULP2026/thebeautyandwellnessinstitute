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

BADGE_ALT = 'Peer-Selected 2026 SRQ Top Doctor, Family Medicine'
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

    # One alt text for the SRQ badge everywhere.
    tpl, n = re.subn(r'alt="(?:2026 SRQ Top Doctors, Peer Review|Peer-Selected 2026 SRQ Top Doctor, Family Medicine)"',
                     'alt="%s"' % BADGE_ALT, tpl)
    assert n, name

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
    return tpl


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
        open(os.path.join(outdir, name), 'wb').write(b)
        assert uuid in tpl, (src, uuid)
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
