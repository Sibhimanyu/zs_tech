# Set 9 — Cards

I carried on with the same Nimbus page from set 5. The navbar and the hero are
the same as before. This time I added two card sections and a footer under them.

## Part 1 — Observing three sites

**Stripe, the customers page.** A card is a logo, a short line about what the
company does, and a link that says "Read the story". Nine of them in a grid,
three across. All nine are built the same way. They use a logo image, not an
icon. The action is a text link with an arrow, not a button.

**Notion, the template gallery.** A card is a screenshot of the template, a
title, the name of the person who made it, and a small line with the price or
the word Free. There are a lot of them, they keep loading as you scroll. Every
card has the same parts, but the screenshots are different shapes so the image
box is a fixed height and the picture is cropped to fit. The whole card is
clickable, there is no separate button.

**Airbnb, the search results.** A card is a photo carousel, the place name, the
distance, the dates and the price, plus a rating on the right. Twenty or so per
page. Same structure every time, but some cards have an extra "Guest favourite"
badge sitting on the photo. The image is a real photo and it is the biggest
part of the card. The whole card is a link to the listing.

## Part 2 — Comparing them

| | What is inside a card | How many | Same structure | Image or icon | Action |
|---|---|---|---|---|---|
| Stripe | logo, one sentence, link | 9 | yes, all identical | logo image | text link with arrow |
| Notion | screenshot, title, author, price | many, keeps loading | yes | screenshot, cropped to fit | whole card is a link |
| Airbnb | photo, title, distance, dates, price, rating | around 20 | yes, with an optional badge | photo | whole card is a link |

**Which elements appeared in nearly every card:** a container holding
everything, a heading, and something to click. All three had a picture of some
kind too.

**Which were optional:** the paragraph. Airbnb has no real description, just
short lines of data. Badges, ratings and prices were also optional, they only
show up when the site has that information.

**Which card would be easiest to reuse with new content:** Stripe's. It is a
logo, a line of text and a link, and nothing inside it depends on the specific
company. Airbnb's card is the hardest to reuse because the rating and the badge
have to be handled even when they are missing.

Filling in the sentence:

> Most cards used **a repeated container element such as an `<article>` or a
> `<div>`** to group related content, **a heading and a paragraph** to display
> information, and **a CSS Grid or a Flexbox row** to arrange multiple cards on
> the page.

## Part 3 — Inspecting the code

I opened the Stripe customers page in DevTools and looked at one card.

The outer container is a `<div>` with the grid on it. Each card is an `<a>`
wrapping the whole thing, which is how the entire card becomes clickable. The
logo is an `<img>`, the title is a heading, the sentence is a `<p>`, and the
"Read the story" line at the bottom is a `<span>` inside the same `<a>`, not a
separate link.

Simplified, the hierarchy is:

```
<section>
  <div class="grid">
    <a class="card">
      <img>
      <h3>
      <p>
      <span>
    </a>
    <a class="card"> ... </a>
    <a class="card"> ... </a>
  </div>
</section>
```

- **What repeats:** the card element itself and every class on it. The tag
  order inside is identical in all nine cards.
- **What is unique per card:** only the content. The logo `src`, the `alt`, the
  heading text, the sentence and the `href`.
- **Could the HTML be simplified:** yes. There were two wrapper divs inside the
  card that only existed to hold padding, and the padding could just as easily
  sit on the card. There was also a `<div>` around the image doing nothing.

The useful thing I took from this is that the card is one shape repeated, and
only the text inside changes. That is exactly what I copied.

## Part 4 — Building the first card section

Five properties I noted from the grid and the cards on Stripe. The brief asks
for layout, spacing and sizing, so these are five that actually move things
around, not five that just make it look nicer:

- **Layout.** `display: grid` on the container. This is the one property that
  creates the rows and columns; without it the cards are just stacked blocks.
- **Layout and sizing.** `grid-template-columns: repeat(3, 1fr)`. The `1fr` is
  what makes all three columns exactly equal, no matter how much text is in
  each card. If it were `auto` the widest card would win.
- **Spacing.** `gap: 28px` for the space between cards instead of margins. Gap
  only goes between the items, so the outside cards do not get a stray margin
  pushing them off the container edge.
