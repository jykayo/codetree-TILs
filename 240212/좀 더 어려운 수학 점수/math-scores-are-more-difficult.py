arr1 = input().split()
mat_a, eng_a = int(arr1[0]), int(arr1[1])
arr2 = input().split()
mat_b, eng_b = int(arr2[0]), int(arr2[1])
if mat_a > mat_b or (mat_a == mat_b and eng_a > eng_b):
    print('A')
else:
    print('B')