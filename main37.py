project_num = int(input("Enter a project number: "))

if project_num == 1:
    students = {
        "Mohamed": {"grades": [100, 90, 80], "age": 20},
        "Ahmed": {"grades": [100, 95, 93], "age": 21},
        "Ali": {"grades": [85, 83, 87], "age": 19},
        "Sara": {"grades": [100, 94, 98], "age": 21}
    }

    print(f"Mohamed grades: {students['Mohamed']['grades']}")
    print(f"Ali age: {students['Ali']['age']}\n")


    sara_grades = students["Sara"]["grades"]

    print("Sara grades:")
    for grade in sara_grades:
        print(grade)


if project_num == 2:
    students = {
        "Mohamed": {
            "grades": {
                "math": 100,
                "english": 90,
                "science": 80,
                "arabic": 100,
                "history": 97
            },
            "school": "Codezilla"
        },

        "Ahmed": {
            "grades": {
                "math": 100,
                "english": 95,
                "science": 93,
                "arabic": 100,
                "history": 94
            },
            "school": "Codezilla"
        },

        "Ali": {
            "grades": {
                "math": 85,
                "english": 83,
                "science": 87,
                "arabic": 100,
                "history": 90
            },
            "school": "Al-Azhar"
        },

        "Sara": {
            "grades": {
                "math": 100,
                "english": 94,
                "science": 98,
                "arabic": 100,
                "history": 100
            },
            "school": "Al-Azhar"
        }
    }

    mohamed_garde_math = students["Mohamed"]["grades"]["math"]
    mohamed_garde_english = students["Mohamed"]["grades"]["english"]
    mohamed_school = students["Mohamed"]["school"]

    print(f"Mohamed grade math: {mohamed_garde_math}")
    print(f"Mohamed grade english: {mohamed_garde_english}")
    print(f"Mohamed school: {mohamed_school}\n")

    ahmed_garde_math = students["Ahmed"]["grades"]["math"]
    ahmed_garde_scinece = students["Ahmed"]["grades"]["science"]
    ahmed_garde_arabic = students["Ahmed"]["grades"]["arabic"]

    print(f"Ahmed grade math: {ahmed_garde_math}")
    print(f"Ahmed grade science: {ahmed_garde_scinece}")
    print(f"Ahmed grade arabic: {ahmed_garde_arabic}\n")

    ali_garde_math = students["Ali"]["grades"]["math"]
    ali_garde_history = students["Ali"]["grades"]["history"]
    ali_garde_scince = students["Ali"]["grades"]["science"]
    ali_garde_arabic = students["Ali"]["grades"]["arabic"]
    ali_school = students["Ali"]["school"]

    print(f"Ali grade math: {ali_garde_math}")
    print(f"Ali grade history: {ali_garde_history}")
    print(f"Ali grade science: {ali_garde_scince}")
    print(f"Ali grade arabic: {ali_garde_arabic}")
    print(f"Ali school: {ali_school}\n")

    sara_garde_math = students["Sara"]["grades"]["math"]
    sara_garde_scince = students["Sara"]["grades"]["science"]
    sara_garde_history = students["Sara"]["grades"]["history"]

    print(f"Sara grade math: {sara_garde_math}")
    print(f"Sara grade science: {sara_garde_scince}")
    print(f"Sara grade history: {sara_garde_history}")


if project_num == 3:
    restaurant_menu = {
        "Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120},
        "Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100},
        "Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20},
        "Desserts": {"Ice Cream": 50, "Chocolate Cake": 60, "Cheese Cake": 70},
        "Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges": 50}
    }

    chicken_burger = restaurant_menu["Burgers"]["Chicken"]
    veggie_pizza = restaurant_menu["Pizzas"]["Veggie"]
    coke = restaurant_menu["Drinks"]["Coke"]
    cheese_cake = restaurant_menu["Desserts"]["Cheese Cake"]
    onion_rings = restaurant_menu["Sides"]["Onion Rings"]

    print("-" * 20)
    print(f"Chicken Burger price: ${chicken_burger}")
    print(f"Veggie Pizza price: ${veggie_pizza}")
    print(f"Coke price: ${coke}")
    print(f"Cheese Cake price: ${cheese_cake}")
    print(f"Onion Rings price: ${onion_rings}")
    print("-" * 20)


if project_num == 4:
    employees = {
        "Mohamed Hassan": {"age": 35, "salary": 20_000, "department": "IT"},
        "Ahmed Khaled": {"age": 24, "salary": 10_000, "department": "IT"},
        "Ali Hamed": {"age": 30, "salary": 15_000, "department": "HR"},
        "Mahmoud Samir": {"age": 28, "salary": 12_000, "department": "HR"},
        "Ahmed Hassan": {"age": 25, "salary": 10_000, "department": "IT"}
    }

    mohamed_hassan = employees["Mohamed Hassan"]["age"]
    ali_hamed = employees["Ali Hamed"]["department"]
    ahmed_khaled = employees["Ahmed Khaled"]["salary"]

    print("-" * 20)
    print(f"Mohamed Hassan age: {mohamed_hassan}")
    print(f"Ali Hamed department: {ali_hamed}")
    print(f"Ahmed Khaled salary: {ahmed_khaled: ,}")

    mahmoud_samir = employees["Mahmoud Samir"]
    ahmed_hassan = employees["Ahmed Hassan"]

    print("-" * 20)
    print(f"Mahmoud Samir is {mahmoud_samir["age"]} years old, he works in {mahmoud_samir["department"]} department and his salary is {mahmoud_samir["salary"]: ,}")
    print(f"Ahmed Hassan is {ahmed_hassan["age"]} years old, he works in {ahmed_hassan["department"]} department and his salary is {ahmed_hassan["salary"]: ,}")
    print("-" * 20)


if project_num == 5:
    students = {
        "Mohamed": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},
        "school": "Codezilla"
        },
        "Ahmed": {"grades": {
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94},
        "school": "Codezilla"
        },
        "Ali": {"grades": {
        "math": 85,
        "english": 83,
        "science": 87,
        "arabic": 100,
        "history": 90},
        "school": "Al-Azhar"
        },
        "Sara": {"grades": {
        "math": 100,
        "english": 94,
        "science": 98,
        "arabic": 100,
        "history": 100},
        "school": "Al-Azhar"
        }
    }


    ali_grade_math = students["Ali"]["grades"]["math"]
    ali_grade_history = students["Ali"]["grades"]["history"]
    ali_grade_scince = students["Ali"]["grades"]["science"]
    ali_grade_arabic = students["Ali"]["grades"]["arabic"]
    ali_garde_english = students["Ali"]["grades"]["english"]

    ali_score = [ali_grade_math, ali_grade_history, ali_grade_scince, ali_grade_arabic, ali_garde_english]
    sum_ali_score = sum(ali_score)

    ali_score_using = sum_ali_score / 500 * 100

    print(f"Ali score: {ali_score_using}") 
