strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)
while True:
    for i in range(lenA - lenB + 1):
        check = True
        for j in range(lenB):
            if strA[i+j] != strB[j]:
                check = False
                break
        if check == True:
            break
    if check == False:
        break
    else:
        strA = strA[:i] + strA[i + lenB:]
        lenA = len(strA)
print(strA)