n1, n2 = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
if n1 < n2:
    print("No")
else:
    for i in range(n1-n2+1):
        booli = True
        for j in range(n2):
            if arr1[i+j] != arr2[j]:
                booli = False
                break
        if booli == True:
            break
    if booli == True:
        print("Yes")
    else:
        print("No")