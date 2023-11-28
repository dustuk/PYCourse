#git input form user
word = input("Enter a word: ")
print("-" * 20)

#conversion word to list and reversed
word_list = list(word)
word_list.reverse()

#conversion word_list to string and print
reversed_word = "".join(word_list)
print(reversed_word)