- **Spacing.** `padding: 28px` on the card. This is the only thing keeping the
  text off the border, and it is on the card rather than on each line of text,
  which is why the card can be re-used with any content.
- **Sizing.** `object-fit: cover` on the card image, with the image box given a
  fixed shape. The pictures Stripe uses are not all the same size, so the box
  decides the shape and the picture is cropped to fill it. Without this every
  card would be a different height.

I left `border-radius` and `box-shadow` off the list even though I use both,
because they are decoration. They change how the card looks but they do not
change where anything sits or how big it is.

My sketch before writing anything:

```
<section class="section">
  <div class="section-container">
    <header class="section-head">
      <p class="section-eyebrow">
      <h2>
      <p class="section-subtext">
    </header>
    <div class="card-grid">          <-- the arrangement
      <article class="card">         <-- the card, identical every time
        <div class="card-media">     <-- slot: an icon here, a picture later
        <div class="card-body">
          <h3 class="card-title">
          <p class="card-text">
          <a class="card-link">
      </article>
      x6
    </div>
  </div>
</section>
```

The two divs inside the card are the part I thought about hardest, because the
brief also tells you to watch out for unnecessary nesting. I decided they are
not unnecessary. `.card-media` and `.card-body` are what let me turn the card
sideways in the second section without touching the HTML: the media becomes a
column on the left and the body becomes the column on the right. A wrapper that
enables a layout is doing work. A wrapper that only holds one thing and has no
rule of its own is the kind you delete.

I used `<article>` for the card because each one stands on its own and would
still make sense if you pulled it out of the page. I used `<h3>` because the
section heading is the `<h2>`, so the card titles sit one level below it. The
icons are inline SVG rather than `<img>` so they can pick up the text colour
with `currentColor`.

The first three cards are Docs, Tasks and Chat, which are the three things the
hero already promises.

### Why the section ended up with six cards, not three

The brief asks for three, and three is what I built first. Then I looked at it
and realised the grid was not really being tested. Three cards in a three
column grid is one row, and one row means `gap` is only ever putting space
between columns. I had never seen it put space between rows, and I had never
seen what happens to two cards that sit above and below each other.

So I wrote three more cards: Search, Permissions and Imports. What that turned
up was worth the extra work:

- The row gap works, and it is the same 28px as the column gap because `gap` is
  one property doing both. If I had wanted them different it would be
  `gap: 40px 28px`, row first.
- Grid sizes each row to its own tallest card, not to the tallest card on the
  whole page. My first row is 272px and my second row is 296px. I did not know
  that until I could see two rows.
- I deliberately made the Permissions card one short line and the Imports card
  four lines, and put them in the same row. The short card stretches to 296px
  to match, and its "Explore permissions" link stays pinned to the bottom
  because of `margin-top: auto`. That one card is the clearest proof on the
  page that the layout is doing the work and not the content.

It also fixed something. With three cards, the two column tablet layout left
the third card sitting alone on its own row. With six there are three full
rows and nothing is orphaned.

### What the AI draft looked like

My prompt was: "Give me the HTML for a three card feature section, each card
with an icon, a heading, a paragraph and a link. No CSS."

The parts I did not keep:

- Every card was a `<div class="feature-card">`. I changed them to `<article>`
  because a card is a self contained piece of content.
- The icon was `<div class="icon"><i class="fa fa-file"></i></div>` which needs
  a whole icon font loaded. I put an inline `<svg>` in a single `<span>`
  instead, so there is no extra request and no extra wrapper.
- Every card had `<div class="card-content">` around the heading, the
  paragraph and the link. I very nearly deleted it, because at that point it
  had no rule of its own. I kept it and renamed it `.card-body`, because once I
  planned the second section I could see it was the thing that would become the
  right hand column. It is the one wrapper in the card that earns its place.
- It also had `<div class="card-image-wrapper">` around the icon. I kept that
  one too, as `.card-media`, for the same reason, and because it is what clips
  the picture when it zooms on hover.
