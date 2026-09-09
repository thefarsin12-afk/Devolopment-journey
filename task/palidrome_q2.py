"""
2. Check if a String is a Palindrome

Question:
Write a function that checks whether a given string is a palindrome.

Example:
Input: "madam"
Output: Palindrome

Input: "hello"
Output: Not Palindrome
"""

def palidrome(word):

    original_word = word

    reverse = ""

    for chara in word.lower():
        reverse = chara + reverse

    if original_word.lower() == reverse:
        print(f"Palidrome {reverse}")

    else:print("Not Palidrome") 

palidrome("Madam")       