class Bank:
    #-----------Attributes-----------
    def __init__(self, name, bank_swif_code):
        self.name = name
        self.bank_code = bank_swif_code
        self.accounts = {}
    
    #------------Methods------------
    def add_customer(self, customer):
        for account in customer.accounts.values():
            self.accounts[account.account_number] = account
