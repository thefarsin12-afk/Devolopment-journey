word = ["madam","tan","ant","racecar","malayalam"]

palindrome = []

for ch in word:

    reverse = ch[::-1]

    if ch == reverse:
        palindrome.append(reverse)
print(palindrome)