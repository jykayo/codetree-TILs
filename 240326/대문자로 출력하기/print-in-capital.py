string = input()
for elem in string:
    if elem >= 'a' and elem <= 'z':
        elem = chr(ord(elem) - ord('a') + ord('A'))
        print(elem, end='')
    elif elem >= 'A' and elem <= 'Z':
        print(elem, end='')