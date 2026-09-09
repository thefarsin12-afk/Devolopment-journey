# vowel_count, consonant_count
word="pneumonoultramicroscopicsilicovolcanoconiosis"

vowel = 0

constant = 0

for check in word:

    if check in "aeiou":

        vowel += 1

    else:

        constant += 1

print(f"vowel, {vowel}")

print(f"constant, {constant}")