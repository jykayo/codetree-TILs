count_arr = [0] * 4
cnt = 0
for i in range(3):
    arr = list(input().split())
    cold = arr[0]
    temp = int(arr[1])
    if cold == 'Y' and temp >= 37:
        count_arr[0] += 1
        cnt += 1
    elif cold == 'N' and temp >= 37:
        count_arr[1] += 1
    elif cold == 'Y' and temp <= 36:
        count_arr[2] += 1
    elif cold == 'N' and temp <= 36:
        count_arr[3] += 1
if cnt >= 2:
    count_arr.append('E')
for i in range(5):
    print(count_arr[i], end=' ')