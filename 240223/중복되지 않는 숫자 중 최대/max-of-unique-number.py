n = int(input())
arr = list(map(int, input().split()))
max_val = -1
for i in range(n):
    if arr[i] > max_val:
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt == 1:
            max_val = arr[i]
print(max_val)