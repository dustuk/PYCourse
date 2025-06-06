project_num = int(input("Enter a project number: "))

if project_num == 1:
    #الادوية واسعارها وكميتها
    inventory = {
        "Paracetamol": {"price":25, "quantity":10},
        "Aspirin": {"price":15, "quantity":20},
        "Ibuprofen": {"price":20, "quantity":15},
        "Cough Syrup": {"price":30, "quantity":5},
        "Augmentin": {"price":100, "quantity":7},
        "Amoxicillin": {"price":80, "quantity":8},
        "Panadol": {"price":25, "quantity":10},
        "Zinc": {"price":15, "quantity":20},
        "Vitamin C": {"price":20, "quantity":15},
        "Fucidin": {"price":30, "quantity":5},
        "Kolanog": {"price":100, "quantity":2},
    }
    
    while True:
        #كتابة اسم الداوءة
        treatment_name = input("Enter treatment name (press Enter to Exit): ").title() #تحويل اول احرف من كل كلمة الى حرف كبير
        
        #للخورج من اللوب اذا كان اسم الدواء فاضي
        if treatment_name == "":
            break
        
        #الحصول على قيمة الدواء
        value = inventory.get(treatment_name)
        
        #اذا كان القيمة موجودة يطبع قيمتها
        if value:
            for item, quantity in value.items():
                print(f"{item}: {quantity}")
        else:
            #اذا الدواء مب موجود يطبع الرسالة
            print("Not Available")


if project_num == 2:
    #معلومات الموظفين
    employees = {
        "Mohamed Hassan": {"age": 25, "salary": 5000, "department": "HR"},
        "Ahmed Kamal": {"age": 30, "salary": 6000, "department": "IT"},
        "Ali Adel": {"age": 35, "salary": 7000, "department": "IT"},
        "Hossam Yehia": {"age": 40, "salary": 8000, "department": "IT"},
        "Ali Alawjan": {"age": 18, "salary": 50000, "department": "CS"}
    }
    
    while True:
        #كتابة اسم الموظف
        employee_name = input("Enter employee name (press Enter to Exit): ").title()
        
        #للخورج من اللوب اذا كان اسم الموظف فاضي
        if employee_name == "":
            break
        
        #الحصول على قيمة الموظف
        value = employees.get(employee_name)
        
        #اذا كان القيمة موجودة يطبع قيمتها
        if value:
            for item, quantity in value.items():
                print(f"{item.title()}: {quantity}")
        else:
            #اذا الموظف مب موجود يطبع الرسالة
            print("Not Available")


if project_num == 3:
    students = {
        "Mohamed Hassan": {
            "Password": "123456",
            "grades": {
                "math": 100,
                "english": 90,
                "science": 80,
                "arabic": 100,
                "history": 97
            }
        },
        "Ahmed Kamal": {
            "Password": "1234",
            "grades": {
                "math": 100,
                "english": 95,
                "science": 93,
                "arabic": 100,
                "history": 94
            }
        },
        "Ali Adel": {
            "Password": "12",
            "grades": {
                "math": 85,
                "english": 83,
                "science": 87,
                "arabic": 100,
                "history": 90
            }
        },
        "Hossam Yehia": {
            "Password": "33",
            "grades": {
                "math": 100,
                "english": 94,
                "science": 98,
                "arabic": 100,
                "history": 100
            }
        }
    }
    
    
    while True:
        #كتابة اسم الطالب
        student_name = input("Enter student name (press Enter to Exit): ").title()
        
        #للخورج من اللوب اذا كان اسم الطالب فاضي
        if student_name == "":
            break
        
        #كتابة كلمة المرور
        student_password = input("Enter the password: ")
        
        #الحصول على قيمة الطالب
        value = students.get(student_name)
        
        #الحصول على قيمة كلمة المرور
        password = value.get("Password")
        
        if password == student_password:
            print(f"Student Name: {student_name}") #يعرض اسم الطالب
            print("Grades:")
            print("-" * 20)
            
            #يعرض الدرجات
            for subject, score in value["grades"].items():
                print(f"{subject.title()}: {score}")
            print("-" * 20)
            percentage = sum(value["grades"].values()) / len(value["grades"]) #يحسب نسبة الطالب
            print(f"Student Percentage: {percentage:.2f}%") #يعرض نسبة الطالب
        else:
            #اذا كان كلمة المرور غير صحيحة يطبع الرسالة
            print("Wrong Password or Student Name")
        

if project_num == 4:
    #الادوية واسعارها
    pharmacy_prices = {
        "panadol": 32,
        "cold free": 25,
        "omega 3": 45,
        "fuciden": 37,
        "augmentin": 50,
        "zinc": 20,
        "vitamin c": 15
    }
    
    while True:
        #كتابة اسم الادوية
        names_of_treatments = input("Enter the names of treatments by a comma (press Enter to Exit):\n").strip().lower().split(", ")#يضيف كل دواء بعد كاما الى قائمة
        print("-" * 20)
        
        #للخورج من اللوب اذا كان اسم الدواء فاضي
        if names_of_treatments == "":
            break
        
        #الحصول على قيمة الدواء
        for name in names_of_treatments:
            value = pharmacy_prices.get(name)
            
            #اذا كان القيمة موجودة يطبع قيمتها
            if value:
                print(f"{name.title()}: {value}")
            else:
                #اذا الدواء مب موجود يطبع الرسالة
                print(f"{name}: is not available")