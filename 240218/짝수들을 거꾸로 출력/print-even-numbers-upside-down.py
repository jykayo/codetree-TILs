n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if arr[n-i-1] % 2 == 0:
        print(arr[n-i-1], end=' ')