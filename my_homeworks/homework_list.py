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

# 24. Write a Python program to append a list to the second list
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
def circular(x1, x2):
    if len(x1) != len(x2):
        return False
    
    return any(x1[i:] + x1[:i] == x2 for i, v in enumerate(x1))

list26 = [1, 2, 3, 4]
list26_copy = [3, 4, 1, 2]
list26_clone = [2, 3, 4, 5]
print(circular(list26, list26_copy))
print(circular(list26, list26_clone))

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

# 32. Write a Python program to check whether a list contains a sublist.
def contain_or_not_sublist(x1,x2):
    for i in range(len(x1) - len(x2) + 1):
        if x1[i:i+len(x2)] == x2:
            return True
    return False

list32 = [1, 2, 3, 4, 5]
list32_copy = [2, 3]
list32_clone = [1, 5]
list32_another = [3, 4, 5]

print(contain_or_not_sublist(list32, list32_copy))  
print(contain_or_not_sublist(list32, list32_clone))  
print(contain_or_not_sublist(list32, list32_another))

# 33. Write a Python program to generate all sublists of a list.
def generate_sublist(x):
    collect = []
    for i in range(len(x)):
        for n in range(i + 1, len(x) + 1):
            collect.append(x[i:n])
    return collect

list33 = [1, 2, 3]
print(generate_sublist(list33))

# 34.  Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
def sieve_of_eratosthenes(x):
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(x ** 0.5) + 1): # doing squeare root
        if primes[i]: # means, if primes[i] == True
            for j in range(i*i,x + 1, i):
                primes[j] = False

    return [i for i in range(x + 1) if primes[i]]

variable34 = 50
print(sieve_of_eratosthenes(variable34))

# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
def concatenate(x, n):
    return [i + str(z) for i in x for z in range(1, n+1)]
    '''store = []
    for i in x:
        for z in range(1, n + 1):
            store.append(i + str(z))
    return store'''

list35 = ["a", "b", "c"]
variable35 = 3
print(concatenate(list35, variable35))

# 36. Write a Python program to get variable unique identification number or string.
def unique_id(x,y,z):
    return id(x), id(y), id(z)

x1 = 100
y1 = "Hello"
z1 = [1, 2, 3]
print(unique_id(x1,y1,z1))

# 37. Write a Python program to find common items from two lists
def common_items(x, y):
    return [i for i in x if i in y]
    '''vault = []
    for i in x:
        if i in y:
                vault.append(i)
    return vault'''

list37 = [1,2,3,4,5]
list37_copy = [9,8,7,6,5,4]
print(common_items(list37,list37_copy))

# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
def position_changing(x):
    for i in range(0,len(x) - 1, 2):
         x[i], x[i + 1] = x[i + 1] , x[i]
    return x

list38 = [1, 2, 3, 4, 5, 6]
print(position_changing(list38))

# 39. Write a Python program to convert a list of multiple integers into a single integer
def connect_int(x):
    return int(''.join(list(map(str, x))))

list39 = [1, 2, 3, 4, 5]
print(connect_int(list39))

# 40. Write a Python program to split a list based on first character of word.

def add_bla(x):
    # step1
    from collections import defaultdict
    groups = defaultdict(list)

    #step2
    for i in x:
        first_char = i[0]
        groups[first_char].append(i)

    return groups

list40 = ["apple", "banana", "apricot", "blueberry", "cherry"]
print(add_bla(list40))

# 41. Write a Python program to create multiple lists.
def multiple_list(x):
    obj ={}
    for i in range(1, x+1):
        obj[i] = []
    return obj

list41 = 20
print(multiple_list(list41))
    

# 42. Write a Python program to find missing and additional values in two lists.
def miss_addition(x1, x2):
    set1 = set(x1)
    set2 = set(x2)

    missing_value = set1 - set2
    additional_value = set2 - set1

    return f'the missing value is {missing_value} and additional value is {additional_value}' 

