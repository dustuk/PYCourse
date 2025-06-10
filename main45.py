txt = """whelcome to codezilla course
we are happy to have you all here
hope you enjoy the course"""

project_num = int(input("Enter a project number: "))

if project_num == 1:
    letter_counter = {}

    for i in txt:
        if i in letter_counter:
            letter_counter[i] += 1
        else:
            letter_counter[i] = 1

    print(letter_counter)

if project_num == 2:
    letter_counter = {}

    for i in txt:
        letter_counter[i] = letter_counter.get(i, 0) + 1

    print(letter_counter)

if project_num == 3:
    letter_counter = {}

    for i in txt:
        letter_counter[i] = letter_counter.setdefault(i, 0) + 1
        

    print(letter_counter)


    