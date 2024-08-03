dictionary = {'c1': 'value1', 'c2': 'value2'}
print(type(dictionary))
print(dictionary)

result = dictionary['c2']
print(result)

client = {'name': 'Juan', 'LastName': 'Fuentes', 'weight': 88, 'size': 1.76}
consult = (client['LastName'])
print(consult)

consult = (client['size'])
print(consult)

dic = {'ci': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s2'])

dic2 = {'ci': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c2'][1].upper())

dic3 = {1: 'a', 2: 'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())
