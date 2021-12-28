# list comprehension
sq_list = [x**2 for x in range(10)] # produces a list of squares
sq_iterator = (x**2 for x in range(10)) #@ produces an iterator of square


print(sq_list)
print(sq_iterator) # prin generator object

for i in sq_iterator:
    print("{}".format(i))
