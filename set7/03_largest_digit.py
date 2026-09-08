# 3. Largest Digit in a Number
# Find the biggest digit without using max().
# I keep the biggest one I have seen so far and replace it when I find a bigger one.

number = 47380

biggest = 0
secondBig = 0
smallest = 10

for digit in str(number):
    if int(digit) > biggest:
        secondBig = biggest
        biggest = int(digit)
    if int(digit) < smallest:
        smallest = int(digit)

print(biggest)
print(secondBig)
print(smallest)
