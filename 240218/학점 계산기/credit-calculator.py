n = int(input())
arr = list(map(float, input().split()))
score = sum(arr)
result = score / len(arr)
print(f"{result:.1f}")
if result >= 4.0:
    print("Perfect")
elif result >= 3.0:
    print("Good")
else:
    print("Poor")