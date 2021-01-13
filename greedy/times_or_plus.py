numbers = input() #  02984
result = int(numbers[0]) #  0

for i in range (1,len(numbers)):
    num = int(numbers[i]) 
    if num <= 1 or result <= 1:
        result += num
    else: result *= num

print(result)

#  오답(초기)
# numbers = list(map(int,input().split()))
# total = 0
# while True:
#     for i in (0,len(numbers)):
#         if numbers[i] == 0 or numbers[i] == 1:
#             total += numbers[i] + numbers[i+1]
#             break
#         total += numbers[i] * numbers[i+1]

# print(numbers)