from abc import ABC, abstractmethod
from enum import Enum
import uuid
import datetime

class TransactionType(Enum):
    #-----------Values-----------
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"
    BALANCE_INQUIRY = "Balance Inquiry"
    TRANSFER = "Transfer"
    VIEW_TRANSACTIONS = "View Transactions"


class Transaction(ABC):
    #-----------Attributes-----------
    def __init__(self, transaction_type, amount=None):
        self.transaction_id = uuid.uuid4()
        self.timestamp = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount
    
    #------------Abstract Methods------------
    @abstractmethod
    def execute(self, account):
        pass


class WithdrawTransaction(Transaction):
    #-----------Attributes-----------
    def __init__(self, amount, atm):
        super().__init__(TransactionType.WITHDRAW, amount)
        self.atm = atm

    #------------Methods------------
    def execute(self, account):
        if self.amount > account.balance:
            self.atm.screen.show_message("Insufficient funds.")
        elif self.amount % 50 != 0:
            self.atm.screen.show_message("Invalid amount. Must be a multiple of 50.")
        else:
            account.balance -= self.amount
            self.atm.screen.show_message(f"Withdrawal successful. New balance: {account.balance}")
            account.add_transaction(self)


class DepositTransaction(Transaction):
    #-----------Attributes-----------
    def __init__(self, amount, atm):
        super().__init__(TransactionType.DEPOSIT, amount)
        self.atm = atm
        
    #------------Methods------------
    def execute(self, account):
        if self.amount % 50 != 0:
            self.atm.screen.show_message("Invalid amount. Must be a multiple of 50.")
        elif self.amount > 5000:
            self.atm.screen.show_message("Maximum deposit amount is 5000.")
        else:
            account.balance += self.amount
            self.atm.screen.show_message(f"Deposit successful. New balance: {account.balance}")
            account.add_transaction(self)


class TransferTransaction(Transaction):
    #-----------Attributes-----------
    def __init__(self, amount, destination_account_number, atm):
        super().__init__(TransactionType.TRANSFER, amount)
        self.destination_account_number = destination_account_number
        self.atm = atm
    
    def execute(self, account, bank):
        if self.amount > account.balance:
            self.atm.screen.show_message("Insufficient funds.")
        elif self.amount % 50 != 0:
            self.atm.screen.show_message("Invalid amount. Must be a multiple of 50.")
        else:
            destination_account = bank.accounts.get(self.destination_account_number)
            if destination_account:
                account.balance -= self.amount
                destination_account.balance += self.amount
                self.atm.screen.show_message(f"Transfer successful. New balance: {account.balance}")
                transaction = TransferTransaction(self.amount, self.destination_account_number, self.atm)
                account.add_transaction(transaction)
                destination_account.add_transaction(transaction)
            else:
                self.atm.screen.show_message("Destination account not found.")


class BalanceInquiryTransaction(Transaction):
    #-----------Attributes-----------
    def __init__(self, atm):
        super().__init__(TransactionType.BALANCE_INQUIRY, amount=0)
        self.atm = atm
        
    #------------Methods------------
    def execute(self, account):
        self.amount = account.balance
        self.atm.screen.show_message(f"Your balance is: {account.balance}")
        account.add_transaction(self)


class ViewTransactionsTransaction(Transaction):
    #-----------Attributes-----------
    def __init__(self, atm):
        super().__init__(TransactionType.VIEW_TRANSACTIONS, amount=0)
        self.atm = atm

    #------------Methods------------
    def execute(self, account):
        self.amount = account.balance
        if not account.transaction_history:
            self.atm.screen.show_message("No transactions found.")
            return
        self.atm.screen.show_message("Transaction History:")
        for transaction in account.transaction_history:
            self.atm.screen.show_message(f"\nTransaction ID: {transaction.transaction_id}")
            self.atm.screen.show_message(f"Timestamp: {transaction.timestamp}")
            self.atm.screen.show_message(f"Transaction Type: {transaction.transaction_type.value}")
            self.atm.screen.show_message(f"Amount: {transaction.amount}")
        account.add_transaction(self)
