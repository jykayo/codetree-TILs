string = input()
for elem in string:
    if elem >= 'a' and elem <= 'z':
        print(chr(ord(elem) - ord('a') + ord('A')), end='')
    elif elem >= 'A' and elem <= 'Z':
        print(chr(ord(elem) - ord('A') + ord('a')), end='')