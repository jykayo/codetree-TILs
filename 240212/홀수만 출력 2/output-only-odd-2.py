arr = input().split()
b = int(arr[0])
a = int(arr[1])
if b % 2 == 1:
    for i in range(b, a-1, -2):
        print(i, end=' ')
else:
    b -= 1
    for i in range(b, a-1, -2):
        print(i, end=' ')