arr = list(map(int, input().split()))
sum = 0
for i in arr:
    if arr[i] == 0:
        chk = i
for i in range(chk):
    sum += arr[i]
print(sum)