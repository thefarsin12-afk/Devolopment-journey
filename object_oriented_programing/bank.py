class Bank:

    acc_number : int

    balance : int

    ac_type : int

    customer_name : str

    def set_account(self,acc_number,balance,ac_type,custommer_name):

        self.acc_number = acc_number

        self.balance = balance

        self.ac_type = ac_type 

        self.customer_name = custommer_name

        print("Account has been created")

    def deposit(self,amount):

        self.balance += amount

        print(f"your {self.acc_number} has been credited with {amount} aval ba is {self.balance} ")


    def withdrw(self,amount):

        if self.balance < amount:

            raise Exception ("Insufiecient Balance...")

        else:
            self.balance -= amount
            print(f"your {self.acc_number} has been debited {amount} aval bal is {self.balance}")

    def get_balance(self):

        print(self,self.balance)

set_account = Bank()

set_account.set_account(123499,2000,2134,"Saleem")

set_account.deposit(2000)






    