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

# Header menu: the three pillars sit above the service list.
DD_LINK = ('<a href="#%s" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border-radius:12px; '
           'color:var(--teal-700); text-decoration:none; font-weight:500; font-size:0.78rem; letter-spacing:0.12em; '
           'text-transform:uppercase; transition:background 180ms var(--ease-standard)" style-hover="background:var(--sage-50)">'
           '<i data-lucide="%s" style="width:15px; height:15px; color:var(--gold-500)"></i>%s</a>')
DD_ROW = ('<div style="grid-column:1 / -1; display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:4px; '
          'padding-bottom:8px; margin-bottom:6px; border-bottom:1px solid var(--border-subtle)">%s</div>' %
          ''.join(DD_LINK % x for x in [('aesthetics', 'sparkles', 'Aesthetics'), ('wellness', 'heart-pulse', 'Medical Wellness'),
                                        ('longevity', 'droplets', 'Longevity &amp; IV')]))
tpl = sub1('display:grid; grid-template-columns:1fr 1fr; gap:4px">',
           'display:grid; grid-template-columns:1fr 1fr; gap:4px">\n                ' + DD_ROW, tpl)

MNAV = ('<a href="#%s" data-mnav-link="" style="font-family:var(--font-display); font-weight:500; font-size:1.9rem; '
        'line-height:1.15; color:#F5F2EA; text-decoration:none">%s</a>\n        ')
tpl = sub1('<a href="#about" data-mnav-link=""', MNAV % ('pillars', 'Treatments') + '<a href="#about" data-mnav-link=""', tpl)

# Footer: a Patient Resources column carries the Fullscript dispensary link.
tpl = sub1('grid-template-columns:1.4fr 1fr 1fr 1fr; gap:48px', 'grid-template-columns:1.4fr 1fr 1fr 1fr 1fr; gap:40px', tpl)
FOOT_LINK = ('<a href="%s"%s style="font-weight:400; font-size:0.9rem; color:rgba(236,240,238,0.72); text-decoration:none; '
             'transition:color 220ms var(--ease-standard)" style-hover="color:#F5F2EA">%s</a>')
FOOT_COL = ('<div>\n        <div style="font-weight:500; font-size:11.5px; letter-spacing:0.22em; text-transform:uppercase; '
            'color:var(--sage-300); margin-bottom:20px">Patient Resources</div>\n'
            '        <div style="display:flex; flex-direction:column; gap:13px">\n          %s\n        </div>\n      </div>\n      ') % \
           '\n          '.join([FOOT_LINK % (pillars.e(pillars.FULLSCRIPT_URL), ' target="_blank" rel="noopener"', 'Professional-Grade Supplements'),
                               FOOT_LINK % ('#book', '', 'Book a Consultation'),
                               FOOT_LINK % ('#faq', '', 'Patient FAQ'),
                               FOOT_LINK % ('tel:9415547546', '', 'Call the Clinic')])
CONNECT = ('<div>\n        <div style="font-weight:500; font-size:11.5px; letter-spacing:0.22em; text-transform:uppercase; '
           'color:var(--sage-300); margin-bottom:20px">Connect</div>')
tpl = sub1(CONNECT, FOOT_COL + CONNECT, tpl)

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
