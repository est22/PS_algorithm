# 스택 수열
# 처음엔 문제 이해가 잘.. 안갔지만 이해함.

import sys
input = sys.stdin.readline

n = int(input()) # 8
stack = [] # 1, 2, 3, 4, ... (입력해야 할 숫자)
answer = [] # + or -
flag = True
cur = 1


for i in range(n):
    num = int(input()) # 4 3 6 8 7 5 2 1 (출력할 숫자)

    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')

    else:
        flag = False


if flag == True:
    for i in answer:
        print(i)
else:
    print('NO')