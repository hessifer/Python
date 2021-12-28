import math

"""
If you have an iterable that is too large to fit in memory in full 
(e.g., when dealing with large files), being able to take and use 
chunks of it at a time can be very valuable. Implement a generator 
function, chunker, that takes in an iterable and yields a chunk of
 a specified size at a time. Calling the function like this:

for chunk in chunker(range(25), 4):
    print(list(chunk))

"""

def main():
    for chunk in chunker(range(25), 4):
        print(list(chunk))


def chunker(iterable, size):
    start = 0
    end = size

    for i in range(math.ceil(len(iterable) / size)):
        yield iterable[start:end]
        start += size
        end += size

if __name__ == '__main__':
    main()
