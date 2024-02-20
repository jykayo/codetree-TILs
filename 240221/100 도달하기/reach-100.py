n = int(input())
arr = [1, n]
for i in range(2, 10):
    arr.append(arr[-2] + arr[-1])
    if arr[i] >= 100:
        break
for elem in arr:
    print(elem, end=' ')