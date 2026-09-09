"""
3. Ignore Spaces 
Check whether a sentence is a palindrome, ignoring spaces.
Example:
Input: "nurses run"
Output: Palindrome
"""

def ignor_space_palidrome(word):

    orinanal_word = word

    reverse = ""

    for chara in word.lower():

        reverse = chara+ reverse

    if orinanal_word == reverse:
        print("Palidrome")

    else:print("Not palidrome")

ignor_space_palidrome("nurses run")            