## Inspecting a hero section

I opened Stripe's homepage in DevTools and looked at the hero.

- The hero is a `<section>` that sits right under the header.
- The main heading is an `<h1>` inside a div that also holds the paragraph and the buttons.
- There is only one heading. There is a small line of text above the `<h1>` but it is a `<p>`, not a heading.
- The buttons are `<a>` tags that are styled to look like buttons.
- The picture side is not a plain `<img>`. It is built out of divs because it is animated.
- The layout uses Flexbox. The text and the picture are side by side as flex children.
- The content is inside a container with a `max-width` and `margin: 0 auto`.
- Spacing comes from padding on the section, gap between the columns, and margins between the heading, paragraph and buttons.
- The hero does not have a fixed height. The height comes from the content and the padding.

## Studying the structure

Dropbox, Pitch, Notion, Stripe and Apple all have heroes but they are not built the same way.

Dropbox has the text on the left and a signup form inside the hero itself:

```
<section>
  <div>
    <h1>
    <p>
    <form>
      <input>
      <button>
  </div>
  <div>
    <img>
  </div>
</section>
```

Pitch and Stripe both use the split layout, text on one side and a picture on the other:

```
<section>
  <div>
    <h1>
    <p>
    <div>
      <a>
      <a>
  </div>
  <div>
    <img>
  </div>
</section>
```

Notion is different. Everything is centred in one column and the screenshot goes below the text instead of beside it. Apple is the simplest looking one. It has a big background image with the text on top of it, and the two actions are plain links with no button styling.

Answers:

- `<section>` is used because the hero is one separate part of the page. A `<div>` would look the same but it does not tell the browser or a screen reader anything.
- There is only one `<h1>` because it is the most important line on the page. Two `<h1>` tags would confuse the order of the headings.
- The actions are links because they take you to another page. A `<button>` is for something that happens on the same page, like opening a menu.
- The text block and the picture block are siblings. They are both children of the container.
- The `<a>` tags are nested inside the button row, which is nested inside the text block, which is nested inside the container.

## Studying the CSS

Five properties I found:

- `display: flex` on the container makes the two columns.
- `gap: 64px` puts space between the two columns without using margin.
- `max-width: 1240px` with `margin: 0 auto` stops the content from stretching across a big screen.
- `font-size: clamp(2.25rem, 4vw + 1rem, 3.5rem)` on the heading makes it grow and shrink with the screen instead of jumping at each breakpoint.
- `line-height: 1.1` on the heading and `1.6` on the paragraph. Tight lines look better on a big heading and loose lines are easier to read in small text.

## My hero plan

I reused my Nimbus navbar from the last assignment. The only change is that the hamburger no longer uses JavaScript. This time it is a hidden checkbox and a label, and the menu opens with a `:checked` rule in CSS.

What I decided before writing code:

- Heading: "The one place for your team's docs." with the last word changing.
- Paragraph: one sentence saying what Nimbus actually is.
- Main action: Get Started, the same button as in the navbar.
- Second action: See how it works, as a plain link with an arrow.
- Picture: an SVG drawing of the app instead of a photo.

My hierarchy:

```
<section class="hero">
  <div class="hero-container">
    <div class="hero-copy">
      <h1>
      <p>
      <div class="hero-actions">
        <a>
        <a>
    </div>
    <div class="hero-media">
      <img>
    </div>
  </div>
</section>
```

I picked the split layout like Pitch and Stripe because Nimbus is a work app, so showing the app next to the text made more sense than a big photo.

## The AI draft

My prompt was: "Generate only the HTML for a SaaS hero section with a heading, a supporting paragraph, a primary and secondary call-to-action, and an image on the right. No CSS."

It gave me this:

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

Checking it before using it:

- The semantic tags are wrong. The hero is a `<div>` and it should be a `<section>`.
- There is not exactly one `<h1>`. It used an `<h2>` for the second line, so there are two headings.
- There are extra divs. `hero-left` and `hero-right` each hold only one thing.
- I would rename `hero-left` and `hero-right` because they stop making sense when the layout stacks on mobile.
- Things are missing. The image has no `alt` and the buttons should be links.

