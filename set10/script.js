/* Split It — a bill splitter in plain JavaScript.
   Flow: enter bill -> choose people -> add tip -> calculate -> view result. */

// ---------------------------------------------------------------- selectors --

const form = document.getElementById("bill-form");

const billInput = document.getElementById("bill");
const peopleInput = document.getElementById("people");
const tipInput = document.getElementById("tip");

const minusBtn = document.getElementById("people-minus");
const plusBtn = document.getElementById("people-plus");
const tipButtons = document.querySelectorAll(".tip-btn");
const resetBtn = document.getElementById("reset");

const fieldInputs = [billInput, peopleInput, tipInput];

const emptyState = document.getElementById("result-empty");
const resultBody = document.getElementById("result-body");
const perPersonOut = document.getElementById("per-person");
const billOut = document.getElementById("out-bill");
const tipOut = document.getElementById("out-tip");
const tipRateOut = document.getElementById("out-tip-rate");
const totalOut = document.getElementById("out-total");
const peopleOut = document.getElementById("out-people");
const roundingNote = document.getElementById("rounding-note");

// ---------------------------------------------------------------- constants --

const MIN_PEOPLE = 1;
const MAX_PEOPLE = 99;
const MAX_TIP = 100;

// Once the user has calculated once, every later edit updates the result live.
// Before that, nothing appears until the button is pressed.
let hasCalculated = false;

// ----------------------------------------------------------------- helpers --

function formatMoney(amount) {
  return "₹" + amount.toFixed(2);
}

function roundToPaise(amount) {
  return Math.round(amount * 100) / 100;
}

// "" / null / spaces -> fallback. Anything else must be a real number.
function readNumber(value, fallback) {
  const trimmed = value.trim();
  if (trimmed === "") {
    return fallback;
  }
  const parsed = Number(trimmed);
  return Number.isNaN(parsed) ? null : parsed;
}

// Each input points at its note through aria-describedby. The note starts out
// holding the hint; an error swaps in, and clearing puts the hint back.
function noteFor(input) {
  return document.getElementById(input.getAttribute("aria-describedby"));
}

function showError(input, message) {
  const note = noteFor(input);
  note.textContent = message;
  note.classList.add("is-error");
  input.classList.add("is-invalid");
}

function clearError(input) {
  const note = noteFor(input);
  note.textContent = note.dataset.hint;
  note.classList.remove("is-error");
  input.classList.remove("is-invalid");
}

// --------------------------------------------------------------- validation --

// Returns the three numbers, or null if anything is wrong. It checks every
// field before returning so the user sees all the problems at once.
function readInputs() {
  let valid = true;

  const bill = readNumber(billInput.value, null);
  if (bill === null) {
    showError(billInput, "Enter the bill amount.");
    valid = false;
  } else if (bill < 0) {
    showError(billInput, "The bill cannot be negative.");
    valid = false;
  } else if (bill === 0) {
    showError(billInput, "The bill must be more than 0.");
    valid = false;
  } else {
    clearError(billInput);
  }

  const people = readNumber(peopleInput.value, null);
  if (people === null) {
    showError(peopleInput, "Enter how many people are sharing.");
    valid = false;
  } else if (!Number.isInteger(people)) {
    showError(peopleInput, "People has to be a whole number.");
    valid = false;
  } else if (people < MIN_PEOPLE) {
    showError(peopleInput, "There has to be at least 1 person.");
    valid = false;
  } else if (people > MAX_PEOPLE) {
    showError(peopleInput, "That is more than " + MAX_PEOPLE + " people.");
    valid = false;
  } else {
    clearError(peopleInput);
  }

  // An empty tip box is not an error, it just means 0%.
  const tip = readNumber(tipInput.value, 0);
  if (tip === null) {
    showError(tipInput, "Tip has to be a number.");
    valid = false;
  } else if (tip < 0) {
    showError(tipInput, "The tip cannot be negative.");
    valid = false;
  } else if (tip > MAX_TIP) {
    showError(tipInput, "Keep the tip at " + MAX_TIP + "% or below.");
    valid = false;
  } else {
    clearError(tipInput);
  }

  if (!valid) {
    return null;
  }
  return { bill: bill, people: people, tip: tip };
}

// ------------------------------------------------------------------- maths --

