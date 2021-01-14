numbers = input()
change_to_zero = 0
change_to_one = 0


if numbers[0] == '1':   #  첫번째가 1이면, 0을 만날때마다 바꿔야함.
    change_to_zero += 1
else:
    change_to_one += 1

for i in range(len(numbers)-1):
    if numbers[i] != numbers[i+1]:
        if numbers[i+1] == '1':
            change_to_zero += 1
        else:
            change_to_one += 1


print(min(change_to_one,change_to_zero))