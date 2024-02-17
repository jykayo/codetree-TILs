arr = list(map(int, input().split()))
cnt = 0
sum = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break;
    elif arr[i] % 2 == 0:
        sum += arr[i]
        cnt += 1
print(cnt, sum)