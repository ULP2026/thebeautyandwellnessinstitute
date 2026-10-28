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
    return ('<li style="display:flex; gap:12px; align-items:baseline; font-weight:300; font-size:0.95rem; line-height:1.5; color:var(--ink-700)">'
            '<span aria-hidden="true" style="flex-shrink:0; width:5px; height:5px; border-radius:1px; background:var(--sage-400); transform:translateY(-2px)"></span>'
            '<span>%s%s</span></li>') % (e(text), sup)


def badge(text, icon):
    return ('<span style="display:inline-flex; align-items:center; gap:6px; font-weight:500; font-size:10.5px; letter-spacing:0.2em; '
            'text-transform:uppercase; color:var(--gold-700); white-space:nowrap">'
            '<i data-lucide="%s" style="width:13px; height:13px; color:var(--gold-500)"></i>%s</span>') % (icon, e(text))


def row(c, p, i):
    tag = ''
    if c.get('featured') and p.get('badge'):
        tag = badge(p['badge'], 'badge-check' if p.get('credential') else 'trending-up')
    sub = ''
    if c.get('eyebrow'):
        sub = ('<span style="display:block; margin-top:6px; font-weight:500; font-size:11px; letter-spacing:0.18em; '
               'text-transform:uppercase; color:var(--teal-600)">%s</span>') % e(c['eyebrow'])
    return (
        '<div id="%s" data-reveal="" data-pl-row="" style="scroll-margin-top:24px; display:grid; grid-template-columns:44px minmax(0, 1fr); gap:20px; padding:30px 0">'
        '<span style="font-family:var(--font-display); font-weight:500; font-size:1.05rem; line-height:2.1; color:var(--sage-500)">%s.%d</span>'
        '<div style="min-width:0">'
        '<div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px 16px">'
        '<h4 style="margin:0; font-family:var(--font-display); font-weight:600; font-size:1.75rem; line-height:1.2; color:var(--ink-900)">%s</h4>%s</div>%s'
        '<p style="margin:10px 0 0; max-width:540px; font-weight:300; font-size:0.97rem; line-height:1.65; color:var(--ink-500)">%s</p>'
        '<ul data-pl-list="" style="list-style:none; margin:20px 0 0; padding:0; display:flex; flex-direction:column; gap:10px">%s</ul>'
        '</div></div>'
    ) % (c['id'], p['num'], i + 1, e(c['title']), tag, sub, e(c['desc']), ''.join(item(x) for x in c['items']))


def credential():
    return (
        '<div data-pl-cred="" style="display:flex; align-items:center; gap:16px; margin-top:24px; padding-top:20px; border-top:1px solid rgba(201,168,106,0.5)">'
        '<span style="flex-shrink:0; display:inline-flex; align-items:center; justify-content:center; width:48px; height:48px; '
        'border-radius:999px; background:var(--gold-300); color:#26302D"><i data-lucide="award" style="width:22px; height:22px"></i></span>'
        '<span style="display:flex; flex-direction:column; gap:3px; min-width:0">'
        '<span style="font-family:var(--font-display); font-weight:600; font-size:1.3rem; line-height:1.2; color:var(--ink-900)">'
        'Board-certified in Obesity Medicine</span>'
        '<span style="font-weight:400; font-size:0.85rem; line-height:1.5; color:var(--ink-500)">'
        'and Family Medicine. Your weight plan is designed and supervised by Dr. Chapman.</span>'
        '</span></div>'
    )


def supplements():
    return (
        '<div id="supplements" data-reveal="" data-pl-supp="" style="margin-top:8px; padding:36px; border-radius:24px; background:var(--paper); box-shadow:var(--shadow-sm); '
        'display:flex; flex-direction:column; align-items:flex-start; gap:14px">%s'
        '<h4 style="margin:0; font-family:var(--font-display); font-weight:600; font-size:1.75rem; line-height:1.2; color:var(--ink-900)">Professional-Grade Supplements</h4>'
        '<p style="margin:0; max-width:560px; font-weight:300; font-size:0.97rem; line-height:1.7; color:var(--ink-500)">'
        'Explore professional-grade nutritional supplements through our Fullscript dispensary. As part of our personalized approach to wellness, '
        'we believe in providing access to high-quality products that support individualized nutritional needs and health goals.</p>'
        '<a href="%s" target="_blank" rel="noopener" style="margin-top:8px; text-decoration:none">'
        '<x-import component-from-global-scope="TBWIDesignSystem_4a5da9.Button" variant="primary" size="md" hint-size="auto,44px">Shop Professional-Grade Supplements</x-import>'
        '</a></div>'
    ) % (eyebrow('Fullscript dispensary'), e(FULLSCRIPT_URL))


def notes(p):
    text = ''.join('<p style="margin:%s 0 0; font-weight:300; font-size:0.8rem; line-height:1.6; color:var(--ink-500)"><sup>%d</sup> %s</p>'
                   % ('24px' if i == 0 else '6px', n, e(NOTES[n])) for i, n in enumerate(p.get('notes', [])))
    if p.get('fine'):
        text += '<p style="margin:24px 0 0; font-weight:300; font-size:0.8rem; line-height:1.6; color:var(--ink-500)">%s</p>' % e(p['fine'])
    return text


