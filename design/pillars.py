"""The three service pillars, rendered as one homepage section.

build_index.py inserts render() ahead of the services marquee and links the
header menu, mobile menu and footer to the anchors defined here (#pillars,
#aesthetics, #wellness, #longevity, #supplements).

Copy rules for this section: no efficacy claims, no unapproved product
presented as an established therapy. Items marked with a note number carry
a footnote; keep those notes when editing.
"""
from html import escape

# Dr. Chapman's Fullscript dispensary. Replace with the direct dispensary link
# (it looks like https://us.fullscript.com/welcome/<name>) once she sends it.
FULLSCRIPT_URL = 'https://fullscript.com/'

AESTHETICS = [
    {
        'id': 'laser-resurfacing', 'title': 'Laser Skin Resurfacing', 'featured': True,
        'desc': 'Resurfacing protocols matched to your skin, your goals, and the downtime you can plan around.',
        'items': ['CO2 laser resurfacing', 'Erbium laser resurfacing',
                  'Fractional laser resurfacing protocols, as appropriate',
                  'Treatment of fine lines, wrinkles, and uneven skin texture'],
    },
    {
        'id': 'hair-restoration', 'title': 'Hair Restoration', 'featured': True,
        'desc': 'Physician-guided options for thinning hair, chosen after a careful look at your history and scalp health.',
        'items': ['Microneedling for hair restoration',
                  'Platelet-Rich Plasma (PRP) hair restoration',
                  ('AnteAGE MD exosome-based treatments', 1)],
    },
    {
        'id': 'wrinkle-relaxers', 'title': 'Wrinkle Relaxers', 'eyebrow': 'Neuromodulators',
        'desc': 'Softens expression lines while keeping your face expressive and recognizably you.',
        'items': ['Botox Cosmetic', 'Dysport', 'Jeuveau', 'Daxxify'],
    },
    {
        'id': 'dermal-fillers', 'title': 'Dermal Fillers & Facial Rejuvenation',
        'desc': 'Restores volume and balance with a measured hand, in service of facial harmony.',
        'items': ['Hyaluronic acid dermal fillers', 'Lip enhancement',
                  'Facial balancing and volume restoration',
                  'Sculptra collagen biostimulation',
                  'Skinvive injectable skin hydration',
                  'Kybella for submental fat reduction'],
    },
]

WELLNESS = [
    {
        'id': 'weight-management', 'title': 'Medical Weight Management', 'featured': True,
        'eyebrow': 'Led by a board-certified Obesity Medicine physician',
        'desc': 'Weight care grounded in obesity medicine: a metabolic evaluation first, then a plan built for your body and designed to last.',
        'items': ['Physician-supervised medical weight management',
                  'GLP-1 medication options, when clinically appropriate',
                  'Semaglutide and tirzepatide options, as applicable',
                  'Metabolic health evaluations',
                  'Personalized weight management plans',
                  'Long-term weight management and maintenance'],
    },
    {
        'id': 'womens-hormones', 'title': "Women's Hormonal Health",
        'desc': 'Clear answers and steady support through perimenopause, menopause, and the changes around them.',
        'items': ['Perimenopause and menopause consultations',
                  'Hormone replacement therapy (HRT)',
                  'Individualized hormonal evaluations',
                  'Ongoing treatment and monitoring'],
    },
    {
        'id': 'mens-hormones', 'title': "Men's Hormonal Health",
        'desc': 'A thorough evaluation of energy, body composition, and testosterone, with treatment only when it is indicated.',
        'items': ['Testosterone replacement therapy (TRT)',
                  'Low testosterone evaluations',
                  'Testosterone deficiency management',
                  'Ongoing treatment and monitoring'],
    },
]

