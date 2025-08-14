class Account:
    #-----------Attributes-----------
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.linked_card = None
        self.transaction_history = []
    
    #------------Methods------------
    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)
    
    def link_card(self, card):
        self.linked_card = card

