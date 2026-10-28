"""Header navigation: desktop dropdowns and the mobile menu.

Every link points at an anchor on the homepage (ids come from the template,
build_index.py and pillars.py) except the Fullscript dispensary.
"""
from pillars import FULLSCRIPT_URL, e

# (top-level label, panel heading, [(link label, href)])
MENU = [
    ('About', 'About the Institute', [
        ('Meet Pamela Chapman, DO, DABOM', '#about'),
        ('Our Philosophy', '#philosophy'),
    ]),
    ('Aesthetics', 'Aesthetics & Regenerative Beauty', [
        ('Botox & Wrinkle Relaxers', '#wrinkle-relaxers'),
        ('Dermal Fillers', '#dermal-fillers'),
        ('Sculptra', '#dermal-fillers'),
        ('Kybella', '#dermal-fillers'),
        ('Skinvive', '#dermal-fillers'),
        ('Laser Skin Resurfacing', '#laser-resurfacing'),
        ('Hair Restoration', '#hair-restoration'),
    ]),
    ('Wellness', 'Medical Wellness & Weight Management', [
        ('Medical Weight Management', '#weight-management'),
        ('GLP-1 Treatment Options', '#weight-management'),
        ("Women's Hormone Therapy", '#womens-hormones'),
        ("Men's Testosterone Therapy", '#mens-hormones'),
    ]),
    ('Longevity', 'Longevity & IV Wellness', [
        ('IV Vitamin Therapy', '#iv-therapy'),
        ('NAD+ & Glutathione', '#iv-therapy'),
        ('Longevity & Peptide Consultations', '#peptides'),
        ('Professional-Grade Supplements', '#supplements'),
    ]),
    ('Patient Resources', 'Patient Resources', [
        ('Fullscript Supplement Dispensary', FULLSCRIPT_URL),
    ]),
]

APPOINTMENT = 'Request an Appointment'

CHEVRON = ('<svg width="10" height="10" sc-camel-view-box="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"></path></svg>')


def target(href):
    return ' target="_blank" rel="noopener"' if href.startswith('http') else ''


def desktop():
    out = []
    for n, (label, heading, links) in enumerate(MENU):
        side = 'right:-16px' if n == len(MENU) - 1 else 'left:-16px'
        items = ''.join(
            '\n                <a href="%s"%s style="display:block; padding:9px 12px; border-radius:10px; color:var(--ink-900); '
            'text-decoration:none; font-weight:400; font-size:0.92rem; line-height:1.35; transition:background 180ms var(--ease-standard)" '
            'style-hover="background:var(--sage-50)">%s</a>' % (e(h), target(h), e(t)) for t, h in links)
        out.append('''
          <div data-dd="" style="position:relative; display:flex; align-items:center">
            <a href="%(first)s" style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-body); font-weight:500; font-size:12.5px; letter-spacing:0.18em; text-transform:uppercase; color:#F7F4ED; text-shadow:0 1px 2px rgba(20,28,26,0.6), 0 2px 12px rgba(20,28,26,0.4); text-decoration:none; white-space:nowrap">%(label)s%(chev)s</a>
            <div data-dd-panel="" style="position:absolute; top:100%%; %(side)s; padding-top:18px; opacity:0; visibility:hidden; transform:translateY(6px); transition:opacity 200ms var(--ease-standard), transform 200ms var(--ease-standard), visibility 200ms">
              <div style="width:300px; padding:18px 10px 10px; border-radius:20px; background:rgba(251,250,246,0.97); backdrop-filter:blur(10px); box-shadow:var(--shadow-lg); border:1px solid var(--border-subtle); display:flex; flex-direction:column; gap:2px">
                <div style="padding:0 12px 10px; margin-bottom:4px; border-bottom:1px solid var(--border-subtle); font-weight:500; font-size:10.5px; letter-spacing:0.2em; text-transform:uppercase; color:var(--teal-600)">%(heading)s</div>%(items)s
              </div>
            </div>
          </div>''' % {'first': e(links[0][1]) if not links[0][1].startswith('http') else '#supplements',
                       'label': e(label), 'chev': CHEVRON, 'side': side, 'heading': e(heading), 'items': items})
    return '<nav data-nav="" style="display:flex; align-items:center; gap:24px">%s\n        </nav>' % ''.join(out)


def mobile():
    groups = []
    for label, heading, links in MENU:
        items = ''.join(
            '\n            <a href="%s"%s data-mnav-link="" style="font-weight:300; font-size:1.02rem; line-height:1.4; '
            'color:rgba(247,244,237,0.82); text-decoration:none">%s</a>' % (e(h), target(h), e(t)) for t, h in links)
        groups.append('''
        <details data-mnav-group="" style="border-bottom:1px solid rgba(247,244,237,0.14)">
          <summary style="display:flex; align-items:center; justify-content:space-between; gap:12px; padding:16px 0; cursor:pointer; list-style:none; font-family:var(--font-display); font-weight:500; font-size:1.55rem; line-height:1.2; color:#F5F2EA">%s%s</summary>
          <div style="display:flex; flex-direction:column; gap:14px; padding:2px 0 20px 2px">%s
          </div>
        </details>''' % (e(heading), CHEVRON.replace('width="10" height="10"', 'width="16" height="16"'), items))
    return ('<nav style="display:flex; flex-direction:column">%s\n        <a href="#book" data-mnav-link="" '
            'style="margin-top:28px; display:flex; align-items:center; justify-content:center; padding:0.9rem 1.6rem; border-radius:999px; '
            'background:var(--gold-300); color:#26302D; font-weight:500; font-size:0.85rem; letter-spacing:0.16em; text-transform:uppercase; '
            'text-decoration:none">%s</a>\n      </nav>') % (''.join(groups), e(APPOINTMENT))


CSS = '''
    [data-mnav-group] > summary::-webkit-details-marker { display: none; }
    [data-mnav-group] > summary svg { transition: transform 220ms var(--ease-standard); flex-shrink: 0; }
    [data-mnav-group][open] > summary svg { transform: rotate(180deg); }
    @media (max-width: 1560px) { [data-nav-phone] { display: none !important; } }
    @media (max-width: 1180px) { [data-nav] { gap: 16px !important; } [data-nav] [data-dd] > a { letter-spacing: 0.12em !important; font-size: 12px !important; } }
    @media (max-width: 1024px) { [data-menu-btn] { display: inline-flex !important; } [data-nav] { display: none !important; } }
'''
