arr = [
    input()
    for _ in range(10)
]
alp = input()
cnt = 0
for i in range(10):
    if arr[i][-1] == alp:
        print(arr[i])
        cnt += 1
if cnt == 0:
    print("None")