while True:
    arr = input().split()
    num1 = int(arr[0])
    num2 = int(arr[1])
    char = arr[2]
    if char != 'C':
        print(num1 * num2)
    elif char == 'C':
        print(num1 * num2)
        break