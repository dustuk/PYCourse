import random


winner_num = random.randint(1, 20)
num = int(input("Enter a number between 1 and 20: "))
print("-" * 20)

if 1 <= num <= 20:
    if num == winner_num:
        print("You win")
    else:
        print(f"You lose the number was {winner_num}")
else:
    print("Please enter a number between 1 and 10")