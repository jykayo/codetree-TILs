arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
if a > b:
    if b > c:
        print(b)
    elif c > a:
        print(a)
    else:
        print(c)
elif b > a:
    if c > b:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)