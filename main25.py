project_num = int(input("Enter a project number: "))

if project_num == 1:
    #Sum the even numbers between 28 and 928 in at least 3 different ways.
    if True:
        total = 0
        for i in range(28, 929, 2):
            total += i

        print(total)
    
    if True:
        total = 0
        for i in range(28, 929):
            if i % 2 == 0:
                total += i
        
        print(total)

    if True:
        lst = list(range(28, 929, 2))
        print(sum(lst))


if project_num == 2:
    #Print the following list in the following form.
    fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
    for i in range(len(fruits)):
        print(f"{i + 1}. {fruits[i]}")


if project_num == 3:
    #Make a Pizza program that interact with the user in the following form.
    print("Welcome to Dustuk Pizza!")
    print("We have the following pizzas: ")
    print("-" * 20)

    pizzas = ['Margherita', 'Pepperoni', 'Super Supreme', 'Hawaiian', 'Meat Lovers', 'Cheese Lovers']
    for i in range(len(pizzas)):
        print(f"{i + 1}. {pizzas[i]}")

    pizza = int(input("Enter the number of pizza you want to order: "))
    num_pizzas = int(input("Enter the number of pizzas you want: "))
    print("-" * 20)

    print("Thanks for choosing Dustuk Pizza!")
    print("Please, Enjoy your time")
    print(f"While we get {num_pizzas} {pizzas[pizza - 1]} pizza ready for you.")