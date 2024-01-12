project_num = input("Enter a project number: ")

if project_num == "1":
    numbers = range(1, 101, 2)

    for number in numbers:
        print(number)


if project_num == "2":
    numbers = range(8, 423, 2)
    
    for number in numbers:
        print(number)


if project_num == "3":
    numbers = range(120, 451, 7)

    for number in numbers:
        print(number)


if project_num == "4":
    numbers = list(range(28, 229, 2))
    total = sum(numbers)
    print(total)