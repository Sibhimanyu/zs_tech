# 3. Find failed students — FIXED
# Bug was: `return failed_students` was indented one level too far in —
# it sat inside the for loop but outside the if. So the loop returned
# after checking just the FIRST student (Asha, who passes), no matter
# what happens with anyone else. failed_students was still empty at that
# point, so nothing printed at all.
# Fix: move the return outside the for loop entirely, so every student
# gets checked before the function returns.

students = [
    {"name": "Asha", "marks": 78},
    {"name": "Ravi", "marks": 32},
    {"name": "Kiran", "marks": 65},
    {"name": "Meera", "marks": 28}
]


def find_failed_students():
    failed_students = []

    for student in students:
        if student["marks"] < 40:
            failed_students.append(student)

    return failed_students


results = find_failed_students()

for student in results:
    print(student["name"])
