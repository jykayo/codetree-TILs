n, m = tuple(map(int, input().split()))
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 1
for col in range(n):
    i = 0
    j = col
    while i < n and j >= 0:
        arr[i][j] = num
        num += 1
        i += 1
        j -= 1
for row in range(1, m):
    i = row
    j = m-1
    while i < n and j >= 0:
        arr[i][j] = num
        num += 1
        i += 1
        j -= 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()