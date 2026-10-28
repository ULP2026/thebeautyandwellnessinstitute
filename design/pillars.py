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
        'icon': 'sun', 'title': 'Laser Skin Resurfacing', 'featured': True,
        'desc': 'Resurfacing protocols matched to your skin, your goals, and the downtime you can plan around.',
        'items': ['CO2 laser resurfacing', 'Erbium laser resurfacing',
                  'Fractional laser resurfacing protocols, as appropriate',
                  'Treatment of fine lines, wrinkles, and uneven skin texture'],
    },
    {
        'icon': 'sprout', 'title': 'Hair Restoration', 'featured': True,
        'desc': 'Physician-guided options for thinning hair, chosen after a careful look at your history and scalp health.',
        'items': ['Microneedling for hair restoration',
                  'Platelet-Rich Plasma (PRP) hair restoration',
                  ('AnteAGE MD exosome-based treatments', 1)],
    },
    {
        'icon': 'sparkles', 'title': 'Wrinkle Relaxers', 'eyebrow': 'Neuromodulators',
        'desc': 'Softens expression lines while keeping your face expressive and recognizably you.',
        'items': ['Botox Cosmetic', 'Dysport', 'Jeuveau', 'Daxxify'],
    },
    {
        'icon': 'gem', 'title': 'Dermal Fillers & Facial Rejuvenation',
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
        'icon': 'scale', 'title': 'Medical Weight Management', 'featured': True,
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
        'icon': 'venus', 'title': "Women's Hormonal Health",
        'desc': 'Clear answers and steady support through perimenopause, menopause, and the changes around them.',
        'items': ['Perimenopause and menopause consultations',
                  'Hormone replacement therapy (HRT)',
                  'Individualized hormonal evaluations',
                  'Ongoing treatment and monitoring'],
    },
    {
        'icon': 'mars', 'title': "Men's Hormonal Health",
        'desc': 'A thorough evaluation of energy, body composition, and testosterone, with treatment only when it is indicated.',
        'items': ['Testosterone replacement therapy (TRT)',
                  'Low testosterone evaluations',
                  'Testosterone deficiency management',
                  'Ongoing treatment and monitoring'],
    },
]

