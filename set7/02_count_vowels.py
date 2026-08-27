# 2. Count the Vowels
# Loop through the letters of a word and count the vowels.

word = "programming"
vowels = "aeiou"

count = 0
for letter in word:
    if letter in vowels:
        count += 1

print(count)
