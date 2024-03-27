cnt = 0
string = []
while True:
    str_input = input()
    if str_input == '0':
        break
    string.append(str_input)
    cnt += 1
print(cnt)
for i in range(0, len(string), 2):
    print(string[i])