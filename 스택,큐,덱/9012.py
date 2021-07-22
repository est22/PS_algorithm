import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    stack = []
    command = input()
    size = 0

    for j in command:
        if j == '(':
            stack.append(j)
            size += 1
        elif j == ')':
            size -= 1
        if size < 0 :
            print("NO")
            break
    if size > 0:
        print("NO")
    elif size == 0:
        print("YES")


