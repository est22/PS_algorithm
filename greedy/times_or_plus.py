numbers = list(map(int,input().split()))
total = 0
while True:
    for i in (0,len(numbers)):
        if numbers[i] == 0 or numbers[i] == 1:
            total += numbers[i] + numbers[i+1]
            break
        total += numbers[i] * numbers[i+1]

print(numbers)