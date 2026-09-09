#chk credit score
credit_score=int(input("Enter your credit score"))

if credit_score>= 300 and credit_score<=579:
    print("Poor")

elif credit_score>=500 and credit_score<=660:
    print("Fair")

elif credit_score>=670 and credit_score<=739:
    print("Good")

elif credit_score>=740 and credit_score<=799:
    print("Very Good")

elif credit_score>=800 and credit_score<=850:
    print("Excelent")                