- The headings were `<h2>`. That would put three `<h2>`s under the section
  `<h2>`, so the outline says they are siblings of the section title instead of
  children of it. I changed them to `<h3>`.
- The links all said "Learn more". I changed them to "Explore docs", "Explore
  tasks" and "Explore chat", because three identical links are hard to tell
  apart if you are tabbing through them with a screen reader.
- It repeated `margin-bottom` on the heading and the paragraph of each card.
  That is one rule on `.card-title` and `.card-text`, not three copies.

The arrow in each link is `<span aria-hidden="true">&rarr;</span>`, so a screen
reader reads "Explore docs" and not "Explore docs right arrow".

## Part 5 — Testing

My card breakpoints are 1000px, 760px, 680px and 480px. The navbar still
switches at 720px from set 5.

- **Desktop, 1440px.** Three columns, two rows. All six cards measure 395px
  wide. Within a row the heights match exactly, and the "Explore" links line up
  along the bottom, which is `margin-top: auto` on the link pushing it down.
- **Tablet, 768px.** Two columns, three rows. All six measure 338px. Because
  six divides by two there is no card left over on its own.
- **Mobile, 375px.** One column, six rows. Each card is now its own row, so the
  heights stop matching and each card is just as tall as its own text. That is
  correct, not a bug: there is nothing beside it to line up with. The wide
  cards in the second section turn from a row into a column, so the picture
  goes on top of the text.

I checked for overflow properly rather than by eye, at 375, 680, 768 and
1000px. At each one I measured `document.documentElement.scrollWidth` against
`clientWidth` and they were equal every time, so nothing is sticking out past
the edge at any size. I also read the widths and the top positions of all six
cards back at each width, which is how I know the columns are exactly equal
rather than nearly equal, and how I could count the rows.

The one thing I had to fix was the images in the wide cards. At full size the
picture column is 260px wide and the image is cropped to fill it with
`object-fit: cover`. When the card stacks on mobile the picture becomes full
width, and the same rule made it very tall.

My first fix was `max-height: 180px`, which worked but was a guess, and because
the image is cropped from the centre it cut the top and bottom off the picture.
I replaced it with `aspect-ratio: 16 / 9` on the media box in the 760px query.
Now the box has a shape rather than a number, it stays that shape at any screen
width, and the crop is much gentler. The desktop arrangement uses
`aspect-ratio: 4 / 3` for the same reason. This is the property I did not know
before this assignment and it turned out to be the useful one.

## Arrangements I tried

Before settling on two, I drew the arrangements from the examples and worked
out what each one does to the card:

- **Three equal columns.** The one I shipped, with six cards in two rows. It
  holds up for any multiple of three. What it needs is paragraphs of roughly
  similar length, because a card that is four lines longer than the others
  drags its whole row down with it.
- **Two columns.** More room per card, so the paragraph can be longer. It is
  what my three column grid becomes at 1000px anyway, which is why I did not
  need it as a separate section.
- **Wide horizontal rows.** The one I shipped second. The picture can be big
  and the text has room, and it reads as a list you go down rather than a set
  you scan across. Right for guides.
- **One big card and two small ones.** I sketched this and did not build it.
  It looks good but the big card needs different content from the small ones,
  so it is not really the same card any more, which is the opposite of what
  this assignment is about.
- **A horizontal scrolling row.** Rejected. It hides content off the side of
  the screen and it is awkward with a keyboard.

I picked the three column grid and the wide rows because they are the two that
look most different from each other while still being the same card. That is
what makes the point that the card and the arrangement are separate things.

## Part 6 — The second layout and the footer

The brief says the second section should reuse the card markup, so I took that
literally. The card in the second section is not a variation of the first one,
it is the same six lines of HTML:

```
<article class="card">
  <div class="card-media">   ... icon in section one, <img> in section two
  <div class="card-body">
    <h3 class="card-title">
    <p class="card-text">
    <a class="card-link">
</article>
```

I could copy a card out of the features section, paste it into the guides
section, change the words, and it would come out as a wide row without me
touching a single class on it.

My first attempt was not like this. I had a `.card-wide` class that I put on
each card in the second section, and the wide cards had two wrapper divs that
the grid cards did not have. It worked and it looked identical, but the two
sections were really two different cards that happened to share a colour. So I
went back and did two things:

