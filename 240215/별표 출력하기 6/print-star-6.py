n = int(input())
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for k in range((n-i)*2-1):
        print('*', end=' ')
    print()
for i in range(2, n+1):
    for l in range(n-i):
        print(' ', end=' ')
    for m in range((i*2-1)):
        print('*', end=' ')
    print()