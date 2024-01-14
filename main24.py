project_num = int(input("Enter a project number: "))

if project_num == 1:
    #Print the total of numbers between 0 to 100.
    total = 0
    for i in range(101):
        total += i
    
    print(total)


if project_num == 2:
    #Print the total of numbers between 70 to 160
    total = 0
    for i in range(70, 161):
        total += i
    
    print(total)


if project_num == 3:
    #Print the total of even numbers between 30 to 470.
    total = 0
    for i in range(30, 471, 2):
        total += i
    
    print(total)


if project_num == 4:
    #Print the total of numbers that are divisible by 3 and between 1 to 1000.
    total = 0  
    for i in range(1, 1000):
        if i % 3 == 0:
            total += i

    print(total)


if project_num == 5:
    #Make a program that calculate the average of the
    #second highest and second lowest numbers that are
    #between 452 and 983 and are divisible by 5 and 7.
    lst = []
    lst_2 = []
    for i in range(452, 983):
        if i % 7 == 0:
            lst.append(i)

        if i % 5 == 0:
            lst_2.append(i)

    print(lst[1], lst[-2])
    print(lst_2[1], lst_2[-2])