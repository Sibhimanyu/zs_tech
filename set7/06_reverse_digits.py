# 6. Reverse the Digits of a Number
# No reversed() and no slicing.
# Each new digit goes in front of what I have built so far, so the order flips.

number = 12345

reversed_digits = ""
for digit in str(number):
    reversed_digits = digit + reversed_digits

print(reversed_digits)
