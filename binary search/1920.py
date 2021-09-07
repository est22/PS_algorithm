# 수 찾기
import sys
import collections
input = sys.stdin.readline


N = int(input())
number = list(map(int, input().split(' ')))
freqs = collections.Counter(number)

M = int(input())
target = list(map(int, input().split(' ')))

for i in range(M):
    if target[i] in freqs:
        print(1)  
    else:
        print(0)
