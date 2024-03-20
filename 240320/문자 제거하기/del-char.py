string = input()
while len(string) > 1:
    num = int(input())
    if num >= len(string):
        num = len(string)-1
    string = list(string)
    string.pop(num)
    string = ''.join(string)
    print(string)