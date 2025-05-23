def d_arraying(x, y, z):
    s =[['*' * x] * y] * z
    for i in s:
        print(i)
    return s
a= 3
b = 4
c = 6
go = d_arraying(c,b,a)

# 50. Write a Python program to sort a list of nested dictionaries.
list50 = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

sorted_list = sorted(list50, key= lambda x: x['key']['subkey'], reverse= False)
print("Sorted List:", sorted_list)