PILLAR = '''
  <section id="%(id)s" data-pl="" aria-labelledby="%(id)s-title" style="background:%(bg)s">
    <div data-pl-grid="" style="max-width:1240px; margin:0 auto; padding:0 40px; display:grid; grid-template-columns:minmax(0, 5fr) minmax(0, 6fr); gap:72px; align-items:start">
      <div data-pl-pin="" style="position:sticky; top:32px; padding:56px 0 48px">
        <figure style="position:relative; margin:0; height:min(36vh, 360px); border-radius:24px; overflow:hidden; background:var(--sage-200); box-shadow:var(--shadow-md)">
          <img src="%(photo)s" alt="%(alt)s" loading="lazy" style="position:absolute; inset:0; width:100%%; height:100%%; object-fit:cover; object-position:%(pos)s; display:block">
          <div style="position:absolute; inset:0; background:linear-gradient(0deg, rgba(20,27,23,0.45) 0%%, rgba(20,27,23,0) 45%%)"></div>
          <span style="position:absolute; left:22px; bottom:14px; font-family:var(--font-display); font-weight:500; font-size:4.5rem; line-height:1; color:#F5F2EA">%(num)s</span>
        </figure>
        <div style="margin-top:28px">%(eb)s</div>
        <h3 id="%(id)s-title" style="margin:14px 0 0; font-family:var(--font-display); font-weight:500; font-size:clamp(2rem,3vw,2.7rem); line-height:1.08; color:var(--ink-900); text-wrap:balance">%(title)s</h3>
        <p style="margin:14px 0 0; max-width:480px; font-weight:300; font-size:0.98rem; line-height:1.65; color:var(--ink-500); text-wrap:pretty">%(lede)s</p>
        %(cred)s
      </div>
      <div data-pl-rows="" style="padding:42px 0 72px; min-width:0">%(rows)s%(supp)s%(notes)s</div>
    </div>
  </section>
'''


def pillar(p):
    return PILLAR % {
        'id': p['id'], 'bg': p['bg'], 'photo': p['photo'], 'alt': e(p['alt']), 'pos': p['pos'], 'num': p['num'],
        'eb': eyebrow('Pillar %s of 03' % p['num']), 'title': e(p['title']), 'lede': e(p['lede']),
        'cred': credential() if p.get('credential') else '',
        'rows': ''.join(row(c, p, i) for i, c in enumerate(p['rows'])),
        'supp': supplements() if p.get('supplements') else '', 'notes': notes(p)}


CSS = '''<style>
    @media (max-width: 1024px) {
      [data-pl-grid] { gap:44px !important; }
    }
    @media (min-width: 769px) and (max-height: 820px) {
      [data-pl-pin] { padding-top:32px !important; top:16px !important; }
      [data-pl-pin] figure { height:30vh !important; }
    }
    @media (max-width: 768px) {
      #pillars { padding:56px 0 8px !important; }
      #pillars > div { padding-left:20px !important; padding-right:20px !important; }
      [data-pl-grid] { grid-template-columns:minmax(0, 1fr) !important; gap:0 !important; padding:0 20px !important; }
      [data-pl-pin] { position:static !important; padding:40px 0 8px !important; }
      [data-pl-pin] figure { height:auto !important; aspect-ratio:4 / 3; }
      [data-pl-pin] figure span { font-size:3.4rem !important; }
      [data-pl-rows] { padding:8px 0 48px !important; }
      [data-pl-row] { grid-template-columns:minmax(0, 1fr) !important; gap:4px !important; padding:22px 0 !important; }
      [data-pl-row] h4 { font-size:1.5rem !important; }
      [data-pl-supp] { padding:28px 22px !important; }
      [data-pl-supp] a, [data-pl-supp] button { width:100% !important; justify-content:center !important; }
      [data-pl-supp] button { white-space:normal !important; height:auto !important; min-height:44px; padding:12px 20px !important; line-height:1.4 !important; text-align:center; }
      [data-pl-jump] { flex-direction:column; align-items:stretch !important; }
    }
  </style>'''

SECTION = '''<!-- ============ PILLARS (design/pillars.py) ============ -->
  %(css)s
  <section id="pillars" data-screen-label="Pillars" style="background:var(--ivory); padding:96px 0 24px">
    <div data-reveal="" style="max-width:820px; margin:0 auto; padding:0 40px; display:flex; flex-direction:column; align-items:center; text-align:center">
      %(eb)s
      <h2 style="margin:18px 0 0; font-family:var(--font-display); font-weight:500; font-size:clamp(2.3rem,3.6vw,3.2rem); line-height:1.1; color:var(--ink-900); text-wrap:balance">Three pillars of care, <em>one physician-led plan.</em></h2>
      <p style="margin:16px 0 0; max-width:600px; font-weight:300; font-size:1.02rem; line-height:1.7; color:var(--ink-500)">Aesthetics, medical wellness, and longevity care, each built on evidence-based treatment, individualized planning, and results that look and feel like you.</p>
      <div data-pl-jump="" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-top:30px">%(jump)s</div>
    </div>
  </section>
%(pillars)s
'''


def render():
    jump = ''.join(
        '<a href="#%s" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; padding:12px 22px; border-radius:999px; '
        'border:1px solid var(--sage-300); color:var(--ink-900); font-weight:500; font-size:0.8rem; letter-spacing:0.14em; '
        'text-transform:uppercase; text-decoration:none; transition:background 220ms var(--ease-standard)" style-hover="background:var(--sage-50)">'
        '<span style="font-family:var(--font-display); font-size:1rem; letter-spacing:0; color:var(--sage-600)">%s</span>%s</a>' % (p['id'], p['num'], e(t))
        for p, t in zip(PILLARS, ['Aesthetics', 'Medical Wellness', 'Longevity & IV']))
    return SECTION % {'css': CSS, 'eb': eyebrow('Our treatments'), 'jump': jump,
                      'pillars': ''.join(pillar(p) for p in PILLARS)}
