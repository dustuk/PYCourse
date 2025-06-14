project_num = input("Enter a project number: ")

if project_num == "1":
    total = 0

    while True:
        num = input("Enter a number: ").lower()

        if num == "done" or len(num) == 0:
            break

        num = int(num)
        total += num
    
    print(f"total is {total}")


if project_num == "2":
    total = 0

    while True:
        num = input("Enter a number: ").lower()

        if num == "done" or len(num) == 0:
            break

        num = int(num)
        
        if num % 2 != 0:
            continue
            
        total += num
        
    print(f"total is {total}")


if project_num == "3":
    total = 0

    while True:
        num = input("Enter a number: ").lower()

        if num == "done" or len(num) == 0:
            break

        num = int(num)

        if num % 2 == 0:
            continue
        
        total += num
    
    print(f"total is {total}")


if project_num == "4":
    total = 1

    while True:
        num = input("Enter a number: ").lower()

        if num == "done" or len(num) == 0:
            break

        num = int(num)

        if num == 0:
            continue
        
        total *= num
    
    print(f"total is {total}")


if project_num == "5":
    numbers = []
    num = 452

    while num < 983:
        if (num % 7 == 0) and (num % 5 != 0):
            numbers.append(num)
        num += 1
    
    numbers.sort()

    second_highest = numbers[-2]
    second_lowest = numbers[1]

    average = (second_highest + second_lowest) / 2

    print(f"The average of the second highest ({second_highest}) and the second lowest ({second_lowest}) numbers is: {average}")


if project_num == "6":
    total = 0

    while True:
        number = input("Enter a number: ")

        if number == "done" or len(number) == 0:
            break

        number = int(number)

        if number % 2 != 0:
            continue

        total += number
    
    print(f"The total is: {total}") 


if project_num == "7":
    total = 0

    while True:
        number = input("Enter a number: ")

        if number == "done" or len(number) == 0:
            break

        number = int(number)

        if number % 3 != 0:
            continue

        total += number

    print(f"The total is: {total}")