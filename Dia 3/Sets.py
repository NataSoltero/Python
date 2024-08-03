my_set = set([1, 2, 3, 4, 5])
print(type(my_set))
print(my_set)

other_set = {1, 2, 3}
print(type(other_set))
print(other_set)

#print(my_set[0])

set_tuple = set((1, 2, 3, 4, (1, 2, 3), 1, 1, 1, 2, 2, 2))
print(type(set_tuple))
print(set_tuple)

print(len(my_set))
print(2 in my_set)

s2 = {3, 4, 5}
s3 = other_set.union(s2)
print(s3)

other_set.add(4)
print(other_set)

other_set.remove(3)
print(other_set)

other_set.discard(6)
print(other_set)

other_set.pop()
print(other_set)

other_set.clear()
print(other_set)
