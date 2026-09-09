langueges = ["Good morning","Good afternoon","Good night"]

fw = open("file_operator\\db_text","w")

for l in langueges:

    fw.write(l+"\n")