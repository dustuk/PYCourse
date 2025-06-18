project_num = input("Enter a project number: ")

if project_num == "1":
        nums = [3, 6, 2, 4, 1, 8, 34, 76, 2, 4, 6, 9, 5, -3, -5, -2, -45, -23, -66]
        def special_sum(nums, only_even = False, only_odd = False, only_positive = False, only_negative = False):
            total = 0
            lst = []
            for num in nums:
                if only_positive and not only_negative:
                    if num >= 0:
                        lst.append(num)
                elif only_negative and not only_positive:
                    if num <= 0:
                        lst.append(num)
                else:
                    lst.append(num)
            
            nums = lst      
            for num in nums:
                if only_even and not only_odd:
                    if num % 2 == 0:
                        total += num
                elif only_odd and not only_even:
                    if num % 2 != 0:
                        total += num
                else:
                    total += num
            return total

        print(special_sum(nums, only_positive = True))
        print(special_sum(nums, only_negative = True))
        print(special_sum(nums, only_even = True))
        print(special_sum(nums, only_even = True, only_positive = True))
        print(special_sum(nums, only_odd = True, only_negative = True))
        print(special_sum(nums, only_odd = True))
        print(special_sum(nums, only_positive = True, only_odd = True))
        print(special_sum(nums, only_negative = True, only_even = True))
        print(special_sum(nums))


elif project_num == "2":
    str_lst = ["1.5", "2", "3.5", "4", "5"]
    float_lst = [1.5, 2.5, 3.5, 4.5, 5.5]
    def convert_list(lst, convert_to_float = False, convert_to_str = False):
        new_list = []
        for i in lst:
            if convert_to_float:
                new_list.append(float(i))
            elif convert_to_str:
                new_list.append(str(i))
            else:
                i = float(i)
                new_list.append(round(i))
                    
        return new_list
    
    
    print(convert_list(str_lst))
    print(convert_list(float_lst))
    print(convert_list(str_lst, convert_to_float = True))
    print(convert_list(float_lst, convert_to_str = True))


elif project_num == "3":
    def max_even_number(*args, nth_max_even_number = False):
        lst = []
        for num in args:
            if num % 2 == 0:
                lst.append(num)
        
        lst.sort(reverse = True)
        
        if nth_max_even_number:
            return lst[nth_max_even_number - 1]
        else:
            return lst[0]
    
    print(max_even_number(64, 52, 84, 76, 45, 36, 88))
    print(max_even_number(64, 52, 84, 76, 45, 36, 88, nth_max_even_number = 3))


elif project_num == "4":
    def average(*args):
        if len(args) == 1:
            args = args[0]
        return sum(args) / len(args)
    
    print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(average((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    print(average({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))