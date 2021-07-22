import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
stack = []

answer = [-1] * N

stack.append(0) # 아무거나 추가함 일단

for i in range(len(s)):
    # 스택이 비지 않고, 스택의 제일 위에 있는 인덱스에 해당하는 값보다 인덱스 i의 값이 크면
    while stack and s[stack[-1]] < s[i]:
        answer[stack[-1]] = s[i]
        stack.pop()

    stack.append(i)

for i in answer:
    print(i, end=" ")
