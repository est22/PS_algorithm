rows = int(input())

for i in range(rows):
    o_x = input()
    score = 0
    point = 0
    for i in o_x:
        if i == 'O':
            point += 1
            score += point
        else:
            point = 0

    print(score)