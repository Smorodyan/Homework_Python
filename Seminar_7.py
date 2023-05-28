# Task 47
'''
values = [1, 23, 42, 'asdfg']
transformation = lambda values: values
transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')
'''


# Task 49:

# def find_farthest_orbit(orbits):
#     max = 0
#     max_i = 0
#     for i in range(len(orbits)):
#         if max < orbits[i][0] * orbits[i][1]:
#             max = orbits[i][0] * orbits[i][1]
#             max_i = i
#     return orbits[max_i]

'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit = max(orbits, key = lambda x: 3.14 * x[0] * x[1] if x[0] != x[1] else False)
print(find_farthest_orbit)
'''


'''
def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x ** 2), res))
print(res)
'''


# Task 51:

values = [0, 2, 9, 6]

same_by = list(filter(lambda x: True if x % 2 == 0 else False, values))
print(same_by)

if same_by == values:
    print("same")
else:
    print("different")

