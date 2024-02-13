n = int(input())
aa = False
for i in range(2, n):
    if n % i == 0:
        aa = True
if aa == True:
    print('C')
else:
    print('N')