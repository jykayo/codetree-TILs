arr = list(map(int, input().split()))
sum = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] < 250:
        sum += arr[i]
        cnt += 1
    else:
        break
print(sum, (f"{sum/cnt:.1f}"))