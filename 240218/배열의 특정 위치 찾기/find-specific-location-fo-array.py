arr = list(map(int, input().split()))
sum = 0
avg = 0
cnt = 0
for i in range(1, len(arr)+1):
    if i % 2 == 0:
        sum += arr[i-1]
    elif i % 3 == 0:
        avg += arr[i-1]
        cnt += 1
avg /= cnt
print(sum, f"{avg:.1f}")