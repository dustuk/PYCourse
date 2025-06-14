project_num = input("Enter a project number: ")

if project_num == "1":
    numbers = [1, 2, 3, 4, 5]
    lst = []

    for number in numbers:
        number **= 2
        lst.append(number)

    print(lst)


if project_num == "2":
    scores = [75, 87, 93, 98, 82, 67, 91, 88]
    lst = []

    for score in scores:
        score = f"{str(score)}%"
        lst.append(score)
    
    print(lst)


if project_num == "3":
    fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]

    for fruit in fruits:
        fruit = fruit.lower()
        print(fruit)


if project_num == "4":
    names = ["mohamed gouda", "islam mahfouz", "ayman hamed", "hassan ali", "mostafa mohamed"]

    for name in names:
        name = name.title()
        print(name)


if project_num == "5":
    word = input("Enter a word: ")
    list(word)

    for letter in word:
        print(letter.upper()) 


if project_num == "6":
    prices = [10.99, 20.99, 30.99, 40.99, 50.99]
    lst = []

    for price in prices:
        price = f"${str(price)}"
        lst.append(price)
    
    print(lst)


if project_num == "7":
    prices = [75, 153, 635, 144, 356, 712, 675, 234]
    total = 0
    i = 0

    for price in prices:
        total += price
        i += 1

    print(total/i)


if project_num == "8":
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    string = str(nums[0])

    for num in nums[1:]:
        string += ", " + str(num)

    print(string)