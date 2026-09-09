fr_all_students = open("file_operator\\fr_all_students.txt","r")

fr_passed_students = open("file_operator\\fr_passed_students.txt","r")

fw_failed_students = open("file_operator\\fw_failed_students.txt","w")

all_students = {all.rstrip("\n") for all in fr_all_students}

passed_students = {p.rstrip("\n") for p in fr_passed_students}

failed_students = all_students.difference(passed_students)

for f in failed_students:

    fw_failed_students.write(f + "\n")

print("complted")    
