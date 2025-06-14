#reserved words game
import random
import time

# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will','there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into','could',
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like','then',
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find','also',
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through','long',
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because','good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world','very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show','house', 'both',
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right','move', 'thing',
'general', 'school', 'never', 'same', 'another', 'begin', 'while','number', 'part',
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child','small', 'since',
'against', 'late', 'home', 'interest', 'large', 'person', 'open','public', 'follow',
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern','around',
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead','system',
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]

index_word = random.randint(0, len(words) - 1)
word = words[index_word]

word_list = list(word)
word_list.reverse()
reversed_word = "".join(word_list)

start_time = time.time()


print("Welcome to the Reserved Words Game!")
print("-" * 20)
print(f"The reserved word is: {reversed_word}")
print("-" * 20)

guess_word = input("Enter a word: ")
print("-" * 20)
end_time = time.time()


total_time = end_time - start_time


if guess_word == word and total_time < 5:
    print("You Won!")
else:
    if guess_word != word:
        print("Wrong Word!")
    if total_time >= 5:
        print("You Took to long!")

    print("You lost!")