from authenticator import Authenticator

class CardReader:
    #-----------Attributes-----------
    def __init__(self, atm):
        self.atm = atm
        self.authenticator = Authenticator(self.atm.bank)
    
    #------------Methods------------
    def insert_card(self, card):
        for i in range(3):
            pin = self.atm.keypad.get_input("Please enter your PIN: ", secure=True)
            account = self.authenticator.authenticate(card.number, pin)
            if account:
                self.atm.display_main_menu(account)
                break
            else:
                if i == 2:
                    self.atm.screen.clear_screen()
                    self.atm.screen.show_message("Maximum attempts reached")
                    self.atm.screen.show_message("Card Ejecting...")
                    self.atm.screen.show_message("Goodbye!")
                else:
                    self.atm.screen.clear_screen()
                    self.atm.screen.show_message("Incorrect PIN. Please try again.")
        return None

