"""
Blackjack
"""
# Provide your solution here
def calculate_score(n1: int,n2: int,n3: int):
    numbers = []
    numbers.append(int(n1))
    numbers.append(int(n2))
    numbers.append(int(n3))
    print(numbers)
    sum_numbers = sum(numbers)
    print(sum_numbers)
    if sum_numbers <= 21:
        return sum_numbers
    else:
        if sum_numbers > 21:
            if 11 in numbers:
                adjusted_sum_numbers = sum_numbers - 10
                if adjusted_sum_numbers < 21:
                    return adjusted_sum_numbers
                else:
                    return "BUST"
            else:
                return "BUST"



"""
Even Numbers
"""
# Provide your solution here

def even_positive_numbers(list):
    new_list=[]
    for i in list:
        new_list.append(int(i))
    for i in new_list:
        # if i % 2 != 0 or i < 0:
        #     new_list.remove(i)
        #     continue
        if i % 2 != 0:
            new_list.remove(i)
            continue
        elif i < 0:
            new_list.remove(i)
            continue
    return new_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

print(calculate_score(9,9,9))
print(calculate_score(2,8,11))
print(calculate_score(3,8,11))
print(calculate_score(11,11,11))

print(even_positive_numbers([1,2,3]))
print(even_positive_numbers([10,22,31,24,35,36]))
print(even_positive_numbers([-10,-22,24,35,36]))