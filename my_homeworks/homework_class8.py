# SUM
a = [1,2,3]
for i in a:
    total = sum(a)
print(total)

# SMALLEST

a = [10,20,30]
for i in a:
    minimum = min(a)
print(minimum)

# LARGEST

a = [11,22,33]
for i in a:
    large = max(a)
print(large)

# EVEN

a = [1,2,3,4,5,6]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

# ODD

c= [1,2,3,4,5,6]
d =[]
for i in c:
    if i % 2 != 0:
        d.append(i)
print(d)