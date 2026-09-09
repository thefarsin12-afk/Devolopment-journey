#Print all Armstrong numbers from 1 to 1000.
count = 0

for number in range(1,1000 + 1):
     
     original_number = number

     total = 0

     digit = len(str(number))

     temp = number


     while temp != 0:

      last_digit = temp % 10

      total = total + last_digit ** digit

      temp = temp // 10

     if total == original_number:
     
      print(original_number)

      count = count +1 
print(f"Total count is {count}")
     

      