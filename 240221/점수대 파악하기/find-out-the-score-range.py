score_arr = list(map(int, input().split()))
result_arr = [0] * 11
for elem in score_arr:
    if elem == 0:
        break
    result_arr[elem // 10] += 1
for elem in range(10, 0, -1):
    print(f"{elem*10} - {result_arr[elem]}")