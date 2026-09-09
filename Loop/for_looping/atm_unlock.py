atm_pin = 1234

for pin in range(1,4):
   
   atm=int(input("Enter your atm pin"))

   if atm == atm_pin:
        print("Youre account opened")
        break

else:
    print("BLOCKED")     