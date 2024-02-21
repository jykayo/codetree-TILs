n1, n2 = list(map(int, input().split()))
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
satis = True
for i in range(n1):
    for j in range(n2):
        if arr_A[i] != arr_B[j]:
            satis = False
    if satis == True:
        break
if satis == True:
    print("Yes")
else:
    print("No")