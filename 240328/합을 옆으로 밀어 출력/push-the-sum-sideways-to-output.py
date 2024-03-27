n1 = int(input())
num = 0
for i in range(n1):
    n2 = int(input())
    num += n2
num = str(num)
a = num[0]
result = ''
for i in range(1, len(num)):
    result += num[i]
result = result + a
print(result)