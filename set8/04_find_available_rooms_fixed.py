# 4. Find available rooms — FIXED
# Bug was: the condition used `!=` instead of `==`. That collected every
# room whose status is NOT "Available" (202 Occupied, 204 Maintenance),
# which is the exact opposite of what the function is supposed to do.
# Fix: change `!=` to `==` so it collects rooms that ARE available.

rooms = [
    {"number": 201, "status": "Available"},
    {"number": 202, "status": "Occupied"},
    {"number": 203, "status": "Available"},
    {"number": 204, "status": "Maintenance"}
]


def find_available_rooms():
    available_rooms = []

    for room in rooms:
        if room["status"] == "Available":
            available_rooms.append(room)

    return available_rooms


results = find_available_rooms()

for room in results:
    print(room["number"])
