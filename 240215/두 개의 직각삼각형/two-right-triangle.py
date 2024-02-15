n = int(input())
for i in range(n):
    for j in range(n-i):
        print('*', end='')
    for k in range(i):
        print(' ', end='')
    for l in range(i):
        print(' ', end='')
    for m in range(n-i):
        print('*', end='')
    print()