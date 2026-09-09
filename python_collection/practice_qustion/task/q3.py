attendance = ["p","p","a","a","o","o","h"]

set_attendance = set(attendance)

attendance_count = {}

for at in set_attendance:

    attendance_count [at] = attendance.count(at)

print(attendance_count)    