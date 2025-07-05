from functions import *
import os
os.chdir(r"C:\Users\iejhd\Desktop\programs\PY\PYCourse\project64")

project_num = input("Enter a project number: ")

if project_num == "1":
    extract_employees_to_csv("job_applications_emails.txt")
elif project_num == "2":
    analyze_books_summaries("books_summaries.txt")