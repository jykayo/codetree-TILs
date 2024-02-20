arr = list(map(int, input().split()))
new_arr = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    if arr[i] % 2 == 1:
        new_arr.append(arr[i] + 3)
    else:
        new_arr.append(arr[i] // 2)
for elem in new_arr:
    print(elem, end=' ')