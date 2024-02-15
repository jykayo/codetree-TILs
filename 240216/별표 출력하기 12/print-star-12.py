n = int(input())
for i in range(n):
    for j in range(n):
        if (i > j and j % 2 == 1) or (i > 0 and j % 2 == 0):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()