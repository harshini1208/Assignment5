class Bank:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        while True:
            user_input=input("""hello,what you like to do
                             1  Enter 1 to create pin
                             2 Enter 2 to deposit
                             3  enter 3 to withdraw
                             4  enter 4 to check balance
                             5  enter 5 to exit""")
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=="5":
                break

            else:
                print("invalid option")

    def create_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully")
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to deposit"))
            self.balance=self.balance+amount
            print("deposit successfully")
            print(f"available balance after deposit{self.balance}")
        else:
            print("invalid pin")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to withdraw"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("succesfully withdraw")
                print("The available balance i :",self.balance)
            else:
                print("insufficient balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
Bank()




