s = input()
lr = input()
for i in range(len(lr)):
    if lr[i] == 'L':
        s = s[1:] + s[0]
    elif lr[i] == 'R':
        s = s[-1] + s[0:-1]
print(s)