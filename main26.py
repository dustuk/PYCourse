project_num = int(input("Enter a project number: "))

if project_num == 1:
    #Flat a nested list in 2 Ways.
    nested_list = [["Hello", "from", "Codezilla"], 
                    ["Python", "Course", "is", "awesome"],
                    ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
    
    if True:
        flat_lst = []
        for lst in nested_list:
            for word in lst:
                flat_lst.append(word)

        print(flat_lst)
    
    if True:
        flat_lst = []

        for lst in nested_list:
            flat_lst.extend(lst)

        print(flat_lst)


if project_num == 2:
    #Find the smallest multiple of 9 in the following list
    numbers = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494,
                486, 885, 341, 484, 598, 950, 859, 716, 488, 584]
    
    numbers.sort()

    for i in numbers:
        if i % 9 == 0:
            print(i)
            break


if project_num == 3:
    #Find the largest number in the following list without using max and sort.
    numbers = [-588, -479, -713, -701, -885, -578, -835, -466,
            -935, -665, -360, -837, -389, -367, -454, -668, 
            -907, -822,-541, -680, -405, -330, -625, -916,
            -331, -876, -689, -753,-810, -648, -787, -952,
            -718, -401, -502, -699, -533, -450, -580, -725]
    
    num = numbers[0]

    for i in numbers:
        if i > num:
            num = i

    print(num)


if project_num == 4:
    #Find the largest even number in the following list without using max and sort.
    numbers = [-500, -694, -762, -445, -348, -361, -758,
            -594, -954, -861, -610, -549, -336, -400, -600,
            -836, -671, -573, -555, -390, -450, -811, -849,
            -870, -815, -694,-951, -588, -484, -609, -674,
            -411, -408, -498, -649, -541, -441, -839, -567,
            -898]
    
    num = numbers[0]

    for i in numbers:
        if i > num and i % 2 == 0:
            num = i
    
    print(num)