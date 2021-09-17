# 그래프탐색 2
# 최소 스패닝 트리 - Kruskal, Prim
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())

q = int(input())
for _ in range(q):
    i, j = map(int, input().split())
    