n1, n2 = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(n1-n2+1):
    cnt = 0
    booli = False
    for j in range(n2):
        if arr1[i] == arr2[j]:
            booli = True
            cnt += 1
        else:
            booli = False
            if cnt == n2:
                break
if booli == False:
    print("No")
else:
    print("Yes")