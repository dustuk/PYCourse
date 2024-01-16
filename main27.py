project_num = int(input("Enter a project number: "))

if project_num == 1:
    #Using For loop search for the word that the user will enter in the following list and print the result.
    words = ['each', 'those', 'feel', 'seem', 'high', 'place',
            'little', 'world', 'very', 'still',
            'nation', 'hand', 'life', 'tell', 'write', 'become',
            'here', 'show', 'house', 'both',
            'between', 'need', 'mean', 'call', 'develop', 'under',
            'last', 'right', 'move', 'thing',
            'general', 'school', 'never', 'same', 'another',
            'begin', 'while', 'number', 'part',
            'turn', 'real', 'leave', 'might', 'want', 'point',
            'form', 'child', 'small', 'since',
            'against', 'late', 'home', 'interest', 'large',
            'person', 'open', 'public', 'follow',
            'during', 'present', 'without', 'again', 'hold',
            'codezilla', 'govern', 'around',
            'head', 'consider', 'word', 'program', 'problem',
            'however', 'lead', 'system',
            'order', 'plan', 'keep', 'face', 'group', 'play',
            'stand', 'increase',
            'early', 'course', 'change', 'help', 'line',
            'possible', 'fact', 'down']
    
    inp = input("Enter a word: ")
    check_word = True

    for word in words:
        if word == inp.lower():
            print(f"The word ({inp}) is in the list")
            check_word = False
            break
    
    if check_word:
        print(f"The word ({inp}) is not in the list")


if project_num == 2:
    #Tell the user if the entered number is a prime number or not.
    num = int(input("Enter a number: "))

    for i in range(2, num):
        print(i)
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")


if project_num == 3:
    #Change list items into their absolute values, and do not forget to look at this question answer.
    numbers = [-500, -694, -762, -445, -348, -361, -758, -594,
            -954, -861, -610, -549, -336, -400, -600, -836, -671, 
            -573, -555, -390, -450, -811, -849, -870, -815, -694, 
            -951, -588, -484, -609, -674, -411, -408, -498, -649,
            -541, -441, -839, -567, -898]
    
    for i in range(len(numbers)):
        numbers[i] = abs(numbers[i])
    
    print(numbers)


if project_num == 4:
    #Find the number of occurrences of the letter a and the letter e in the following list
    lst_words = [['have', 'that', 'they', 'with', 'this', 'from',
                'which', 'would', 'will', 'there', 'make', 'when', 'more',
                'other', 'what', 'time', 'about', 'than', 'into', 'could'],
                [ 'state', 'only', 'year', 'some', 'take', 'come', 'these',
                'know', 'like', 'then', 'first', 'work', 'such', 'give',
                'over', 'think', 'most', 'even', 'find', 'also', 'after',
                'many', 'must', 'look', 'before', 'great', 'back', 'through',
                'long'],
                [ 'where', 'much', 'should', 'well', 'people', 'gouda', 'just',
                'because', 'good', 'each', 'those', 'feel', 'seem', 'high',
                'place', 'little', 'world', 'very', 'still', 'nation', 'hand',
                'life', 'tell', 'write', 'become', 'here', 'show', 'house',
                'both', 'between', 'need', 'mean', 'call', 'develop', 'under',
                'last', 'right', 'move', 'thing'],
                ['general', 'school', 'never', 'same', 'another', 'begin',
                'while', 'number', 'part', 'turn', 'real', 'leave', 'might',
                'want', 'point', 'form', 'child', 'small', 'since', 'against',
                'late', 'home', 'interest', 'large', 'person', 'open',
                'public', 'follow', 'during', 'present', 'without', 'again',
                'hold', 'codezilla', 'govern', 'around', 'head', 'consider',
                'word', 'program', 'problem', 'however', 'lead', 'system'],
                ['order', 'plan', 'keep', 'face', 'group', 'play', 'stand',
                'increase', 'early', 'course', 'change', 'help', 'line',
                'possible', 'fact', 'down']]
    
    count_a = 0
    count_e = 0

    for lst in lst_words:
        for word in lst:
            for little in word:
                if little == "a":
                    count_a += 1
                
                if little == "e":
                    count_e += 1

    print(f"Number of occurrences of the letter a: {count_a}")
    print(f"Number of occurrences of the letter e: {count_e}")
