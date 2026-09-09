# TBWI Design System
### The Beauty & Wellness Institute · Dr. Pamela Chapman

A calm, physician-led design system for an aesthetics + medical-wellness clinic. The visual identity is botanical and clinical-warm: sage green and slate teal on warm ivory, set in a high-contrast serif paired with a clean geometric sans.

---

## 1. Company & product context

**TBWI (The Beauty & Wellness Institute)** combines aesthetic treatments and medical wellness care to help patients look and feel their best, "from the inside out." Founded/led by **Dr. Pamela Chapman**.

Offering — four pillars:
- **Aesthetics** — Botox, fillers, Sculptra, hair restoration
- **Wellness** — hormone therapy, weight management, peptides, IV therapy
- **Supplements** — medical-grade supplements delivered through Fullscript
- **Care** — 1:1 physician-led consultation tying it all together

**Primary surface represented here:** the TBWI marketing website (`ui_kits/website/`). No app, portal, or slide template was provided, so none were invented.

### Source materials
- `uploads/TBWI Primary Logo.png` — the primary lockup (botanical sprig in a pill frame, arched "THE BEAUTY AND WELLNESS INSTITUTE", serif "DR. PAMELA CHAPMAN" wordmark). Copied into `assets/logos/`.
- ⚠️ **`TBWI Design System Guide.pdf` was referenced but did NOT arrive in the project.** All tokens, type, and rules below are derived from the logo + brand description and are a best-faithful reconstruction. **Re-upload the guide** to reconcile exact colors, fonts, and spacing.

---

## 2. Content fundamentals — how TBWI writes

- **Voice:** warm, reassuring, and quietly premium. Medical authority without coldness; a spa calm without fluff.
- **Person:** addresses the reader as **"you"**; the clinic is **"we."** The physician is named directly ("Dr. Chapman").
- **Casing:** sentence case for headlines and body. **UPPERCASE with wide letter-spacing** only for eyebrows, nav, buttons, and badges (the signature tracked-caps motif).
- **Tone of headlines:** short, benefit-led, often with an italic serif clause for lift.
  - e.g. *"Look and feel your best, **from the inside out.**"*
  - *"Aesthetics, refined."* · *"Four pillars of beauty & wellness"*
- **Body copy:** plain-spoken and specific; names treatments rather than abstractions ("hormone therapy, weight management, and peptides" — not "holistic solutions").
- **Emoji:** never. **Exclamation marks:** rare. Numbers used only when meaningful (years, %, pillars).
- **Ampersand** "&" is used freely in headings and labels ("Botox & Fillers", "Beauty & Wellness").
- **Fine print** is honest and soft ("Results vary by individual. Consultation required.").

---

## 3. Visual foundations

**Color.** Two brand hues on warm neutrals:
- **Sage `#889878`** (primary) — from the botanical mark. Used for primary buttons, icon frames, accents.
- **Slate teal `#608078`** (secondary) — from the wordmark. Used for links, secondary actions, the inverse band, and serif stat figures.
- **Warm neutrals** — ivory canvas `#F7F4ED`, paper `#FBFAF6`, greige borders, and a desaturated **green-charcoal ink** (`#2C322B`) for text (never pure black).
- **Champagne gold `#C9A86A`** — a single premium accent, used sparingly (member/physician CTAs, awards).
- Full 50–900 ramps for sage & teal in `tokens/colors.css`; semantic aliases (`--brand`, `--accent`, `--surface-card`, `--text-body`, …) are what components consume.

**Type.** `tokens/typography.css`
- **Display:** Cormorant Garamond — high-contrast elegant serif, 500–600 weight, slight negative tracking, italic for emphasis clauses. Headings and hero.
- **Body / UI:** Jost — geometric sans, weights 300–600. Body copy leans light (300) at large sizes.
- **Eyebrow motif:** Jost 500, 0.22em tracking, uppercase, teal — optionally flanked by short hairline rules. This sits above most serif headings and is the system's signature.
- ⚠️ Both are **Google Fonts substitutes** for the unspecified brand fonts (see §1).

**Spacing & layout.** 4px base scale (`--space-1`…`--space-10`). Generous vertical rhythm — sections breathe at `--space-9` (96px). Content max-width 1200px; prose 680px.

