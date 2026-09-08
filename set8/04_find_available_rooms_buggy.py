# 4. Find available rooms — BUGGY (original, not corrected)
# This is the code as given. Run it and you get 202 and 204 (the
# unavailable rooms) instead of 201 and 203.

rooms = [
    {"number": 201, "status": "Available"},
    {"number": 202, "status": "Occupied"},
    {"number": 203, "status": "Available"},
    {"number": 204, "status": "Maintenance"}
]


def find_available_rooms():
    available_rooms = []

    for room in rooms:
        if room["status"] != "Available":
            available_rooms.append(room)

    return available_rooms


results = find_available_rooms()

for room in results:
    print(room["number"])
