s, q = input().split()
q = int(q)
for _ in range(q):
    num = int(input())
    if num == 1:
        s = s[1:] + s[0]
    elif num == 2:
        s = s[-1] + s[:-1]
    elif num == 3:
        s = s[::-1]
    print(s)