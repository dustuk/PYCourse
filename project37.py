project_num = int(input("Enter the project number: "))

if project_num == 1:
    #حساب متوسوط درجات المدارس
    schools = {
        "Codezilla":{
            "Mohamed Hassan": {
                "math": 100,
                "english": 90,
                "science": 85,
                "arabic": 100,
                "history": 97
            },
            "Ahmed Kamal": {
                "math": 100,
                "english": 95,
                "science": 93,
                "arabic": 100,
                "history": 94
            }
        },
        "Al-Azhar": {
            "Ali Adel": {
                "math": 85,
                "english": 83,
                "science": 87,
                "arabic": 100,
                "history": 90
            },
            "Mariam Ali": {
                "math": 100,
                "english": 94,
                "science": 98,
                "arabic": 100,
                "history": 100
            }
        }
    }
    
    schools_average_percentage = {}
    students_total_percentage = []
    
    for school in schools:
        for student in schools[school]:
            subjects_grades = schools[school][student]
            total_percentage = sum(subjects_grades.values()) / len(subjects_grades)
            students_total_percentage.append(total_percentage)
        
        school_average_percentage = sum(students_total_percentage) / len(students_total_percentage)
        schools_average_percentage[school] = school_average_percentage
        students_total_percentage = []  
    
    for school, school_average_percentage in schools_average_percentage.items():
        print(f"The average total percentage for {school} school is: {school_average_percentage:.2f}%")


if project_num == 2:
    # available items
    hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25}
    cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30}
    desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheesecake": 70}

    menu = {
        "1": hot_drinks,
        "2": cold_drinks,
        "3": desserts
    }

    menu_names = {
        "1": "Hot Drinks",
        "2": "Cold Drinks",
        "3": "Desserts"
    }

    print("Welcome to Alawjan Cafe")

    options = """
1. Hot Drinks
2. Cold Drinks
3. Desserts
"""

    order = {}

    while True:
        print(options)
        choice = input("Please Enter the Number of the Item Type (press Enter to Finish Order): ")

        if choice == "":
            break

        if choice in menu:
            items = list(menu[choice].items())
            print(f"\n{menu_names[choice]} Menu:")
            for idx, (item, price) in enumerate(items, 1):
                print(f"{idx}. {item}: {price}")

            try:
                item_num = int(input("Enter item number: "))
                if 1 <= item_num <= len(items):
                    quantity = int(input("Please enter quantity: "))
                    item_name = items[item_num - 1][0]

                    # إضافة الكمية إلى الطلب (أو جمعها إذا كانت مكررة)
                    if item_name in order:
                        order[item_name]["quantity"] += quantity
                    else:
                        order[item_name] = {"price": menu[choice][item_name], "quantity": quantity}
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    # طباعة الفاتورة
    print("\n" + "-" * 30)
    print("Your order summary:")
    print("-" * 30)
    total = 0
    for item, info in order.items():
        item_total = info["price"] * info["quantity"]
        total += item_total
        print(f"{item}: {info['quantity']} x {info['price']} = {item_total}")
    print("-" * 30)
    print(f"Total: {total}")
    print("Thank you for visiting Alawjan Cafe!")
