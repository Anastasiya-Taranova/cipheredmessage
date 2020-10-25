import re
import sys


def text_from_file():
    with open(sys.argv[1], 'r') as f:
        text = [line.rstrip('\n') for line in f]
        return text


def remove_identical_letters(string):
    text = re.sub(r'([a-z])\1+', r'', string)
    print(text)


if __name__ == '__main__':
    content = text_from_file()

    for string in content:
        remove = remove_identical_letters(string)
