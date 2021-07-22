import sys
input = sys.stdin.readline

stack = []

for i in range(int(input())):
    func = input().split()

    if func[0] == 'push':
        stack.append(func[1])
    elif func[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif func[0] == 'size':
        print(len(stack))
    elif func[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

