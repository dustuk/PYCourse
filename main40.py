project_num = int(input("Enter the project number: "))

if project_num == 1:
    menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,
            "Meat Lovers Pizza": 150, "Chicken Pizza": 130}
    
    while True:
        add_item = input("Enter the name of the item to add to the menu (press Enter to Exit): ").title()
        
        if add_item == "":
            print("The New Menu:")
            for item, price in menu.items():
                print(f"{item}: {price}")
            break
        
        if add_item in menu:
            print(f"{add_item} is already in the menu.")       
        else:
            item_price = int(input("Enter item price: "))
            menu[add_item] = item_price
            print(f"Added {add_item} to the menu.")


if project_num == 2:
    menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,
            "Meat Lovers Pizza": 150, "Chicken Pizza": 130,
            "Beef Burger": 100, "Chicken Burger": 80}
    
    while True:
        remove_item = input("Enter item name to be deleted (press Enter to Exit): ").title()
        
        if remove_item == "":
            print("The New Menu:")
            for item, price in menu.items():
                print(f"{item}: {price}")
            break
        
        if remove_item in menu:
            while True:
                sure = input(f"Are you sure you want to delete {remove_item}? (y/n): ").lower()
                if sure == "y":
                    del menu[remove_item]
                    print(f"{remove_item} has been deleted")
                    break
                elif sure != "n":
                    print("Invalid input, please enter 'y' or 'n'.")
                    continue
                break
        else:
            print("Item not found")


if project_num == 3:
    menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,
            "Meat Lovers Pizza": 150, "Chicken Pizza": 130,
            "Beef Burger": 100, "Chicken Burger": 80}
    
    while True:
        update_item = input("Enter item name to be updated (press Enter to Exit): ").title()
        
        if update_item == "":
            print("The New Menu:")
            for item, price in menu.items():
                print(f"{item}: {price}")
            break
        
        if update_item in menu:
            new_price = int(input(f"Enter the new price: "))
            menu[update_item] = new_price
            print(f"{update_item} has been updated")
        else:
            print("Item not found")


if project_num == 4:
    menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,
            "Meat Lovers Pizza": 150, "Chicken Pizza": 130,
            "Beef Burger": 100, "Chicken Burger": 80}
    
    while True:
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Exit")
        print("")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_item = input("Enter the name of the item to add to the menu (press Enter to Exit): ").title()
            
            if add_item == "":
                continue
            
            if add_item in menu:
                print(f"{add_item} is already in the menu.")
            else:
                item_price = int(input("Enter item price: "))
                menu[add_item] = item_price
                print(f"Added {add_item} to the menu.")
                
        elif choice == "2":
            remove_item = input("Enter item name to be deleted (press Enter to Exit): ").title()
            
            if remove_item == "":
                continue

            if remove_item in menu:
                while True:
                    sure = input(f"Are you sure you want to delete {remove_item}? (y/n): ").lower()

                    if sure == "y":
                        del menu[remove_item]
                        print(f"{remove_item} has been deleted")
                        break
                    elif sure != "n":
                        print("Invalid input, please enter 'y' or 'n'.")
                        continue
                    
                    break
            else:
                print("Item not found")
        
        elif choice == "3":
            update_item = input("Enter item name to be updated (press Enter to Exit): ").title()

            if update_item == "":
                continue
            
            if update_item in menu:
                new_price = int(input(f"Enter the new price: "))
                menu[update_item] = new_price
                print(f"{update_item} has been updated")
            else:
                print("Item not found")
                      
        elif choice == "4":
            print("The New Menu:")
            for item, price in menu.items():
                print(f"{item}: {price}")
            break
        else:
            print("Invalid choice, please try again.")
            

if project_num == 5:
    import random
    
    # dictionary with the words and definitions
    words = {
        "Absence": "The lack or unavailability of something or someone.",
        "Approval": "Having a positive opinion of something or someone.",
        "Answer": "The response or receipt to a phone call, question, or letter.",
        "Attention": "Noticing or recognizing something of interest.",
        "Amount": "A mass or a collection of something",
        "Borrow": "To take something with the intention of returning it after a period of time.",
        "Baffle": "An event or thing that is a mystery and confuses.",
        "Ban": "An act prohibited by social pressure or law.",
        "Banish": "Expel from the situation, often done officially.",
        "Banter": "Conversation that is teasing and playful.",
        "Characteristic": "referring to features that are typical to the person, place, or thing.",
        "Cars": "Four-wheeled vehicles used for traveling.",
        "Care": "extra responsibility and attention.",
        "Chip": "a small and thin piece of a larger item.",
        "Cease": "to eventually stop existing.",
        "Dialogue": "A conversation between two or more people.",
        "Decisive": "a person who can make decisions promptly.",
    }
    
    while True:
        print("1. Review random word")
        print("2. Test yourself")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            word = random.choice(list(words.keys()))
            print(f"Word: {word}")
            print(f"Definition: {words[word]}")
                
        elif choice == "2":
            word = random.choice(list(words.keys()))
            print(f"Definition: {words[word]}")
            
            
            for i in range(3):
                answer = input("Enter the word: ").title()
                
                if answer == word:
                    print("Correct answer")
                    break
                else:
                    if i < 2:
                        print(f"Wrong answer you have {2 - i} more chance")
                        continue
                    else:
                        print("Wrong answer you have no more chances")
                        print(f"The correct answer is {word}")
            

        elif choice == "3":
            break
        
        else:
            print("Invalid option")
    
    print("Have a nice day!")