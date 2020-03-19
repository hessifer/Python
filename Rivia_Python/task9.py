"""
Write a simple method that writes the text hello world to a file named message.txt.
If the file exists, overwrite it.
"""

def main():
    with open('message.txt', 'w+') as fh:
        fh.write('hello world\n')

if __name__ == '__main__':
    main()