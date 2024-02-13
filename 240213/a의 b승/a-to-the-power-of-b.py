arr = input().split()
a = int(arr[0])
b = int(arr[1])
mul = 1
for i in range(b):
    mul *= a
print(mul)