# 5. Even or Odd, One to N
# Loop from 1 to n and say whether each number is even or odd.

n = 4

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
