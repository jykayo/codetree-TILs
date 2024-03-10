arr = ["apple", "banana", "grape", "blueberry", "orange"]
alp = input()
cnt = 0
for i in range(len(arr)):
    if arr[i][2] == alp or arr[i][3] == alp:
        print(arr[i])
        cnt += 1
print(cnt)