arr = input().split()
a = int(arr[0])
b = int(arr[1])
a *= 10
print("0.", end='')
for i in range(20):
    print(a // b, end='')
    a = a % b * 10