list42 = [1, 2, 3, 4, 5]
list42_copy = [4, 5, 6, 7, 8]
print(miss_addition(list42, list42_copy))

# 43. Write a Python program to split a list into different variables.
def splitting(x):
    return {f'var{i + 1}': value for i,value in enumerate(x) }

list43 = [1, 2, 3, 4, 5]
print(splitting(list43))

# 44.  Write a Python program to generate groups of five consecutive numbers in a list.
def mulitple_groups(start, end, group_size = 5):
    groups = []
    for i in range(start, end, group_size):
        group = list(range(i, i + group_size))
        groups.append(group)
    return groups

groups = mulitple_groups(1, 21)  # Generates groups from 1 to 20
print(groups)

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def ultimate_sort(x):
    flatten_list = [j for i in x for j in i]
    return sorted(set(flatten_list))


list45 = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
print(ultimate_sort(list45))

# 47. Write a Python program to insert an element before each element of a list.
def blabber(x1, x2):
    result = []
    for i in x1:
        result.append(x2)  # Add x2 first
        result.append(i)   # Then add the current item
    return result

list47 = [1, 2, 3, 4, 5]
insert_element = 0
print(blabber(list47, insert_element))

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
def nested_seperate(x):
    for i in x:
        print(i)   

list48 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_seperate(list48)

# 49. Write a Python program to convert list to list of dictionaries.
def list_dict(x1, x2):
    converted_to_dict = dict(zip(x1, x2))
    
    return converted_to_dict

list49 = ["Black", "Red", "Maroon", "Yellow"]
list49_copy =  ["#000000", "#FF0000", "#800000", "#FFFF00"]
print(list_dict(list49, list49_copy))

# 50. Write a Python program to sort a list of nested dictionaries.
list50 = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

sorted_list = sorted(list50, key= lambda x: x['key']['subkey'], reverse= False)
print("Sorted List:", sorted_list)

# 51. Write a Python program to split a list every Nth element.\
def split_list_every_nth(x1, x2):
    return [x1[i:i + x2] for i in range(0,len(x1), x2)]

list51 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
dummpy51 = 5  # Split every 5th element
print(split_list_every_nth(list51, dummpy51))

# 54 Write a Python program to concatenate elements of a list.
def concatenate(x):
    connect = ' '.join(x)
    return connect

list54 = ['Hello', 'World', 'Python', 'is', 'awesome']
print(concatenate(list54))

# 55. Write a Python program to remove key-value pairs from a list of dictionaries.
def specific_dict(x):
    keys_to_remove = 'key1'
    return [{k: v for k, v in i.items() if k != keys_to_remove } for i in x]

list55 = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
print(specific_dict(list55))

# 56. Write a Python program to convert a string to a list
def string_list(x):
    new_list = x.split()
    return new_list

string56 = "Hello World Python"
print(string_list(string56))

# 57. Write a Python program to check if all items in a given list of strings are equal to a given string.
def checkis(x1, x2):
    return all(i == x2 for i in x1)

list57 = ["green", "green", "green", "green"]
list57_copy = ["green", "orange", "black", "white"]
print(checkis(list57, 'green'))
print(checkis(list57_copy, 'green'))

# 58.  Write a Python program to replace the last element in a list with another list.
def replace_last(x1, x2):
    return x1[:-1] + x2


list58 = [1, 3, 5, 7, 9, 10]
list58_copy = [2, 4, 6, 8]
print(replace_last(list58, list58_copy))

# 59.  Write a Python program to check whether the n-th element exists in a given list.
def exist_not(x1, x2):
    if -len(x1) <= x2 < len(x1):
        return x1[x2]
    else:
        return 'index not available'
    
list59 = [10, 20, 30, 40, 50]

print(exist_not(list59, 3)) 
print(exist_not(list59, -1))   
print(exist_not(list59, -6))  
print(exist_not(list59, 10))


# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
def small_tuple(x):
    return min(x, key=lambda i: i[1])

list60 = [(4, 1), (1, 2), (6, 4),(5,0)]
print(small_tuple(list60))

