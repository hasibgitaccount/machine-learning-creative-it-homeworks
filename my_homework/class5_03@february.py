set1 = {1,2,3}
print(set1)
print(type(set1))
print(len(set1))

#in terms of set duplicate value is not allowed. only the unique value is allowed.


set2 = {1,1,1,2,2,4,4,10,12}
print(set2)# the answer will be {1,2,4,10,12}. so only unique value.
#whereas, we could've able to print all those integers using list. lets give an example :
list1 = {1,1,1,2,2,4,4,10,12}
print(list1)


#multiple data type is supported in set. lets give a example:

set3 = {'hasib', 5, 7.12, True}
print(set3) # it will print all of those.
# the same goes for list as well. list also supports multiple data types. lets give some example :
list3 = ['chinku', True, 3, 4.23]
print(list3)



#indexing or slicing is not allowed in set. lets give an example :
set4 = {10,20}
#print(set1[1])  its going to give us a error
#so the only viable solution is to convert the set into a list. lets give an example :
list2 = list(set1)
print(list2)
print(list2[1])
# by that example we can easily get to the conclusion that list supports indexing and slicing


