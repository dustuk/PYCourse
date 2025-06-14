project_num = int(input("Enter a project number: "))

if project_num == 1:
    #print the pizza name and price for the following pizzas
    #Pepperoni, Chicken, Hawaiian
    pizzas = {
        "Margherita": 100,
        "Pepperoni": 120,
        "Meat Lovers": 150,
        "Chicken": 130,
        "Cheese": 100,
        "Veggie": 120,
        "Hawaiian": 150,
        }
    
    pizza_of_print = ["Pepperoni", "Chicken", "Hawaiian"]
    
    for pizza in pizza_of_print:
        print(f"{pizza} pizza price is {pizzas[pizza]}")
    
if project_num == 2:
    #Print the following drinks from the menu.
    #Coke, Mango Juice, Tea, Coffee
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

    drinks_of_print = ["Coke", "Mango Juice", "Tea", "Coffee"]
    
    for drink in drinks_of_print:
        print(f"{drink} drink price is {drinks[drink]}")


if project_num == 3:
    #Add the following desserts to the restaurant menu.
    #Ice Cream - 30, Chocolate Cake - 60, Cheese Cake - 70, Brownie - 40, Donut - 30
    menu = {
        "Cheese pizza": 100,
        "Veggie pizza": 120,
        "Hawaiian pizza": 150,
        "Coke": 30,
        "Sprite": 25,
        "Fanta": 25,
        "Pepsi": 30
        }
    
    desserrts = {
        "Ice Cream": 30,
        "Chocolate Cake": 60,
        "Cheese Cake": 70,
        "Brownie": 40,
        "Donut": 30
    }

    for dessert, price in desserrts.items():
        menu[dessert] = price
    
    for item, price in menu.items():
        print(f"{item}: {price}")


if project_num == 4:
    #Increase the prices of pizzas by 20 percent then print the restaurant menu.
    menu = {
    "Cheese pizza": 100,
    "Veggie pizza": 120,
    "Hawaiian pizza": 150,
    "Coke": 30,
    "Sprite": 25,
    "Fanta": 25,
    "Pepsi": 30
    }
    
    for item, price in menu.items():
        if "pizza" in item:
            menu[item] = price * 1.2
            
        print(f"{item}: {menu[item]}")
        

if project_num == 5:
    #print soda items from the following menu
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
    
    soda_items = ["Coke", "Sprite", "Fanta", "Pepsi"]
    
    for item, price in drinks.items():
        if item in soda_items:
            print(f"{item}: {price}")


if project_num == 6:
    """Make a Pizza program that asks the user about the
        wanted pizza, and if available, it prints the pizza and
        its price. otherwise, you should print a sorry
        message."""
        
    pizza_order = input("What pizza would you like to order? ").title()
    
    pizzas = {"Margherita": 100, "Pepperoni": 120,
                "Meat Lovers": 150, "Chicken": 130}
    
    if pizza_order in pizzas:
        print(f"{pizza_order} pizza is available and its price is {pizzas[pizza_order]}")
    else:
        print(f"Sorry, {pizza_order} pizza is not available.")


if project_num == 7:
    #Print the menu after increasing the prices by 20%
    pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
    
    for pizza, price in pizzas.items():
        pizzas[pizza] = price * 1.2
        print(f"{pizza}: {pizzas[pizza]:.0f}")
        

if project_num == 8:
    #Print the following menu in a nice format for the user
    pizzas = {"Margherita": 100,
            "Pepperoni": 120,
            "Meat Lovers": 150,
            "Chicken": 130,
            "Chicken Ranch": 140,
            "Cheese": 110
            }
    
    for pizza, price in pizzas.items():
        print(f"{pizza:<20} : {price:>5}")
        
        
if project_num == 9:
    """Using the following information make a program
        that allows the user to get the school of the student
        when they enter the student name or the student id."""
        
    schools = {
        "Codezilla School":
        {'1100':"Mohamed Gouda", '1101':"Islam Hesham",
        '1102':"Ayman Mohamed", '1103':"Ahmed Khaled"},
        
        "Al Dorra School":
        {'2100':"Ahmed Hassan", '2101':"Mahmoud Ali",
        '2102':"Adham Wael", '2103':"Khaled Ali"},
        
        "Mostafa Kamel School":
        {'3105':"Hazem Ahmed", '3106':"Omar Mohamed",
        '3107':"Hussein Kamal", '3109':"Ali Ahmed"}
        }
    
    student = input("Enter the student name or ID: ").strip().title()
    found = False
    for school, students in schools.items():
        for student_id, name in students.items():
            if student == name or student == student_id:
                print(f"Student {name} with ID {student_id} is from {school}.")
                found = True
                break
        if found:
            break
    if not found:
        print(f"Sorry, {student} not found.")


if project_num == 10:
    #Increase the salaries of the following employees by 40%.
    employees = {
        "Ahmed Hassan": 12_000,
        "Mohamed Ahmed": 20_000,
        "Ali Ahmed": 15_000,
        "Khaled Ali": 10_000,
        "Omar Mohamed": 13_000,
        "Hazem Ahmed": 24_000,
        }
    
    for employee, salary in employees.items():
        employees[employee] = salary * 1.4
        print(f"{employee}: {employees[employee]:,.0f}")