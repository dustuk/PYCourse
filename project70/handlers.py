from transactions import *

class WithdrawHandler:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
    
    #------------Methods------------
    def handle(self, account):
        while True:
            amount = self.atm.keypad.get_input("Enter the amount to withdraw: ")
            try:
                amount = int(amount)
                if amount <= 0:
                    self.atm.screen.show_message("Invalid amount, Please enter a positive value.")
                    continue
                transaction = WithdrawTransaction(amount, self.atm)
                transaction.execute(account)
                break
            except ValueError:
                self.atm.screen.show_message("Invalid input. Please enter a valid amount.")


class DepositHandler:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
    
    #------------Methods------------
    def handle(self, account):
        while True:
            amount = self.atm.keypad.get_input("Enter the amount to deposit: ")
            try:
                amount = int(amount)
                if amount <= 0:
                    self.atm.screen.show_message("Invalid amount, Please enter a positive value.")
                    continue
                transaction = DepositTransaction(amount, self.atm)
                transaction.execute(account)
                break
            except ValueError:
                self.atm.screen.show_message("Invalid input. Please enter a valid amount.")


class TransferHandler:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
        
    #------------Methods------------
    def handle(self, account):
        while True:
            amount = self.atm.keypad.get_input("Enter the amount to transfer: ")
            destination_account_number = self.atm.keypad.get_input("Enter the destination account number: ")
            try:
                amount = int(amount)
                if amount <= 0:
                    self.atm.screen.show_message("Invalid amount, Please enter a positive value.")
                    continue
                transaction = TransferTransaction(amount, destination_account_number, self.atm)
                transaction.execute(account, self.atm.bank)
                break
            except ValueError:
                self.atm.screen.show_message("Invalid input. Please enter a valid account number.")


class BalanceInquiryHandler:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
        
    #------------Methods------------
    def handle(self, account):
        transaction = BalanceInquiryTransaction(self.atm)
        transaction.execute(account)


class ViewTransactionsHandler:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
        
    #------------Methods------------
    def handle(self, account):
        transaction = ViewTransactionsTransaction(self.atm)
        transaction.execute(account)


class ChangePinHandler:
    #-----------Variables-----------
    MAX_ATTEMPTS = 3

    #-----------Attributes-----------    
    def __init__(self, atm):
        self.atm = atm

    #------------Methods------------
    def get_old_pin(self, account):
        for attempt in range(self.MAX_ATTEMPTS):
            old_pin = self.atm.keypad.get_input("Enter your old PIN: ", secure=True)
            if account.linked_card.set_pin(old_pin, old_pin):
                return old_pin
            if attempt == self.MAX_ATTEMPTS - 1:
                self.atm.screen.clear_screen()
                self.atm.screen.show_message("Maximum attempts reached")
                self.atm.screen.exit_massage()
            self.atm.screen.clear_screen()
            self.atm.screen.show_message("Incorrect PIN. Please try again.")

    def get_new_pin(self, old_pin):
        while True:
            new_pin = self.atm.keypad.get_input("Enter your new PIN: ", secure=True)
            if new_pin == old_pin:
                self.atm.screen.show_message("New PIN cannot be the same as the old PIN.")
            elif len(new_pin) == 4 and new_pin.isdigit():
                return new_pin
            else:
                self.atm.screen.show_message("PIN must be 4 digits. Please try again.")

    def confirm_new_pin(self, old_pin, new_pin, account):
        for attempt in range(self.MAX_ATTEMPTS):
            confirm_pin = self.atm.keypad.get_input("Confirm your new PIN: ", secure=True)
            if confirm_pin == new_pin:
                account.linked_card.set_pin(old_pin, new_pin)
                self.atm.screen.show_message("PIN change successful.")
                return True
            if attempt == self.MAX_ATTEMPTS - 1:
                self.atm.screen.clear_screen()
                self.atm.screen.show_message("Maximum attempts reached")
                return False
            self.atm.screen.clear_screen()
            self.atm.screen.show_message("PIN confirmation failed. Please try again.")
        return False

    def handle(self, account):
        old_pin = self.get_old_pin(account)
        new_pin = self.get_new_pin(old_pin)
        self.confirm_new_pin(old_pin, new_pin, account)

