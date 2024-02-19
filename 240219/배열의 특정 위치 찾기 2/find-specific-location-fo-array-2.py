arr = list(map(int, input().split()))
osum = 0
esum = 0
for i in range(len(arr)):
    if i % 2 == 0:
        osum += arr[i]
    else:
        esum += arr[i]
if osum > esum:
    print(osum - esum)
else:
    print(esum - osum)