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
    return sorted(large)[-1]

list3 = [121,220,31,47]
lar = find_large_num(list3)
print(lar)

# 4. Write a Python program to get the smallest number from a list.
def find_small_num(small):
    return sorted(small)[0]
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

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def tuple_sort(tuple):
    return sorted(tuple, key=lambda x: x[-1])

list6 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorty = tuple_sort(list6)
print(sorty)

# 7. Write a Python program to remove duplicates from a list.
list7 = [10,20,30,40,50,60,30,20,10]
'''def distinguish(duplicate):
    set1 = set()
    for i in duplicate:
        if i not in set1:
            set1.add(i)
    return set1

result = distinguish(list7)
print(list(result))'''

def alternative(duplicate):
    return list(set(duplicate))

result = alternative(list7)
print(result)

# 8. Write a Python program to check a list is empty or not.
def empty_or_full(x):
    if not x:
        return 'the list is empty'
    else:
        return 'the list is not emply'

list8 = [] 
check = empty_or_full(list8)
print(check)

# 9. Write a Python program to clone or copy a list
def clones(x):
    return list(x)

list9 = [1,2,3,4,5]
cloning = clones(list9)
print(cloning)

# i added some element in the clone variable but it didnt apply in the real list.
cloning.append(6)
print(cloning)
print(list9)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def crazy(n, x):
    result = []
    for i in x:
        if len(i) > n:
            result.append(i)
    return result

list10 = ['apple', 'cherry', 'banana']
ok = crazy(5, list10)
print(ok)

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def inter(n, x):
    return bool(set(n) & set(x))

list11 = [1,2,3,4,5]
list11_copy = [9,8,7,6,5]
checking = inter(list11, list11_copy)
print(checking)

# another way
def clone(x1, x2):
    for i in x1:
        if i in x2:
            return True
    else:
        return False
        
cloning = clone(list11, list11_copy)
print(cloning)

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
def remove_elements(x):
    '''result = []
    for i, v in enumerate(x):
        if i not in (0,4,5):
            result.append(v)
    return result'''
    result = [v for i, v in enumerate(x) if i not in (0,4,5)]
    return result


list12 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
showdown = remove_elements(list12)
print(showdown)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *
def arrays(layers, rows, columns):
    result = [[['*' for _ in range(columns)] for _ in range(rows)] for _ in range(layers)]
    '''for _ in range(layers):
        layer = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append('*')
            
            layer.append(row)

        result.append(layer)'''

    return result

def print_3d_array(x):
    for layer in x:
        for row in layer:
            print(row)

        print()

list13 = arrays(3,4,6)        
print_3d_array(list13)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
def remove_even(x):
    result = [i for i in x if i % 2 != 0]
    return result

list14 = [7, 8, 120, 25, 44, 20, 27]
even = remove_even(list14)
print(even)

# question 15 and 16 is unavailable.
# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
def square(x):
    result = [i**2 for i in range(1, x+1)]
    return result

list17 = 30
multiplication = square(list17)[5:]
print(multiplication)

# 18. Write a Python program to generate all permutations of a list in Python.
def permutating(x):
    from itertools import permutations
    result = list(permutations(x))
    return result

list18 = [1,2,3]
done = permutating(list18)
print(done)


# 19.  Write a Python program to get the difference between the two lists.
def difference(x1, x2):
    result = [i for i in x1 if i not in x2]
    return result

list19 = [1,2,3,4,5]
list19_copy = [9,8,7,6,5]
yup = difference(list19, list19_copy)
print(yup)


# 20. Write a Python program access the index of a list.
def access_index(x):
    result =[(i, v) for i, v in enumerate(x)]
    return result

list20 = [10,20,30,40,50]
call = access_index(list20)
print(call)



# my first usecase of list comprehension.
'''def even_numbers(x):
    even = [i for i in x if i % 2 == 0]
    return even


e = [1,2,3,4,5,6]
calc = even_numbers(e)
print(calc)'''

# 21. Write a Python program to convert a list of characters into a string.
def list_to_string(x):
    return ''.join(x)

list21 = ['h','e','l','l','o']
consolidate = list_to_string(list21)
print(consolidate)

# 22. Write a Python program to find the index of an item in a specified list.

list22 = [10,20,30]
fit = list22.index(10)
print(fit)

# 23. Write a Python program to flatten a shallow list.
def flatten(x):
    import itertools
    return list(itertools.chain(*x))

list23 = [[1,2,3],[4,5,6],[6,7,8,9]]
merge = flatten(list23)
print(merge)

# Write a Python program to append a list to the second list
def appending(x, y):
    return x + y

list24 = [1,2,3]
list24_copy = [4,5,6]
merging = appending(list24, list24_copy)
print(merging)

# 25. Write a Python program to select an item randomly from a list.
def fetch_random_item(x):
    import random
    return random.choice(x)

list25 = ['chinku','pinku','shullu','shukshuk','lokpak']
time = fetch_random_item(list25)
print(time)

# 26. Write a python program to check whether two lists are circularly identical. 

# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(x):
    return sorted(x)[1]

list27 = [90,50,20,10,40,70]
here = second_smallest(list27)
print(here)

# 28. Write a Python program to find the second largest number in a list.
def second_largest(x):
    return sorted(x)[-2]

list28 = [90,50,20,10,40,70]
print(second_largest(list28))


# 29. Write a Python program to get unique values from a list.
def sort_the_unique(x):
    return list(set(x))

list29 = [10,10,30,60,70,30,20]
print(sort_the_unique(list29))

# 30.  Write a Python program to get the frequency of the elements in a list.
def frequency_check(x):
    from collections import Counter
    return dict(Counter(x))

list30 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(frequency_check(list30))

# 31. Write a Python program to count the number of elements in a list within a specified range.
def odd_question(x1, x2, x3):
    return sum(1 for i in x1 if x2 <= i <= x3)
    '''counter = 0
    for i in x1:
        if x2 <= i <= x3:
            counter += 1
    return counter'''

list31 = [3, 10, 7, 15, 20, 5, 8, 13]
low = 10
high = 25
print(odd_question(list31, low, high))

# 32.

# 33.

# 34.

# 35.

# 36.

# 37. 

# 38.

# 39.

# 40. 