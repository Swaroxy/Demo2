#Clear
dict1 = {'id':1, 'adress' : 'Balaju', 'email':'raj@gmail.com'}
print(dict1)
dict1.clear()
print(dict1)

#Copy
dict2 = {'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
dict3 = dict2
print(dict3)
print(id(dict2))
print(id(dict3))
dict4 = dict3.copy()
print(id(dict4))

#Get
dict2 = {'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
print(dict2['id'])
print(dict2['address'])
print(dict2['email'])

print(dict2.get('id')) #1
print(dict2.get('address'))
print(dict2.get('email'))



#keys
dict1={'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
print(dict1.keys())
result=dict1.keys()

for key in result:
    print(dict1.get(key))

#Pop
dict1 = {'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
print(dict1.pop('id'))
print(dict1)

#Popitem
dict1 = {'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
print(dict1.popitem())
print(dict1)

#Setdefault
dict1 = {'id':1, 'address':'Balaju', 'email':'raj@gmail.com'}
dict1.setdefault('phone')
print(dict1)

#Values
values = dict1.values()
for value in values:
print(value)
