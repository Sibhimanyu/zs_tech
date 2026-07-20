# Level 2: build "Hello, World!" from ASCII codes (no string literal)
codes = [1,2,3,4,5,6,7]
a = ""
for c in codes:
    a += chr(c)
print(a)