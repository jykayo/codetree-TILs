n = int(input())
alp = 'A'
for i in range(n):
    for j in range(i+1):
        print(alp, end='')
        alp = chr(ord(alp)+1)
        if alp == chr(ord('Z')+1):
            alp = 'A'
    print()