a, b = tuple(map(int, input().split()))
arr = [0] * 10
while a > 1:
    arr[a % b] += 1
    a //= b
result = 0
for elem in arr:
    result += (elem * elem)
print(result)