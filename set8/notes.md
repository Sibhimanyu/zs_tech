## Problem solving - logical thinking

Ten files, two per problem: a `_buggy.py` (the original code exactly as
given, unmodified) and a `_fixed.py` (the corrected version), each with a
comment at the top explaining the bug. Run any of them, e.g.
`python3 01_find_orders_by_status_buggy.py` and
`python3 01_find_orders_by_status_fixed.py`, to see the wrong output
before and the right output after.

For each one: what I saw when I ran it, what the actual bug was, and why
it caused that specific wrong output.

## 1. Find orders by status

Ran it first and only got `101`, even though 103 is also Delivered.

The `return matching_orders` line was indented inside the `for` loop, right
under the `append`. So the very first time the status matches, the function
appends the order and immediately returns — it never gets to loop around to
order 103. The loop needs to finish checking every order before returning,
so the fix is just dedenting that return to line up with the `for`, outside it.

## 2. Find expensive products

Same shape of bug as problem 1. Expected `Keyboard` and `Monitor`, got only
`Keyboard`.

Keyboard (1500) is the first product and it already meets the >= 1000
condition, so the function appended it and returned on the spot — Monitor
(12000) never even got looked at. Fix: move `return expensive_products`
out of the loop.

## 3. Find failed students

Expected `Ravi` and `Meera`, got nothing at all — not even an error, just
an empty result.

This one's trickier: the return was indented to be inside the `for` loop
but outside the `if`. So no matter what happens on the first student
checked, the function returns right after checking them once. The first
student in the list is Asha, who passes (78 marks), so `failed_students`
is still `[]` when it returns after that one check. Ravi and Meera never
get checked. Fix: dedent the return so it's outside the whole loop, not
just outside the `if`.

## 4. Find available rooms

Expected 201 and 203 (the Available ones), got 202 and 204 instead — the
exact opposite.

The condition was `if room["status"] != "Available"`, which collects every
room that is NOT available. Simple sign flip: `!=` should be `==`.

## 5. Book appointment

Tried booking Dr. Kumar at 2:00 PM, expected "Appointment booked", got
"Time slot unavailable" instead.

The check `if appointment["doctor"] == doctor` only compares the doctor
name, so as soon as it finds any existing appointment for Dr. Kumar (the
10:00 AM one) it rejects the new booking, regardless of the time. It
should only reject when the doctor AND the time both match an existing
appointment. Fix: `if appointment["doctor"] == doctor and
appointment["time"] == time`.
