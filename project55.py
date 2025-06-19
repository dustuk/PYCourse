project_num = input("Enter a project number: ")

if project_num == "1":
    def is_dividible_by(num, divisor = 2):
            return num % divisor == 0
    
    print(is_dividible_by(10))
    print(is_dividible_by(9))
    print(is_dividible_by(10, 5))
    print(is_dividible_by(9, 5))



elif project_num == "2":
    def is_even(list):
        return ["Even" if num % 2 == 0 else "Odd" for num in list]
    
    print(is_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


elif project_num == "3":
    def is_prime(num):
        if num < 2:
            return "Not Prime"
        for i in range(2, num):
            if num % i == 0:
                return "Not Prime"
        return "Prime"

    print(is_prime(10))
    print(is_prime(11))
    print(is_prime(12))
    print(is_prime(13))


elif project_num == "4":
    def convert_unit(num, unit):
        unit = unit.lower()
        result = 0
        if unit == "km":
            result = num * 0.62137
            new_unit = "Miles"
        elif unit == "miles":
            result = num * 1.6093
            new_unit = "Km"
        elif unit == "celsius":
            result = num * 1.8 + 32
            new_unit = "Fahrenheit"
        elif unit == "fahrenheit":
            result = (num - 32) / 1.8
            new_unit = "Celsius"
        else :
            return "Invalid Unit"
        
        return f"{num} {unit} is {result:.2f} {new_unit}"
    
    print(convert_unit(100, "Km"))
    # output: 100 km is 62.14 miles
    print(convert_unit(100, "Miles"))
    # output: 100 miles is 160.93 km
    print(convert_unit(30, "Celsius"))
    # output: 30 Celsius is 86.00 Fahrenheit
    print(convert_unit(86, "fahrenheit"))
    # output: 86 Fahrenheit is 30.00 Celsius