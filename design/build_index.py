"""Build the deployable index.html from a design-canvas bundle export.

Media (images, video) leave the inline manifest and are served as static
files from assets/site/, named by content hash so the immutable cache
header on /assets is safe. Fonts and scripts stay inline.

Usage, from the repo root:
  python3 design/build_index.py design/canvas/index-TBWI-Website.html . design/canvas/hero-loop-h264.mp4
"""
import sys, json, re, base64, gzip, hashlib, os

src, repo, video_override = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding='utf-8').read()

def grab(kind):
    m = re.search(r'(<script type="__bundler/%s">\s*)(.*?)(\s*</script>)' % kind, t, re.S)
    return m, json.loads(m.group(2))

m_man, man = grab('manifest')
m_tpl, tpl = grab('template')

def sub1(old, new, s, count=1):
    n = s.count(old)
    assert n == count, (old[:80], n)
    return s.replace(old, new)

# ---- template fixes -------------------------------------------------------
TITLE = 'The Beauty and Wellness Institute | Dr. Pamela Chapman, Bradenton FL'
DESC = ('Functional medicine, medical weight loss, hormone therapy, peptides, IV therapy, '
        'injectables, and a day spa in Bradenton, Florida, all led by Dr. Pamela Chapman.')
HEAD = ('<title>%s</title>\n<meta name="description" content="%s">\n'
        '<meta name="theme-color" content="#26302D">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
        '<meta property="og:type" content="website">\n<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n') % (TITLE, DESC, TITLE, DESC)
tpl = sub1('<meta name="viewport" content="width=device-width, initial-scale=1">\n',
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + HEAD, tpl)

# Marquee listed IV Therapy twice and skipped Peptide Therapy (both copies of the loop).
iv = re.compile(r'<i data-lucide="droplet"([^>]*)></i>(<span[^>]*>)IV Therapy</span></div>(\s*<div[^>]*><i data-lucide="flower-2")')
tpl, n = iv.subn(r'<i data-lucide="dna"\1></i>\2Peptide Therapy</span></div>\3', tpl)
assert n == 2, n

# Mobile map: a !important height pinned the 3D plane at 420px inside a 250px box,
# so the flat map rose over the clinic text while scrolling in. The scroll handler
# already sizes the plane (420px cap on mobile).
tpl = sub1('      [data-area-plane] { height: 420px !important; }\n', '', tpl)

# Mobile map: the Anna Maria label hung off the left edge of the screen.
tpl = sub1('data-area-key="ami" data-side="right" data-mside="left"',
           'data-area-key="ami" data-side="right" data-mside="center"', tpl)

# Mobile process: scale(0.7) meant for the decorative rings also shrank the photo
# shade on steps 1, 4 and 5, leaving a grey box under the step counter.
tpl = sub1('[data-rs="proc"] [data-media] > div:last-child { transform: scale(0.7); }',
           '[data-rs="proc"] [data-media="1"] > div:last-child, [data-rs="proc"] [data-media="2"] > div:last-child { transform: scale(0.7); }', tpl)

# Pins respond to tap as well as hover.
tpl = sub1('Hover a pin to see', 'Hover or tap a pin to see', tpl, count=2)

# ---- service pillars (design/pillars.py) ----------------------------------
import pillars
tpl = sub1('<!-- ============ SERVICES (pinned horizontal) ============ -->',
           pillars.render() + '  <!-- ============ SERVICES (pinned horizontal) ============ -->', tpl)

# Pinned pillar steps: hook into the page's mount and scroll handler.
tpl = sub1("    this.procIdx = 0;\n", "    this.procIdx = 0;\n" + pillars.JS_INIT, tpl)
tpl = sub1("    // Pinned process steps\n", pillars.JS_SCROLL + "    // Pinned process steps\n", tpl)

# Navigation (design/nav.py): About, the three pillars, Patient Resources and
# the appointment button.
import nav
tpl, n = re.subn(r'<nav data-nav="".*?</nav>', lambda m: nav.desktop(), tpl, flags=re.S)
assert n == 1, n
mn = tpl.index('<div data-mnav=""')
seg_start = tpl.index('<nav style="display:flex; flex-direction:column; gap:22px">', mn)
seg_end = tpl.index('</nav>', seg_start) + len('</nav>')
tpl = tpl[:seg_start] + nav.mobile() + tpl[seg_end:]
tpl = sub1('justify-content:space-between; padding:110px 28px 40px;',
           'justify-content:flex-start; gap:32px; overflow-y:auto; overscroll-behavior:contain; padding:110px 28px 40px;', tpl)
tpl = sub1('hint-size="auto,38px">Book a Consultation</x-import>', 'hint-size="auto,38px">%s</x-import>' % nav.APPOINTMENT, tpl)
tpl = sub1('    ::selection {', nav.CSS.lstrip('\n') + '    ::selection {', tpl)
# Every dropdown opens on hover and keyboard focus, not just the first.
tpl = sub1("""    const dd = document.querySelector('[data-dd]');
    const ddp = document.querySelector('[data-dd-panel]');
    if (dd && ddp) {""", """    document.querySelectorAll('[data-dd]').forEach(dd => {
      const ddp = dd.querySelector('[data-dd-panel]');
      if (!ddp) return;""", tpl)
