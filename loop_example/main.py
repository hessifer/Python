my_dict = {'a': [0, 1, 2, 3], 'b': [0, 1, 2, 3], 'c': [0, 1, 2, 3], 'd': [0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)
