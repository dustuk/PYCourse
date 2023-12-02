import random

winner_num = random.randint(1, 6)

print("Guess the Roll Dice!")
num = int(input("Enter a number between 1 and 6\n"))
print("-" * 20)

if 1 <= num <= 6:
    print(f"The Dice is {winner_num}")
    if num == winner_num:
        print("You Won!")
    else:
        print("You Lost!")
else:
    print("Please enter a number between 1 and 6")