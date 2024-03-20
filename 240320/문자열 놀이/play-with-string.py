s, q = input().split()
q = int(q)
for i in range(q):
    num, a, b = list(input().split())
    num = int(num)
    if num == 1:
        s = list(s)
        a = int(a)
        b = int(b)
        s[a-1], s[b-1] = s[b-1], s[a-1]
        s = ''.join(s)
        print(s)
    elif num == 2:
        s = list(s)
        for j in range(len(s)):
            if s[j] == a:
                s[j] = b
        s = ''.join(s)
        print(s)