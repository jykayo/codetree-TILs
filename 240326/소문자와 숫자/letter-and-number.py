string = input()
for elem in string:
    if elem >= 'a' and elem <= 'z':
        print(elem, end='')
    elif elem >= 'A' and elem <= 'Z':
        elem = chr(ord(elem) - ord('A') + ord('a'))
        print(elem, end='')
    elif elem >= '0' and elem <= '9':
        print(elem, end='')