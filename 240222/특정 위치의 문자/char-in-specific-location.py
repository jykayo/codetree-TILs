arr = ['L', 'E', 'B', 'R', 'O', 'S']
c = input()
idx = -1
for elem in arr:
    if elem == c:
        idx = elem
if idx == -1:
    print("None")
else:
    print(arr.index(c))