function splitBill(bill, people, tipPercent) {
  const tipAmount = roundToPaise(bill * (tipPercent / 100));
  const total = roundToPaise(bill + tipAmount);
  const perPerson = roundToPaise(total / people);

  // perPerson is rounded, so the shares do not always add back up to the total.
  const remainder = roundToPaise(total - perPerson * people);

  return {
    bill: bill,
    people: people,
    tipPercent: tipPercent,
    tipAmount: tipAmount,
    total: total,
    perPerson: perPerson,
    remainder: remainder
  };
}

// ------------------------------------------------------------------ output --

function showResult(result) {
  emptyState.hidden = true;
  resultBody.hidden = false;

  perPersonOut.textContent = formatMoney(result.perPerson);
  billOut.textContent = formatMoney(result.bill);
  tipOut.textContent = formatMoney(result.tipAmount);
  tipRateOut.textContent = "(" + result.tipPercent + "%)";
  totalOut.textContent = formatMoney(result.total);
  peopleOut.textContent = result.people === 1 ? "1 person" : result.people + " people";

  if (result.remainder === 0) {
    roundingNote.hidden = true;
    roundingNote.textContent = "";
  } else {
    const extra = formatMoney(Math.abs(result.remainder));
    roundingNote.hidden = false;
    roundingNote.textContent =
      result.remainder > 0
        ? "Rounding leaves " + extra + " over — one person pays that bit extra."
        : "Rounding is " + extra + " over the total — one person can pay that much less.";
  }

  // Replay the little scale animation on every fresh number.
  perPersonOut.classList.remove("is-updated");
  void perPersonOut.offsetWidth;
  perPersonOut.classList.add("is-updated");
}

function hideResult() {
  emptyState.hidden = false;
  resultBody.hidden = true;
}

// ------------------------------------------------------------------ actions --

function calculate() {
  const inputs = readInputs();
  if (inputs === null) {
    hideResult();
    return;
  }
  hasCalculated = true;
  showResult(splitBill(inputs.bill, inputs.people, inputs.tip));
}

// Live updates, but only after the first successful Calculate, and without
// shouting an error at someone who is still halfway through typing.
function recalculateIfLive() {
  if (!hasCalculated) {
    return;
  }
  calculate();
}

function syncCounterButtons() {
  const people = readNumber(peopleInput.value, null);
  minusBtn.disabled = people !== null && people <= MIN_PEOPLE;
  plusBtn.disabled = people !== null && people >= MAX_PEOPLE;
}

function stepPeople(direction) {
  const current = readNumber(peopleInput.value, null);
  const base = current === null || current < MIN_PEOPLE ? MIN_PEOPLE : Math.floor(current);
  const next = Math.min(MAX_PEOPLE, Math.max(MIN_PEOPLE, base + direction));

  peopleInput.value = next;
  clearError(peopleInput);
  syncCounterButtons();
  recalculateIfLive();
}

// The presets and the custom box are two ways of setting one value, so
// whichever was used last is the one that shows as active.
function highlightTipPreset() {
  const value = tipInput.value.trim();
  tipButtons.forEach(function (button) {
    button.classList.toggle("is-active", value !== "" && button.dataset.tip === value);
  });
}

function resetAll() {
  form.reset();
  peopleInput.value = 2;

  fieldInputs.forEach(clearError);

  hasCalculated = false;
  hideResult();
  highlightTipPreset();
  syncCounterButtons();
  billInput.focus();
}

// ----------------------------------------------------------------- listeners --

form.addEventListener("submit", function (event) {
  event.preventDefault(); // no page refresh between calculations
  calculate();
});

minusBtn.addEventListener("click", function () {
  stepPeople(-1);
});

plusBtn.addEventListener("click", function () {
  stepPeople(1);
});

tipButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    tipInput.value = button.dataset.tip;
    clearError(tipInput);
    highlightTipPreset();
    recalculateIfLive();
  });
});

billInput.addEventListener("input", recalculateIfLive);

peopleInput.addEventListener("input", function () {
  syncCounterButtons();
  recalculateIfLive();
});

tipInput.addEventListener("input", function () {
  highlightTipPreset();
  recalculateIfLive();
});

resetBtn.addEventListener("click", resetAll);

// ------------------------------------------------------------------- start --

fieldInputs.forEach(function (input) {
  const note = noteFor(input);
  note.dataset.hint = note.textContent;
});

highlightTipPreset();
syncCounterButtons();
hideResult();