LONGEVITY = [
    {
        'id': 'iv-therapy', 'title': 'IV Vitamin Therapy', 'eyebrow': 'The IV Lounge',
        'desc': 'Our IV Lounge uses vitamin infusion protocols from Olympia Pharmaceuticals, selected after a review of your health history.',
        'items': ['IV hydration', 'Vitamin and nutrient infusion protocols',
                  'NAD+ treatments', 'Glutathione treatments',
                  'Vitamin B12 injections',
                  'Additional vitamin and wellness injections'],
    },
    {
        'id': 'peptides', 'title': 'Longevity & Peptide Treatments',
        'desc': 'An evidence-informed conversation about healthy aging, starting with an individual medical consultation.',
        'items': ['NAD+', 'Glutathione', ('BPC-157', 2), ('GLOW peptide protocols', 2),
                  ('Additional peptide options, as appropriate', 2)],
    },
]

NOTES = {
    1: ('Exosome-based products are not FDA-approved to treat hair loss. Availability is '
        'subject to regulatory review, and suitability is discussed at consultation.'),
    2: ('Some peptide therapies are investigational and are not FDA-approved drugs. We '
        'discuss them only within an individual medical consultation, where clinically '
        'appropriate, and make no claims about their effectiveness.'),
}


PILLARS = [
    {
        'id': 'aesthetics', 'num': '01', 'bg': 'var(--sage-100)', 'title': 'Aesthetics & Regenerative Beauty',
        'photo': '/assets/site/e8a35dd0aaaaceea.jpg', 'pos': '50% 30%',
        'alt': 'Aesthetic injectable treatment at The Beauty and Wellness Institute',
        'lede': ('Sophisticated aesthetic treatment with natural-looking results. We plan for facial harmony, '
                 'collagen support, and healthy skin, with every treatment plan built around your face and your goals.'),
        'rows': AESTHETICS, 'badge': 'Now expanding', 'notes': [1],
    },
    {
        'id': 'wellness', 'num': '02', 'bg': 'var(--teal-100)', 'title': 'Medical Wellness & Weight Management',
        'photo': '/assets/site/f47b063bbf9ba2da.jpg', 'pos': '42% 55%',
        'alt': 'Physician-supervised medical weight management consultation',
        'lede': ('A physician-led approach to hormonal health, metabolic wellness, and medical weight management, '
                 'for men and women noticing changes in energy, body composition, or overall well-being. '
                 'Evidence-based treatment, individualized care, sustainable results.'),
        'rows': WELLNESS, 'badge': 'Obesity Medicine', 'credential': True,
        'fine': ('Prescription medications, including GLP-1 and hormone therapies, are prescribed only after a '
                 'medical evaluation and only when clinically appropriate. Results vary by individual.'),
    },
    {
        'id': 'longevity', 'num': '03', 'bg': '#EEE6D6', 'title': 'Longevity & IV Wellness',
        'photo': '/assets/site/d3e70d35718af6ca.jpg', 'pos': '50% 50%',
        'alt': 'The IV Lounge at The Beauty and Wellness Institute',
        'lede': ('Our IV Lounge, nutrient therapies, and personalized longevity care, each starting with an '
                 'individual medical consultation and an evidence-informed approach to healthy aging.'),
        'rows': LONGEVITY, 'notes': [2], 'supplements': True,
    },
]


def e(s):
    return escape(s, quote=True)


def eyebrow(text):
    return ('<div style="display:flex; align-items:center; gap:10px">'
            '<span style="width:6px; height:6px; background:var(--teal-500); border-radius:1px"></span>'
            '<span style="font-weight:500; font-size:12px; letter-spacing:0.22em; text-transform:uppercase; color:var(--teal-600)">%s</span>'
            '</div>') % e(text)


def item(it):
    text, note = (it, None) if isinstance(it, str) else it
    sup = '<sup style="font-size:0.7em; color:var(--teal-600)">%d</sup>' % note if note else ''
    return ('<li style="display:flex; gap:10px; align-items:baseline; font-weight:300; font-size:0.9rem; line-height:1.45; color:var(--ink-700)">'
            '<span aria-hidden="true" style="flex-shrink:0; width:5px; height:5px; border-radius:1px; background:var(--sage-500); transform:translateY(-2px)"></span>'
            '<span>%s%s</span></li>') % (e(text), sup)


