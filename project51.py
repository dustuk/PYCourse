project_num = input("Enter a project number: ")

if project_num == "1":
    pizzas = {
        "Margherita": 120,
        "Pepperoni": 200,
        "Hawaiian": 150,
        "Meat Lovers": 250,
        "Mushroom": 140,
    }
    
    def pizza():
        for key, value in pizzas.items():
            print(f"{key}: {value}")
    
    pizza()


elif project_num == "2":
    def employee_info(name, age, salary):
        print(f"Name: {name.title()}")
        print(f"Age: {age}")
        print(f"Salary: {salary}")
    
    #1
    employee_info("mohamed ahmed", 25, 10_000)
    #2
    employee_info("hassan Ali", 33, 15_000)
    #3
    employee_info("Ali Hassan", 30, 20_000)
    #4
    employee_info("Ahmed Mohamed", 35, 15_000)
    #5
    employee_info("Hazem Khaled", 28, 15_000)
    #6
    employee_info("Hamed Ali", 25, 14_000)
    #7
    employee_info("Mohamed Khedr", 25, 13_000)


elif project_num == "3":
    def students_info(name, age, city = "Cairo", school = "Codezilla"):
        print(f"Name: {name.title()}")
        print(f"Age: {age}")
        print(f"City: {city.title()}")
        print(f"School: {school.title()}")
    
    
    students_info("ahmed mohamed", 25)
    students_info("mohamed ahmed", 33, school = "al-azhar")
    students_info("ali hassan", 30, city = "alexandria")
    students_info("hazem khaled", 35, "new york", "al-azhar")
    students_info("hamed ali", 25, "tanta", "al durra")


elif project_num == "4":
    def print_student(name, grades, school = "Codezilla"):
        print(f"Student: {name.title()}")
        print(f"School: {school.title()}")
        print(f"Grades:")
        print("-" * 7)
        for key, value in grades.items():
            print(f"{key}: {value}") 

    
    
    name = "hamada codezilla"
    
    grades = {
        "math": 99,
        "english": 98,
        "science": 99,
        "arabic": 100,
        "history": 99
    }
    
    print_student(name, grades)