1. Gave the grid cards the same `.card-media` and `.card-body` wrappers, with
   the icon sitting in the media slot where the picture goes in the other
   section.
2. Deleted `.card-wide` and moved its job onto the container, so it is now
   `.card-list .card { flex-direction: row }`.

That second change is the one that makes it click. **The card does not know
which layout it is in. The parent decides.** `.card-grid` puts them in three
equal columns and renders the media slot as a small icon tile. `.card-list`
stacks them and turns each one sideways. Same card both times.

The footer is a flex row that holds the brand, four links and the copyright
line, and it stacks into a column under 760px. The brand reuses the same
`.brand` and `.brand-mark` classes as the navbar, so it needed no new CSS at
all.

## Bonus — Hover

Every card lifts by 4px, deepens its shadow and darkens its border on hover,
and the arrow link inside it changes colour and opens its gap from 6px to 10px
so the arrow slides right. Any card with a picture in it also scales that
picture to 1.05, and because `overflow: hidden` is on the card the picture is
clipped by the rounded corner, so it zooms without growing the card. That rule
is `.card:hover .card-media img`, not a wide-card rule, so it would work in the
grid section too the day I put a picture there.

All of it is on a 0.25s ease transition, except the image zoom which is 0.4s
because a slow zoom looks better than a fast one. The transitions are declared
on the element, not inside `:hover`, so it eases back out as well as in.

I added a `prefers-reduced-motion: reduce` block that turns the transitions and
both transforms off. The colour and shadow changes stay, so you can still tell
the card is interactive. I also gave the links a `:focus-visible` outline,
because everything I described so far only happens for a mouse.

## Reflection

**Which semantic elements did I use most.** `<article>` for the cards and
`<section>` for the two card sections. Inside a card it is `<h3>`, `<p>` and
`<a>` every time. The `<header>` around each section title was worth using
because the eyebrow, the heading and the description are one unit. The only
plain divs left are `.card-grid`, `.card-list`, `.card-media` and `.card-body`,
and all four exist to do layout.

**Why cards are a good example of reusable HTML.** The card is one shape and
the content is the only thing that changes. I wrote the markup once and used it
nine times, and the two sections that look completely different are not just
similar markup, they are byte for byte the same element. The card carries no
information about where it is on the page, so the same six lines can be three
across or one wide. If I had built the second section from scratch I would have
had two sets of card styles to keep in sync, and they would have drifted the
first time I changed a colour.

**How much of the card CSS I reused.** I can count it, because the file is
grouped that way. Ten rules apply to every card in both sections: `.card`,
`.card-body`, `.card-title`, `.card-text`, `.card-link`, `.card-media img`, the
three hover rules and the focus outline, plus the reduced motion block. Each
arrangement then adds exactly four rules of its own. So the second layout cost
me four new rules and no new HTML at all.

Going from three cards to six is the same story from the other direction. It
cost three more `<article>` blocks and not one line of CSS, because
`repeat(3, 1fr)` never said anything about how many cards there are. Adding a
seventh would also be free. That is the part I would not have believed before I
tried it.

The reason it is that cheap is the order I wrote things in. Everything about
what a card *is* — the border, the radius, the shadow, the type sizes, the
hover — is on `.card` and its children. Everything about where cards *sit* is
on `.card-grid` or `.card-list`. Nothing crosses over. When I had `.card-wide`
the two were mixed together, and that is exactly why the second section cost
more than it should have.

**What I changed in the AI code.** Divs to articles, `<h2>` to `<h3>`, an icon
font to inline SVG, and I rewrote the three identical "Learn more" links so
they say what they link to. I also pulled the repeated margins out into one
rule per element instead of one per card.

The interesting one was the wrappers. The draft had two divs inside each card
and my first instinct, from the last assignment, was to delete both. I kept
them, and keeping them is what made the second section free. So the lesson is
not "AI adds too many divs and you should delete them". It is that a wrapper
is worth keeping exactly when it has a job, and you sometimes cannot tell
whether it has a job until you know what the next section looks like.
