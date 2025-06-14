project_num = int(input("Enter a project number: "))


if project_num == 1:
    #Store the following data inside the dictionary
    fruits = {
        "apple" : 20,
        "banana" : 15,
        "orange" : 10,
        "strawberry" : 30,
        "mango" : 25,
    }

    print(fruits)



if project_num == 2:
    #Create a dictionary to store student names and grades as follows
    grades = {
        "Mohamed Hassan" : 83,
        "Ahamed Khaled" : 97,
        "Ali Hamed" : 75,
        "Mahmoud Samir" : 89,
    }

    print(grades)


if project_num == 3:
    #Create a dictionary called drinks that contains the following information
    drinks = {
        "Coke" : 10,
        "Sprite" : 8,
        "Fanta" : 8,
        "Pepsi" : 10,
    }

    print(drinks)



if project_num == 4:
    #Create a dictionary with the order of codezilla students in a competition.
    #The key is the order and the value is the name of the student
    students = {
        1 : "Mohamed Ahmed",
        2 : "Ahmed Khaled",
        3 : "Ali Hamed",
        6 : "Mahmoud Samir",
        8 : "Ahmed Hassen",
    }

    print(students)


if project_num == 5:
    #Debug the following code, keeping the first and last names separated.
    grades = {
        ("Ahmed", "Hassan") : 87,
        ("Hossam", "Ali") : 90,
        ("Mohamed", "Kamel") : 74,
        ("Ali", "Hamed") : 100,
        ("Ahmed", "Khaled") : 95
    }

    print(grades)



if project_num == 6:
    #Print the prices of the following Pizzas from the menu.
    pizzas = {
        "Margherita": 100,
        "Pepperoni": 120,
        "Meat Lovers": 150,
        "Chicken": 130,
        "Cheese": 100,
        "Veggie": 120,
        "Hawaiian": 150,
    }

    for pizza in pizzas:
        print(f"{pizza} Pizza : ${pizzas[pizza]}")



if project_num == 7:
    #Print the prices of the following drinks
    drinks = {
        "Coke": 30,
        "Sprite": 25,
        "Fanta": 25,
        "Pepsi": 30,
        "Tea": 20,
        "Coffee": 25,
        "Orange Juice": 30,
        "Mango Juice": 30
    }

    for drink in drinks:
        print(f"{drink} : ${drinks[drink]}")
        


if project_num == 8:
    #Add the following desserts to the menu and update the price of Hawaiian pizza to 190.
    menu = {
        "Cheese pizza": 100,
        "Veggie pizza": 120,
        "Hawaiian pizza": 150,
        "Coke": 30,
        "Sprite": 25,
        "Fanta": 25,
        "Pepsi": 30
    }

    menu["Ice Cream"] = 30
    menu["Chocolate Cake"] = 60
    menu["Cheese Cake"] = 70
    menu["Brownie"] = 40
    menu["Donut"] = 30

    menu["Hawaiian pizza"] = 190

    print(menu)



if project_num == 9:
    #Print the prices of Soda items from the menu (from Coke to Pepsi)
    drinks = {
        "Latte": 30,
        "Coke": 30,
        "Sprite": 25,
        "Fanta": 25,
        "Pepsi": 30,
        "Tea": 20,
        "Coffee": 25,
        "Orange Juice": 30,
        "Mango Juice": 30
    }

    for drink in drinks:
        if drink == "Coke" or drink == "Sprite" or drink == "Fanta" or drink == "Pepsi":
            print(f"{drink} : ${drinks[drink]}")



if project_num == 10:
    #Print available pizzas and their prices for the customer.
    pizzas = {
        "Margherita": 100,
        "Pepperoni": 120,
        "Meat Lovers": 150,
        "Chicken": 130
    }

    for pizza in pizzas:
        print(f"{pizza} : ${pizzas[pizza]}")