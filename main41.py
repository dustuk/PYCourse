project_num = int(input("Enter the project number: "))

if project_num == 1:
    students = {
        "Mohamed Hassan": {"grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97},
            "school": "Codezilla"
        },
        "Ahmed Kamal": {"grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94},
            "school": "Codezilla"
        },
        "Ali Adel": {"grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90},
            "school": "Al-Azhar"
        },
        "Hossam Yehia": {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100},
            "school": "Al-Azhar"
        }
    }
    
    for student, info in students.items():
        print("-" * 20)
        total_grades = sum(info["grades"].values()) / len(info["grades"])
        print(f"{student} has the highest total precentage which is {total_grades:.2f}%")
        print("-" * 20)
        for subject, grade in info["grades"].items():
            print(f"{subject.capitalize()}: {grade}")


if project_num == 2:
    inventory = {"Paracetamol": {"price":25, "quantity":10},
                    "Aspirin": {"price":15, "quantity":20},
                    "Ibuprofen": {"price":20, "quantity":15},
                    "Cough Syrup": {"price":30, "quantity":5},
                    "Augmentin": {"price":100, "quantity":7},
                    "Amoxicillin": {"price":80, "quantity":8},
                    "Panadol": {"price":25, "quantity":10},
                    "Zinc": {"price":15, "quantity":20},
                    "Vitamin C": {"price":20, "quantity":15},
                    "Fucidin": {"price":30, "quantity":5},
                    "Kolanog": {"price":100, "quantity":2},
                    }
    
    option = """
1. Add new item
2. Remove items
3. Update items
4. Check Available quantitiy
5. Print treatment information
6. Exit
"""
    
    while True:
        print(option)
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"{"-" * 3}Adding new item{"-" * 3}")
            while True:
                item_name = input("Enter the item name (press Enter to Exit): ").title()

                if item_name == "":
                    print("Exiting item entry.")
                    break
            
                if item_name not in inventory:
                    item_price = int(input("Enter the item price: "))
                    item_quantity = int(input("Enter the item quantity: "))
                    inventory[item_name] = {"price": item_price, "quantity": item_quantity}
                    print(f"{item_name} has been added to the inventory.")
                    break
                else:
                    print(f"{item_name} already exists in the inventory.")

        elif choice == "2":
            print(f"{"-" * 3}Removing item{"-" * 3}")
            while True:
                item_name = input("Enter the item name to remove (press Enter to Exit): ").title()

                if item_name == "":
                    print("Exiting item removal.")
                    break

                if item_name in inventory:
                    while True:
                        sure = input(f"Are you sure you want to delete {item_name}? (y/n): ").lower()
                        if sure == "y":
                            del inventory[item_name]
                            print(f"{item_name} has been removed from the inventory.")
                            break
                        elif sure == "n":
                            print(f"{item_name} removal cancelled.")
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                            continue
                    break
                else:
                    print(f"{item_name} does not exist in the inventory.")
        
        elif choice == "3":
            print(f"{"-" * 3}Updating item{"-" * 3}")
            while True:
                item_name = input("Enter item name to be updated (press Enter to Exit): ").title()

                if item_name == "":
                    print("Exiting item update.")
                    break

                if item_name in inventory:
                    new_price = int(input("Enter the new price: "))
                    new_quantity = int(input("Enter the new quantity: "))
                    inventory[item_name] = {"price": new_price, "quantity": new_quantity}
                    print(f"{item_name} has been updated.")
                    break
                else:
                    print(f"{item_name} does not exist in the inventory.")
                
        elif choice == "4":
            print(f"{"-" * 3}Checking available quantity{"-" * 3}")
            while True:
                item_name = input("Enter item name to be checked (press Enter to Exit): ").title()

                if item_name == "":
                    print("Exiting quantity check.")
                    break

                if item_name in inventory:
                    print(f"We have {inventory[item_name]['quantity']} {item_name} units.")
                    break
                else:
                    print(f"{item_name} does not exist in the inventory.")
        
        elif choice == "5":
            print(f"{"-" * 3}Printing treatment information{"-" * 3}")
            while True:
                item_name = input("Enter item name (press Enter to Exit): ").title()

                if item_name == "":
                    print("Exiting treatment information printing.")
                    break
                
                if item_name in inventory:
                    print(f"Item: {item_name}")
                    print(f"Price: {inventory[item_name]['price']}")
                    print(f"Quantity: {inventory[item_name]['quantity']}")
                    break
                else:
                    print(f"{item_name} does not exist in the inventory.")

        elif choice == "6":
            print("Have a nice day!")
            break
        
        else:
            print("Invalid choice, please try again.")