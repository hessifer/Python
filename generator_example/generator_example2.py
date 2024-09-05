# using a list
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines


lines = read_large_file('large_file.txt')


# using a generator
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line


lines_gen = read_large_file('large_file.txt')
