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

# 3. Write a Python program to get the largest number from a list.
def find_large_num(large):
    result = large[0]
    for i in large:
        if i > result:
            result = i
        else:
            pass
    return result

list3 = [1,2,3,4]
lar = find_large_num(list3)
print(lar)

# 4. Write a Python program to get the smallest number from a list.
def find_small_num(small):
    result = small[0]
    for i in small:
        if i < result:
            result = i
        else:
            pass
    return result
list4 = [4,3,2,1]
sma = find_small_num(list4)
print(sma)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def string(str):
    result = 0
    for i in str:
        if len(i) > 1 and i[0] == i[-1]:
            result += 1
        else:
            pass
    return result

list5 = ['abc', 'aba', '1221']
count = string(list5)
print(count)

