n = int(input())
if n == 2:
    print(28)
elif (n <= 7 and n % 2 == 1) or (n <= 12 and n % 2 == 0):
    print(31)
else:
    print(30)