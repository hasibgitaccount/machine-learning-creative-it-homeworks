# data structures
'''
1. list.
2. set.
3. tuple.
4. dictionary.
'''

# LIST

'''list1 = [0]
print(type(list))
print(len(list1)) # we can know the length of a list using len.'''

'''list2 = ['hasib', 5, 5.5, False] # a list can hold all data types
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])'''

# lists are mutable(modifiable).

# 1. add a element. -> APPEND, EXTEND, INSERT.
# 2. remove a element -> POP, REMOVE, DEL, CLEAR.

list3 = [10, 20, 30, 40, 50]
'''
list3[2] = 3
print(list3)'''

#INSERT. 
'''
#insert is used like .insert(index, value) is used to add a element in a specific position of a list.
it does not replace an element, instead it shifts them to the right.
'''

'''list3.insert(len(list3), 60)
print(list3)
list3.insert(2, 30)
print(list3)'''

# APPEND

'''
 append adds an element to the end of a list. 
it modifies a list, does'nt create a new one.
'''

list4 = [10, 20, 30, 40]
'''list4.append(50)
print(list4)
list4.append('melon')
print(list4)
list4.append([50,60])
print(list4)'''

print(list3 + list4)

# EXTEND

# extend adds multiple elements to the element at the end unlike append who treats as a single element.

'''list5 = [11, 22, 33, 44]
list5.extend(list4)
print(list5)
list5.extend((55,66))
print(list5)
list5.extend([77,88])
print(list5)'''
