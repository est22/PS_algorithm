import sys
from collections import deque
input = sys.stdin.readline

def bfs(matrix):
    queue = deque()
    a = [0,0,-1,1,1,1,-1,-1] # x좌표, y좌표상으로 상 하 좌 우 우상 우하 좌상 좌하 
    b = [1,-1,0,0,1,-1,1,-1]
    island = 0
    # 아무것도 안한 초기 상태. 제일 최초의 1을 탐색
    for i in range(h):
        for j in range(w):
            # 아직 안방문한 곳 중 1이 있다면 큐에 추가
            if matrix[i][j] == 1 and visited[i][j] == False:
                queue.append(i)
                queue.append(j)
                visited[i][j] = True
                while queue: # 이 과정을 반복
                    x = queue.popleft()
                    y = queue.popleft()
                    for k in range(0,8):  # 주변 팔방 탐색
                        p = x + int(a[k]) # 여기가 1차고비
                        q = y + int(b[k])
                        # 2차 고비
                        # 위의 p, q포지션(1의 주변 포지션)이 1이고 아직 방문 안했을때
                        if 0 <= int(p) < h and 0 <= int(q) < w and matrix[p][q]==1 and visited[p][q]==False:
                            queue.append(p)
                            queue.append(q)
                            visited[p][q] = True
                
                island += 1
    print(island)

w, h = map(int, input().split())

while w != 0 and h != 0:
    matrix = [[x for x in map(int, input().split())] for y in range(h)] ### 인접행렬 받기 list comprehension
    visited = [[False for _ in range(w)] for _ in range(h)]

    bfs(matrix) 

    w, h = map(int, input().split())
