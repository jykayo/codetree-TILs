import sys
n = int(input())
arr = list(map(int, input().split()))
arr_idx = []
max_val = -sys.maxsize
for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]
        arr_idx.append(i+1)

for i in range(len(arr_idx)-1, -1, -1):
    print(arr_idx[i], end=' ')