tpl = sub1("""      dd.addEventListener('focusin', open); dd.addEventListener('focusout', close);
    }""", """      dd.addEventListener('focusin', open); dd.addEventListener('focusout', close);
    });""", tpl)

# "Our Philosophy" lands on The Institute statement.
tpl = sub1('<section data-screen-label="The Institute"', '<section id="philosophy" data-screen-label="The Institute"', tpl)

# Footer: a Patient Resources column carries the Fullscript dispensary link.
tpl = sub1('grid-template-columns:1.4fr 1fr 1fr 1fr; gap:48px', 'grid-template-columns:1.4fr 1fr 1fr 1fr 1fr; gap:40px', tpl)
FOOT_LINK = ('<a href="%s"%s style="font-weight:400; font-size:0.9rem; color:rgba(236,240,238,0.72); text-decoration:none; '
             'transition:color 220ms var(--ease-standard)" style-hover="color:#F5F2EA">%s</a>')
FOOT_COL = ('<div>\n        <div style="font-weight:500; font-size:11.5px; letter-spacing:0.22em; text-transform:uppercase; '
            'color:var(--sage-300); margin-bottom:20px">Patient Resources</div>\n'
            '        <div style="display:flex; flex-direction:column; gap:13px">\n          %s\n        </div>\n      </div>\n      ') % \
           '\n          '.join([FOOT_LINK % (pillars.e(pillars.FULLSCRIPT_URL), ' target="_blank" rel="noopener"', 'Professional-Grade Supplements'),
                               FOOT_LINK % ('#book', '', 'Book a Consultation'),
                               FOOT_LINK % ('#faq', '', 'Patient FAQ')])
CONNECT = ('<div>\n        <div style="font-weight:500; font-size:11.5px; letter-spacing:0.22em; text-transform:uppercase; '
           'color:var(--sage-300); margin-bottom:20px">Connect</div>')
tpl = sub1(CONNECT, FOOT_COL + CONNECT.replace('>Connect<', '>Contact<'), tpl)

# Services column: the old eight-service list predates the pillars, so the
# column now links to the three pillars instead.
svc = re.compile(r'<div>\n        <div style="[^"]*">Services</div>\n        <div style="display:flex; flex-direction:column; gap:13px">\n.*?\n        </div>\n      </div>\n      ', re.S)
PILLAR_COL = ('<div>\n        <div style="font-weight:500; font-size:11.5px; letter-spacing:0.22em; text-transform:uppercase; '
              'color:var(--sage-300); margin-bottom:20px">Treatments</div>\n'
              '        <div style="display:flex; flex-direction:column; gap:13px">\n          %s\n        </div>\n      </div>\n      ') % \
             '\n          '.join(FOOT_LINK % ('#' + p['id'], '', pillars.e(p['title'])) for p in pillars.PILLARS)
tpl, n = svc.subn(lambda m: PILLAR_COL, tpl)
assert n == 1, n

# Contact column: Instagram and Facebook already appear as icons under the logo,
# so the column keeps the phone and the address (which opens directions).
tpl = re.sub(r'\n          <a href="https://www\.(instagram|facebook)\.com/[^"]*" target="_blank" rel="noopener" style="font-weight:400;[^\n]*</a>',
             '', tpl)
assert tpl.count('instagram.com') == 1 and tpl.count('facebook.com') == 1
ADDR = '<span style="font-weight:300; font-size:0.9rem; line-height:1.6; color:rgba(236,240,238,0.6)">6114 Manatee Ave W<br>Bradenton, FL 34209</span>'
tpl = sub1(ADDR, '<a href="https://www.google.com/maps/search/?api=1&amp;query=6114+Manatee+Ave+W,+Bradenton,+FL+34209" '
                 'target="_blank" rel="noopener" style="font-weight:300; font-size:0.9rem; line-height:1.6; '
                 'color:rgba(236,240,238,0.6); text-decoration:none; transition:color 220ms var(--ease-standard)" '
                 'style-hover="color:#F5F2EA">6114 Manatee Ave W<br>Bradenton, FL 34209</a>', tpl)

# ---- move media out of the inline manifest --------------------------------
outdir = os.path.join(repo, 'assets', 'site')
os.makedirs(outdir, exist_ok=True)
EXT = {'image/jpeg': 'jpg', 'image/png': 'png', 'video/mp4': 'mp4'}
for uuid in list(man):
    e = man[uuid]
    if e['mime'] not in EXT:
        continue
    b = base64.b64decode(e['data'])
    if e['compressed']:
        b = gzip.decompress(b)
    if e['mime'] == 'video/mp4':
        b = open(video_override, 'rb').read()  # H.264 re-encode of the HEVC export
    name = '%s.%s' % (hashlib.sha256(b).hexdigest()[:16], EXT[e['mime']])
    open(os.path.join(outdir, name), 'wb').write(b)
    assert uuid in tpl, uuid
    tpl = tpl.replace(uuid, '/assets/site/' + name)
    del man[uuid]

# ---- reassemble ------------------------------------------------------------
def enc(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\u002F')

out = t[:m_man.start(2)] + enc(man) + t[m_man.end(2):m_tpl.start(2)] + enc(tpl) + t[m_tpl.end(2):]
out = sub1('<title>Bundled Page</title>', HEAD.rstrip('\n').replace('\n', '\n  '), out)
open(os.path.join(repo, 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out.encode()), 'bytes; manifest entries left', len(man))
