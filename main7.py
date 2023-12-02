import random

winner1 = random.randint(1, 20)
winner2 = random.randint(1, 20)
winner3 = random.randint(1, 20)
winner4 = random.randint(1, 20)

winners = [winner1, winner2, winner3, winner4]

num = int(input("Enter a number between 1 and 20: "))
print("-" * 20)

if 1 <= num <= 20:
    if num in winners:
        print("You won!")
    else:
        print("You Lost!")
else:
    print("Please enter a number between 1 and 20")