import os
import re
os.chdir(r"C:\Users\iejhd\Desktop\programs\PY\PYCourse\project62")

with open("emails.txt", encoding="utf-8") as f:
    emails = f.read()

valid_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", emails)

with open("valid_emails.txt", "w", encoding="utf-8") as f:
    for email in valid_emails:
        f.write(f"{email}\n")


print("Valid emails saved to valid_emails.txt")
