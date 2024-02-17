stu = int(input())
cnt = 0
for i in range(stu):
    arr = list(map(int, input().split()))
    avg = 0
    for j in range(len(arr)):
        avg += arr[j]
    avg /= len(arr)
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)