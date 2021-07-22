while True:
    s = input()
    if s == '.':
        break
    stack = []
    for i in s:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            stack.append(i)
        elif (i == ')' and stack and stack[-1] == '(') or (i == ']' and stack and stack[-1] == '['):
            stack.pop()
        else:
            stack.append(0) #스택에 아무거나 추가해서(반복문을 나갔을때 하나라도 있어야 코드를 줄일 수 있기 때문에) 반복문을 나가기
            break
    print('no' if stack else 'yes')

    '''
    .(마침표) 기준으로 split하는거..rstrip() 해야하나 sys.stdin.readlines()해야하나 고민

    ->처음에 몇문장이라고 입력받는 수가 없으니 그냥 while문 안에 for문

    런타임 에러 나서 if..elif..else 조건문 최소화


    '''
