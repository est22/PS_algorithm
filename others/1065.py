# 한수
import sys
input = sys.stdin.readline
N = int(input())



def hansu(N):
    
    if N < 100: 
        return N

    else:
        count = 99
        for i in range(100, N+1):
            nums = list(map(int, str(i))) ##### 주의 #####
            if nums[0] - nums[1] == nums[1] - nums[2]:
                count += 1
        return count

print(hansu(N))


####### 주의 #######
'''
str(N)이 아니라 str(i)를 해야하는 이유 

str(i)를 하면 i = 124라고 했을 때, 
[1, 0, 0] -> [1, 0, 1] -> ... -> [1, 2, 3] -> [1, 2, 4]
로 하나씩 증가하면서 리스트 안의 수가 변한다.

str(N)을 하면 계속
[1, 2, 4]의 반복으로 변동이 없다.
for문으로 카운트를 해주어야하는데.. 조건으로 비교를 한다고 해도 
nums는 변동이 없이 계속 같은 형태로 출력이 되므로 계속 count가 올라간다.

'''
