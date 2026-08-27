# 3. Largest Digit in a Number
# Find the biggest digit without using max().
# I keep the biggest one I have seen so far and replace it when I find a bigger one.

number = 47382

biggest = 0
for digit in str(number):
    if int(digit) > biggest:
        biggest = int(digit)

print(biggest)
