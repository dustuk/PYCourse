project_num = input("Enter a project number: ")

if project_num == "1":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    
    for number in numbers:
        total += number

    print(total)


if project_num == "2":
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(number ** 2)


if project_num == "3":
    string = "Codezilla Python Course"
    for character in string:
        print(character)


if project_num == "4":
    prices = [10.99, 9.99, 15.99, 7.99, 12.99]
    total = 0

    for price in prices:
        total += price

    print(total)


if project_num == "5":
    numbers = [1, 2, 3, 4, 5]
    total = 1

    for number in numbers:
        total *= number
    
    print(total)


if project_num == "6":
    nums = []
    total = 0

    while True:
        num = input("Enter a number: ")

        if num == "done" or len(num) == 0:
            break

        num = float(num)
        nums.append(num)
    
    for number in nums:
        total += number
    
    print(total)