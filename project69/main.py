import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    #------------------Attributes------------------
    def __init__(self):
        self.name = ""
        self.symbol = ""
        
    #------------------Methods------------------
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, please use letters only.")
            
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, Choose your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol, please use a single letter.")


class Menu:
    #------------------Methods------------------
    def display_main_menu(self):
        while True: 
            print("welcome to tic tac toe game")
            print("1. Start Game")
            print("2. Quit Game")
            choice = input("Enter your choice (1 or 2): ")
            if self.validate_choice(choice):
                return choice
    
    def display_endgame_menu(self):
        while True:
            print("Game Over")
            print("1. Restart Game")
            print("2. Quit Game")
            choice = input("Enter your choice (1 or 2): ")
            if self.validate_choice(choice):
                return choice

    def validate_choice(self, choice):
        if choice not in ["1", "2"]:
            print("Invalid choice, please try again.")
            return False
        return True
    
    
class Board:
    #------------------Attributes------------------
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    
    #------------------Methods------------------
    def display_board(self):
         for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice].isdigit()
        
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]
    
    
class Game:
    #------------------Attributes------------------
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    
    #------------------Methods------------------
    def start_game(self):
        clear_screen()
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game() 
    
    def setup_players(self):
        used_symbols = set()
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            while True:
                player.choose_symbol()
                if player.symbol not in used_symbols:
                    used_symbols.add(player.symbol)
                    break
                else:
                    print("Symbol already taken. Choose a different one.")
            clear_screen() 
            
    def play_game(self):
        while True:
            self.play_turn()
            has_winner = self.check_win()
            if has_winner or self.check_draw():
                clear_screen()
                self.board.display_board()
                if has_winner:
                    print(f"{self.players[1 - self.current_player_index].name} ({self.players[1- self.current_player_index].symbol}) wins!")
                else:
                    print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
     
    def play_turn(self):
        clear_screen()
        self.board.display_board()
        player = self.players[self.current_player_index]
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Enter the cell number (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice - 1, player.symbol):
                    break
                else:
                    print("Invalid move, please try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        
        self.switch_player()
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        
    def check_win(self):
        WINNING_COMBINATIONS = [
            [0, 1, 2],  # الصف العلوي
            [3, 4, 5],  # الصف الأوسط
            [6, 7, 8],  # الصف السفلي
            [0, 3, 6],  # العمود الأول
            [1, 4, 7],  # العمود الثاني
            [2, 5, 8],  # العمود الثالث
            [0, 4, 8],  # القطر من اليسار لليمين
            [2, 4, 6],  # القطر من اليمين لليسار
        ]
        
        for combo in WINNING_COMBINATIONS:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False
    
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
    
    def quit_game(self):
        print("Thank you for playing!")
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.start_game()