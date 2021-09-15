# 상근이의 여행
''' '모든 곳이 연결된 그래프'->최소 비행기 수: (나라 수 - 1) '''

# import sys

# input = sys.stdin.readline

# T = int(input())    # 테스트 케이스 수

# for i in range(T):
#     country, airplane = map(int, input().split())
#     for j in range(airplane):
#         a, b = map(int, input().split())
#     print(country-1)


'''탐색'''
import sys
input = sys.stdin.readline

T = int(input())    # 테스트 케이스 수

def dfs(node, edge):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for i in range(T):
    country, airplane = map(int, input().split())
    for j in range(airplane):
        a, b = map(int, input().split())
    print(country-1)

