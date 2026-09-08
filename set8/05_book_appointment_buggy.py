# 5. Book appointment — BUGGY (original, not corrected)
# This is the code as given. Booking Dr. Kumar at 2:00 PM prints
# "Time slot unavailable" even though he is free at that time.

appointments = [
    {"doctor": "Dr. Kumar", "time": "10:00 AM"},
    {"doctor": "Dr. Sharma", "time": "11:00 AM"}
]


def book_appointment(doctor, time):
    for appointment in appointments:
        if appointment["doctor"] == doctor:
            return "Time slot unavailable"

    appointments.append({
        "doctor": doctor,
        "time": time
    })

    return "Appointment booked"


print(book_appointment("Dr. Kumar", "2:00 PM"))
