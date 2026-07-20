# Navbar Exercise — Notes

## 1. Notes from inspecting 2–3 navbars

Inspected the live markup of **GitHub**, **Stripe**, and **Notion** (viewed page source / dev tools on their homepages).

| Site | Structure | Layout | Notes |
|---|---|---|---|
| GitHub | `<header>` wrapping a `<nav aria-label="Global">` | Flexbox row, logo far left, links + auth buttons far right | Uses a visually-hidden `aria-label` on `<nav>` for accessibility; button ("Sign up") is visually distinct (filled, brand color) from the plain text links |
| Stripe | `<header class="navigation">` wrapping `<nav id="navigation-menu">` | Flexbox row, logo left, nav links centered/left-of-center, CTA button right | Nav sits in a full-width header with a bottom hairline; links use generous horizontal spacing (~32px+) |
| Notion | `<nav aria-label="Main">` | Flexbox row, logo left, links grouped left, "Get Notion free" button right, high-contrast | Very minimal — no visible border, relies on whitespace alone to separate nav from page content |

**Common patterns across all three:**
- All wrap navigation in semantic `<header>` + `<nav>` (never a plain `<div>`).
- All use **Flexbox** with `justify-content: space-between` (logo on one end, actions on the other).
- All give the primary action (sign up / get started) a visually distinct **button**, while other links stay plain text.
- All rely on padding/whitespace rather than heavy borders or shadows to separate the navbar from content.

### Completed observation sentence
> Most navbars I saw use **a `<header>` element wrapping a semantic `<nav>`** for structure and **Flexbox with space-between alignment** for layout.

---

## 2. Navbar plan

Project: a fictional SaaS product called **Nimbus** (lightweight team task/project manager).

| Decision | Choice |
|---|---|
| Brand name | **Nimbus** |
| Links (4) | Product · Features · Docs · Pricing |
| Most important link | **Pricing** — it's the page most likely to convert a visitor into a signup |
| Button decision | Yes — one primary CTA button, **"Get Started"**, plus a plain-text **"Log in"** link immediately to its left (mirrors the GitHub/Notion pattern of separating "return visitor" vs. "new visitor" actions) |

---

## 3. Paper sketch (text stand-in)

```
┌──────────────────────────────────────────────────────────────────┐
│  [N] Nimbus     Product   Features   Docs   Pricing   Log in  [Get Started] │
└──────────────────────────────────────────────────────────────────┘
   ^logo+name        ^ nav links, evenly spaced         ^ auth   ^ CTA button
```

Layout logic: logo+brand pinned left, the four nav links grouped together just right of the brand, then login link + CTA button pinned to the far right — same left-cluster/right-cluster split observed in all three inspected sites.

---

## 4. AI-generated HTML — comparison answers

See `index.html`. Comparing it against the plan and inspected sites:

- **Structure match:** Uses `<header class="navbar">` wrapping `<nav aria-label="Main">`, matching the `<header>` + `<nav>` pattern seen in all three inspected navbars.
- **Links match:** Contains exactly the 4 planned links (Product, Features, Pricing, Docs) inside a `<ul>`, no more, no fewer.
- **Most important link:** Pricing is present as a plain nav link (not a button) — consistent with the plan; it's positioned last in the link group so it's the item right before the auth actions, giving it slight visual emphasis.
- **Button decision honored:** A `<button>`-styled anchor "Get Started" is included, separated from the plain "Log in" link — matches the planned CTA behavior.
- **Difference from inspected sites:** Real sites (GitHub/Stripe) often add a mobile hamburger toggle; this version stays desktop-focused per the sketch, since the exercise scope didn't call for responsive nav-collapse logic.

---

## 5. Design spec

| Aspect | Spec |
|---|---|
| Background | White (`#ffffff`) navbar on a white page — no color block, to keep the "clean SaaS" feel from Stripe/Notion |
| Text | Brand name: bold, dark navy (`#1a1f36`); nav links: medium-gray (`#4b5563`), shifting to navy on hover; CTA button text: white on brand indigo (`#4f46e5`) |
| Spacing | 32px gap between nav links; 40px gap between the link group and the brand; 16px gap between "Log in" and the "Get Started" button |
| Border / shadow | 1px solid hairline border-bottom (`#e5e7eb`) — no drop shadow, matching Notion's minimal-border approach rather than Stripe's heavier separation |
| Padding | Navbar: 16px vertical / 32px horizontal container padding; CTA button: 10px vertical / 20px horizontal, 6px border-radius |
| Overall feel | Clean, minimal, modern SaaS — generous whitespace, sans-serif type, understated color, one clear visual accent (the indigo CTA button) |

---

## 6. AI-generated CSS — comparison answers

See `style.css`. Comparing it against the design spec:

- **Background/border:** `.navbar` uses white background + `1px solid #e5e7eb` bottom border, no box-shadow — matches spec exactly (Notion-style restraint over Stripe-style heavier separation).
- **Text colors:** Brand uses `#1a1f36` bold; links use `#4b5563` with a `:hover` transition to `#1a1f36` — matches spec.
- **Spacing:** `.nav-links` uses `gap: 32px`; `.navbar` uses `justify-content: space-between` to split brand/links/actions into clusters, same as the sketch and the inspected-site pattern.
- **Button styling:** `.btn-primary` uses the indigo `#4f46e5` fill, white text, `6px` radius, `10px/20px` padding — matches spec; `.login-link` stays plain text to visually subordinate it to the CTA, same as GitHub/Notion's return-visitor-vs-new-visitor treatment.
- **Where it diverges intentionally:** No box-shadow was added even on hover/scroll, keeping strictly to the "no heavy shadow" spec rule rather than defaulting to a common shadow-on-scroll pattern.
