import random

lst = []
for i in range(1000):
    lst.append(random.randint(1, 1000))


unique_nums = set(lst)
average_lst = sum(lst)/len(lst)
average_unique = sum(unique_nums)/len(unique_nums)


print(f"Number of unique numbers is: {len(unique_nums)}")
print(f"Average of the list is: {average_lst:.2f}")
print(f"Average of the unique numbers is: {average_unique:.2f}")