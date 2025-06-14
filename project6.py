total = 0

while True:
    num = input("Enter a number: ")

    if num == "done" or len(num) == 0:
        break

    num = int(num)
    
    if num % 2 != 0:
        continue
        
    total += num
    

print(f"total is {total}")