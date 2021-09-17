import sys
input = sys.stdin.readline

# 그래프 입력받을 때 list comprehension
matrix = [list(map(str, input().split())) for _ in range(5)]

def dfs(x, y, number):
    if len(number) == 6:
        if number not in answer:
            answer.append(number)
        return 
        
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1] 

    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, number + matrix[ddx][ddy]) 


answer = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])  # 0,0~4,4 검사
print(len(answer))