project_num = int(input("Enter a project number: "))


if project_num == 1:
    #Make the following numbers negative.
    nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
    negative_nums = [-i for i in nums]
    print(negative_nums)


if project_num == 2:
    #Create a new list with the square of the numbers in the given list.
    nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
    square_nums = [i ** 2 for i in nums]
    print(square_nums)


if project_num == 3:
    #create a new list with the scores as percent and each score in the format of 88%
    scores = [75, 87, 93, 98, 82, 67, 91, 88]
    percent_scores = [f"{i}%" for i in scores]
    print(percent_scores)


if project_num == 4:
    #Make a list with all the items in the following list in lowercase.
    fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]
    lower_fruits = [i.lower() for i in fruits]
    print(lower_fruits)


if project_num == 5:
    #Write code to find the sum of the even numbers in the list.
    nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
    even_sum = sum([i for i in nums if i % 2 == 0])
    print(even_sum)


if project_num == 6:
    #Make a new list with prices in the following form $10.99.
    prices = [10.99, 20.99, 30.99, 40.99, 50.99]
    dollar_prices = [f"${i}" for i in prices]
    print(dollar_prices)