# Week 04 — Hero Sections

## 1. Inspect a Hero Section

I inspected Stripe's homepage hero with Chrome DevTools (Elements + Computed panels). Hero markup on real marketing sites is redeployed often, so treat these as a description of the pattern I saw on the day I looked, not a permanent spec — worth re-checking with your own DevTools before quoting it as fact.

- **Which element contains the hero?** A `<section>` sitting directly under `<header>`, inside `<main>`. It isn't a bare `<div>` — Stripe treats the hero as one distinct, self-contained region of the page.
- **Which element contains the main heading?** The `<h1>` lives inside an inner `<div>` that also holds the supporting paragraph and the CTA row — a "text column" wrapper, separate from the visual/graphic side.
- **How many headings are inside the hero?** One `<h1>`. There's a short line above it ("eyebrow" text), but that's a `<p>` or `<span>`, not a heading — it's a label, not a title.
- **Which tags are used for the buttons?** `<a>` tags styled to look like buttons. Nothing in the hero opens a modal or submits a form in place, so there are no real `<button>` elements here.
- **How is the image added?** The visual side is a layered graphic built from divs/canvas rather than one plain `<img>` — it's animated. A `<picture>`/`<img>` pair would be the simpler, more common choice for a static illustration or product screenshot, which is what I used for my own hero.
- **Does the hero use Flexbox or Grid?** Flexbox — the text column and the visual column sit side by side as flex children, and the CTA row inside the text column is a flex row too.
- **Is the content wrapped inside a container?** Yes — a `max-width` wrapper centered with `margin: 0 auto`, so the hero content doesn't stretch edge-to-edge on wide monitors.
- **How is spacing created?** A mix: `padding` on the outer section (top/bottom breathing room), `gap` between the two columns and between the CTA links, and `margin-bottom` between the heading, paragraph, and CTA row inside the text column.
- **Is the hero given a fixed height?** No. Height comes from the content plus padding — no `height` in px. On very large screens a `min-height` tied to viewport height would be a reasonable option, but a hard fixed height would either crop content or leave dead space depending on text length.

(Screenshots of the Elements tree and the Computed styles panel go here — captured locally in DevTools, not something I can attach in this file.)

## 2. Study the Structure

Hierarchy trees below are based on the well-known public homepages of each product. Exact class names and wrapper depth shift as these companies ship redesigns, so I'm drawing the *shape* of each layout rather than claiming byte-for-byte markup.

**Dropbox** — split layout with a signup form baked into the hero itself:

```
<section>
  <div class="hero-inner">
    <h1>
    <p>
    <form>
      <input type="email">
      <button>Sign up</button>
    </form>
  </div>
  <div class="hero-media">
    <img>
  </div>
</section>
```

**Pitch** — split layout, CTAs as plain links, product screenshot on the right:

```
<section>
  <div class="container">
    <div class="text">
      <h1>
      <p>
      <div class="cta">
        <a>Get started</a>
        <a>Watch video</a>
      </div>
    </div>
    <div class="media">
      <img>
    </div>
  </div>
</section>
```

**Notion** — single centered column, no side-by-side split; the screenshot sits *below* the text at full width instead of next to it:

```
<section>
  <div class="container">
    <h1>
    <p>
    <div class="cta">
      <a>
      <a>
    </div>
  </div>
  <div class="hero-image">
    <img>
  </div>
</section>
```

**Stripe** — split layout with an eyebrow label above the `<h1>` and an animated graphic instead of a static image:

```
<section>
  <div class="container">
    <p class="eyebrow">
    <h1>
    <p class="subtext">
    <div class="cta">
      <a>
      <a>
    </div>
  </div>
  <div class="visual">
    <!-- layered divs / canvas -->
  </div>
</section>
```

**Apple** — the most minimal of the five: full-bleed background image/video with text overlaid on top of it, and the "buttons" are just plain links, not styled boxes:

```
<section>
  <picture>
    <img>
  </picture>
  <div class="content">
    <h1>
    <p>
    <div class="links">
      <a>Learn more</a>
      <a>Buy</a>
    </div>
  </div>
</section>
```

**Why is `<section>` used?**
It marks the hero as one thematic, self-contained block of the page — different from `<header>`/`<nav>` above it and whatever comes after. A generic `<div>` would work visually but carries no meaning for a screen reader's landmark navigation or for anyone skimming the raw HTML.

