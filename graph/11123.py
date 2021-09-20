# 양 한마리..양 두마리..
import sys
from typing import Hashable
sys.setrecursionlimit(10000)    #파이썬:재귀 깊이 제한을 풀어줘야함
input = sys.stdin.readline


T = int(input())
H, W = map(int, input().split())



def numLambs(self, grid):
    def dfs(i,j):
        if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
        grid[i][j] != '1':
            return
        grid[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1) 

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

for i in range(T):
    for j in range(H):
        grid = list(input())
        numLambs(grid)

#####################################################
#####################################################

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if not check[nx][ny] and a[nx][ny] == '#':
            dfs(nx, ny)

for _ in range(int(input())):
    ans = 0
    H, W = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    check = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if not check[i][j] and a[i][j] == '#':
                dfs(i, j)
                ans += 1
    print(ans)


