'''
### 5. Sleep Duration
- < 6: Sleep Deprived
- 6 – 8: Healthy Sleep
- > 8: Oversleeping
'''
sleep_time = int(input("Enter your duration"))

if sleep_time <6:
    print("Sleep Deprived")

elif sleep_time >=6 and sleep_time <=8:
    print("Healthy Sleep")

else:
    print("Over sleep")    