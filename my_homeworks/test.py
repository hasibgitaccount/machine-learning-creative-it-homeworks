def d_arraying(x, y, z):
    s =[['*' * x] * y] * z
    for i in s:
        print(i)
    return s
a= 3
b = 4
c = 6
go = d_arraying(c,b,a)
