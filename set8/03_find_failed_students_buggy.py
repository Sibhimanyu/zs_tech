# 3. Find failed students — BUGGY (original, not corrected)
# This is the code as given. Run it and nothing prints at all.

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
