my_list = ['a', 'b', 'c']
print(type(my_list))

other_list = ['hello', 55, 6.1]

result = len(my_list)
print(result)

result = my_list[0]
print(result)
result = my_list[0:1]
print(result)
result = my_list[0:2]
print(result)
result = my_list[0:]
print(result)

my_list2 = ['d', 'e', 'f']
print(my_list + my_list2)

my_list3 = my_list + my_list2
print(my_list3)

my_list3[0] = 'alfa'
print(my_list3)

my_list3.append('g')
print(my_list3)

my_list3.pop()
print(my_list3)

deleted = my_list3.pop(0)
print(my_list3)
print(deleted)

lista = ['g', 'o', 'b', 'm', 'c']
print(lista)
lista.sort()
print(lista)

new_list = lista.sort()
print(new_list)
print(type(new_list))

lista.reverse()
print(lista)
