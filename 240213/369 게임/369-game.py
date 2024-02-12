n = int(input())
for i in range(1, n+1):
    if i >= 10:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print(0, end=' ')
        elif i % 30 >= 0 and i % 30 < 10:
            print(0, end=' ')
        else:
            print(i, end=' ')
    elif i <= 10:
        if i % 3 == 0:
            print(0, end=' ')
        else:
            print(i, end=' ')