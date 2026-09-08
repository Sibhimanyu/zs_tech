# 1. Find orders by status — FIXED
# Bug was: `return matching_orders` sat inside the for loop, right after
# the first append. So the function returned the moment it found the
# FIRST match instead of finishing the loop. That is why order 101
# printed but 103 never got a chance to be checked.
# Fix: move the return outside the loop (dedent it) so the loop finishes
# checking every order first.

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


results = find_orders_by_status("Delivered")

for order in results:
    print(order["id"])