def badge(text, icon):
    return ('<span style="display:inline-flex; align-items:center; gap:6px; margin-bottom:8px; font-weight:500; font-size:10px; letter-spacing:0.2em; '
            'text-transform:uppercase; color:var(--gold-700); white-space:nowrap">'
            '<i data-lucide="%s" style="width:12px; height:12px; color:var(--gold-500)"></i>%s</span>') % (icon, e(text))


def category(c, p):
    tag = ''
    if c.get('featured') and p.get('badge'):
        tag = badge(p['badge'], 'badge-check' if p.get('credential') else 'trending-up')
    sub = ''
    if c.get('eyebrow') and not c.get('featured'):
        sub = ('<span style="display:block; margin-top:4px; font-weight:500; font-size:10px; letter-spacing:0.18em; '
               'text-transform:uppercase; color:var(--teal-600)">%s</span>') % e(c['eyebrow'])
    return (
        '<div data-tcat="" style="min-width:0">%s'
        '<h4 style="margin:0; font-family:var(--font-display); font-weight:600; font-size:1.4rem; line-height:1.2; color:var(--ink-900)">%s</h4>%s'
        '<ul style="list-style:none; margin:12px 0 0; padding:0; display:flex; flex-direction:column; gap:6px">%s</ul>'
        '</div>'
    ) % (('<div>%s</div>' % tag) if tag else '', e(c['title']), sub, ''.join(item(x) for x in c['items']))


def credential():
    return (
        '<div data-pl-cred="" style="display:flex; align-items:center; gap:14px; margin-bottom:26px; padding:14px 18px; border-radius:16px; '
        'background:rgba(251,250,246,0.7); border:1px solid rgba(201,168,106,0.55)">'
        '<span style="flex-shrink:0; display:inline-flex; align-items:center; justify-content:center; width:42px; height:42px; '
        'border-radius:999px; background:var(--gold-300); color:#26302D"><i data-lucide="award" style="width:20px; height:20px"></i></span>'
        '<span style="display:flex; flex-direction:column; gap:2px; min-width:0">'
        '<span style="font-family:var(--font-display); font-weight:600; font-size:1.2rem; line-height:1.2; color:var(--ink-900)">'
        'Board-certified in Obesity Medicine</span>'
        '<span style="font-weight:400; font-size:0.82rem; line-height:1.45; color:var(--ink-500)">'
        'and Family Medicine. Your weight plan is designed and supervised by Dr. Chapman.</span>'
        '</span></div>'
    )


def supplements():
    return (
        '<div data-pl-supp="" style="margin-top:26px; padding:22px 26px; border-radius:20px; background:var(--paper); box-shadow:var(--shadow-sm); '
        'display:flex; flex-direction:column; align-items:flex-start; gap:14px">'
        '<div style="min-width:0">%s'
        '<h4 style="margin:10px 0 0; font-family:var(--font-display); font-weight:600; font-size:1.4rem; line-height:1.2; color:var(--ink-900)">Professional-Grade Supplements</h4>'
        '<p style="margin:8px 0 0; font-weight:300; font-size:0.86rem; line-height:1.55; color:var(--ink-500)">'
        'Explore professional-grade nutritional supplements through our Fullscript dispensary. As part of our personalized approach to wellness, '
        'we believe in providing access to high-quality products that support individualized nutritional needs and health goals.</p>'
        '</div>'
        '<a href="%s" target="_blank" rel="noopener" style="text-decoration:none">'
        '<x-import component-from-global-scope="TBWIDesignSystem_4a5da9.Button" variant="primary" size="sm" hint-size="auto,38px">Shop Professional-Grade Supplements</x-import>'
        '</a></div>'
    ) % (eyebrow('Fullscript dispensary'), e(FULLSCRIPT_URL))


def notes(p):
    style = 'margin:%s 0 0; font-weight:300; font-size:0.74rem; line-height:1.5; color:var(--ink-500)'
    text = ''.join('<p style="%s"><sup>%d</sup> %s</p>' % (style % ('22px' if i == 0 else '4px'), n, e(NOTES[n]))
                   for i, n in enumerate(p.get('notes', [])))
    if p.get('fine'):
        text += '<p style="%s">%s</p>' % (style % '22px', e(p['fine']))
    return text


