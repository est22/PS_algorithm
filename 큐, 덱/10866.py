# 덱
from collections import deque
import sys
input = sys.stdin.readline().strip()

N = int(input())
dq = deque()

for i in range(N):
    func = list(input().split())

    if func[0] == "push_front":
        dq.appendleft(func[1])

    elif func[0] == "push_back":
        dq.append(func[1])

    elif func[0] == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    
    elif func[0] == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq.pop())

    elif func[0] == "empty":
        if not dq:
            print(1)
        else:
            print(0)

    elif func[0] == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])

    elif func[0] == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])