cairo = ["Islam Mahfouz", "Mohamed Gouda", "Hatem Medhat"]
riyadh = ["Ayman Hamed", "Seif Ali", "Adham Wael"]
casablanca = ["Ahmed Ashraf", "Mahrous Samy", "Amr Ahmed"]
dubai = ["Ahmed Alaa", "kareem Ayman", "Osama Ashraf"]

office = input("Enter the name of the office: ").lower()

match office:
    case "cairo" | "egypt" | "eg":
        employees = cairo
    case "riyadh" | "saudi arabia" | "ksa" | "saudi":
        employees = riyadh
    case "casablanca" | "morocco":
        employees = casablanca
    case "dubai" | "uae" | "emirates" | "united arab emirates":
        employees = dubai
    case _:
        employees = None
        print("Not found")

if employees:
    print(f"The employees of {office} office are: {", ".join(employees[:-1])} and {employees[-1]}")