**Corners.** Soft throughout, echoing the logo's pill/oval frame: cards `--radius-lg` (18px), inputs `--radius-md` (12px), **buttons & chips fully pill** (`--radius-pill`).

**Shadows.** Diffuse, low-opacity, **green-tinted** (not gray) — `--shadow-sm/md/lg`. Cards rest on `sm`, lift to `lg` on hover.

**Backgrounds.** Warm ivory canvas; sunken greige bands for trust strips/footer; one **inverse teal** band (`--surface-inverse`, teal-700) for the physician intro. Imagery is presented in **soft sage→teal tonal gradient placeholders** (no stock photos shipped — fill with real clinic/portrait photography). No busy patterns or textures.

**Motion.** Gentle and calm — `--dur-base` 220ms, `--ease-standard`/`--ease-out`. **No bounce.** Hover = lift + deepen shadow (cards) or darken fill (buttons). Press is implied by the same easing; avoid hard scale-downs.

**Hover/press states.**
- Primary button → darker sage fill. Secondary → soft teal tint. Ghost → sunken greige. Gold → deeper gold + white text.
- Cards / ServiceCards → translateY(-2/-3px) + `--shadow-lg`.
- Inputs → sage border + soft sage focus ring (`--shadow-focus`).

**Borders.** Hairline greige (`--border-subtle`/`--border-default`); never heavy. Dividers are 1px greige rules, often used between stats.

**Transparency/blur.** Reserved for the sticky header (88% canvas + 10px backdrop blur). Otherwise surfaces are opaque.

---

## 4. Iconography

- **System:** [Lucide](https://lucide.dev) — thin, **rounded 1.5px stroke** line icons that echo the botanical line-work of the logo mark. Loaded from CDN (`unpkg.com/lucide`). This is a **substitution**: no brand icon set was provided; Lucide is the closest match in weight and feel.
- **Color:** icons render in `--sage-600` by default; inside ServiceCard they sit in a **pill-shaped sage-bordered frame** (a nod to the logo's pill enclosure).
- **Usage:** `<i data-lucide="sparkles"></i>` then `lucide.createIcons()`. Common glyphs: `sparkles, leaf, flower-2, droplet, syringe, heart-pulse, pill, calendar-heart, user-round`.
- **No emoji. No unicode-glyph icons.** A single `→` arrow is used as a textual "learn more" affordance.
- See `guidelines/iconography.card.html`.

---

## 5. Index / manifest

**Root**
- `styles.css` — global entry point (consumers link this); `@import` list only.
- `readme.md` — this guide.
- `SKILL.md` — Agent-Skill wrapper for use in Claude Code.

**`tokens/`** — `fonts.css` (Google Fonts import + substitution note), `colors.css`, `typography.css`, `spacing.css` (spacing/radius/shadow/motion/layout), `base.css` (element resets + `.tbwi-eyebrow/-display/-rule`).

**`assets/logos/`** — `TBWI-primary-logo.png` (color, on light), `TBWI-logo-cream.png` (reversed, for dark/teal), `TBWI-logo-sage.png` (solid sage mono stamp).

**`components/`** (namespace `window.TBWIDesignSystem_*` — see `check_design_system`)
- `core/` — **Button**, **Badge**, **Card**, **Eyebrow**
- `forms/` — **Input**, **Switch**
- `brand/` — **ServiceCard**, **Stat**
- each: `<Name>.jsx` + `.d.ts` + `.prompt.md`, with one `*.card.html` specimen per directory.

**`ui_kits/website/`** — high-fidelity TBWI marketing site recreation. `index.html` runs an interactive **Home → Booking** flow composed from the primitives: `SiteHeader`, `Hero`, `TrustStrip`, `ServicesGrid`, `AboutDr`, `BookingScreen`, `SiteFooter`, `App`.

**`guidelines/`** — foundation specimen cards for the Design System tab (Colors, Type, Spacing, Brand).

---

## 6. Caveats (please reconcile)
1. **Design-system guide PDF is missing** — colors/type/spacing are reconstructed from the logo + brief.
2. **Fonts are substitutes** — Cormorant Garamond + Jost stand in for the real brand fonts. Send the licensed font files.
3. **Iconography is Lucide** (substitute). Swap if TBWI has a defined icon set.
4. **No photography** — image areas use brand-tonal placeholders; drop in real clinic/portrait imagery.
