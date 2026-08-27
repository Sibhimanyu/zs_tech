# 8. First Repeated Digit
# Find the first digit that has already appeared earlier in the number.
# The digits I have seen are kept in a string, not a list.

number = 4927492

seen = ""
found = ""
for digit in str(number):
    if digit in seen:
        found = digit
        break
    seen += digit

if found == "":
    print("No repeated digit")
else:
    print(found)
