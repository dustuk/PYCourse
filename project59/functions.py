import copy
import time
import random

# دالة لمسح سطر واحد في الكونسول (تُستخدم لإخفاء النص بعد ظهوره)
def clear_line():
    print('\r' + ' ' * 100 + '\r', end='', flush=True)


# دالة لحساب المتوسط لعدد غير معروف من القيم
def average(*args):
    try:
        # إذا تم تمرير عنصر واحد وكان داخله مجموعة من الأرقام (مثل list أو tuple)
        if len(args) == 1 and args[0]:
            args = args[0]
        # إذا لم يتم تمرير أي قيمة
        elif len(args) == 0:
            raise TypeError
        
        # التأكد أن كل القيم أرقام صحيحة أو عشرية
        for arg in args:
            if not isinstance(arg, (int, float)):
                if isinstance(arg, str):
                    raise ValueError
                else:
                    raise TypeError
            
        return sum(args) / len(args)  # حساب المتوسط
    except TypeError:
        return "Please Enter Number to Calculate Average"  # رسالة خطأ في حالة النوع
    except ValueError:
        return "Cannot Enter a String"  # رسالة خطأ في حالة وجود نص


# دالة لإعطاء زيادة في الراتب لموظفين في قسم معين
def give_raise(employees, criteria, salary_raise=0):
    # إنشاء نسخة من الموظفين الذين ينتمون للقسم المحدد
    updated_employees = copy.deepcopy(
        [employee for employee in employees if employee['department'] == criteria]
    )
    # تطبيق الزيادة على كل موظف
    for employee in updated_employees:
        employee['salary'] += salary_raise
    return updated_employees

# دالة لطباعة الراتب قبل وبعد الزيادة للموظفين المحددين
def print_employees(employees, updated_employees, criteria):
    # استخراج الموظفين الأصليين من القسم المحدد
    original = [e for e in employees if e['department'] == criteria]
    # مقارنة وطباعة الراتب قبل وبعد الزيادة
    for old, new in zip(original, updated_employees):
        print(f"{old['name']} salary was {old['salary']:,.2f}$ and is now {new['salary']:,.2f}$")


# دالة رئيسية لتعليم اللغة الإنجليزية
def learn_english(words):
    def main():
        # القائمة الرئيسية للاختيارات
        menu = """1. Review random word
2. Test yourself
3. Exit"""

        while True:
            print(menu)
            choice = input("Enter your choice: ")
            if choice == "1":
                review_random_words()  # مراجعة كلمة عشوائية
            elif choice == "2":
                test_yourself()  # اختبار ذاتي
            elif choice == "3":
                break  # إنهاء البرنامج
            else:
                print("Invalid option")  # خيار غير صحيح
    
    # دالة لمراجعة كلمة وتعريفها بشكل عشوائي
    def review_random_words():
        word = random.choice(list(words.keys()))
        print(f"Word: {word}")
        print(f"Definition: {words[word]}")
        print("-" * 20)
    
    # دالة لاختبار المستخدم: يظهر التعريف ثم يختبره بإدخال الكلمة
    def test_yourself():
        word = random.choice(list(words))
        definition = words[word]
        # عرض التعريف
        print(f"Definition: {definition}", end='', flush=True)
        time.sleep(5)  # الانتظار 5 ثواني
        clear_line()  # مسح السطر

        # إعطاء المستخدم 3 محاولات
        for i in range(1, 4):
            answer = input("Enter the word: ").title()
            if answer == word:
                print("-" * 20)
                print("Congratulations you got the correct answer")  # تهنئة
                break
            else:
                attempt = "attempt" if (3 - i) == 1 else "attempts"
                
                if i < 3:
                    print(f"Incorrect answer, you have {3 - i} {attempt} remaining")  # تنبيه بعدد المحاولات المتبقية
                    continue
                
                print(f"Incorrect answer, you have {3 - i} {attempt} remaining") # تنبيه بعدد المحاولات المتبقية
                print("-" * 20)
                print(f"The correct answer is {word}")  # إظهار الجواب الصحيح
                print("Better luck next time.")  # تشجيع

    main()  # تشغيل الدالة الرئيسية داخل تعلم الإنجليزية