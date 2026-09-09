
# realtive path link note correct then error using:try,execpt,finally
try:
    fr = open("error_handling\\ey_words.txt")
    for line in fr:

        print(line)

except Exception as e:

    print(e)

finally:

    print("db commit...")            