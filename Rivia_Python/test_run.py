def reverse_str3(x):
    i = 1
    reversed = ''
    while len(reversed) < len(x):
        reversed += x[len(x) - i]
        i += 1
    return reversed

print(reverse_str3("charles"))