# One pinned step per pillar, the same mechanics as How We Work: the section
# is tall, the stage sticks to the viewport, and scroll progress picks the
# step. Steps crossfade; their copy slides like the process steps do.
STEP = '''
      <div data-tstep="%(i)d" class="%(cls)s" aria-labelledby="%(id)s-title" style="background:%(bg)s">
        <div data-tleft="" style="display:flex; flex-direction:column; min-height:0">
          <figure data-tmedia="" style="position:relative; margin:0; flex:0 0 52%%; min-height:0; overflow:hidden; background:var(--sage-200)">
            <img src="%(photo)s" alt="%(alt)s" style="position:absolute; inset:0; width:100%%; height:100%%; object-fit:cover; object-position:%(pos)s; display:block">
            <div style="position:absolute; inset:0; pointer-events:none; background:linear-gradient(180deg, rgba(38,48,45,0.55) 0%%, rgba(38,48,45,0) 34%%)"></div>
          </figure>
          <div data-tcopy="" style="flex:1; min-height:0; padding:34px 56px 40px; display:flex; flex-direction:column; justify-content:center">
            %(eb)s
            <h3 id="%(id)s-title" style="margin:14px 0 0; font-family:var(--font-display); font-weight:500; font-size:clamp(2rem,3vw,2.8rem); line-height:1.06; color:var(--ink-900); text-wrap:balance">%(title)s</h3>
            <p style="margin:14px 0 0; max-width:520px; font-weight:300; font-size:0.96rem; line-height:1.6; color:var(--ink-500); text-wrap:pretty">%(lede)s</p>
          </div>
        </div>
        <div data-tright="" data-tcopy="" style="min-height:0; padding:64px 64px 48px; display:flex; flex-direction:column; justify-content:center">
          %(cred)s
          <div data-tgrid="" style="display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:30px 40px">%(cats)s</div>
          %(supp)s%(notes)s
        </div>
      </div>'''


def step(i, p):
    return STEP % {
        'i': i, 'cls': 'is-on' if i == 0 else '', 'id': p['id'], 'bg': p['bg'],
        'photo': p['photo'], 'alt': e(p['alt']), 'pos': p['pos'],
        'eb': eyebrow('Pillar %s' % p['num']), 'title': e(p['title']), 'lede': e(p['lede']),
        'cred': credential() if p.get('credential') else '',
        'cats': ''.join(category(c, p) for c in p['rows']),
        'supp': supplements() if p.get('supplements') else '', 'notes': notes(p)}


def anchors():
    # Menu links land on the scroll position where their pillar is showing.
    out = []
    for i, p in enumerate(PILLARS):
        ids = [p['id']] + [c['id'] for c in p['rows']] + (['supplements'] if p.get('supplements') else [])
        top = 'calc((100%% - 100vh) * %d / %d + 2vh)' % (i, len(PILLARS)) if i else '0'
        out += ['<span id="%s" data-tanchor="" aria-hidden="true" style="position:absolute; left:0; top:%s; width:1px; height:1px"></span>' % (a, top)
                for a in ids]
    return '\n    '.join(out)


