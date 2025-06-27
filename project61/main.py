import os
os.chdir(r"C:\Users\iejhd\Desktop\programs\PY\PYCourse\project61")

def main():
    project_num = input("Enter a project number: ")
    
    if project_num == "1":
        project1()
    elif project_num == "2":
        books_summary()


def project1():
    with open("atomic_habits_summary.txt", encoding="utf-8") as f:
        atomic_habits = f.read()
    
    with open("deep_work_summary.txt", encoding="utf-8") as f:
        deep_work = f.read()
        
    with open("dopamine_nation_summary.txt", encoding="utf-8") as f:
        dopamine_nation = f.read()
        
    with open("project1.txt", "w", encoding="utf-8") as f:
        f.write(f"{atomic_habits}\n{deep_work}\n{dopamine_nation}"[::-1].upper())


def books_summary():
    with open("atomic_habits_summary.txt", encoding="utf-8") as f:
        atomic_habits = f"atomic habits summary:\n{f.read()}"
    
    with open("deep_work_summary.txt", encoding="utf-8") as f:
        deep_work = f"deep work summary:\n{f.read()}"
        
    with open("dopamine_nation_summary.txt", encoding="utf-8") as f:
        dopamine_nation = f"dopamine nation summary:\n{f.read()}"
    
    with open("so_good_to_ignore_summary.txt", encoding="utf-8") as f:
        so_good_to_ignore = f"so good to ignore summary:\n{f.read()}"
        
    with open("the_lady_tasting_tea_summary.txt", encoding="utf-8") as f:
        the_lady_tasting_tea = f"the lady tasting tea summary:\n{f.read()}"
        
    with open("the_power_of_habits_summary.txt", encoding="utf-8") as f:
        the_power_of_habits = f"the power of habits summary:\n{f.read()}"
        
    with open("books_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"{atomic_habits}\n\n{deep_work}\n\n{dopamine_nation}\n\n{so_good_to_ignore}\n\n{the_lady_tasting_tea}\n\n{the_power_of_habits}")
    
    
    
main()