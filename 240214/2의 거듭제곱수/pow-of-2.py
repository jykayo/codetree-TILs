n = int(input())
num = 1
x = 0
while True:
    if num == n:
        break
    else:
        num *= 2
        x += 1
print(x)