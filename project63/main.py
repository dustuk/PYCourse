import os
import csv
os.chdir(r"C:\Users\iejhd\Desktop\programs\PY\PYCourse\project63")


def main():
    #read the data from the file
    employees_data = read_csv_file("employees_data")
    #update the data
    updated_employees_data = update_salary(employees_data)
    #sort the data
    sorted_employees_data = sorted_data(updated_employees_data) 
    #write the data
    write_csv_file("updated_employees_data", sorted_employees_data)
    
    print("Data has been updated and saved to the new CSV file")

def read_csv_file(file_name: str):
    """Read the data from a CSV file and return it as a list of lists.
    
    parameters:
        file_name: string that contains the name of the file to be read
    returns:
        list of lists that contains the data from the CSV file
    """
    with open(f"{file_name}.csv") as f:
        data = list(csv.reader(f))
    return data

def update_salary(employees_data: list):
    """Update the salary of each employee in the data by doubling it.
    
    Parameters:
        employees_data: list of lists that contains the data of the employees
    
    Returns:
        list of lists that contains the updated data of the employees
    """
    for data in employees_data:
        data[-1] = data[-1].replace(",", "")
        data[-1] = f"{float(data[-1]) * 2:,.2f}"
    return employees_data

def sorted_data(data: list):
    """Sort the data by the salary in descending order and then by the name in ascending order.
    
    Parameters:
        data: list of lists that contains the data of the employees
    
    Returns:
        list of lists that contains the sorted data of the employees
    """
    return sorted(data, key=lambda employee: (employee[-1], employee[0])) 

def write_csv_file(file_name: str, data: list):
    """Write the data to a CSV file.
    
    Parameters:
        file_name: string that contains the name of the file to be written
        data: list of lists that contains the data to be written
    
    Returns:
        None
    """
    with open(f"{file_name}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == "__main__":
    main()