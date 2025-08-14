import msvcrt

class Keypad:
    #------------Methods------------
    def get_secure_input(self, message):
        print(message, end="", flush=True)
        secure_input = ""
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}:  # Enter
                print()
                break
            elif char == b'\x08':  # Backspace
                if secure_input:
                    secure_input = secure_input[:-1]
                    print("\b \b", end="", flush=True)
            else:
                try:
                    char_decoded = char.decode('utf-8')
                except UnicodeDecodeError:
                    continue
                secure_input += char_decoded
                print("*", end="", flush=True)
        return secure_input
    
    def get_input(self, message, secure=False):
        return self.get_secure_input(message) if secure else input(message)