LONGEVITY = [
    {
        'icon': 'droplets', 'title': 'IV Vitamin Therapy', 'eyebrow': 'The IV Lounge',
        'desc': 'Our IV Lounge uses vitamin infusion protocols from Olympia Pharmaceuticals, selected after a review of your health history.',
        'items': ['IV hydration', 'Vitamin and nutrient infusion protocols',
                  'NAD+ treatments', 'Glutathione treatments',
                  'Vitamin B12 injections',
                  'Additional vitamin and wellness injections'],
    },
    {
        'icon': 'hourglass', 'title': 'Longevity & Peptide Treatments',
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

ARROW = ('<svg width="14" height="14" sc-camel-view-box="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path>'
         '<path d="m12 5 7 7-7 7"></path></svg>')


def e(s):
    return escape(s, quote=True)


def eyebrow(text, dark=False):
    dot, ink = ('var(--sage-300)', 'var(--sage-300)') if dark else ('var(--teal-500)', 'var(--teal-600)')
    return ('<div style="display:flex; align-items:center; gap:10px">'
            '<span style="width:6px; height:6px; background:%s; border-radius:1px"></span>'
            '<span style="font-weight:500; font-size:12px; letter-spacing:0.22em; text-transform:uppercase; color:%s">%s</span>'
            '</div>') % (dot, ink, e(text))


def item(it, dark):
    text, note = (it, None) if isinstance(it, str) else it
    sup = ('<sup style="font-size:0.7em; color:%s">%d</sup>' % ('var(--gold-300)' if dark else 'var(--teal-600)', note)) if note else ''
    return ('<li style="display:flex; gap:10px; align-items:flex-start; font-weight:300; font-size:0.95rem; line-height:1.55; color:%s">'
            '<i data-lucide="check" style="flex-shrink:0; width:16px; height:16px; margin-top:3px; color:%s"></i>'
            '<span>%s%s</span></li>') % ('rgba(247,244,237,0.86)' if dark else 'var(--ink-700)',
                                        'var(--gold-300)' if dark else 'var(--sage-500)', e(text), sup)


def card(c, badge=None, delay=0, badge_icon='trending-up', on_dark=False):
    dark = c.get('featured', False)
    bg = ('background:linear-gradient(160deg, #34423D, #2C3834); border:1px solid rgba(201,168,106,0.5); box-shadow:var(--shadow-lg)' if dark and on_dark else
          'background:#26302D; border:1px solid rgba(247,244,237,0.08); box-shadow:var(--shadow-lg)' if dark else
          'background:var(--paper); border:1px solid var(--border-subtle); box-shadow:var(--shadow-sm)')
    head = '#F5F2EA' if dark else 'var(--ink-900)'
    body = 'rgba(247,244,237,0.68)' if dark else 'var(--ink-500)'
    frame = ('border:1px solid rgba(201,168,106,0.55); color:var(--gold-300)' if dark else
             'border:1px solid var(--sage-300); color:var(--sage-600)')
    tag = ''
    if badge:
        tag = ('<span style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; border-radius:999px; '
               'background:rgba(201,168,106,0.16); border:1px solid rgba(201,168,106,0.4); font-weight:500; font-size:10.5px; '
               'letter-spacing:0.18em; text-transform:uppercase; color:var(--gold-300); white-space:nowrap">'
               '<i data-lucide="%s" style="width:12px; height:12px"></i>%s</span>') % (badge_icon, e(badge))
    sub = ''
    if c.get('eyebrow'):
        sub = ('<span style="display:block; margin-top:8px; font-family:var(--font-body); font-weight:500; font-size:11px; letter-spacing:0.18em; '
               'text-transform:uppercase; color:%s">%s</span>') % ('var(--gold-300)' if dark else 'var(--teal-600)', e(c['eyebrow']))
    return (
        '<article data-reveal="%d" data-pl-card="" style="%s; border-radius:24px; padding:32px; display:flex; flex-direction:column; min-width:0">'
        '<div style="display:flex; align-items:flex-start; justify-content:space-between; gap:12px">'
        '<span style="display:inline-flex; align-items:center; justify-content:center; width:46px; height:46px; border-radius:999px; flex-shrink:0; %s">'
        '<i data-lucide="%s" style="width:19px; height:19px"></i></span>%s</div>'
        '<h4 style="margin:22px 0 0; font-family:var(--font-display); font-weight:600; font-size:1.6rem; line-height:1.2; color:%s">%s%s</h4>'
        '<p style="margin:12px 0 0; font-weight:300; font-size:0.97rem; line-height:1.65; color:%s">%s</p>'
        '<ul style="list-style:none; margin:22px 0 0; padding:20px 0 0; border-top:1px solid %s; display:flex; flex-direction:column; gap:10px">%s</ul>'
        '</article>'
    ) % (delay, bg, frame, c['icon'], tag, head, e(c['title']), sub, body, e(c['desc']),
         'rgba(247,244,237,0.12)' if dark else 'var(--border-subtle)',
         ''.join(item(i, dark) for i in c['items']))


def notes(nums, dark=False):
    color = 'rgba(247,244,237,0.55)' if dark else 'var(--ink-500)'
    return ''.join('<p style="margin:%s 0 0; max-width:820px; font-weight:300; font-size:0.8rem; line-height:1.6; color:%s">'
                   '<sup>%d</sup> %s</p>' % ('28px' if i == 0 else '6px', color, n, e(NOTES[n]))
                   for i, n in enumerate(nums))


def pillar_head(pid, num, title, body, dark=False):
    head = '#F5F2EA' if dark else 'var(--ink-900)'
    text = 'rgba(247,244,237,0.7)' if dark else 'var(--ink-500)'
    return (
        '<div data-reveal="" style="max-width:760px">%s'
        '<h3 id="%s-title" style="margin:18px 0 0; font-family:var(--font-display); font-weight:500; font-size:clamp(2.2rem,3.6vw,3.2rem); line-height:1.08; color:%s; text-wrap:balance">%s <em>%s</em></h3>'
        '<p style="margin:18px 0 0; max-width:640px; font-weight:300; font-size:1.02rem; line-height:1.7; color:%s; text-wrap:pretty">%s</p>'
        '</div>'
    ) % (eyebrow('Pillar %s' % num, dark), pid, head, e(title[0]), e(title[1]), text, e(body))


def principles(words):
    return ('<div data-reveal="80" style="display:flex; flex-wrap:wrap; gap:10px; margin-top:26px">%s</div>' %
            ''.join('<span style="display:inline-flex; align-items:center; padding:8px 16px; border-radius:999px; '
                    'border:1px solid var(--sage-300); background:var(--sage-50); font-weight:400; font-size:0.85rem; '
                    'color:var(--ink-700)">%s</span>' % e(w) for w in words))


def credential():
    return (
        '<div data-reveal="80" data-pl-cred="" style="margin-top:36px; display:flex; align-items:center; gap:22px; padding:24px 28px; '
        'border-radius:22px; background:linear-gradient(135deg, rgba(201,168,106,0.2), rgba(201,168,106,0.06)); '
        'border:1px solid rgba(201,168,106,0.45); max-width:860px">'
        '<span style="flex-shrink:0; display:inline-flex; align-items:center; justify-content:center; width:58px; height:58px; '
        'border-radius:999px; background:var(--gold-300); color:#26302D"><i data-lucide="award" style="width:26px; height:26px"></i></span>'
        '<span style="display:flex; flex-direction:column; gap:6px; min-width:0">'
        '<span style="font-weight:500; font-size:11px; letter-spacing:0.2em; text-transform:uppercase; color:var(--gold-300)">Dr. Pamela Chapman</span>'
        '<span style="font-family:var(--font-display); font-weight:500; font-size:1.65rem; line-height:1.2; color:#F5F2EA">'
        'Board-certified in Obesity Medicine <em style="color:rgba(247,244,237,0.75)">and Family Medicine</em></span>'
        '<span style="font-weight:300; font-size:0.92rem; line-height:1.6; color:rgba(247,244,237,0.68)">'
        'Your weight management plan is designed and supervised by a physician with specialty training in the medical treatment of obesity.</span>'
        '</span></div>'
    )


def supplements():
    return (
        '<div id="supplements" data-reveal="" data-pl-supp="" style="margin-top:28px; display:grid; grid-template-columns:minmax(0, 1fr) auto; '
        'gap:32px; align-items:center; padding:36px 40px; border-radius:24px; background:var(--sage-100); border:1px solid rgba(136,152,120,0.28)">'
        '<div style="min-width:0">%s'
        '<h4 style="margin:16px 0 0; font-family:var(--font-display); font-weight:600; font-size:1.9rem; line-height:1.15; color:var(--ink-900)">Professional-Grade Supplements</h4>'
        '<p style="margin:12px 0 0; max-width:620px; font-weight:300; font-size:0.98rem; line-height:1.7; color:var(--ink-500)">'
        'Explore professional-grade nutritional supplements through our Fullscript dispensary. As part of our personalized approach to wellness, '
        'we believe in providing access to high-quality products that support individualized nutritional needs and health goals.</p>'
        '</div>'
        '<a href="%s" target="_blank" rel="noopener" style="text-decoration:none">'
        '<x-import component-from-global-scope="TBWIDesignSystem_4a5da9.Button" variant="primary" size="md" hint-size="auto,44px">Shop Professional-Grade Supplements</x-import>'
        '</a></div>'
    ) % (eyebrow('Fullscript dispensary'), e(FULLSCRIPT_URL))


CSS = '''<style>
    [data-pl-grid] { display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:24px; margin-top:48px; }
    [data-pl-grid="3"] { grid-template-columns:minmax(0, 1.25fr) minmax(0, 1fr) minmax(0, 1fr); }
    [data-pl-jump] a { transition:background 220ms var(--ease-standard), border-color 220ms var(--ease-standard); }
    @media (max-width: 1024px) {
      [data-pl-grid="3"] { grid-template-columns:repeat(2, minmax(0, 1fr)); }
      [data-pl-grid="3"] > :first-child { grid-column:1 / -1; }
      [data-pl-aes] { grid-template-columns:minmax(0, 1fr) !important; }
      [data-pl-aes] > figure { aspect-ratio:16 / 9 !important; }
    }
    @media (max-width: 768px) {
      #pillars > div, [data-pl-band] > div { padding-left:20px !important; padding-right:20px !important; }
      [data-pl-band] { padding-top:56px !important; padding-bottom:56px !important; }
      #pillars { padding-top:56px !important; }
      [data-pl-grid], [data-pl-grid="3"] { grid-template-columns:minmax(0, 1fr); gap:16px; margin-top:32px; }
      [data-pl-card] { padding:26px 22px !important; border-radius:20px !important; }
      [data-pl-cred] { flex-direction:column; align-items:flex-start !important; padding:22px !important; }
      [data-pl-supp] { grid-template-columns:minmax(0, 1fr) !important; padding:28px 22px !important; }
      [data-pl-supp] a, [data-pl-supp] button { width:100% !important; justify-content:center !important; }
      [data-pl-supp] button { white-space:normal !important; height:auto !important; min-height:44px; padding:12px 20px !important; line-height:1.4 !important; text-align:center; }
      [data-pl-jump] { flex-direction:column; align-items:stretch !important; }
    }
  </style>'''


def render():
    jump = ''.join(
        '<a href="#%s" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; padding:12px 22px; border-radius:999px; '
        'border:1px solid var(--sage-300); background:var(--paper); color:var(--ink-900); font-weight:500; font-size:0.8rem; letter-spacing:0.14em; '
        'text-transform:uppercase; text-decoration:none" style-hover="background:var(--sage-50); border-color:var(--sage-500)">'
        '<i data-lucide="%s" style="width:15px; height:15px; color:var(--sage-600)"></i>%s</a>' % (a, i, e(t))
        for a, i, t in [('aesthetics', 'sparkles', 'Aesthetics'), ('wellness', 'heart-pulse', 'Medical Wellness'),
                        ('longevity', 'droplets', 'Longevity & IV')])
    return '''<!-- ============ PILLARS (design/pillars.py) ============ -->
  %(css)s
  <section id="pillars" data-screen-label="Pillars" style="background:var(--ivory); padding:96px 0 0">
    <div data-reveal="" style="max-width:820px; margin:0 auto; padding:0 40px; display:flex; flex-direction:column; align-items:center; text-align:center">
      %(eb)s
      <h2 style="margin:18px 0 0; font-family:var(--font-display); font-weight:500; font-size:clamp(2.3rem,3.6vw,3.2rem); line-height:1.1; color:var(--ink-900); text-wrap:balance">Three pillars of care, <em>one physician-led plan.</em></h2>
      <p style="margin:16px 0 0; max-width:600px; font-weight:300; font-size:1.02rem; line-height:1.7; color:var(--ink-500)">Aesthetics, medical wellness, and longevity care, each built on evidence-based treatment, individualized planning, and results that look and feel like you.</p>
      <div data-pl-jump="" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-top:30px">%(jump)s</div>
    </div>
  </section>

  <section id="aesthetics" data-pl-band="" aria-labelledby="aesthetics-title" style="background:var(--ivory); padding:72px 0 96px">
    <div style="max-width:1240px; margin:0 auto; padding:0 40px">
      <div data-pl-aes="" style="display:grid; grid-template-columns:minmax(0, 7fr) minmax(0, 5fr); gap:56px; align-items:center">
        <div style="min-width:0">%(aes_head)s%(aes_tags)s</div>
        <figure data-reveal="120" style="position:relative; margin:0; aspect-ratio:4 / 3; border-radius:24px; overflow:hidden; background:var(--sage-200); box-shadow:var(--shadow-lg)">
          <img src="/assets/site/e8a35dd0aaaaceea.jpg" alt="Aesthetic treatment at The Beauty and Wellness Institute" loading="lazy" style="position:absolute; inset:0; width:100%%; height:100%%; object-fit:cover; display:block">
        </figure>
      </div>
      <div data-pl-grid="">%(aes_cards)s</div>
      %(aes_notes)s
    </div>
  </section>

  <section id="wellness" data-pl-band="" aria-labelledby="wellness-title" style="background:#26302D; padding:96px 0">
    <div style="max-width:1240px; margin:0 auto; padding:0 40px">
      %(wel_head)s
      %(cred)s
      <div data-pl-grid="3">%(wel_cards)s</div>
      <p style="margin:28px 0 0; max-width:820px; font-weight:300; font-size:0.8rem; line-height:1.6; color:rgba(247,244,237,0.55)">Prescription medications, including GLP-1 and hormone therapies, are prescribed only after a medical evaluation and only when clinically appropriate. Results vary by individual.</p>
    </div>
  </section>

  <section id="longevity" data-pl-band="" aria-labelledby="longevity-title" style="background:var(--ivory); padding:96px 0">
    <div style="max-width:1240px; margin:0 auto; padding:0 40px">
      %(lon_head)s
      <div data-pl-grid="">%(lon_cards)s</div>
      %(supp)s
      %(lon_notes)s
    </div>
  </section>

''' % {
        'css': CSS, 'eb': eyebrow('Our treatments'), 'jump': jump,
        'aes_head': pillar_head('aesthetics', 'one', ('Aesthetics &', 'regenerative beauty.'),
                                'Sophisticated aesthetic treatment with natural-looking results. We plan for facial harmony, '
                                'collagen support, and healthy skin, with every treatment plan built around your face and your goals.'),
        'aes_tags': principles(['Natural results', 'Facial harmony', 'Collagen support', 'Healthy skin', 'Individualized plans']),
        'aes_cards': ''.join(card(c, 'Now expanding' if c.get('featured') else None, 80 * (i % 2))
                             for i, c in enumerate(AESTHETICS)),
        'aes_notes': notes([1]),
        'wel_head': pillar_head('wellness', 'two', ('Medical wellness &', 'weight management.'),
                                'A physician-led approach to hormonal health, metabolic wellness, and medical weight management. '
                                'For men and women noticing changes in energy, body composition, or overall well-being who want '
                                'knowledgeable, personalized medical guidance, with evidence-based treatment and sustainable results.', dark=True),
        'cred': credential(),
        'wel_cards': ''.join(card(c, 'Obesity Medicine' if c.get('featured') else None, 80 * i, 'badge-check', on_dark=True) for i, c in enumerate(WELLNESS)),
        'lon_head': pillar_head('longevity', 'three', ('Longevity &', 'IV wellness.'),
                                'Our IV Lounge, nutrient therapies, and personalized longevity care, each starting with an individual '
                                'medical consultation and an evidence-informed approach to healthy aging.'),
        'lon_cards': ''.join(card(c, None, 80 * i) for i, c in enumerate(LONGEVITY)),
        'supp': supplements(),
        'lon_notes': notes([2]),
    }
