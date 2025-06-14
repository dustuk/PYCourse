project_num = int(input("Enter the project number: "))

if project_num == 1:
    students = {
        "Mohamed Hassan": {"grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97},
            "school": "Codezilla"
        },
        "Ahmed Kamal": {"grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94},
            "school": "Codezilla"
        },
        "Ali Adel": {"grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90},
            "school": "Al-Azhar"
        },
        "Sara Ahmed": {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100},
            "school": "Al-Azhar"
        }
    }
    
    for student, info in students.items():
        print(f"Student Name: {student}")
        print(f"School: {info['school']}")
        print("Grades:")
        for subject, grade in info['grades'].items():
            print(f"{subject.capitalize()}: {grade}")
        print("-" * 20)
        

if project_num == 2:
    #print the total grades for each students
    tudents = {
        "Mohamed Hassan": {"grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97},
            "school": "Codezilla"
        },
        "Ahmed Kamal": {"grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94},
            "school": "Codezilla"
        },
        "Ali Adel": {"grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90},
            "school": "Al-Azhar"
        },
        "Sara Islam": {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100},
            "school": "Al-Azhar"
        }
    }
    
    for student, info in tudents.items():
        total_grades = sum(info['grades'].values()) / len(info['grades'])
        print(len(info['grades']))
        print(f"{student}'s total percentage: {total_grades:.2f}%")
        print("-" * 20)
        

if project_num == 3:
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
        "Israa Ali": {"grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100}
        }
    }
    
    student_name = input("Please, Enter the name of the student: ").title()
    
    if student_name in students:
        print(f"{student_name} got the following grades:")
        
        for subject, grade in students[student_name]['grades'].items():
            print(f"{subject.capitalize()}: {grade}")
            
        print("-" * 20)
        
        for subject, grade in students[student_name]['grades'].items():
            total_grades = sum(students[student_name]['grades'].values()) / len(students[student_name]['grades'])
        
        print(f"{student_name}'s total percentage is {total_grades:.2f}%")
        
    else:
        print(f"Sorry, we don't have info about thei student")
        