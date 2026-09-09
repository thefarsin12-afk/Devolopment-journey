"""

4.  Add “.com” to each website name
    Input:[“google”,“amazon”,“github”,“openai”]
    Output:[“google.com”,“amazon.com”,“github.com”,“openai.com”]

"""

domains = ["Google","Amazon","Github","Openai"]

result = [d+".com" for d in domains]

print(result)