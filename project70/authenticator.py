class Authenticator:
    #------------Attributes------------
    def __init__(self, bank):
        self.bank = bank
    
    #------------Methods------------
    def authenticate(self, card_number, pin):
        for account in self.bank.accounts.values():
            if account.linked_card and account.linked_card.number == card_number and account.linked_card.get_pin() == pin:
                return account
        return None

