print("Welcome to Codezilla Fruits Store!")

fruits_basket = []
total_price = 0


while True:    
    #Make the following Codezilla Fruits Store Program.
    available_fruits = [
    ["Apple", 30],
    ["Banana", 20],
    ["Orange", 25],
    ["Mango", 40],
    ["Strawberry", 35],
    ["Blueberry", 50],
    ["Peach", 45],
    ["Pineapple", 55],
    ["Watermelon", 30],
    ["Grapes", 50],
    ["Cherry", 60],
    ["Kiwi", 45]
    ]

    print("-" * 20)
    print("1. View Available Fruits and buy")
    print("2. Total price of basket")
    print("3. Quit")
    print("-" * 20)

    number_choice = int(input("Enter the number of your choice: "))


    if number_choice == 1:
        print("-" * 20)
        print("Available Fruits:")
        print("-" * 20)

        i = 0
        for fruit, price in available_fruits:
            i += 1
            print(f"{i}. {fruit}: {price}$")
        

        while True:
            print("-" * 20) 
            fruit_choice = int(input("Enter the number of the item(0 to return to previous menu): "))

            if fruit_choice == 0:
                print("Returning to previous menu...")
                break
            else:
                print(f"{available_fruits[fruit_choice - 1][0]} added to basket successfully!")
                fruits_basket.append(available_fruits[fruit_choice - 1])
                total_price += available_fruits[fruit_choice - 1][1]
            


    if number_choice == 2:
        print(f"Total price of basket: {total_price}$")
    

    if number_choice == 3:
        if fruits_basket != []:
            print("Fruits basket:")
            print("-" * 20)

            for fruit, price in fruits_basket:
                print(f"{fruit}: {price}$")

            print("-" * 20)
            print(f"Total price of basket: {total_price}$")
            print("Thank for Choosing Codezilla Fruits Store!")
            print("See you again soon!")
        else:
            print("Your basket is Empty!")
            print("Thank for Choosing Codezilla Fruits Store!")
            print("See you again soon!")
        
        break