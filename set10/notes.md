# Set 10 — Mini Bill Splitter

A small web app that takes a bill, a number of people and a tip percentage, and
works out what each person pays. HTML, CSS and vanilla JavaScript, no libraries.

Files: `index.html`, `style.css`, `script.js`.

## What it does

The flow the brief asks for, left to right: enter the bill, choose the people,
add a tip, press Calculate, read the result.

- **Bill amount** — a number input with a ₹ sign sitting inside it.
- **Number of people** — a `+ / −` counter. The middle is still a real number
  input, so you can type 12 instead of pressing `+` ten times.
- **Tip** — five preset buttons (0, 5, 10, 15, 20) and a custom box under them.
  Leaving the box empty means 0%, which is what the brief specifies.
- **Calculate** — the main button. **Reset** sits next to it.
- **Result** — the per-person amount in large type, then a breakdown of the
  bill, the tip, the total and the number of people.

Bonus items done: Reset button, preset tip buttons, and live updating when an
input changes.

## The three things I actually had to learn

### 1. The form was refreshing the page

My first version used a `<form>` with a `<button>Calculate</button>` inside it.
Pressing the button wiped everything and the result flashed up and vanished. A
submit button inside a form submits the form, and submitting reloads the page.

Two ways out. I could stop using a form, or I could stop the default behaviour:

```js
form.addEventListener("submit", function (event) {
  event.preventDefault();
  calculate();
});
```

I kept the form. Listening on `submit` rather than on the button's `click`
means Enter works from inside any of the inputs, which is what you want when
you have just typed the bill. The brief says the user should not need to
refresh between calculations — this is the line that makes that true.

The `+`, `−` and tip buttons are all `type="button"`, because a `<button>`
inside a form defaults to `type="submit"`. Before I set that, clicking `+` also
ran a calculation and reloaded the page.

### 2. Empty is not the same as zero, and both are different from invalid

`Number("")` is `0`, not `NaN`. So if I had written `Number(billInput.value)` an
empty bill box would quietly calculate a bill of ₹0 instead of telling the user
to fill it in. That is the bug I would have shipped.

I wrote one helper that keeps the three cases apart:

```js
function readNumber(value, fallback) {
  const trimmed = value.trim();
  if (trimmed === "") {
    return fallback;
  }
  const parsed = Number(trimmed);
  return Number.isNaN(parsed) ? null : parsed;
}
```

`null` means "they typed something that is not a number". The `fallback` is
what an empty box means, and that is the whole point — it is different per
field. The bill passes `null` as the fallback, because an empty bill is an
error. The tip passes `0`, because the brief says an empty tip is 0%.

Same helper, opposite behaviour, decided by the caller.

### 3. Rounding does not add back up

`₹100` between 3 people is `₹33.33` each. Three times `33.33` is `₹99.99`. One
paisa has gone missing, and the app was confidently showing a breakdown that
did not balance.

I could not make it add up — you cannot pay a third of a paisa — so instead of
hiding it I calculate the difference and say it out loud:

```js
const remainder = roundToPaise(total - perPerson * people);
```

If it is not zero, a line appears under the breakdown: *"Rounding leaves ₹0.01
over — one person pays that bit extra."* It also handles the other direction,
because rounding up (₹1000 + 10% between 3) makes the shares come to a paisa
*more* than the total.

I also round the tip and the total to paise as they are computed rather than
only when printing, so the number the user sees and the number the next step
uses are the same number. `toFixed(2)` on its own only changes the display, and
the hidden extra decimals then leak into the breakdown.

## Validation

Every field is checked, and all of them are checked before anything is reported,
so the user sees every problem at once instead of fixing one and discovering
the next. `readInputs()` returns `null` if anything failed and an object of the
three numbers if everything passed — so the calculation function never has to
think about bad input at all.

| Field | Rejected | Message |
|---|---|---|
| Bill | empty, not a number | Enter the bill amount. |
| Bill | negative | The bill cannot be negative. |
| Bill | zero | The bill must be more than 0. |
| People | empty, not a number | Enter how many people are sharing. |
| People | 2.5 | People has to be a whole number. |
| People | 0 or less | There has to be at least 1 person. |
| People | over 99 | That is more than 99 people. |
| Tip | not a number | Tip has to be a number. |
| Tip | negative | The tip cannot be negative. |
| Tip | over 100 | Keep the tip at 100% or below. |

Blocking zero people is the one that matters most, because dividing by zero in
JavaScript does not throw. It gives `Infinity`, and `Infinity.toFixed(2)` is
the string `"Infinity"`, so the app would have shown "₹Infinity" rather than
failing in any way I could catch.

The error `<p>` for each field has `min-height` in CSS, so the layout does not
jump when a message appears and disappears. Each one has `role="alert"` and is
wired to its input with `aria-describedby`.

## Live updating, and why it waits

The bonus asks for the result to update as you type. Doing that naively means
someone who has typed `1` on their way to `100` gets the answer for a ₹1 bill,
and someone who has cleared the bill box to retype it gets an error message
shouted at them mid-keystroke.

So there is one flag:

```js
let hasCalculated = false;
```

Before the first successful Calculate, typing does nothing and the result panel
shows its empty state. After it, every keystroke re-runs the calculation. The
button is still the thing that starts it, which is what the brief describes,
and the live updating is the convenience on top. Reset sets the flag back to
`false`.

## Small decisions

- **The tip presets and the custom box are one value, not two.** Clicking 15%
  writes `15` into the custom box. Typing `15` into the box lights up the 15%
  button. There is no separate "selected preset" variable to keep in sync,
  because the input *is* the state — `highlightTipPreset()` just reads it back.
  This was originally two variables and they drifted apart within a minute.
- **The `−` button disables itself at 1 and `+` at 99**, rather than silently
  refusing, so the limit is visible before you hit it.
- **The counter steps from a floor.** If the box has `3.7` in it, `+` gives 4,
  not 4.7, because `Math.floor` runs before the step.
- **I removed the native number spinners** with `appearance: none`. Two sets of
  up/down controls on the people field looked like a mistake.
- **`void perPersonOut.offsetWidth`** between removing and adding the animation
  class. Without it the browser batches the two changes and the animation never
  replays on the second calculation. Reading `offsetWidth` forces a reflow in
  between, which is the trick that makes it restart.
- **The result card is `aria-live="polite"`**, so the new amount is announced
  instead of only appearing.

## Design

One card for the inputs, one for the result, side by side on desktop. The result
card is solid indigo against white so it is obviously the answer and not another
field, and it is `position: sticky` so it stays in view while you edit.

Every input has a real `<label>` (the tip group uses a `<fieldset>` and
`<legend>`, since the presets and the custom box share one label). Hover and
focus states are on all four kinds of control, focus rings are `:focus-visible`
so they only show for keyboard use, and there is a `prefers-reduced-motion`
block that turns the transitions and the pop animation off.

Three widths: two columns above 860px, stacked below, and under 480px the tip
presets go from five across to three and the buttons stack.

## Reflection

The JavaScript ideas the assignment was really about were small — `getElementById`,
`addEventListener`, `textContent`, an arithmetic function. What took the time
was everything around them: that an empty string is not a missing value, that a
form submits unless you tell it not to, and that rounding money is a real
decision rather than a formatting step.

The structure I would keep next time is the split into `readInputs` → `splitBill`
→ `showResult`. `splitBill` takes three numbers and returns an object; it never
touches the DOM and it does not know that a text box exists. I could test it in
the console by calling it with numbers directly, which is exactly what I did to
find the rounding problem.
