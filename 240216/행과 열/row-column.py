arr = input().split()
a = int(arr[0])
b = int(arr[1])
for i in range(a):
    for j in range(b):
        print((i+1)*(j+1), end=' ')
    print()