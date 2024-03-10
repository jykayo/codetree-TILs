n, m = tuple(map(int, input().split()))
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for _ in range(m):
    row, col = tuple(map(int, input().split()))
    arr[row-1][col-1] = row*col
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()