s = input()
lens = len(s)
for _ in range(lens+1):
    print(s)
    s = s[-1] + s[:-1]