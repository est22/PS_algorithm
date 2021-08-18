# 맥주축제
import sys
import heapq

day, sum_preference, kind = map(int,input().split()) # N, M, K
pq = [] # 선호도(V) -> 우선순위 큐
heapq.heapify(pq)
l = [] # 도수 레벨(C)

for _ in range(kind):
    preference, alch = map(int,sys.stdin.readline().split()) # 선호도V, 도수레벨C
    l.append((preference,alch)) # [(2, 5), (4, 6), (3, 3), (4, 3), (1, 4)]
l.sort(key=lambda x: (x[1],x[0])) # [(3, 3), (4, 3), (1, 4), (2, 5), (4, 6)]
find = False
now_alchol = 0
s = 0

for i in range(kind):
    heapq.heappush(pq,l[i][0])

    s += l[i][0] # 3 7 8 9
    now_alchol = l[i][1] # 3 3 4 5
    if len(pq) == day:
        if s >= sum_preference:
            find = True
            print(now_alchol)
            break
        else:
            s -= heapq.heappop(pq)
if not find:
    print(-1)