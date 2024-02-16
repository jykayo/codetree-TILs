n = int(input())
alp = 'A'
for i in range(n):
    for j in range(n):
        if i > j:
            print(' ', end=' ')
        else:
            print(alp, end=' ')
            alp = chr(ord(alp)+1)
            if ord(alp) > ord('Z'):
                alp = 'A'
    print()