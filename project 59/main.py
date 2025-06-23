from functions import *

# طلب من المستخدم إدخال رقم المشروع
project_num = input("Enter a project number: ")

# المشروع الأول: اختبار دالة المتوسط average
if project_num == "1":
    print(average(1, 2, 3, 4, 5))                  # تمرير أرقام مفصولة
    print(average([1, 2, 3, 4, 5]))                # تمرير قائمة
    print(average((1, 2, 3, 4, 5)))                # تمرير Tuple
    print(average({1, 2, 3, 4, 5}))                # تمرير Set
    print(average([]))                            # تمرير قائمة فاضية
    print(average("Hello"))                       # تمرير نص
    print(average(1, 2, 3, 4, "5"))                # تمرير رقم كنص
    print(average())                              # عدم تمرير أي شيء


# المشروع الثاني: إعطاء زيادة رواتب لموظفي قسم معين
elif project_num == "2":
    # قائمة الموظفين تحتوي على معلومات الاسم، العمر، الراتب، القسم
    employees = [
        {'name': 'Mohamed Ali', 'age': 25, 'salary': 45_000, 'department': 'Sales'},
        {'name': 'Islam Ahmed', 'age': 30, 'salary': 60_000, 'department': 'Marketing'},
        {'name': 'Osama Ashraf', 'age': 35, 'salary': 38_000, 'department': 'Sales'},
        {'name': 'Seif Ali', 'age': 40, 'salary': 77_000, 'department': 'Engineering'},
        {'name': 'Ayman Hamed', 'age': 45, 'salary': 80_000, 'department': 'Sales'},
        {'name': 'Ahmed Alaa', 'age': 33, 'salary': 76_000, 'department': 'Marketing'},
    ]
    
    # إعطاء زيادة بمقدار 10,000$ للموظفين في قسم المبيعات (Sales)
    new_employees = give_raise(employees, "Sales", 10_000)
    
    # طباعة المعلومات القديمة والجديدة للموظفين الذين حصلوا على الزيادة
    print_employees(employees, new_employees, "Sales")


# المشروع الثالث: برنامج تعلم كلمات إنجليزية
elif project_num == "3":
    # قاموس الكلمات مع تعريفاتها
    words = {
        "Absence": "The lack or unavailability of something or someone.",
        "Approval": "Having a positive opinion of something or someone.",
        "Answer": "The response or receipt to a phone call, question, or letter.",
        "Attention": "Noticing or recognizing something of interest.",
        "Amount": "A mass or a collection of something",
        "Borrow": "To take something with the intention of returning it after a period of time.",
        "Baffle": "An event or thing that is a mystery and confuses.",
        "Ban": "An act prohibited by social pressure or law.",
        "Banish": "Expel from the situation, often done officially.",
        "Banter": "Conversation that is teasing and playful.",
        "Characteristic": "referring to features that are typical to the person, place, or thing.",
        "Cars": "Four-wheeled vehicles used for traveling.",
        "Care": "extra responsibility and attention.",
        "Chip": "a small and thin piece of a larger item.",
        "Cease": "to eventually stop existing.",
        "Dialogue": "A conversation between two or more people.",
        "Decisive": "a person who can make decisions promptly.",
    }

    # تشغيل برنامج تعلم الكلمات
    learn_english(words)
