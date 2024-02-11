arr1 = input().split()
age_a, gen_a = int(arr1[0]), arr1[1]
arr2 = input().split()
age_b, gen_b = int(arr2[0]), arr2[1]
if ((age_a >= 19 or age_b >= 19) and (gen_a == 'M' or gen_b == 'M')):
    print(1)
else:
    print(0)