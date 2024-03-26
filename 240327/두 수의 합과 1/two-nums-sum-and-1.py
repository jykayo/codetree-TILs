a, b = list(map(int, input().split()))
num = a + b
num = str(num)
cnt = 0
for i in range(len(num)):
    if num[i] == '1':
        cnt += 1
print(cnt)