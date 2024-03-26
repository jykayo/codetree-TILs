a, b = input().split()
check1 = 0
check2 = 0
for i in range(len(a)):
    if a[i] > '9' or a[i] < '0':
        check1 = i
        break
    else:
        check1 = len(a)
for j in range(len(b)):
    if b[j] > '9' or b[j] < '0':
        check2 = j
        break
    else:
        check2 = len(b)
str_a = a[:check1]
str_b = b[:check2]

print(int(str_a) + int(str_b))