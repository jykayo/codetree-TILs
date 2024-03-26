string = input()
result = 0
for elem in string:
    if ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        result += ord(elem) - ord('0')
print(result, end='')