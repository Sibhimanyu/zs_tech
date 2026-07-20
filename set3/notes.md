## Notion

Notion has a `<nav>` tag for the main navigation, but it also uses a lot of `<div>` tags to hold things together. The logo is on the left, the links are in the middle, and Log in and Get Notion free are on the right. Product, Solutions and Resources are buttons because they open small menus.

## GitHub

GitHub puts the whole top part inside a `<header>`. The `<nav>` tag is harder to find because it is deep inside the code. The GitHub logo is on the left, then there are menu buttons like Platform and Solutions, and the search, Sign in and Sign up parts are on the right.

## Stripe

Stripe uses both `<header>` and `<nav>`. Its logo comes first, then it has buttons like Products, Solutions and Developers that open menus. Pricing is just a normal link. Sign in and Contact sales are placed on the right, and it also has a hamburger button for smaller screens.

## What they have in common

All three are mostly set up in the same way. They have a logo, some navigation links and an important button on the right. They use links to go to other pages and buttons when something needs to open.

Most navbars I saw use `<header>` and `<nav>` for structure and Flexbox for layout.

## My navbar plan

My brand name is Nimbus. It is a made-up app.

I chose four links:

- Product
- Features
- Docs
- Pricing

Pricing is the most important link because people can use it to decide if they want the product. I decided to add a Get Started button because I want it to stand out. I also added Log in as a normal link because it is less important than the main button.

## My paper sketch

This is my simple sketch of the layout:

[N] Nimbus   Product  Features  Docs  Pricing   Log in  [Get Started]

The logo and name go on the left, the four links go in the middle, and Log in and Get Started go on the right.

## HTML comparison

The generated HTML follows my plan because it has the Nimbus brand, all four links, Log in and the Get Started button. Like GitHub and Stripe, it uses a `<header>` and `<nav>`. It also uses `<ul>` and `<li>` for the links. My navbar is much simpler than the real ones because it does not have big dropdown menus or a search box. I added a mobile hamburger button, which is something all three websites also have.

## Design spec

- Background: white so it looks simple and clean.
- Text: dark navy for the brand and gray for the links.
- Overall feel: clean, modern and not too busy. The indigo cta should stand out most.