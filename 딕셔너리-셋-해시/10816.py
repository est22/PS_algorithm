# 숫자카드 2
import sys
import collections
input = sys.stdin.readline


N = int(input())
cards = list(map(int, input().split(' ')))
freqs = collections.Counter(cards)

M = int(input())
search = list(map(int, input().split(' ')))

for i in range(M):
    if search[i] in freqs:
        print(freqs[search[i]], end= ' ') ############ 
    else:
        print(0, end=' ')





