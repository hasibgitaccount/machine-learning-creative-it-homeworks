# prime number
# prime number is a type of number where the number is not divisible by any number other than 1 and that number. 
'''
5 = 1,5 -> prime
4 = 1,2,4 -> not prime
'''
# add the number that is divisible by non primal number
def prime_no(x):
    result = []
    for i in range(2, x):
        if x % i == 0: 
            result.append(i)
        else:
            pass
    return result

n = 50
calling = prime_no(n)
print(calling)

# now if you use 'break' then only the first one will come 
n = 50
result = []
for i in range(2, n):
    if n % i == 0: 
        result.append(i)
        break
print(result)

n = 12
assume = 'prime'
for i in range(2,n):
    if n % i == 0:
        assume = 'non prime'
    else:
        pass
print(assume)