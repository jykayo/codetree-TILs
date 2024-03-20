strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)
while True:
    idx = -1
    for i in range(lenA - lenB + 1):
        check = True
        for j in range(lenB):
            if strA[i+j] != strB[j]:
                check = False
                break
        if check == True:
            idx = 0
            break
    if idx == -1:
        break
    strA = strA[:i] + strA[i + lenB:]
    lenA = len(strA)
print(strA)