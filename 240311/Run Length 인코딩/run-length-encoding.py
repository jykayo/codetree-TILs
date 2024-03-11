string = input()
result = ""
rlencoding = string[0]
cnt = 1
for temp in string[1:]:
    if temp == rlencoding:
        cnt += 1
    else:
        result += rlencoding
        result += str(cnt)
        rlencoding = temp
        cnt = 1
result += rlencoding
result += str(cnt)
print(len(result))
print(result)