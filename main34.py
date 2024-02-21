import random

project_num = int(input("Enter a project number: "))


if project_num == 1:
    #Write code to find the sum of numbers that are
    #divisible by 3 and between 20 and 140 then print 
    #the numbers separated by a comma.
    nums = [num for num in range(20, 141) if num % 3 == 0]
    print(nums)
    print(sum(nums))


if project_num == 2:
    #Make a List with 20 random numbers between 100 and 1000.
    nums = [random.randint(100, 1000) for num in range(20)]
    print(nums)


if project_num == 3:
    #Make list with 100 random numbers between 100
    #and 10,000 that are divisible by 3 and 5.
    nums  = [random.randint(100, 10000) for num in range(100) if i % 3 == 0 and i % 5 == 0]
    print(nums)


if project_num == 4:
    #Modify this list of words to make All words are uppercase
    words = [
    'have', 'that', 'they', 'with', 'this', 'from',
    'which', 'would', 'will', 'there','make', 'when',
    'more', 'other', 'what', 'time','about', 'than',
    'into', 'could', 'state', 'only', 'year', 'some',
    'take', 'come', 'these', 'know', 'like', 'then',
    'first', 'work', 'such', 'give', 'over', 'think',
    'most', 'even', 'find', 'also','after', 'many',
    'must', 'look', 'before', 'great', 'back',
    'through', 'long', 'where', 'much', 'should',
    'well', 'people', 'gouda','just', 'because',
    'good', 'each', 'those', 'feel', 'seem', 'high',
    'place', 'little', 'world', 'very', 'still',
    'nation', 'hand', 'life', 'tell', 'write', 'become'
    ]

    words = [word.upper() for word in words]
    print(words)


if project_num == 5:
    #Edit words list to gain the following outputs.
    words = [["Hello", "from", "Codezilla"],
        ["Python", "Course", "is", "awesome"],
        ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

    words = [" ".join(word) for word in words]
    words_upper = [word.replace(" ", "-").upper() for word in words]
    print(words)
    print(words_upper)


if project_num == 6:
    #Convert all the following numbers into positive numbers.
    nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99]
    positive_nums = [abs(num) for num in nums]
    print(positive_nums)


if project_num == 7:
    #Flat the following nested list
    nested_list = [["Hello", "from", "Codezilla"],
        ["Python", "Course", "is", "awesome"],
        ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
    
    flat_list = [word for lst in nested_list for word in lst]
    print(flat_list)


if project_num == 8:
    #Make a list of tuples with the first element as the
    #word and the second element as the length of the word.
    words = ["Hello", "from", "Codezilla", "Python", "Course"]
    word_lengths = [(word, len(word)) for word in words]
    print(word_lengths)