string1 = input()
string2 = input()
for i in range(len(string1)):
    if string1[i] != ' ':
        print(string1[i], end='')
for i in range(len(string2)):
    if string2[i] != ' ':
        print(string2[i], end='')