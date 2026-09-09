source = "type a word..."

target = "type a word..."

position = 0

for chara in source.lower():
    if chara < position(len(target)):
        position = position + 1

if position == len(target):
    print("Kangaroo word")

else:print("Not kangaroo word")            