I fixed all of that by hand first, then asked AI for the CSS using my corrected HTML.

## Five changes I made

1. I changed `<div class="hero-section">` to `<section class="hero">` because the hero is one separate region of the page and a div does not say that.
2. I changed the `<h2>` to a `<p>` because that line is a description, not a title.
3. I removed the `hero-left` and `hero-right` wrappers because each one had only one child and flex works fine without them.
4. I changed both `<button>` tags to `<a>` because they go to other pages.
5. I renamed `hero-left` and `hero-right` to `hero-copy` and `hero-media` because those names still make sense after the layout stacks.
6. I added a real `alt` to the image because without it a screen reader user gets nothing.
7. I replaced a margin on the button with `gap: 24px` on the row because gap only adds space between the items, so nothing is left over if they wrap.

Some extra things I looked into:

- Divs get nested a lot because they have no meaning, so they are safe to use as boxes for layout. Sections stay flat because putting a section inside a section says it is a separate region inside another separate region, which is usually not true.
- `max-width` is needed on the container and on the paragraph so the lines do not get too long to read. It is not needed on the `.hero` section itself, because that should stay full width.
- I used `rem` for font sizes and spacing because it is always based on the root size, so nesting does not make values pile up like `em` can. I only used `px` for thin borders.

## Testing

My breakpoints are 900px and 480px for the hero and 720px for the navbar.

- On mobile at 375px the container turns into a column, so the picture goes under the text and everything is centred. The heading wraps to two or three lines and does not overflow. The buttons wrap onto separate lines and are still easy to tap. The navbar is in hamburger mode.
- On tablet at 768px it is still the stacked layout but the heading usually fits on two lines instead of three.
- On desktop at 1440px it is two columns again. Above 1440px the container grows to `1360px` and the gap opens up to `80px` so the layout does not just get emptier at the sides.
- The HTML does not change at any size. Only the CSS changes.

Bonus, large screens: on something like a 27 inch monitor `max-width` becomes necessary, not optional, or the paragraph line gets far too long. The ceiling in `clamp()` matters more too, because a plain `vw` font size with no limit would make the heading huge. Growing the gap and centring the container with `margin: 0 auto` is what stops the hero from looking stretched.

## Reflection

- I used `<section>` for the hero, one `<h1>`, `<p>` for the paragraph, `<a>` for both actions and `<img>` with a real `alt`. I only kept the divs that actually do layout work.
- `display: flex` had the biggest effect, together with `flex-direction: column` in the 900px media query. That one pair of rules is what switches the whole thing between two columns and stacked.
- AI generated the extra `hero-left` and `hero-right` wrappers, an `<h2>` that should have been a `<p>`, and buttons that should have been links.
- I simplified it by cutting four wrapper divs down to two, replacing the fixed heading size with one `clamp()`, and using gap instead of one-off margins.
- I think someone else could read it. The class names say what each part is instead of where it sits, and there are no wrappers that exist for no reason.

## Bonus animation

I added two animations, both with no JavaScript.

The heading, paragraph, buttons and picture fade in and slide up when the page loads, about 0.1s apart, and the picture keeps floating slowly. All of it is inside `@media (prefers-reduced-motion: no-preference)`, so it only runs for people who have not asked their computer for less motion.

The last word of the heading also changes on a loop, from docs to tasks to chats to ideas. It works with four spans stacked on top of each other inside a box with `overflow: hidden`. They all run the same keyframes, but each one starts 2 seconds later than the last on an 8 second loop, so only one is visible at a time.

The rotating part is `aria-hidden="true"` and there is a hidden plain sentence after it saying "docs, tasks, chats and ideas", because a screen reader cannot read text that keeps changing. Under reduced motion the animation is turned off and only the first word is shown, so the sentence still reads properly.
