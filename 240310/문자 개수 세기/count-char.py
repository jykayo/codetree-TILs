string = input()
alp = input()
cnt = 0
for i in range(len(string)):
    if string[i] == alp:
        cnt += 1
print(cnt)