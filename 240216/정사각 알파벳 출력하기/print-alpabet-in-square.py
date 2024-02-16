n = int(input())
alp = 'A'
for i in range(n):
    for j in range(n):
        print(alp, end='')
        alp = chr(ord(alp)+1)
    print()