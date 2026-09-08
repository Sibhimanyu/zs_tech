# 1. Find orders by status — BUGGY (original, not corrected)
# This is the code as given. Run it and you only get 101, not 103.

orders = [
    {"id": 101, "status": "Delivered"},
    {"id": 102, "status": "Pending"},
    {"id": 103, "status": "Delivered"},
    {"id": 104, "status": "Cancelled"}
]


def find_orders_by_status(required_status):
    matching_orders = []

    for order in orders:
        if order["status"] == required_status:
            matching_orders.append(order)
            return matching_orders

    return matching_orders


results = find_orders_by_status("Delivered")

for order in results:
    print(order["id"])
