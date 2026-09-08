# 5. Book appointment — FIXED
# Bug was: the check only compared the doctor, not the time. So it
# rejected Dr. Kumar for ANY new time slot just because he already has
# one appointment at 10:00 AM, even though 2:00 PM is free.
# Fix: only reject when BOTH the doctor and the time match an existing
# appointment (i.e. that exact slot is already taken).

appointments = [
    {"doctor": "Dr. Kumar", "time": "10:00 AM"},
    {"doctor": "Dr. Sharma", "time": "11:00 AM"}
]


def book_appointment(doctor, time):
    for appointment in appointments:
        if appointment["doctor"] == doctor and appointment["time"] == time:
            return "Time slot unavailable"

    appointments.append({
        "doctor": doctor,
        "time": time
    })

    return "Appointment booked"


print(book_appointment("Dr. Kumar", "2:00 PM"))
