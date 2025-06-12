# available items
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
burgers = {"Beef": 100, "Chicken": 80, "Bacon": 120}
drinks = {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30}
soups = {"Chicken Soup": 50, "Beef Soup": 60, "Mushroom Soup": 40}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheese Cake": 70}

order = {}
total_price = 0

options = """
1. Pizzas
2. Burgers
3. Drinks
4. Soups
5. Desserts
"""
options2 = """
1. Add another item
2. View the order
3. Clear the order
4. Exit
"""


print("Welcome to Alawjan Restaurant")

while True:
    print(options) 
    user_input = input("Please, Enter the number of the item you want (Enter to exit): ")
    
    if user_input == "1":
        for i, item in enumerate(pizzas, 1):
            price = pizzas.get(item)
            print(f"{i}. {item}: {price}")
        
        pizza_number = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
        
        if pizza_number == 0:
            continue
        
        if pizza_number in range(1, len(pizzas) + 1):
            pizza_name = list(pizzas.keys())[pizza_number - 1]
            quantity = int(input("Please, Enter the quantity: "))
            
            pizza_quantity = order.get(pizza_name, {}).get("quantity", 0) + quantity
            
            item_info = {
                pizza_name: {
                    "price": pizzas.get(pizza_name),
                    "quantity": pizza_quantity
                }
            }
            
            order.update(item_info)
            
        else:
            print(f"Invalid option. Please enter a number between 1 and {len(pizzas)}.")
            continue
            
    elif user_input == "2":
        for i, item in enumerate(burgers, 1):
            price = burgers.get(item)
            print(f"{i}. {item}: {price}")
        
        burger_number = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
        
        if burger_number == 0:
            continue
        
        if burger_number in range(1, len(burgers) + 1):
            burger_name = list(burgers.keys())[burger_number - 1]
            quantity = int(input("Please, Enter the quantity: "))
            
            burger_quantity = order.get(burger_name, {}).get("quantity", 0) + quantity
            
            item_info = {
                burger_name: {
                    "price": burgers.get(burger_name),
                    "quantity": burger_quantity
                }
            }
            
            order.update(item_info)
        
        else:
            print(f"Invalid option. Please enter a number between 1 and {len(burgers)}.")
            continue
    
    elif user_input == "3":
        for i, item in enumerate(drinks, 1):
            price = drinks.get(item)
            print(f"{i}. {item}: {price}")
        
        drink_number = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
        
        if drink_number == 0:
            continue
        
        if drink_number in range(1, len(drinks) + 1):
            drink_name = list(drinks.keys())[drink_number - 1]
            quantity = int(input("Please, Enter the quantity: "))
            
            drink_quantity = order.get(drink_name, {}).get("quantity", 0) + quantity
            
            item_info = {
                drink_name: {
                    "price": drinks.get(drink_name),
                    "quantity": drink_quantity
                }
            }
            
            order.update(item_info)
        
        else:
            print(f"Invalid option. Please enter a number between 1 and {len(drinks)}.")
            continue
    
    elif user_input == "4":
        for i, item in enumerate(soups, 1):
            price = soups.get(item)
            print(f"{i}. {item}: {price}")
        
        soup_number = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
        
        if soup_number == 0:
            continue
        
        if soup_number in range(1, len(soups) + 1):
            soup_name = list(soups.keys())[soup_number - 1]
            quantity = int(input("Please, Enter the quantity: "))
            
            soup_quantity = order.get(soup_name, {}).get("quantity", 0) + quantity
            
            item_info = {
                soup_name: {
                    "price": soups.get(soup_name),
                    "quantity": soup_quantity
                }
            }
            
            order.update(item_info)
        
        else:
            print(f"Invalid option. Please enter a number between 1 and {len(soups)}.")
            continue
    
    elif user_input == "5":
        for i, item in enumerate(desserts, 1):
            price = desserts.get(item)
            print(f"{i}. {item}: {price}")
        
        dessert_number = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
        
        if dessert_number == 0:
            continue
        
        if dessert_number in range(1, len(desserts) + 1):
            dessert_name = list(desserts.keys())[dessert_number - 1]
            quantity = int(input("Please, Enter the quantity: "))
            
            dessert_quantity = order.get(dessert_name, {}).get("quantity", 0) + quantity
            
            item_info = {
                dessert_name: {
                    "price": desserts.get(dessert_name),
                    "quantity": dessert_quantity
                }
            }
            
            order.update(item_info)
        
        else:
            print(f"Invalid option. Please enter a number between 1 and {len(desserts)}.")
            continue
            
    
    elif user_input == "":
        break
    
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        continue
    
    
    print(options2)
    user_input2 = input("Please, Enter your choice: ")
    
    if user_input2 == "1":
        continue
    
    elif user_input2 == "2":
        print("-" * 50)
        print("Your order is:")
        print("-" * 50)
        
        for item, details in order.items():
            print(f"Item: {item}")
            
            price = details.get("price")
            quantity = details.get("quantity")
            
            total_price_item = price * quantity
            total_price += total_price_item
            
            print(f"Price: {price}")
            print(f"Quantity: {quantity}")
            
            print("-" * 20)
            print(f"Item Total: {total_price_item}")    
            print("-" * 50)
        
        print(f"Total: {total_price}")
        print("-" * 50)
        
    elif user_input2 == "3":
        while True:
            sure = input("Are you sure you want to clear the order? (y/n): ").lower()
        
            if sure == "y":
                order.clear()
                print("Order has been cleared")
                break
            elif sure == "n":
                print("Order has not been cleared")
                break
            else:
                print("Invalid input, please enter 'y' or 'n'")
        
        
    elif user_input2 == "4":
        print("Quitting the program...")
        break
    
    else:
        print("Invalid option. Please enter a number between 1 and 4.")


print("-" * 50)
print("Your order is:")
print("-" * 50)
        
for item, details in order.items():
    print(f"Item: {item}")
            
    price = details.get("price")
    quantity = details.get("quantity")
            
    total_price_item = price * quantity
    total_price += total_price_item
            
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
            
    print("-" * 20)
    print(f"Item Total: {total_price_item}")    
    print("-" * 50)
        
print(f"Total: {total_price}")
print("-" * 50)