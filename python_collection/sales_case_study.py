#store and organze first 6 month sales

sales = [100000 , 120000 , 110000 , 115000 , 100000 , 11600]
#          0        1        2        3         4        5

march_month = [2]

#update may month sales as 195000
update_march_month = sales [4] = 105000

#display all sales using index
for i in range(0,len(sales)):

    print (sales[i])

#display sales > 10000
for amount in sales:

    if amount > 100000:
        print(amount)