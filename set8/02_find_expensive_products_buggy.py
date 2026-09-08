# 2. Find expensive products — BUGGY (original, not corrected)
# This is the code as given. Run it and you only get Keyboard, not Monitor.

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

    return expensive_products


results = find_expensive_products(1000)

for product in results:
    print(product["name"])
