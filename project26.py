project_num = int(input("Enter a project number: "))


if project_num == 1:
    #Print the students’ names and grades in the following form
    student_names = ["Mohamed", "Ahmed", "Ali", "Sara"]
    student_grades = [[96, 78, 82, 80], [86, 92, 98, 90], [76, 88, 90, 72], [78, 86, 98, 88]]

    for student, grades in zip(student_names, student_grades):
        print(f"Student: {student}")
        print(f"Grades:")
        print(*grades, sep=", ")
        print("-" * 20)

        average = sum(grades) / len(grades)
        print(f"{student} has an average grade of {average:.2f}")
        print("-" * 40)

if project_num == 2:
    #Using unpacking operator make these lists into one list
    grades1 = [96, 78, 82, 80]
    grades2 = [86, 92, 98, 90]
    grades3 = [76, 88, 90, 72]
    grades4 = [78, 86, 98, 88]

    lst = [*grades1, *grades2, *grades3, *grades4]
    print(lst)