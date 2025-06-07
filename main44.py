project_num = int(input("Enter the project number: "))

if project_num == 1:
    #قائمة المنتجات واسعارها وكميتها
    products = {
        "T-Shirt": {"price": 300, "quantity": 10},
        "Shirt": {"price": 250, "quantity": 20},
        "Pants": {"price": 300, "quantity": 15},
        "Shoes": {"price": 400, "quantity": 5},
        "Socks": {"price": 25, "quantity": 7},
        "Hat": {"price": 50, "quantity": 8},
        "Gloves": {"price": 50, "quantity": 10},
        "Sweater": {"price": 500, "quantity": 20},
        "Jacket": {"price": 900, "quantity": 15},
        "Coat": {"price": 1000, "quantity": 5},
        "Scarf": {"price": 110, "quantity": 2},
    }
    
    
    while True:
        #كتابة اسم المنتج
        product_name = input("Enter the product name (press Enter to Exit): ").title()
        
        #للخورج من اللوب اذا كان اسم المنتج فاضي
        if product_name == "":
            break
        
        #الحصول على سعر المنتج
        price = products.get(product_name, {}).get("price", "Not Available")
        
        #الحصول على كمية المنتج
        quantity = products.get(product_name, {}).get("quantity", "Not Available")
        
        #طباعة البيانات
        message = f"""
Product: {product_name}
Price: {price}
Quantity: {quantity}
"""

        print(message)



if project_num == 2:
    #قائمة المرضى
    patients = {
        "Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1},
        "Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2},
        "Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3},
        "Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4}
    }
    
    while True:
        #كتابة اسم المريض
        patient_name = input("Enter the patient name (press Enter to Exit): ").title()
        
        #للخورج من اللوب اذا كان اسم المريض فاضي
        if patient_name == "":
            break
        
        #الحصول على عمر المريض
        age = patients.get(patient_name, {}).get("age", "Not Available")
        
        #الحصول على المرض
        disease = patients.get(patient_name, {}).get("disease", "Not Available")
        
        #الحصول على غرفة المريض
        room = patients.get(patient_name, {}).get("room", "Not Available")
        
        #طباعة البيانات
        message = f"""
Patient: {patient_name}
Age: {age}
Disease: {disease}
Room: {room}
"""

        print(message)
        

if project_num == 3:
        #قائمة الادوية واسعارها وكميتها
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
            treatment_name = input("Enter the treatment name seperated by comma (press Enter to Exit): ").title().strip().split(", ")
            
            #للخورج من اللوب اذا كان اسم الدواء فاضي
            if treatment_name == "":
                break
            
            for treatment in treatment_name:
                price = inventory.get(treatment, {}).get("price", "Not Available")
                quantity = inventory.get(treatment, {}).get("quantity", "Not Available")
                
                message = f"""Treatment: {treatment}
Price: {price}
Quantity: {quantity}
{"-" * 20}"""
                print(message)


if project_num == 4:
    students = {
        "Mohamed Hassan": {"grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97}
        },
        "Ahmed Kamal": {"grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94}
        },
        "Ali Adel": {"grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90}
        },
        "Hossam Yehia": {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100}
        }
    }
    
    while True:
        #كتابة اسم الطالب
        student_name = input("Enter student name (press Enter to Exit): ").title()
        
        #للخورج من اللوب اذا كان اسم الطالب فاضي
        if student_name == "":
            break
        
        #الحصول على درجات الطالب
        gredes = students.get(student_name, {}).get("grades")
        
        #طباعة اسم الطالب
        print(f"Student: {student_name}")
        
        #طباعة درجات الطالب اذا كانت درجات الطالب متاحه
        if gredes:
            for subject, score in gredes.items():
                print(f"{subject.title()}: {score}")
        else:
            #طباعة رسالة اذا كانت درجات الطالب غير متاحه
            print("No grades available.")