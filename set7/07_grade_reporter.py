# 7. Live Grade Reporter
# Ask for n scores one at a time and print the grade straight away.
# Nothing is stored: the score is used and then thrown away on the next loop.

n = int(input("How many scores? "))

for i in range(n):
    score = int(input("Score: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")
