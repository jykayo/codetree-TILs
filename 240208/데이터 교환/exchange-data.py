a, b, c = 5, 6, 7
# temp = a
# a = c
# c = b
# b = temp
a, b, c = c, a, b
print(a)
print(b)
print(c)