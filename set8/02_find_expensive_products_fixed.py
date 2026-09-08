# 2. Find expensive products — FIXED
# Bug was: same shape as problem 1. `return expensive_products` was
# indented inside the for loop, right after the first match is appended.
# Keyboard (1500) matches and the function returned immediately, so
# Monitor (12000) never got checked even though it also qualifies.
# Fix: move the return outside the loop.

products = [
    {"name": "Keyboard", "price": 1500},
    {"name": "Mouse", "price": 700},
    {"name": "Monitor", "price": 12000},
    {"name": "USB Cable", "price": 400}
]


def find_expensive_products(minimum_price):
    expensive_products = []

    for product in products:
        if product["price"] >= minimum_price:
            expensive_products.append(product)

    return expensive_products


results = find_expensive_products(1000)

for product in results:
    print(product["name"])
