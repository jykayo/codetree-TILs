s, q = input().split()
q = int(q)
for i in range(q):
    num, a, b = input().split()
    num = int(num)
    if num == 1:
        a = int(a)
        b = int(b)
        s = list(s)
        s[a-1], s[b-1] = s[b-1], s[a-1]
        print(''.join(s))
    elif num == 2:
        for j in range(len(s)):
            if s[j] == a:
                s[j] = b
        print(''.join(s))