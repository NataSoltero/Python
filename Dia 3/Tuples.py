my_tuple = (1, 2, 3, 4)
print(type(my_tuple))
print(my_tuple[-2])

t = (1, 2, (10, 20), 4)
print(t[2])
print(t[2][0])

t = list(t)
print(type(t))

T = (1, 2, 3)
x, y, z = T
print(x, y, z)

a = (1, 2, 3, 1)
print(len(a))
print(a.count(1))
print(a.index(1))
