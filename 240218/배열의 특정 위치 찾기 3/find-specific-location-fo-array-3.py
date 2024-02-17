arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)):
    if arr[i] == 0:
        chk = i
        break
for i in range(1, 4):
    sum += arr[chk-i]
print(sum)