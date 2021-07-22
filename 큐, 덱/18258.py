# 큐2

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque([])

for i in range(n):
    func = input().split()

    if func[0] == 'push':
        dq.append(func[1])
    elif func[0] == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif func[0] == 'size':
        print(len(dq))
    elif func[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif func[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif func[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq(-1))
'''
데크 없이 구현했더니
런타임 에러나서 그냥 데크 씀

stack = []

for i in range(int(input())):
    func = input().split()

    if func[0] == 'push':
        stack.append(func[1])
    elif func[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif func[0] == 'size':
        print(len(stack))
    elif func[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif func[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack(-1))

'''

