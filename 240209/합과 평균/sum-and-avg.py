inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum = a + b
ave = sum / len(arr)
print(f"{sum} {ave:.1f}")