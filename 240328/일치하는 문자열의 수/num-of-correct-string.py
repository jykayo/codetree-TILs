n, str_a = input().split()
n = int(n)
cnt = 0
for i in range(n):
    string = input()
    if str_a == string:
        cnt += 1
print(cnt)