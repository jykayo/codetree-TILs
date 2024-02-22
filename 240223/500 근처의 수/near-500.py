arr = list(map(int, input().split()))
over, under = 1000, 0
for elem in arr:
    if elem > 500 and elem < over:
        over = elem
    if elem < 500 and elem > under:
        under = elem
print(under, over)