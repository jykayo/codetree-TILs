n = int(input())
arr = list(map(int, input().split()))
max_val = -1
for i in range(n-1):
    satis = True
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            arr[j] = 0
            satis = False
            break
    if satis == True and arr[i] > max_val:
        max_val = arr[i]
if arr[-1] > max_val and arr[-1] != 0:
    max_val = arr[-1]
print(max_val)