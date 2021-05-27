n = int(input())
numbers = list(map(int,input().split()))
max_score = max(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] / max_score * 100

print(sum(numbers)/n)