CSS = '''<style>
    [data-tstep] { position:absolute; inset:0; display:grid; grid-template-columns:1fr 1fr; opacity:0; visibility:hidden; transition:opacity 0.6s var(--ease-standard), visibility 0.6s; }
    [data-tstep].is-on { opacity:1; visibility:visible; }
    [data-tstep] [data-tcopy] { transform:translateY(26px); transition:transform 0.55s var(--ease-out); }
    [data-tstep].is-on [data-tcopy] { transform:translateY(0); }
    [data-tstep].is-past [data-tcopy] { transform:translateY(-26px); }
    [data-rs="proc"] > div:last-child { order:-1; }
    @media (max-height: 820px) and (min-width: 1025px) {
      [data-tright] { padding:52px 56px 32px !important; }
      [data-tgrid] { gap:20px 36px !important; }
      [data-tcat] li { font-size:0.84rem !important; }
      [data-tcat] h4 { font-size:1.25rem !important; }
      [data-tleft] figure { flex-basis:46% !important; }
      [data-tleft] [data-tcopy] p { font-size:0.9rem !important; }
      [data-pl-supp] p { display:none; }
    }
    @media (max-width: 1024px) {
      #pillars { height:auto !important; }
      #pillars > [data-rs="treat"] { position:static !important; height:auto !important; overflow:visible !important; padding:0 !important; }
      [data-tstep] { position:relative; inset:auto; grid-template-columns:minmax(0, 1fr); opacity:1; visibility:visible; }
      [data-tstep] [data-tcopy] { transform:none !important; }
      [data-tleft] figure { flex:none !important; aspect-ratio:4 / 3; }
      [data-treat-label] { position:static !important; padding:56px 40px 28px; color:var(--teal-600) !important; background:var(--ivory); }
      [data-treat-label] span { background:var(--teal-500) !important; }
      [data-treat-counter] { display:none !important; }
      [data-tright] { padding:8px 56px 56px !important; }
    }
    @media (max-width: 768px) {
      [data-treat-label] { padding:48px 20px 24px; }
      [data-tleft] [data-tcopy] { padding:28px 20px 20px !important; }
      [data-tright] { padding:4px 20px 48px !important; }
      [data-tgrid] { grid-template-columns:minmax(0, 1fr) !important; gap:26px !important; }
      [data-pl-supp] { padding:22px !important; }
      [data-pl-supp] a, [data-pl-supp] button { width:100% !important; justify-content:center !important; }
      [data-pl-supp] button { white-space:normal !important; height:auto !important; min-height:44px; padding:12px 20px !important; line-height:1.4 !important; text-align:center; }
      [data-pl-cred] { align-items:flex-start !important; }
    }
  </style>'''

SECTION = '''<!-- ============ PILLARS (design/pillars.py) ============ -->
  %(css)s
  <section id="pillars" data-screen-label="Pillars" data-treat="" style="position:relative; height:%(h)dvh; background:var(--ivory)">
    %(anchors)s
    <div data-rs="treat" style="position:sticky; top:0; height:100vh; overflow:hidden">
      <h2 data-treat-label="" style="position:absolute; z-index:4; top:44px; left:56px; margin:0; display:flex; align-items:center; gap:10px; font-family:var(--font-body); font-weight:500; font-size:12px; letter-spacing:0.22em; text-transform:uppercase; color:#F5F2EA">
        <span style="width:6px; height:6px; background:var(--sage-200); border-radius:1px"></span>Our treatments
      </h2>
      <div data-treat-counter="" style="position:absolute; z-index:4; top:34px; right:calc(50%% + 56px); font-family:var(--font-display); font-weight:500; font-size:2.6rem; line-height:1; color:#F5F2EA">
        <span data-tcounter="">1</span><span style="opacity:0.5"> / %(n)d</span>
      </div>%(steps)s
    </div>
  </section>
'''

# Wired into the page's componentDidMount / scroll handler by build_index.py.
JS_INIT = '''    this.treatEl = document.querySelector('[data-treat]');
    this.tsteps = $('[data-tstep]');
    this.tcounter = document.querySelector('[data-tcounter]');
    this.treatIdx = 0;
'''

JS_SCROLL = '''    // Pinned treatment pillars (same mechanics as the process steps)
    if (this.treatEl && this.tsteps.length) {
      const r = this.treatEl.getBoundingClientRect();
      const total = r.height - vh;
      const p = Math.max(0, Math.min(0.999, total > 0 ? -r.top / total : 0));
      const n = this.tsteps.length;
      const idx = Math.min(n - 1, Math.floor(p * n));
      if (idx !== this.treatIdx) {
        this.treatIdx = idx;
        this.tsteps.forEach((s, i) => { s.classList.toggle('is-on', i === idx); s.classList.toggle('is-past', i < idx); });
        if (this.tcounter) this.tcounter.textContent = String(idx + 1);
      }
    }
'''


def render():
    return SECTION % {'css': CSS, 'h': 100 * (len(PILLARS) + 1), 'anchors': anchors(), 'n': len(PILLARS),
                      'steps': ''.join(step(i, p) for i, p in enumerate(PILLARS))}
