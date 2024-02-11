arr = input().split()
b = int(arr[0])
a = int(arr[1])
if b % 2 == 0:
    while b >= a:
        print(b, end=' ')
        b -= 2
else:
    b -= 1
    while b >= a:
        print(b, end=' ')
        b -= 2