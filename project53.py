import random

project_num = input("Enter a project number: ")

if project_num == "1":  
    def count_positive_even_numbers(*args):
        count = 0
        for num in args:
            if num > 0 and num % 2 == 0:
                count += 1
        return count
    
    print(count_positive_even_numbers(1, 2, 3, -4, -5, -6, -7, 8, 9, 10))
    
    
elif project_num == "2":
    def generate_random_even_numbrs(num_even_numbers, range_start, range_end):
        even_numbers = []
        while len(even_numbers) < num_even_numbers:
            num = random.randint(range_start, range_end)
            if num % 2 == 0:
                even_numbers.append(num)
        return even_numbers
    
    print(generate_random_even_numbrs(20, 1, 100))
    
    
elif project_num == "3":
    def convert_list_to_integers(lst):
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        return lst
    
    print(convert_list_to_integers(["1", "2", "3", "4", "5"]))