# 바이러스
import sys
input = sys.stdin.readline


N = int(input())
pairs = int(input())
s = [[0] * N for i in range(N)]
visit = [0 for i in range(N)]

def dfs(v):
    visit[v] = 1
    for i in range(N):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)
for i in range(pairs):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1
dfs(0)

cnt = 0
for i in range(1, N):
    if visit[i] == 1:
        cnt += 1
print(cnt)