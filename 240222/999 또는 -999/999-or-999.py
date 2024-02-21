arr = list(map(int, input().split()))
max_val, min_val = arr[0], arr[0]
for i in range(1, len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]
print(max_val, min_val)