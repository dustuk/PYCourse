available_items = {
    "Samsung s24": {
        "price": 2999,
        "quantity": 10
    },
    "Samsung s24 Plus": {
        "price": 3499,
        "quantity": 7
    },
    "Samsung s24 Ultra": {
        "price": 4499,
        "quantity": 18
    },
    "Samsung s25": {
        "price": 3399,
        "quantity": 5
    },
    "Samsung s25 Plus": {
        "price": 3999,
        "quantity": 4
    },
    "Samsung s25 Ultra": {
        "price": 4999,
        "quantity": 8
    }
}

# 1. view available items and buy what he/she wants
# 2. view shopping cart which contains bought items
# 3. view the total price of the shopping cart
# 4. delete items from the shopping cart
# 5. clear the shopping cart
# 6. quit the program

# initialize the shopping cart as a dictionary
cart = {}

menu_message = """
What would you like to do?
1. View available items
2. View Cart
3. View total
4. Delete item
5. Clear Cart
6. Quit
"""

# we need to make a loop to keep the program running until user quits
while True:
    # print menu message
    print(menu_message)
    
    # get the user's choice
    user_input = input("Enter the number of your choice: ")
    
    # 1. if the user chose to view available items
    if user_input == "1":
        print("The available items are:")
        for i, item in enumerate(available_items, 1):
            # get the item price
            item_price = available_items.get(item).get("price")
            
            # get the item quantity
            item_quantity = available_items.get(item).get("quantity")
            
            # check if item is available
            if item_quantity > 0:
                print(f"{i}. {item}: {item_price} SAR")
            else:
                print(f"{i}. {item}: {item_price} SAR (out of stock)")
                
        # get thhe item the user wants to buy
        item_choice = int(input("Enter the number of the item you want to buy: "))
        
        if 1 <= item_choice <= len(available_items):
            # get the order/item name from the item number
            order_name = list(available_items.keys())[item_choice - 1]
            
            # add the bought/purchased item to the cart
            if available_items[order_name]["quantity"] > 0:
                #get the price of the bought item
                order_price = available_items.get(order_name).get("price")
        
                #get the quantity of the bought item
                order_quantity = cart.get(order_name, {}).get("quantity", 0) + 1
            
                # save order info
                order_info = {
                    order_name: {
                        "price": order_price,
                        "quantity": order_quantity
                    }
                }
            
                # add order info to the cart
                cart.update(order_info)
                
                # confirm taht the order is added to the cart
                print(f"{order_name} has been added to the cart successfully.")
                
                #subtract 1 from the quantity of the item in the available items
                available_items[order_name]["quantity"] -= 1
            else:
                print("Sorry, the item is out of stock.")
        else:
            print(f"Invalid item number. Please Enter a number between 1 and {len(available_items)}")
    
    # 2. if the user chose to view cart
    elif user_input == "2":
        if cart:
            print("\nCart:")
            print("-" * 30)
            
            for item in cart:
                item_price = cart.get(item).get("price")
                item_quantity = cart.get(item).get("quantity")
                print(f"{item}: {item_price} SAR x {item_quantity}")  
                
            print("-" * 30)
            
        #else if the cart is empty, print no items have been bought
        else:
            print("No items have been bought")
            
    # 3. if the user chose to view total price
    elif user_input == "3":
        if cart:
            total_price = 0
            
            for item in cart:
                item_price = cart.get(item).get("price")
                item_quantity = cart.get(item).get("quantity")
                
                #get the total price of each item in the cart
                total_price_item = item_price * item_quantity
                
                #sum all the items in the cart to get the total price
                total_price += total_price_item
            
            print(f"\nTotal price of cart: {total_price} SAR")
        else:
            print("No items have been bought")
    
    # 4. if the user chose to delete an item
    elif user_input == "4":
        if cart:
            print("\nCart:")
            print("-" * 30)
            
            for i, item in enumerate(cart, 1):
                item_price = cart.get(item).get("price")
                item_quantity = cart.get(item).get("quantity")
                print(f"{i}. {item}: {item_price} SAR x {item_quantity}")
                
            print("-" * 30)
            
            while True:
                delete_item = int(input("Enter the number of the item you want to delete (enter 0 to cancel): "))
                
                if delete_item == 0:
                    break
                
                if 1 <= delete_item <= len(cart):
                    sure = input("Are you sure you want to delete this item? (y/n): ").lower()
    
                    if sure == "y":
                        item_to_delete = list(cart.keys())[delete_item - 1]
                        del cart[item_to_delete]
                        print(f"{item_to_delete} has been deleted from the cart successfully.")
                        break
                    
                    elif sure == "n":
                        print("Deletion has been cancelled.")
                        break
                    
                    else:
                        print("Invalid input, please enter 'y' or 'n'.")
                                    
                else:
                    print(f"Invalid item number. Please Enter a number between 1 and {len(cart)}")
        else:
            print("No items have been bought")
    
    # 5. if the user chose to clear the cart
    elif user_input == "5":
        if cart:
            sure = input("Are you sure you want to clear the cart? (y/n): ").lower()
            
            if sure == "y":
                cart.clear()
                print("Cart has been cleared")
            elif sure != "n":
                print("Invalid input, please enter 'y' or 'n'.")
            else:
                print("Cart has not been cleared")
                
        else:
            print("No items have been bought")
                
    # 6. if the user chose to exit the program/quit
    elif user_input == "6":
        print("Quitting the program...")
        break
    
    # 5. if the user chose an invalid option
    else:
        print("Invalid option. Please enter a number between 1 and 6.")




#if cart contains  items, print the cart
if cart:
    print("\nCart:")
    print("-" * 30)
    
    total_price = 0
    
    for item in cart:
        item_price = cart.get(item).get("price")
        item_quantity = cart.get(item).get("quantity")
    
        #get the total price of each item in the cart
        total_price_item = item_price * item_quantity
        
        #sum all the items in the cart to get the total price
        total_price += total_price_item
    
        print(f"{item}: {item_price} SAR x {item_quantity}")  
    
    print("-" * 30)
    print(f"Total price of cart: {total_price} SAR")
    print("-" * 30)
    
#else if the cart is empty, print no items have been bought
else:
    print("No items have been bought")