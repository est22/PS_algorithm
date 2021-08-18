# 콘서트
import sys
import heapq
input = sys.stdin.readline

n = int(input())
ticket = map(int,input().split())

heap = []
for num in ticket:
    heapq.heappush(heap,num)

sorted_nums = []
while heap:
    sorted_nums.append(heapq.heappop(heap))


cur = 1

for i in range(len(sorted_nums)):
    if cur == sorted_nums[i]:
        cur += 1
    else:
        break
print(cur)






