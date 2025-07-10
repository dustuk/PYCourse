def main():
    project_num = input("Enter a project number: ")
    
    if project_num == "1":
        project1()
    elif project_num == "2":
        project2()
    else:
        print("Invalid input, please enter 1 for project 1 or 2 for project 2.")


def project1():
    class Item:
        
        num_of_items = 0
        all_items = []
        
        def __init__(self, item, price, quantity):
            self.item = item
            self.price = price
            self.quantity = quantity
            Item.num_of_items += 1
            Item.all_items.append(self)
        
        def __str__(self):
            return f"\nItem: {self.item}\nPrice: {self.price}\nQuantity: {self.quantity}\n"
        
        def __repr__(self):
            return f"Item('{self.item}', {self.price}, {self.quantity})"
            
    
    # Create an item
    item1 = Item("Atomic Habits", 10, 2)
    item2 = Item("Deep Work", 20, 1)
    item3 = Item("So Good They Can't Ignore You", 15, 3)
    item4 = Item("Digital Minimalism", 12, 2)
    # Display the number of items
    print(f"Number of items: {Item.num_of_items}")
    # result:
    # Number of items: 4
    # Display all items
    print(Item.all_items)
    # result:
    # [Item('Atomic Habits', 10, 2), Item('Deep Work', 20, 1),
    # Item('So Good They Can't Ignore You', 15, 3), Item('Digital Minimalism', 12, 2)]
    # print each item in all_items
    for item in Item.all_items:
        print(item)
        print("##################")
    
    # result:
    # Item: Atomic Habits
    # Price: 10
    # Quantity: 2

    # ##################

    # Item: Deep Work
    # Price: 20
    # Quantity: 1

    # ##################

    # Item: So Good They Can't Ignore You
    # Price: 15
    # Quantity: 3

    # ##################

    # Item: Digital Minimalism
    # Price: 12
    # Quantity: 2

    # ##################


def project2():
    class BankAccount:
        
        bank_name = "Alawjan Bank"
        num_of_accounts = 0
        all_accounts = []
        
        def __init__(self, account, balance):
            self.account = account
            self.balance = balance
            BankAccount.num_of_accounts += 1
            BankAccount.all_accounts.append(self)
            
        def __str__(self):
            return f"\nAccount: {self.account}\nBalance: {self.balance}\n"
        
        def __repr__(self):
            return f"BankAccount('{self.account}', {self.balance})"
        
        def display_balance(self):
            print(f"Account: {self.account} Balance: ${self.balance}")
        
        def add_money(self, amount):
            if amount < 0:
                print("Invalid amount. added amount must be positive.")
                return
            self.balance += amount
            print(f"added ${amount} into account {self.account}")
        
        def withdraw(self, amount):
            if amount > self.balance or amount < 0:
                print("Insufficient funds or invalid amount.")
                return
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account}")
        
    print(BankAccount.bank_name) # Codezilla
    account1 = BankAccount("5577", 1000)
    account2 = BankAccount("1234", 2000)
    print(BankAccount.num_of_accounts)
    # 2
    print(BankAccount.all_accounts)
    # [BankAccount('5577', 1000), BankAccount('1234', 2000)]
    account1.display_balance()
    # Account 5577 balance: 1000
    account2.display_balance()
    # Account 1234 balance: 2000
    account1.add_money(500) # added 500 into account 5577.
    account1.display_balance() # Account 5577 balance: 1500
    account2.withdraw(1000) # Withdrew 1000 from account 1234.
    account2.display_balance() # Account 1234 balance: 1000
    account1.withdraw(2000) # Insufficient funds or invalid amount.
    account1.withdraw(-1000) # Insufficient funds or invalid amount.
    print(account1)
    # Account Number: 5577
    # Balance: $1500
    print(account2)
    # Account Number:1234
    # Balance: $1000


if __name__ == "__main__":
    main()