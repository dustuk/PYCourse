txt = """One of the most effective ways to reduce the friction
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a
method for making cues more
obvious but you can also optimize your environment to make
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your
daily
routine
Habits are easier to build when they fit into the flow of your
life
You are more likely to go to the gym if it is on your way to
work
because stopping does not add much friction to your lifestyle
"""

project_num = int(input("Enter a project number: "))

if project_num == 1:
    txt = txt.replace(" ", "").replace("\n", "").lower()

    word_counter = {}

    for i in txt:
        if i in word_counter:
            word_counter[i] += 1
        else:
            word_counter[i] = 1

    print(word_counter)



if project_num == 2:
    txt = txt.replace(" ", "").replace("\n", "").lower()

    word_counter = {}

    for i in txt:
        word_counter[i] = word_counter.get(i, 0) + 1

    print(word_counter)



if project_num == 3:
    txt = txt.replace(" ", "").replace("\n", "").lower()

    word_counter = {}

    for i in txt:
        word_counter[i] = word_counter.setdefault(i, 0) + 1

    print(word_counter)


if project_num == 4:
    txt = txt.lower().split()
    
    word_counter = {}

    for i in txt:
        word_counter[i] = word_counter.setdefault(i, 0) + 1

    print(word_counter)



if project_num == 5:
    txt = txt.lower().split()
    
    word_counter = {}

    for i in txt:
        if i in word_counter:
            word_counter[i] += 1
        else:
            word_counter[i] = 1

    print(word_counter)


if project_num == 6:
    february_shopping_list = {
        1: ['meat', 'chicken', 'chicken', 'chicken', 'bread', 'chocolate', 'meat'],
        2: ['bread', 'milks', 'butter', 'butter', 'chocolate'],
        3: ['butter', 'meat', 'milks'],
        4: ['butter', 'bread', 'nuts'],
        5: ['butter', 'bread', 'chocolate', 'chocolate'],
        6: ['nuts', 'butter', 'butter', 'butter', 'chocolate', 'butter'],
        7: ['cheese', 'milks', 'butter', 'nuts'],
        8: ['cheese', 'meat', 'nuts', 'yoghurt', 'cheese'],
        9: ['chocolate', 'milks', 'milks', 'chocolate', 'milks', 'eggs', 'meat'],
        10: ['yoghurt', 'butter', 'chocolate', 'cheese', 'butter'],
        11: ['cheese', 'meat', 'yoghurt'],
        12: ['eggs', 'chocolate', 'meat', 'eggs', 'butter'],
        13: ['bread', 'eggs', 'yoghurt', 'yoghurt', 'chicken', 'chocolate'],
        14: ['milks', 'meat', 'meat'],
        15: ['meat', 'chicken', 'butter', 'nuts', 'nuts'],
        16: ['meat', 'meat', 'chicken']
    }
    
    items_prices = {
        'meat': 250,
        'chicken': 140,
        'bread': 10,
        'chocolate': 20,
        'milks': 42,
        'butter': 75,
        'nuts': 90,
        'cheese': 65,
        'yoghurt': 25,
        'eggs': 120
    }
    
    counter = {}
    item_price = 0
    total_price = 0

    for i in february_shopping_list.values():
        for j in i:
            counter[j] = counter.setdefault(j, 0) + 1

    
    for key, value in counter.items():
        print(f"{key}: {value}")
    
    print("-" * 20)
    
    for key, value in counter.items():
        item_price = items_prices[key] * value
        total_price += item_price
        print(f"{key}: {item_price}")

    print("-" * 20)
    print(f"Total Price: {total_price}")