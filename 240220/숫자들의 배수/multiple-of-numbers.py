n = int(input())
cnt = 0
arr = [n]
for i in range(1, 100):
    arr.append(arr[-1] + arr[0])
    if arr[-1] % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
for i in range(len(arr)):
    print(arr[i], end=' ')