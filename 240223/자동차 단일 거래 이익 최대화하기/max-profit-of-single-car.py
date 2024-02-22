n = int(input())
# arr = list(map(int, input().split()))
arr = [9, 7, 5, 3, 1]
idx = 0
cheep = arr[0]
for i in range(n):
    if arr[i] < cheep:
        cheep = arr[i]
        idx = i
expen = arr[idx]
for i in range(idx, n):
    if arr[i] > expen:
        expen = arr[i]
print(expen - cheep)