project_num = input("Enter a project number: ")

if project_num == "1":
    num = 0
    total = 0

    while num <= 100:
        total += num
        num += 1

    print(f"total of numbers between 0 to 100 is: {total}")


if project_num == "2":
    num = 70
    total = 0

    while num <= 160:
        total += num
        num += 1

    print(f"total of numbers between 70 to 160 is: {total}")


if project_num == "3":
    num = 30
    total = 0

    while num <= 470:
        if num % 2 == 0:
            total += num

        num += 1

    print(f"total of even numbers between 30 to 470 is: {total}")


if project_num == "4":
    num = 0
    total = 0

    while num <= 1000:
        if num % 3 == 0:
            total += num
        
        num += 1

    print(f"total of numbers that are divisible by 3 between 1 to 1000 is: {total}")


if project_num == "5":
    num = 0
    total = 0

    while num <= 2000:
        if num % 3 == 0 and num % 7 == 0:
            total += num
        
        num += 1

    print(f"total of numbers that are divisible by 3 and 7, between 1 to 2000 is: {total}")


if project_num == "6":
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    string = str(nums[0])
    index = 1

    while index < len(nums):
        string += ", " + str(nums[index])
        index += 1

    print(string)
