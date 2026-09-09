text = "a man a canal panama"

consonats = { ch for ch in text if ch not in "aeiou" and ch.isalpha()}

print(consonats)