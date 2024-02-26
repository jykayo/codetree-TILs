arr = [
    list(map(int, input().split()))
    for _ in range(2)
]
total = 0
cnt = 0
for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr[i][j]
        cnt += 1
    total += sum
    print(f"{(sum/4):.1f}", end=' ')
print()
for j in range(4):
    sum = 0
    for i in range(2):
        sum += arr[i][j]
        cnt += 1
    total += sum
    print(f"{(sum/2):.1f}", end=' ')
print()
print((f"{(total/cnt):.1f}"))