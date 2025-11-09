my_dict = {
    'c1': 'valu1e1',
    'c2': 'value2',
    'c3': 'value3'
}

# Keys should be unique, cannot be sequence types like lists, tuples, dictionaries
print(my_dict)
print(type(my_dict))
print(my_dict['c2'])

customer = {
    'name' : 'John',
    'last_name' : 'Doe',
    'weight': 88,
    'height': 1.76
}

print(customer['last_name'])

# Changing values
customer['weight'] = 90
print(customer['weight'])

dic = {
    1:55, 
    2: [1,2,3],
    3: {
        'a': 'b',
        'c': 'd'
    }
}

print(dic[3]['c'])
# Adding a new key-value pair
dic[3]['d'] = 'new value'

print(dic)