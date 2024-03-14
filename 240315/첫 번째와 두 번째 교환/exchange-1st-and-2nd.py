string = input()
string = list(string)
alp1 = string[0]
alp2 = string[1]
for i in range(len(string)):
    if string[i] == alp1:
        string[i] = alp2
    elif string[i] == alp2:
        string[i] = alp1
result = ''.join(string)
print(result)