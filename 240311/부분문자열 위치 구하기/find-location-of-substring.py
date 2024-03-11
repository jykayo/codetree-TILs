string = input()
target = input()
check = -1
for i in range(len(string)):
    if string[i] == target[0]:
        for j in range(1, len(target)):
            if string[i+j] != target[j]:
                break
            else:
                check = i
if check == -1:
    print("No")
else:
    print(check)