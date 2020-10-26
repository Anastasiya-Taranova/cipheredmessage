import sys


def get_from_file():
    file = sys.argv[1]
    return file


def read_from_file(file):
    text = open(file).read()
    return text


def list_text(text):
    list = [text[i] for i in range(len(text))]
    return list


def remove_duplicates(chars):
    count = 0
    while count < (len(chars) - 1):
        if chars[count] == chars[count + 1]:
            chars.pop(count)
            chars.pop(count)
            if count != 0:
                count -= 1
            continue
        else:
            count += 1
    return chars


def return_to_str(list):
    str = ''.join(list)
    return str


def main():
    infile = get_from_file()
    text_from_file = read_from_file(infile)
    chars = list_text(text_from_file)
    no_duplicates = remove_duplicates(chars)
    text = return_to_str(no_duplicates)
    print(text)


main()
