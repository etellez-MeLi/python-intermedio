from functools import reduce

my_list = [1,4,5,6,9,13,19,21]

odd = [i for i in my_list if i%2 != 0]
odd1 = list(filter(lambda x: x%2 != 0, my_list))

print(odd)
print(odd1)


map_list = [1,2,3,4,5]

squares = [i**2 for i in map_list]
squares_map = list(map(lambda x: x**2, map_list))

print(squares)
print(squares_map)


reduce_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a * b, reduce_list)
print(all_multiplied)