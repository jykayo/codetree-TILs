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
    if satis == True:
        max_val = arr[i]
print(max_val)