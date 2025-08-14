class Customer:
    #-----------Attributes-----------
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.accounts = {}
    
    #------------Methods------------
    def add_account(self, account):
        self.accounts[account.account_number] = account

