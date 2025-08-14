from keypad import Keypad
from screen import Screen   
from handlers import *

class AtmInterface:
    #-----------Attributes-----------
    def __init__(self, bank, location):
        self.bank = bank
        self.location = location
        self.keypad = Keypad()
        self.screen = Screen()
        self.withdraw_handler = WithdrawHandler(self)
        self.deposit_handler = DepositHandler(self)
        self.transfer_handler = TransferHandler(self)
        self.balance_inquiry_handler = BalanceInquiryHandler(self)
        self.view_transactions_handler = ViewTransactionsHandler(self)
        self.change_pin_handler = ChangePinHandler(self)
    
    #------------Methods------------
    def display_main_menu(self, account):
        self.screen.clear_screen()
        while True:
            self.screen.show_message("Main Menu")
            self.screen.show_message("1. Withdraw")
            self.screen.show_message("2. Deposit")
            self.screen.show_message("3. Transfer")  
            self.screen.show_message("4. Balance Inquiry")
            self.screen.show_message("5. View Transactions")
            self.screen.show_message("6. Change PIN")
            self.screen.show_message("7. Exit")
            choice = self.keypad.get_input("Enter your choice: ")
            match choice:
                case "1":
                    self.withdraw_handler.handle(account)
                case "2":
                    self.deposit_handler.handle(account)
                case "3":
                    self.transfer_handler.handle(account)
                case "4":
                    self.balance_inquiry_handler.handle(account)        
                case "5":
                    self.view_transactions_handler.handle(account)
                case "6":
                    self.change_pin_handler.handle(account)
                case "7":
                    self.screen.clear_screen()
                    self.screen.exit_massage()
                case _:
                    self.screen.show_message("Invalid choice. Please try again.")
            self.keypad.get_input("\nPress Enter to continue...")
            self.screen.clear_screen()

