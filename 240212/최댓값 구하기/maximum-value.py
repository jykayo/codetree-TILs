arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
elif b >= a:
    if b >= c:
        print(b)
    else:
        print(c)