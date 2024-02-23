n = int(input())
arr = list(map(int, input().split()))
max_val = 0
for i in range(n):
    for j in range(i+1, n):
        price = arr[j] - arr[i]
        if price > max_val:
            max_val = price
print(max_val)