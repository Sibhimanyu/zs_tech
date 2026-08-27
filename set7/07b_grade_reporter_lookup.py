# 7b. Live Grade Reporter, without a score variable
# An alternative I tried. The main answer is 07_grade_reporter.py.
#
# The score is used exactly once, so it never needs a name.
# score // 10 turns 0 to 100 into a bucket from 0 to 10, and each position
# in the string is the grade for that bucket:
#
#   index:  0  1  2  3  4  5  6  7  8  9  10
#   grade:  F  F  F  F  F  F  F  C  B  A  A
#
# Known bug I left in on purpose: a negative score gets an A.
# -5 // 10 is -1, because Python floors downwards, and a negative index
# counts from the end of the string, so it lands on the last A.
# The if / elif version in 07_grade_reporter.py prints F for -5, correctly.

n = int(input("How many scores? "))

for i in range(n):
    print("FFFFFFFCBAA"[int(input("Score: ")) // 10])
