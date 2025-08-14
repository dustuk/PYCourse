import os
import sys

class Screen:
    #------------Methods------------
    def show_message(self, message):
        print(message)
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exit_massage(self):
        print("Card Ejecting...")
        print("Goodbye!")
        sys.exit()

