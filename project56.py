import random
import string

project_num = input("Enter a project number: ")

if project_num == "1":
    def special_sum(numbers, **kwargs):
        if kwargs.get("only_even"):
            return sum([number for number in numbers if number % 2 == 0])
        elif kwargs.get("only_odd"):
            return sum([number for number in numbers if number % 2 != 0])
        elif kwargs.get("only_positive"):
            return sum([number for number in numbers if number > 0])
        elif kwargs.get("only_negative"):
            return sum([number for number in numbers if number < 0])
        elif kwargs.get("only_positive_even"):
            return sum([number for number in numbers if number > 0 and number % 2 == 0])
        elif kwargs.get("only_positive_odd"):
            return sum([number for number in numbers if number > 0 and number % 2 != 0])
        elif kwargs.get("only_negative_even"):
            return sum([number for number in numbers if number < 0 and number % 2 == 0])
        elif kwargs.get("only_negative_odd"):
            return sum([number for number in numbers if number < 0 and number % 2 != 0])
        else:
            return sum(numbers)
    
    # complete the rest of the code here
    numbers = [1, -2, -3, 4, -5, -6, -7, 8, 9, -10, 11, 12, 13, 14, -15, -16, 17, 18, 19, 20]
    print(f"Sum of all numbers: {special_sum(numbers)}")
    print(f"Total even numbers: {special_sum(numbers, only_even=True)}")
    print(f"Total odd numbers: {special_sum(numbers, only_odd=True)}")
    print(f"Total positive numbers: {special_sum(numbers, only_positive=True)}")
    print(f"Total negative numbers: {special_sum(numbers, only_negative=True)}")
    print(f"Total positive even numbers: {special_sum(numbers, only_positive_even=True)}")
    print(f"Total positive odd numbers: {special_sum(numbers, only_positive_odd=True)}")
    print(f"Total negative even numbers: {special_sum(numbers, only_negative_even=True)}")
    print(f"Total negative odd numbers: {special_sum(numbers, only_negative_odd=True)}")


elif project_num == "2":
    def print_grades(name, **kwargs):
        print(f"{name.title()}'s grades:")
        print("-" * 20)
        for subject, score in kwargs.items():
            print(f"{subject.title()}: {score}")
        print("-" * 20)
        
    print_grades("Mohamed Hamed", math=90, english=80, arabic=100, physics=95, chemistry=85)
    print_grades("Ahmed Khaled", math=80, english=70, arabic=90, physics=85, chemistry=75)
    

elif project_num == "3":
    def random_password(length=8, complex=False):
        if length < 4:
            return "Password length must be at least 4 characters."

        # المجموعات الأساسية
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # نبدأ بكلمة السر مع كل نوع حرف مرة وحدة على الأقل
        password_chars = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]

        remaining_length = length - 4

        if complex:
            # نضمن أن نصف كلمة السر رموز خاصة على الأقل
            special_needed = max(length // 2 - 1, 0)  # -1 لأننا أضفنا رمز خاص بالفعل
            password_chars += [random.choice(special) for _ in range(special_needed)]
            remaining_length -= special_needed

        # نكمل العدد المتبقي بأحرف من جميع المجموعات
        all_chars = lower + upper + digits + special
        password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

        # نخلط الأحرف لتكون عشوائية
        random.shuffle(password_chars)

        return ''.join(password_chars)

        
    print(random_password())
    print(random_password(1))
    print(random_password(10))
    print(random_password(16, True))