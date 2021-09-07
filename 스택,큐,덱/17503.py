import sys
import heapq

input = sys.stdin.readline
day, sum_taste, kind = map(int,input().split())
l = []
pq = []
heapq.heapify(pq)

for _ in range(kind):
    taste, alch = map(int,sys.stdin.readline().split())
    l.append((taste,alch)) # [(2, 5), (4, 6), (3, 3), (4, 3), (1, 4)]

l.sort(key=lambda x: (x[1],x[0])) # [(3, 3), (4, 3), (1, 4), (2, 5), (4, 6)] 최솟값 찾기. 알콜 낮은순서부터 먼저 정렬하고, 그다음 우선순위.
find = False
now_alchol = 0
s = 0

for i in range(kind):
    heapq.heappush(pq,l[i][0])
    s += l[i][0]
    now_alchol = l[i][1]
    if len(pq) == day:
        if s >= sum_taste:
            find = True
            print(now_alchol)
            break
        else:
            s -= heapq.heappop(pq)
if not find:
    print(-1)