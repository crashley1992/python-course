# my_dict = {'key1': 'value', 'key2': 'value2'}
# print(my_dict)

# my_dict['key1']

# prices_lookup = {'apple':2.99, 'oranges':1.99}
# print(['apple'])

# d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
# print(d['k3']['insideKey'])

pets = {'cat1': "Ayra", "cat:2": "Karrigan", "dog1": "Korra"}

pets_items = pets.items()
print(pets_items)

# The view object returned by .items() yields the key-value pairs 
# one at a time and allows you to iterate through a dictionary in Python
for item in pets.items():
    print(item)

for key in pets.keys():
    print(key + " keys")

