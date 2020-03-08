def rev(name):
    ptr = len(name) - 1
    letters = []

    while ptr >= 0:
        letters.append(name[ptr])
        ptr -= 1
    return "".join(letters)


def rev2(name):
    res = ''
    for c in name:
        res = c + res
    
    return res


def rev3(name):
    return name[::-1]
   

print(rev('miles'))
print(rev2('charles'))
print(rev3('pat'))

