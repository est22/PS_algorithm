import sys
from collections import deque

input = sys.stdin.readline

def solution():
    func = input().rstrip()
    _ = input().rstrip() # 입력받을 리스트 원소 수
    arr = deque(input().rstrip().strip('[]').split(','))

    flag = 0 # 0: 앞에서 삭제, 1: 뒤에서 삭제
    for c in func:
        if c == 'D':
            if not arr:
                print("error")
                return
            if flag == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            flag = 1 - flag # flag 뒤집기
            # flag = 0 1
            # flag = 1 0
    if flag == 0:
        print('['+','.join(arr)+']')
    else:
        print('['+','.join(arr[::-1])+']')


for i in range(int(input())):
    solution()