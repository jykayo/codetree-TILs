string = input()
arr = list(string)
arr[1:2] = 'a'
arr[-2:-1] = 'a'
result = ''.join(arr)
print(result)