string_a = input()
string_b = input()
cnt = 0
for _ in range(len(string_a)):
    string_a = string_a[-1] + string_a[0:-1]
    cnt += 1
    if string_a == string_b:
        break
    if len(string_a) == cnt and string_a != string_b:
        cnt = -1
print(cnt)