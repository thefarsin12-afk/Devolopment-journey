words = ["hello","hai","python","program"]

#{"hello:5", "hai:3", "python":6 ,"program":7}

add_hello = {word:len(word) for word in words}
print(add_hello)