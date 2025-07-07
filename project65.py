def main():
    while True:
        project_num = input("Enter a project number (1-3), or 'q' to quit: ")
        if project_num == "1":
            project1()
        elif project_num == "2":
            project2()
        elif project_num == "3":
            project3()
        elif project_num.lower() == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

def project1():
   # 1. Fix the Stupid Class
    class Hamada:
        def __init__(self):
            self.name = 'Hamada'
            self.age = 25
            self.job = 'Hamada'


        def stupid(self):
            print('Hamada is not stupid')
            
    # make an instance of the class Hamada
    hamada = Hamada()
    
    # print the attributes of the instance
    print(hamada.name)
    print(hamada.age)
    print(hamada.job)
    
    # call the method stupid() of the instance
    hamada.stupid()
    
    # add an attribute to the instance hamada
    hamada.phonenumber = '0123456789'
    
    # print the attribute phonenumber of the instance
    print(hamada.phonenumber)
    
    # Edit the attribute age of the instance hamada
    hamada.age = 35
    
    # print the attribute age of the instance
    print(hamada.age)

def project2():
   class Item:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity
        
        def display(self):
            print(f"Name: {self.name}")
            print(f"Price: ${self.price}")
            print(f"Quantity: {self.quantity}")
            print(f"Total: ${self.price * self.quantity}")

   item1 = Item("Atomic Habits", 10, 2)
   item2 = Item("Deep Work", 20, 1)
   #Display item information
   item1.display()
   item2.display()


def project3():
    class BankAccount:
        def __init__(self, account, balance):
            self.account = account
            self.balance = balance
                
        def display_balance(self):
            print(f"Account: {self.account}") 
            print(f"Balance: ${self.balance}")
        
        def add_money(self, amount):
            if amount < 0:
                print("Invalid amount. added amount must be positive.")
                return
            self.balance += amount
            print(f"added ${amount} into account {self.account}")

        def withdraw(self, amount):
            if amount < 0:
                print("Invalid amount. withdraw amount must be positive.")
                return
            if amount > self.balance:
                print("Insufficient funds or invalid amount.")
                return
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account}")
    
    account1 = BankAccount("5577", 1000)
    account1.display_balance() # Account 5577 balance: 1000
    account1.add_money(500) # added 500 into account 5577.
    account1.display_balance() # Account 5577 balance: 1500
    account1.add_money(-100)
    # Invalid amount. added amount must be positive.
    account1.display_balance() # Account 5577 balance: 1500
    account1.withdraw(200) # Withdrew 200 from account 5577.
    account1.display_balance() # Account 5577 balance: 1300
    account1.withdraw(1500)
    # Insufficient funds or invalid amount.
    account1.display_balance() # Account 5577 balance: 1300
        
main()