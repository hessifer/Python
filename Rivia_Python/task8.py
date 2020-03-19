def build_greeting(name: str) -> str:
    '''Builds and returns a simple greeting.'''
    return "{}, Python coding is so much fun!".format(name)


def main():
    '''Main entry of program.'''
    name = 'Charles'
    print(build_greeting(name))


if __name__ == '__main__':
    main()
