# dictionary
''' for example in oxford dictionary there are some words and then the meaning of those words. but a word can have multiple meaning . in python the dictionary works exactly the same. there are two main things . one is key whcih stands for the word and the value which stands for meaning . just like dictionary a key can have multiple values but not vice versa. 
'''

'''
dict1 = {'key': 'value'}
print(dict1['key'])
'''

'''
dict2 = {
    'one':{'hasib': 'god gifted'},
     True:2,
    'three':3,
    'list': [1,[2,3,4],5],
    'tuple': (1,2,3)
}
#in dictionary the keys can have only data types like string, integer and float and boolean
#while values can have both data types and structures like in addition list, set, tuple.

print(dict2['one'])
print(dict2[True])
print(dict2.keys())
print(dict2.values())
'''

'''
classroom = {
    'girls': {'a':11, 'b':(22,44), 'c':33, 'd':{'roll':(55,66)}},
    'boys': ['d', 'e', 'f']
}

print(classroom['girls'])
print(classroom['girls']['b'])
print(type(classroom['girls']['b']))
print(classroom['girls']['b'][0])
print(classroom['girls']['d'].keys())
print(classroom['girls']['d'].values())

classroom['girls']['e'] = 100
classroom['girls']['a'] = 111
del classroom['girls']['c']
print(classroom['girls'])
'''

classroom_girls = {'girls': {'a':11, 'b':(22,44), 'c':33, 'd':{'roll':(55,66)}}}
classroom_boys = {'boys': ['d', 'e', 'f']}
classroom_girls.update(classroom_boys)
print(classroom_girls['girls'])
print(classroom_girls.get('girls'))
print(classroom_girls.get('girl'))
print(classroom_girls.get('girl', 50))


list1 = [10,20,30,40]
print(list1.index(20))