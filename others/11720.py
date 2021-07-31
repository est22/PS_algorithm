# 숫자의 합
N = int(input())
nums = input()
sum = 0

for i in range(len(nums)):
    sum += int(nums[i])
print(sum)