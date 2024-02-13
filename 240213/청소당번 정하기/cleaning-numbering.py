toi = 0
loc = 0
cla = 0
n = int(input())
for i in range(1, n+1):
    if i % 12 == 0:
        toi += 1
    elif i % 3 == 0:
        loc += 1
    elif i % 2 == 0:
        cla += 1
print(cla, loc, toi)