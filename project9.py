#create a strong password using numbers, letters and punctuation marks
import string
import random

project_num = input("Enter a project number: ")

if project_num == "1":
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = int(input("Enter the length of your password: "))
    password = ""


    while len(password) < password_length:
        random_characters = random.choice(characters)
        password += random_characters


    print(f"Your password is: {password}")


if project_num == "2":
    characters = string.ascii_uppercase + string.digits + string.punctuation
    password_length = int(input("Enter the length of your password: "))
    password = ""


    while len(password) < password_length:
        random_characters = random.choice(characters)
        password += random_characters


    print(f"Your password is: {password}")


if project_num == "3":
    length = int(input("Enter the desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    letter_count = length // 2 + length % 2
    
    password = []
    i = 0

    while i < letter_count:
        password.append(random.choice(string.ascii_letters))
        i += 1
    
    while len(password) < length:
        password.append(random.choice(characters))


    random.shuffle(password)
    password = "".join(password)
    
    print(f"Generated password: {(password)}")