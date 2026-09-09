"""
string_object.lower() return lower case version of string object

string_object.upper() return uppercase version of string


string_object.isalpha() return true if string object is an alphabet

string_object.isdigit() return true if string object is an digit

string_object.isalnum() returns true if string object is alphanumeric


string_object.count(value) return frequency of value return 0 if value not exist

string_object.find(value) return index position of first occurance of value return -1 otherwise

string_object.rfind(value) return index position of last occurance of value return -1 otherwise

string_object.index(value) return index position of fiest occurance of value return error otherwise



string_object.startswith(substr) return True if string object starts with substr 
string_object.endswith(substr) return True if string object ends with substr 

string_object.replace(old,new) replace old string with new 

string_object.strip(value) remove value from both end
string_object.lstrip(value) remove value from begining
string_object.rstrip(value) remove value from end

"a" in "apple" 

"""

text="@hello@"

new_text = text.strip("@")

print(new_text)
# text = "i hate python"

# new_text = text.replace("hate","love")

# print(new_text)


# word= "python"

# print(word.startswith("Py"))

# print(word.endswith("in"))


# greetings = "good morning"

# uppercase_greetings = greetings.upper()

# print(uppercase_greetings)

# text = "HELLO THERE"

# lowercase_text = text.lower()

# print(lowercase_text)

# """
# isalpha()
# isdigit()
# isalnum()
# count(value) return frequency of value
# """

# text="helloworld"
# #     0123456789


# # l_count = text.count("hai")

# # print(l_count)

# print(text.find("v"))

# print(text.rfind("X"))


# # index(char)

# print(text.index("x"))