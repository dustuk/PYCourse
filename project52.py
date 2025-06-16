project_num = input("Enter a project number: ")

if project_num == "1":
    def sum_odd_numbers(numbers):
        total = 0
        for number in numbers:
            if number % 2 == 1:
                total += number
        return total
        
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    total_odd = sum_odd_numbers(numbers)
    print(total_odd)


elif project_num == "2":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]

    def maximum_even_num(numbers):
        max_num = None
        for number in numbers:
            if number % 2 == 0:
                if max_num is None or number > max_num:
                    max_num = number
        return [max_num] if max_num is not None else []
    
    print(maximum_even_num(numbers))
    print(maximum_even_num(neg_numbers))


elif project_num == "3":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]

    def minimum_odd_num(numbers):
        min_num = None
        for number in numbers:
            if number % 2 == 1:
                if min_num is None or number < min_num:
                    min_num = number
        return [min_num] if min_num is not None else []
    
    print(minimum_odd_num(numbers))
    print(minimum_odd_num(neg_numbers))


elif project_num == "4":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]

    def count_even_numbers(numbers):
        count = 0
        for number in numbers:
            if number % 2 == 0:
                count += 1
        return count
    
    print(count_even_numbers(numbers))
    print(count_even_numbers(neg_numbers))


elif project_num == "5":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]

    def count_nag_odd_numbers(numbers):
        count = 0
        for number in numbers:
            if number % 2 == 1 and number < 0:
                count += 1
        return count
    
    print(count_nag_odd_numbers(numbers))
    print(count_nag_odd_numbers(neg_numbers))


elif project_num == "6":
    txt = "welcome at codezilla python course we are happy to have you here"
    
    def capitalize_vowels_and_first_letters(txt):
        vowels = "aeiou"
        words = txt.split()
        result_words = []

        for word in words:
            new_word = word[0].upper()

            for ch in word[1:]:
                if ch.lower() in vowels:
                    new_word += ch.upper()
                else:
                    new_word += ch

            result_words.append(new_word)

        return " ".join(result_words)
    
    print(capitalize_vowels_and_first_letters(txt))
    