import re
import sys


def text_from_file():
    with open(sys.argv[1], 'r') as f:
        text = [line.replace(' ', '') for line in f]
        return text


r = re.compile(r'([a-z])\1')


def remove_identical_letters(string):
    text = r.sub(r'', string)
    print(text)


if __name__ == '__main__':
    content = text_from_file()

    for string in content:
        remove = remove_identical_letters(string)
