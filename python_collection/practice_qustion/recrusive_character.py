#identfy first occurence
word = ["a","b","a","c","d"]

first_ocurence = []

for ch in word:

    if ch in first_ocurence:
        print(ch)
        break

    else:
        first_ocurence.append(ch)

#method in dictionary
#better in dictinary beacuse fast is dictionary
word = ["a","b","b","a","c","d"]

first_ch = {}

for ch in word:

    if ch in first_ch:
        print(ch)
        break

    else:
        first_ch [ch]=1