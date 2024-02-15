n = int(input())
a = 11
for i in range(n):
    num = a
    for j in range(n):
        print(num, end=' ')
        num += 2
    a += 2
    print()