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

# find all the even numbers in range 1 to 100
def even_100(x):
    result = [i for i in range(1, x + 1) if i % 2 == 0]
    return result

example = 100
answer = even_100(example)
print(answer)

# find first 10 even numbers
def even_10(x):
    counter = 0
    even = []
    for i in range(1, x + 1):
        if i % 2 == 0:
            counter += 1
            if counter > 10:
                break
        even.append(i)
    return even

a = 1000
called = even_10(a)
print(called)


def check_prime(n):
    assume = 'prime'
    for i in range(2,n):
        if n % i == 0:
            assume = 'non prime'
            break
    return assume

existence = 17
result = check_prime(existence)
print(result)

# find the first 10 prime number
counter = 0
for i in range(1,1000000):
    result = check_prime(i)
    if result == 'prime':
        counter += 1
        if counter <= 10:
            print(i)
        else:
            break