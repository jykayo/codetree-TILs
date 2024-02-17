arr = list(map(int, input().split()))
sum = 0
a = 0
for i in range(len(arr)):
    if arr[i] == 0:
        a = i
        break
    sum += arr[i]
print(sum, (f"{(sum/a):.1f}"))