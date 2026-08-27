## Loops practice set

Eight files, one per problem. Run any of them with `python3 01_sum_to_n.py`.

The input is a variable at the top of each file, so I can change it and run it again. Problem 7 is the only one that asks the user, because that problem says to.

For each one I wrote down what the loop variable actually is, a trace I did by hand, and one edge case I checked.

## 1. Sum of numbers 1 to n

`i` is the number I am adding right now. It goes 1, 2, 3 up to n. `total` is everything added so far.

Trace with n = 6: total starts at 0, then becomes 1, 3, 6, 10, 15, 21.

`range(1, n + 1)` needs the `+ 1` because range stops before the last number. Without it the loop would end at 5 and print 15.

Edge case: n = 0. The range is empty so the loop never runs and it prints 0, which is right.

## 2. Count the vowels

`letter` is one character of the word. `count` is how many vowels I have found so far.

Trace with "programming": r no, o yes (1), g no, r no, a yes (2), m no, m no, i yes (3), n no, g no. So 3.

I used `if letter in vowels` with vowels as the string "aeiou" instead of writing five `or` conditions.

Edge case: "rhythm" has no vowels and prints 0. It also only works on lowercase, so "PROGRAMMING" would print 0. I would fix that with `word.lower()` if it mattered.

## 3. Largest digit

`digit` is one character of the number as text. `biggest` is the largest one I have seen up to this point.

I turn the number into a string so I can loop over the digits, then turn each digit back into an int to compare it.

Trace with 47382: biggest starts at 0, 4 is bigger so 4, 7 is bigger so 7, 3 is not, 8 is bigger so 8, 2 is not. Answer 8.

Starting `biggest` at 0 is safe because no digit is below 0, so the first digit always replaces it.

Edge cases: a single digit like 7 prints 7, because the one loop step replaces the starting 0. A tie like 5225 prints 5 once, since I use `>` and not `>=` it keeps the first one it found, but the answer is the same either way. A negative number would break it, because the minus sign is not a digit.

## 4. Multiplication table

`i` is which multiple I am on, 1 to 10. `n` never changes inside the loop.

Trace with n = 4: 4 x 1 = 4, then 4 x 2 = 8, and so on to 4 x 10 = 40. Ten lines.

`range(1, 11)` is fixed here because the table is always 1 to 10, so it does not depend on the input.

Edge case: n = 0 prints ten lines that all end in 0. That is not wrong, just boring.

## 5. Even or odd, 1 to n

`i` is the number being tested. Nothing is remembered between steps, each number is checked on its own.

`i % 2` is the remainder after dividing by 2. It is 0 for even numbers and 1 for odd ones.

Trace with n = 4: 1 has remainder 1 so Odd, 2 has remainder 0 so Even, 3 Odd, 4 Even.

Edge case: n = 0 prints nothing at all, because the range is empty. I checked that it does not crash.

## 6. Reverse the digits

`digit` is one character of the number. `reversed_digits` is the answer I am building.

The trick is `digit + reversed_digits` and not the other way around. Every new digit goes in front of what I already have, so the order comes out backwards.

Trace with 12345: "" then "1", then "21", then "321", then "4321", then "54321".

If I had written `reversed_digits + digit` it would just rebuild the number in the same order.

Edge case: 1200 prints 0021. The digits really are reversed, but the leading zeros look odd. If the answer had to be a number I would wrap it in `int()`, which would give 21.

## 7. Live grade reporter

`i` is just the count of how many scores I have asked for. I never use `i` inside the loop, it only controls how many times the loop runs. `score` is the one score I am dealing with right now.

Nothing is stored. Each time round the loop `score` is overwritten, so the old score is gone. That is what the problem asked for.

`elif` matters here. Once a score matches one branch the rest are skipped, so I do not have to write `score >= 80 and score < 90`. A score of 95 stops at the first check.

Trace with 95, 82, 61: 95 is 90 or more so A. 82 fails the first check, passes 80 so B. 61 fails all three so F.

Edge case: n = 0 asks for no scores and just ends. A score like 200 still prints A, since I do not check for silly numbers.

### Doing it without a score variable

I wondered if I could avoid the `score` variable completely. That is in `07b_grade_reporter_lookup.py`.

My first idea was to put `input()` straight into the if chain, like `if int(input()) >= 90`. That does not work. Every `input()` is a new question, so one score would get asked for two or three times. Something has to hold the value if I want to check it more than once.

The version that does work uses no if at all:

```python
print("FFFFFFFCBAA"[int(input("Score: ")) // 10])
```

`score // 10` turns any score from 0 to 100 into a bucket from 0 to 10, and each position in that string is the grade for its bucket. The score is only used once, so it never needs a name. I checked the boundaries and 90 gives A, 89 gives B, 70 gives C and 69 gives F.

It has a bug I left in. A negative score gets an A. `-5 // 10` is `-1`, because Python rounds down instead of towards zero, and a negative index counts from the end of the string, so it lands on the last A. The if / elif version gives F for -5, which is right.

I am keeping the if / elif one as my real answer for two reasons. The problem asks for `if / elif / else` in its own tags, and the lookup skips them entirely. And the bucket trick only works because the cutoffs are exactly every ten. If the grades were 93, 85 and 78 the string would not line up any more, but `elif` would still read the same.

I also tried the walrus operator, `(s := int(input()))`, but that is still an assignment, so it does not really answer the question.

One more thing I had wrong at first: I thought the `score` variable was the thing the problem was telling me not to do. It is not. "Without storing the scores" means do not collect them in a list and go through them afterwards. One variable that gets overwritten is not storing them, because after the second loop the first score is gone for good. That is the actual point of the problem.

## 8. First repeated digit

`digit` is the digit I am looking at now. `seen` is a string of every digit before this one. `found` holds the answer.

The check has to happen before I add the digit to `seen`. If I added it first, every digit would look like a repeat of itself.

Trace with 4927492: 4 not in "" so seen is "4". 9 not in "4" so seen is "49". 2 so seen is "492". 7 so seen is "4927". Then 4 is already in "4927", so the answer is 4 and I break out.

I used `break` because the problem wants the first repeat, so once I have it there is no reason to keep looping.

Edge cases: 12345 has no repeat, so `found` stays empty and it prints "No repeated digit". A single digit like 7 also prints that, which is right, since one digit cannot repeat.

## What I noticed across all eight

Three of these (largest digit, reverse, first repeat) turn the number into a string first. That is because you cannot loop over an int directly, but you can loop over its digits as text.

Four of them use the same shape: start a variable before the loop, change it a bit on every step, then print it after the loop ends. `total`, `count`, `biggest` and `reversed_digits` are all doing the same job with different names.

The other four print inside the loop instead and do not remember anything, which is why the grade reporter can work without storing the scores.