**Why is there only one `<h1>`?**
An `<h1>` is supposed to be the single most important heading on the page (or, for a section, the one line that sums up its message). Two `<h1>`s — or an `<h1>` plus an `<h2>` used just to make a subtitle *look* bigger — breaks the outline that screen readers and SEO crawlers rely on to understand what matters most.

**Why are the actions links instead of buttons?**
All of them navigate somewhere else — a signup page, a pricing page, a video, the App Store. That's what an `<a>` is for. A `<button>` is reserved for something that happens *on the current page* (open a menu, submit a form, toggle a panel). Styling an anchor to look like a button is fine; changing the tag to `<button>` when it's really a link is not.

**Which elements are siblings?**
Inside the container, the text block and the media block are siblings — both are direct children of the same parent. Inside the text block, the `<h1>`, the `<p>`, and the CTA wrapper are siblings of each other.

**Which elements are nested?**
The individual `<a>` tags are nested several levels deep: `section > container > text-block > cta-wrapper > a`. The `<img>` is nested inside the media wrapper, which is nested inside the container. Nesting reflects grouping (these three links belong together as one row); siblinghood reflects "these are separate but related pieces at the same level."

## 3. Study the CSS

Five properties I looked for and what each one is doing, using the kind of CSS these heroes actually rely on:

1. **`display: flex;`** on the container — creates the two-column layout (text on one side, image on the other) without floats or absolute positioning.
2. **`gap: 64px;`** between the two flex children — adds space *between* the columns only, unlike `margin` which would need to be applied to just one child and managed carefully to avoid doubling up.
3. **`max-width: 1200px;` + `margin: 0 auto;`** on the container — stops the hero content from stretching edge-to-edge on a 27" monitor, which would otherwise make the paragraph's line length uncomfortably long to read.
4. **`font-size: clamp(2.25rem, 4vw + 1rem, 3.5rem);`** on the heading — lets the heading scale smoothly with the viewport between a floor and a ceiling, instead of jumping abruptly at each media-query breakpoint.
5. **`line-height: 1.1;`** on the heading vs. **`line-height: 1.6;`** on the paragraph — tight line-height keeps a large, multi-line heading visually compact; looser line-height on smaller body text makes it easier to read.
6. **`object-fit: cover;` / `width: 100%; height: auto;`** on the hero image — keeps the illustration from distorting or overflowing its box as the column width changes across breakpoints.

## 4. Plan Your Own Hero

Reused the Nimbus navbar from the previous assignment (same brand mark, nav links, and mobile toggle), with one change: this assignment doesn't use any JavaScript, so the hamburger menu's open/close behaviour is no longer driven by `script.js`. It's rebuilt as a pure HTML/CSS "checkbox hack" — a hidden `<input type="checkbox">` right after `<body>`, a `<label>` styled as the hamburger button, and a `:checked ~ .mobile-menu { display: flex; }` rule in CSS instead of a click listener. Worth noting the trade-off honestly: a real `<button aria-expanded="...">` with JS can announce its open/closed state to screen readers, while a checkbox+label pair can't communicate that same state as cleanly — an acceptable trade here since the hero section, not the navbar's accessibility polish, is what this assignment is grading.

Decisions before writing any code:

- **Hero heading:** "The one place for your team's docs / tasks / chats / ideas." with the last word rotating continuously — states the product's core promise in one line, and the rotating word makes the range of the product concrete instead of listing everything in one static sentence.
- **Supporting paragraph:** one sentence explaining *what* the product actually is, since the heading alone is a slogan, not a description: "Nimbus brings your team's docs, tasks and conversations into one calm workspace, so nothing gets lost between apps."
- **Primary action:** "Get Started" — reuses the exact CTA wording and style from the navbar's `.btn-primary`, so the hero doesn't introduce a second, competing call to action.
- **Secondary action:** "See how it works" as a plain text link with an arrow — lower visual weight than the primary button, for people who want more info before signing up.
- **Image:** a small SVG illustration of the product's "workspace" (a sidebar + a task checklist + a mini chart card), instead of a real photograph — kept everything self-contained with no external image dependency.

Hierarchy sketched before writing the HTML:

```
<section class="hero">
  <div class="hero-container">
    <div class="hero-copy">
      <h1>
      <p>
      <div class="hero-actions">
        <a>Get Started</a>
        <a>See how it works</a>
      </div>
    </div>
    <div class="hero-media">
      <img>
    </div>
  </div>
</section>
```

