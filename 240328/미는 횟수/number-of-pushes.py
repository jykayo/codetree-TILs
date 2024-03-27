string_a = input()
string_b = input()
cnt = 0
while string_a != string_b:
    string_a = string_a[-1] + string_a[0:-1]
    cnt += 1
print(cnt)