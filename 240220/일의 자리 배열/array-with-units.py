arr = list(map(int, input().split()))
new_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
new_arr[0] = arr[0]
new_arr[1] = arr[1]
for i in range(8):
    new_arr[i+2] = new_arr[i] + new_arr[i+1]
for i in range(10):
    print(new_arr[i] % 10, end=' ')