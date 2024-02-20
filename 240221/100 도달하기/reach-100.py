n = int(input())
arr = [1, n]
i = 2
while True:
    arr.append(arr[-2] + arr[-1])
    if arr[i] >= 100:
        break
    i += 1
for elem in arr:
    print(elem, end=' ')