arr = tuple(map(int, input().split()))
for i in range(10):
    if arr[i] == 0:
        break;
    a = i
for i in range(a, -1, -1):
    print(arr[i], end=' ')