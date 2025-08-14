from account import Account
from bank import Bank
from customer import Customer   
from atm import AtmInterface
from cardReader import CardReader
from card import Card

def main():
    hsbc_bank = Bank("HSBC", "HSBCEGXX")

    customer1 = Customer("John Doe", "123 Main St", "123-456-7890", "V4OQd@example.com")
    account1 = Account("123456789")
    card1 = Card("1234-5678-9012-3456", "1234")
    
    customer2 = Customer("Sarah Smith", "123 Main St", "233-456-7890", "HtNwI@example.com")
    account2 = Account("987654321")
    card2 = Card("2345-6789-0123-4567", "2345")
    
    customer1.add_account(account1)
    hsbc_bank.add_customer(customer1)
    account1.link_card(card1)

    customer2.add_account(account2)
    hsbc_bank.add_customer(customer2)
    account2.link_card(card2)

    atm = AtmInterface(hsbc_bank, "123 Main St")
    card_reader = CardReader(atm)
    card_reader.insert_card(card1) 
    
if __name__ == "__main__": 
    main()