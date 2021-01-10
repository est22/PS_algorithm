n, m = map(int, input().split())
result = 0

for i in range(n):
    numbers = list(map(int,input().split()))
    min_num = min(numbers)
    result = max(result,min_num)
print(result)