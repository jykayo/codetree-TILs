a = input()
b = input()
num1 = ''
num2 = ''
for elem in a:
    if ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        num1 += elem
for elem in b:
    if ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        num2 += elem
result1 = int(num1)
result2 = int(num2)
print(result1 + result2)