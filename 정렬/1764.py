# 듣보잡
import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
havent_seen = set()
havent_heard = set()

for name in range(N):
    havent_seen.add(input().rstrip())

for name in range(M):
    havent_heard.add(input().rstrip())

result = sorted(list(havent_seen & havent_heard))

print(len(result))
for i in result:
    print(i)




