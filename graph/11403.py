# 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def bfs(start, end, matrix):
    queue = deque()
    queue.append(start)
    visited = set()

    while queue:
        x = queue.popleft()
        visited.add(x)
        next_row = matrix[x]
        for i in range(len(next_row)):
            if next_row[i] == 1:
                if i == end:
                    return 1
                elif i not in visited:
                    queue.append(i)
                    visited.add(i)
    return 0



ans = [[0 for i in range(N)] for i in range(N)]

# 출력
for j in range(N):
    for i in range(N):
        ans[j][i] = bfs(j,i,matrix)
    print(*ans[j])


###################### 플루이드 - 워셜 알고리즘 #############
'''
import sys
input = sys.stdin.readline

N = int(input())
visited = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            visited[a][b] = max(visited[a][b], visited[a][k]&visited[k][b])

for i in range(N):
    for j in range(N):
        print(visited[i][j], end=" ")
    print()

'''
