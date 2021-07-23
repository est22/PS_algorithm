from collections import deque
import sys

input = sys.stdin.readline
'''
deque -> iterable한 데이터를 받을 수 있다.
iterable : for문을 사용할 수 있는 친구들이다.
'''


dq = deque(range(1, int(input()) + 1))

while len(dq) != 1:
    dq.popleft() # 위쪽에 있는 카드 삭제
    # 위쪽에 있는 카드를 삭제해서 아래로 보낸다.
    dq.append(dq.popleft())

print(dq[0])