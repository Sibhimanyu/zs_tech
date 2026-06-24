# Level 2: build "Hello, World!" from ASCII codes (no string literal)
codes = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
print("".join(chr(c) for c in codes))
