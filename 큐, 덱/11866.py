# 요세푸스 문제
from collections import deque
import sys
input = sys.stdin.readline

'''
qsize(): 객체의 크기를 반환해준다.
put(): 객체에 value를 넣어준다.
get() : 큐로 따지면 dequeue를 해주는 메소드
'''
N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])

print("<", end='')
while q:
    for i in range(K - 1):
        q.append(q.popleft())
    print(q.popleft(), end='')
    if q:
        print(", ", end='')
print(">")


