import sys
n = int(input())
arr = list(map(int, input().split()))
min_val = sys.maxsize
for i in arr:
    if i < min_val:
        min_val = i
        cnt = 1
    elif i == min_val:
        cnt += 1
print(min_val, cnt)