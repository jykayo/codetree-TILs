n = int(input())
arr = [
    input()
    for _ in range(n)
]
result = ""
for elem in arr:
    result += elem
print(result)