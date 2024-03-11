string = input()
result = []
for i in range(len(string)):
    if i % 2 == 1:
        result.append(string[i])
for i in range(len(result)-1, -1, -1):
    print(result[i], end='')