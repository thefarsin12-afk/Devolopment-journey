"""w.a.p display vowel count"""

word="supercalifragilisticexpialidocious"

vovel_count = 0

for count in word:

    if count.lower() in "aeiou":

        vovel_count = vovel_count+1

print(f"vovel_count",{vovel_count})    