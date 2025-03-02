# 1. Write a Python program to sum all the items in a list.
def calculate_sum(s):
    result = 0
    for i in s:
        result = result + i
    return result

list1 = [1,2,3,4]
cal_sum = calculate_sum(list1)
print(cal_sum)

# 2. Write a Python program to multiplies all the items in a list.
def multiply(mu):
    result = 1
    for i in mu:
        '''result = result * i'''
        result *= i
    return result

list2 = [1,2,3,4]
mul = multiply(list2)
print(mul)