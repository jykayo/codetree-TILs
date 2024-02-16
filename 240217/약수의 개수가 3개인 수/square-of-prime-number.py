arr = input().split()
start = int(arr[0])
end = int(arr[1])
cnt = 0
for i in range(start, end+1):
    div = 0
    for j in range(1, i):
        if i % j == 0:
            div += 1
    if div == 3:
        cnt += 1
print(cnt)