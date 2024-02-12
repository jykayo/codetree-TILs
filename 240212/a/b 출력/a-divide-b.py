arr = input().split()
a = int(arr[0])
b = int(arr[1])
print(f"{a/b:.1f}", end='')
for i in range(19):
    a = (a * 10) % b
    print(int((a * 10) / b), end='')