n1, n2 = list(map(int, input().split()))
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
for i in range(n1):
    satis = True
    for j in range(n2):
        if arr_A[i] != arr_B[j]:
            satis = False
    if satis == True:
        break
if satis == True:
    print("Yes")
else:
    print("No")