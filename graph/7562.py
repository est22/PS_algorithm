# 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(x, y, last_x, last_y):
    q = deque()
    q.append([x, y])
    matrix[x][y] = 1    # count

    while q:
        x, y = q.popleft()

        if x == last_x and y == last_y:
            return matrix[x][y] - 1     # acc. line 26

        # search around
        for i in range(8): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < I and 0 <= ny < I:
                if matrix[nx][ny] == 0:
                    q.append([nx, ny])
                    matrix[nx][ny] = matrix[x][y] + 1 




T = int(input())
while T:
    I = int(input())
    matrix = [[0] * I for _ in range(I)] # for문 순회하는 인덱스로 알파벳을(i) 넣으면 not accessed 뜸.
    cur_x, cur_y = map(int,input().split())
    goal_x, goal_y = map(int, input().split())
    
    # Test case 3 treatment
    if cur_x == goal_x and cur_y == goal_y:
        print(0) 
        T -= 1
        continue # go back to 30 line..
    ans = bfs(cur_x, cur_y, goal_x, goal_y)
    print(ans)
    T -= 1
