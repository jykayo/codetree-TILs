sum = 0
cnt = 0
while True:
    age = int(input())
    if age >= 30 or age <= 19:
        break
    sum += age
    cnt += 1
print(f"{(sum / cnt):.2f}")