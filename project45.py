import random


winning_coin = random.randint(1, 2)

if winning_coin == 1:
    coin_face = "Heads"
else:
    coin_face = "Tails"


print("Guess the coin flip!\nEnter")
coin = int(input("1 for Heads\n2 for Tails\n"))
print("-" * 20)


if coin in [1, 2]:
    print(f"The Coin is {coin_face}")
    if coin == winning_coin:
        print("You Won!")
    else:
        print("You Lost!")
else:
    print("Please enter 1 or 2")