n, q = list(map(int, input().split()))
n_arr = list(map(int, input().split()))
for _ in range(q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        a = arr[1]
        print(n_arr[a-1])
    elif arr[0] == 2:
        a = arr[1]
        if a not in n_arr:
            print(0)
        else:
            print(n_arr.index(a)+1)
    elif arr[0] == 3:
        a, b = arr[1], arr[2]
        for i in range(a-1, b):
            print(n_arr[i], end=' ')
        print()