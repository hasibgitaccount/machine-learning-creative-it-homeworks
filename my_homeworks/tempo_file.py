def inter(n, x):
    return bool(set(n) & set(x))

list11 = [1,2,3,4,5]
list11_copy = [9,8,7,6,5]
checking = inter(list11, list11_copy)
print(checking)

def clone(x1, x2):
    for i in x1:
        if i in x2:
            return True
    else:
        return False
        
cloning = clone(list11, list11_copy)
print(cloning)
