project_num = int(input("Enter a project number: "))

if project_num == 1:
    #Make your own Multiplication table like the following.
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        
        print("-" * 20)


if project_num == 2:
    #Make All the following list items uppercase.
    words = ['have', 'that', 'they', 'with', 'this', 'from',
            'which', 'would', 'will', 'there', 'make', 'when', 'more',
            'other', 'what', 'time', 'about', 'than', 'into', 'could',
            'state', 'only', 'year', 'some', 'take', 'come', 'these',
            'know', 'like', 'then', 'first', 'work', 'such', 'give',
            'over', 'think', 'most', 'even', 'find', 'also', 'after',
            'many', 'must', 'look',
            'before', 'great', 'back', 'through', 'long', 'where', 'much',
            'should', 'well', 'people', 'gouda', 'just', 'because', 'good',
            'each', 'those', 'feel', 'seem', 'high', 'place', 'little',
            'world', 'very', 'still', 'nation', 'hand', 'life', 'tell',
            'write', 'become', 'here', 'show', 'house', 'both', 'between',
            'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
            'move', 'thing', 'general', 'school', 'never', 'same',
            'another', 'begin', 'while', 'number', 'part', 'turn', 'real',
            'leave', 'might', 'want', 'point', 'form', 'child', 'small',
            'since', 'against', 'late', 'home', 'interest', 'large',
            'person', 'open', 'public', 'follow', 'during', 'present',
            'without', 'again', 'hold', 'codezilla', 'govern', 'around',
            'head', 'consider', 'word', 'program', 'problem', 'however',
            'lead', 'system', 'order', 'plan', 'keep', 'face', 'group',
            'play', 'stand', 'increase', 'early', 'course', 'change',
            'help', 'line', 'possible', 'fact', 'down']
    
    for word in words:
        print(word.upper())


if project_num == 3:
    #Do the following: A. convert each inner list to a string and join them
    #with a space and add them to a list named sentences.
    #B. Make another list replace spaces with dashes and
    #convert each word to uppercase.
    words = [["Hello", "from", "Codezilla"],
            ["Python", "Course", "is", "awesome"],
            ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
    
    sentences = []
    for lst in words:
        sentence = " ".join(lst)
        sentences.append(sentence)
    
    print(sentences)

    sentences = []
    for lst in words:
        sentence = "-".join(lst).upper()
        sentences.append(sentence)
    
    print(sentences)


if project_num == 4:
    #Find the smallest number in the following list without using min and sort.
    numbers = [-588, -479, -713, -701, -885, -578, -835, -466,
            -935, -665, -360, -837, -389, -367, -454, -668, -907,
            -822, -541, -680, -405, -330, -625, -916, -331, -876, 
            -689, -753, -810, -648, -787, -952, -718, -401, -502, 
            -699, -533, -450, -580, -725]
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    
    print(smallest)


if project_num == 5:
    #Find the smallest, odd number in the following list without using min and sort.
    numbers = [-500, -694, -762, -445, -348, -361, -758, -594, 
            -954, -861, -610, -549, -336, -400, -600, -836, 
            -671, -573,-555, -390, -450, -811, -849, -870, 
            -815, -694, -951, -588, -484, -609, -674, -411, 
            -408, -498, -649, -541, -441, -839, -567, -898]
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest and number % 2 != 0:
            smallest = number
    
    print(smallest)


if project_num == 6:
    #Find the average word length in the following sentence.
    sentence = """Python is a widely used high-level
                general-purpose interpreted dynamic programming language
                Its design philosophy emphasizes code readability and its
                syntax allows programmers to express concepts in fewer lines of
                code
                than possible in many other languages
                The language provides constructs intended to enable clear
                programs on both a small and large scale"""
    
    for word in sentence.split():
        average = sum(len(word) for word in sentence.split()) / len(sentence.split())
    
    print(f"The average word length is: {average:.2f}")


if project_num == 7:
    #Debug the following code with at least 2 solutions,
    #so that "Found Codezilla!" is the last printed output.
    nested_list = [["Hello", "from", "Codezilla"],
                ["Python", "Course", "is", "awesome"],
                ["I", "enjoy", "learning", "Python"]]
    
    for lst in nested_list:
        print(lst)
        for word in lst:
            print(word)
            if word == "Codezilla":
                print("Found Codezilla!")
            
            exit() # EXIT THE WHOLE PROGRAM
    
    ##########
            
    # Solution 2: comparing words and exit the program with continue and exit() function
    for lst in nested_list:
        print(lst)
        for word in lst:
            print(word)
            if word != "Codezilla":
                continue
            else:
                print("Found Codezilla!")
                exit()