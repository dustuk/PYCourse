import copy

project_number = input("Enter a project number: ")

if project_number == "1":
    def filter_strings(lst, letter):
        return [string for string in lst if letter in string]
    
    strings = ['apple', 'banana', 'pear', 'orange']
    filtered_strings = filter_strings(strings, 'g')
    print(filtered_strings)
    

elif project_number == "2":
    def remove_duplicates(lst):
        return list(set(lst))
    
    numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    unique_numbers = remove_duplicates(numbers)
    print(unique_numbers) 


elif project_number == "3":
    employees = [
        {'name': 'Mohamed Ali', 'age': 25, 'salary': 45_000, 'department': 'Sales'},
        {'name': 'Islam Ahmed', 'age': 30, 'salary': 60_000, 'department': 'Marketing'},
        {'name': 'Osama Ashraf', 'age': 35, 'salary': 38_000, 'department': 'Sales'},
        {'name': 'Seif Ali', 'age': 40, 'salary': 77_000, 'department': 'Engineering'},
        {'name': 'Ayman Hamed', 'age': 45, 'salary': 80_000, 'department': 'Sales'},
        {'name': 'Ahmed Ali', 'age': 33, 'salary': 76_000, 'department': 'Marketing'},
    ]
    
    def give_raise(employees, critaria, salary_raise = 0):
        new_employees = copy.deepcopy([employee for employee in employees if employee['department'] == critaria])
        for employee in new_employees: 
            employee['salary'] += salary_raise
        return new_employees
    
    def print_employees(employees, new_employees, critaria):
        critaria_employees = [employee for employee in employees if employee['department'] == critaria]
        for i in range(len(critaria_employees)):
            print(f"{critaria_employees[i]['name']} salary was {critaria_employees[i]['salary']:,.2f}$ and is now {new_employees[i]['salary']:,.2f}$")
        
            
    new_employees = give_raise(employees, "Sales", 10_000)
    # Print the new and old information of employees
    print_employees(employees, new_employees, "Sales")