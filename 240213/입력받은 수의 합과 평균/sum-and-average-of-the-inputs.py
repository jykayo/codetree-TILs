n = int(input())
sum = 0
cnt = 0
for i in range(n):
    a = int(input())
    sum += a
    cnt += 1
print(sum, f"{(sum / cnt):.1f}")