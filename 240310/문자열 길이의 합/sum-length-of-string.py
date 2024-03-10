n = int(input())
arr = [
    input()
    for _ in range(n)
]
cnt = 0
str_arr = 0
for i in range(n):
    str_arr += len(arr[i])
    if arr[i][0] == 'a':
        cnt += 1
print(str_arr, cnt)