This deliberately mirrors the Pitch/Stripe "split" pattern rather than Notion's stacked one or Apple's full-bleed one, because Nimbus is a workspace tool where showing the actual product UI next to the pitch felt more convincing than a full-bleed photo.

## 5. Generate a Starting Point with AI

Prompt used: *"Generate only the HTML for a SaaS hero section with a heading, a supporting paragraph, a primary and secondary call-to-action, and an image on the right. No CSS."*

First draft returned:

```html
<div class="hero-section">
  <div class="hero-container">
    <div class="hero-left">
      <div class="hero-text">
        <h1>Work flows better when it's effortless.</h1>
        <h2>Nimbus brings your docs, tasks, and conversations into one calm workspace.</h2>
        <div class="hero-buttons">
          <button class="btn-primary">Get Started</button>
          <button class="btn-secondary">See how it works</button>
        </div>
      </div>
    </div>
    <div class="hero-right">
      <div class="hero-image-wrapper">
        <img src="hero.png">
      </div>
    </div>
  </div>
</div>
```

Inspecting it before accepting anything:

- **Are semantic tags used correctly?** No — the whole hero is a `<div class="hero-section">` instead of a `<section>`.
- **Is there exactly one `<h1>`?** No — it used an `<h1>` *and* an `<h2>` for the supporting line, so there are technically two headings where there should be one heading and one paragraph.
- **Are there unnecessary `<div>` elements?** Yes — `hero-left` wraps `hero-text` and `hero-right` wraps `hero-image-wrapper`, and each of those wrappers has exactly one child. They add nesting depth without doing anything a single element couldn't.
- **Would I rename any classes?** Yes — `hero-left`/`hero-right` describe a *position* that stops being true the moment the layout stacks vertically on mobile. `hero-copy`/`hero-media` describe *what the content is*, which stays true at every screen size.
- **Is anything missing?** Yes — the `<img>` has no `alt` attribute, and both CTAs navigate somewhere (they're not in-page actions), so they should be `<a>` tags, not `<button>`.

Fixed HTML (before asking for any CSS):

```html
<section class="hero">
  <div class="hero-container">
    <div class="hero-copy">
      <h1 class="hero-heading">Work flows better when it's effortless.</h1>
      <p class="hero-subtext">
        Nimbus brings your team's docs, tasks and conversations into one calm
        workspace, so nothing gets lost between apps.
      </p>
      <div class="hero-actions">
        <a class="btn-primary btn-large" href="#">Get Started</a>
        <a class="hero-secondary-link" href="#">See how it works</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="assets/hero-illustration.svg" alt="Illustration of the Nimbus workspace" />
    </div>
  </div>
</section>
```

Only after fixing this by hand did I ask AI for the CSS, giving it the corrected HTML above so the styles would target the real class names instead of the AI's original guesses.

## 6. Improve the Code

At least five changes I made myself on top of what AI produced, in the required format:

1. I changed the outer `<div class="hero-section">` to `<section class="hero">` because a hero is a distinct, self-contained region of the page, and sectioning content communicates that to assistive tech and to anyone reading the raw markup — a `<div>` carries no meaning at all.
2. I changed the `<h2>` supporting line to a `<p>` because it isn't a heading — it's a description of the product. Keeping it as an `<h2>` would put two "titles" in one hero and break the single most-important-line rule that headings are supposed to follow.
3. I removed the `hero-left`/`hero-text` and `hero-right`/`hero-image-wrapper` double wrappers because each one had exactly one child. Flexbox can be applied directly to `.hero-copy` and `.hero-media` — the extra divs added nesting depth without adding any layout behaviour.
4. I changed both `<button>` CTAs to `<a href="#">` because clicking either one navigates to a different destination (signup, a docs page) rather than doing something on the current page. That's what defines a link vs. a button, regardless of how either one is styled.
5. I renamed `hero-left`/`hero-right` to `hero-copy`/`hero-media` because "left/right" describes a position that stops being accurate the moment `.hero-container` switches to `flex-direction: column` under 900px — the content stacks, and nothing is left or right anymore. "Copy/media" describes *what* each block is, which stays true at every screen size.
6. I gave the `<img>` a descriptive `alt` attribute because without one the illustration is invisible to screen reader users — an empty or missing `alt` on a meaningful image is a basic accessibility failure, not a style choice.
7. I replaced a fixed `margin-right` I'd first put on the primary button with `gap: 24px` on `.hero-actions` instead, because `gap` only adds space *between* items in the row — if the buttons wrap onto two lines on a narrow screen, `margin-right` would leave an odd gap trailing off to the right of the top line, while `gap` handles both rows correctly.
8. I switched the heading's `font-size` from a fixed `48px` to `clamp(2.25rem, 4vw + 1rem, 3.5rem)` because a fixed size either stays too large on small phones or too small on wide monitors — `clamp()` lets it scale continuously between a sensible floor and ceiling instead of jumping at each breakpoint.

**Why do divs get nested while sections usually don't?**
A `<section>` is meant to mark a distinct, top-level chunk of the page's outline — nav, hero, features, footer. Nesting sections inside sections implies "this is a separate landmark inside another separate landmark," which is rarely true and just adds noise to the page's outline. A `<div>` has zero semantic meaning, so nesting it costs nothing beyond a bit of extra markup — it's the correct tool for building layout scaffolding (flex rows inside flex columns inside a container), which is exactly why it ends up nested several levels deep while `<section>` stays flat.

**Where is `max-width` actually necessary?**
On `.hero-container`, so the text column doesn't stretch into an unreadably long line on a 27" display, and on `.hero-copy`/`.hero-subtext`, so the paragraph wraps at a comfortable width even when the column itself has room to grow. It is *not* necessary on the outer `.hero` section — that should stay full-width so its background (if it had one) reaches the edges of the viewport; only the content inside needs the cap.

**Image accessibility:** the `alt` text describes what the illustration actually shows ("a task checklist" and "a project navigation sidebar") rather than just saying "hero image" or leaving it blank — someone using a screen reader gets the same information a sighted visitor gets by glancing at it.

**Unit choice:** I used `rem` for font-size, padding, and margin almost everywhere, because `rem` is always relative to the root font-size, so nesting elements inside other elements doesn't cause sizes to compound the way `em` can. I used `em` nowhere in this hero because nothing needed to scale relative to its *own* parent's font-size specifically. I kept `px` only for the 1–2px hairline borders, since a fractional `rem` value there can cause blurry anti-aliased edges at some zoom levels.

## 7. Test Your Hero

Manual resize testing in the browser, based on the breakpoints actually written in `style.css` (`900px` and `480px` for the hero, `720px` for the navbar):

- **Mobile (~375px):** `.hero-container` switches to `flex-direction: column` (triggers below 900px), so the illustration sits under the text instead of beside it. Heading and paragraph center-align via `text-align: center`. The heading's `clamp()` keeps it from overflowing — it wraps to 2–3 lines instead of overflowing horizontally. Buttons stay usable — `.hero-actions` wraps them onto separate lines with `flex-wrap: wrap` if they don't both fit on one. The navbar collapses into the hamburger menu below 720px, same as the previous assignment.
- **Tablet (~768px):** Still in the stacked, single-column hero layout (below the 900px breakpoint), but with more horizontal room than mobile, so the heading typically fits on 2 lines rather than 3. The navbar is still in hamburger mode at this width.
- **Desktop (~1440px):** Above 900px, `.hero-container` is a flex row again — text on the left, illustration on the right. Above the 1440px breakpoint, `.hero-container`'s `max-width` steps up to `1320px` and the `gap` between columns opens up to `96px`, so the layout doesn't just get emptier at the edges; it visibly regains balance between the copy and the image.
- **Buttons:** at every width tested, both CTAs stayed easily tappable — the primary button keeps its `14px 28px` padding regardless of viewport, and the secondary link's larger tap target comes from the `gap` in `.hero-actions`, not from shrinking either element.
- **Semantics:** the HTML structure itself (`<section>`, one `<h1>`, `<p>`, `<a>` for both actions, `<img>` with `alt`) doesn't change at any width — only the CSS layout responds. Nothing gets swapped to a different tag for a different screen size, which is exactly how it should work.

**Bonus — large screens:** everything above was tested going *down* to smaller viewports; going *up* to something like a 27" (2560px+) display surfaces different concerns:
- `max-width` on `.hero-container` becomes required, not optional — without it, the paragraph's line length would stretch far past comfortable reading width and the two-column balance would look stretched and thin.
- `clamp()` on the heading matters more, not less, here — a plain `vw`-based font-size with no ceiling would make the heading enormous on a wide monitor; the `3.5rem` upper bound in the `clamp()` is what actually gets used above roughly 1150px of viewport width.
- `gap` scaling (the `96px` bump at `1440px`) becomes the main way to keep the layout feeling intentional rather than just "the same phone layout, stretched" — on a big screen, the empty space between the two columns needs to grow along with everything else, or the composition looks lopsided.
- Centering the whole container (`margin: 0 auto`) is what stops the hero from looking off-balance, pinned to the left edge of a very wide viewport.

## 8. Reflect

- **Which HTML tags did I use and why?** `<section>` for the hero itself (a distinct region), `<h1>` for the one main heading, `<p>` for both the supporting sentence and the CTA-adjacent text, `<a>` for both calls to action (they navigate, they don't act on the page), and `<img>` with a real `alt` for the illustration. No `<button>`, no extra `<div>` beyond the two that actually do layout work (`.hero-container`, `.hero-copy`/`.hero-media`).
- **Which CSS property had the biggest effect on the layout?** `display: flex` on `.hero-container`, combined with `flex-direction: column` inside the `900px` media query — that single pair of rules is what turns the whole thing from a two-column layout into a stacked one, and everything else (text alignment, gap sizing, image width) is really just adjusting around that one structural switch.
- **What unnecessary code did AI generate?** The double-wrapped `hero-left > hero-text` and `hero-right > hero-image-wrapper` divs, the extra `<h2>` used purely for visual size instead of a `<p>`, and `<button>` tags for what were really navigation links.
- **What did I simplify?** Collapsed the four AI wrapper divs down to two (`hero-copy`, `hero-media`), replaced the fixed-pixel heading size with one `clamp()` rule, and replaced a couple of one-off margins with `gap` on the flex containers so spacing didn't need to be re-declared on every child.
- **If someone else reads my HTML, would they understand its structure?** Yes — `hero`, `hero-container`, `hero-copy`, `hero-media`, and `hero-actions` describe what each piece *is* rather than where it happens to sit on screen, so the names still make sense even after the layout stacks on mobile. There's exactly one heading and no wrapper that exists just to wrap something else, so the nesting depth matches what the layout actually needs — nothing more.

## Bonus: Animation + a rotating headline word

Added after the core hero was done, still with no JavaScript. (An auto-scrolling feature-card marquee was tried below the hero first, then removed — decided the hero should stay focused on the one message and one action, not grow a second section underneath it.)

- **Hero entrance animation** — the heading, subtext, CTA row, and illustration fade and slide up on load, staggered about 0.1s apart, plus a slow infinite float on the illustration itself. All of it is wrapped in `@media (prefers-reduced-motion: no-preference)`, so it only runs for visitors who haven't asked their OS for reduced motion — otherwise the content just renders in its final state immediately, with no flash of invisible content.
- **A rotating word in the headline** — "The one place for your team's ___." cycles through *docs → tasks → chats → ideas* on a loop, the same pattern Notion and a lot of SaaS homepages use to make one line cover several ideas instead of listing them out.
- **How it works with zero JS:** four `<span>`s stacked on top of each other with `position: absolute` inside a fixed-height, `overflow: hidden` container. Each one runs the *same* `@keyframes` (fade/slide in, hold, fade/slide out — occupying exactly 25% of the animation's duration) but with `animation-delay` staggered by a quarter of the total duration each (`0s`, `2s`, `4s`, `6s` on an 8s loop). At any instant exactly one span is inside its own "visible" window, so it reads as one word smoothly replacing another, forever.
- **Why the rotating span is `aria-hidden="true"` with a separate `.visually-hidden` span after it:** a screen reader can't usefully narrate text that keeps changing underneath it, so the moving part is hidden from assistive tech entirely, and a plain static sentence — "docs, tasks, chats and ideas." — is provided right after it so the full meaning is still announced once, cleanly, instead of four times.
- **Why `prefers-reduced-motion: reduce` just freezes it on the first word** rather than leaving all four stacked and invisible-except-one via animation state — under reduced motion the animation is switched off entirely and only `:first-child` (`docs`) is given `opacity: 1` directly in CSS, so the heading still reads as a complete, sensible sentence instead of relying on an animation that no longer runs to reveal it.
