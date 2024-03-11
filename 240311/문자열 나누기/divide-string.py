n = int(input())
arr = input().split()
result = ""
for i in range(n):
    result += str(arr[i])
for i in range(len(result)):
    print(result[i], end='')
    if (i+1) % 5 == 0:
        print()