arr = input().split()
cm = int(arr[0])
kg = int(arr[1])
m = cm/100
bmi = kg//(m*m)
print(f"{bmi:.0f}")
if bmi >= 25:
    print("Obesity")