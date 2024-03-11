string, alp = input().split()
check = -1
for i in range(len(string)):
    if string[i] == alp:
        check = 0
if check == 0:
    print(string.index(alp))
else:
    print("No")