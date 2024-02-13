n = int(input())
cnt = 0
i = 1
while n >= 1:
    n //= i
    cnt += 1
    i += 1
    if n > 1:
        continue
print(cnt)