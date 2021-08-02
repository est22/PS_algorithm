# 체스판 다시 칠하기
N, M = map(int, input().split())
data = [input() for i in range(N)]


def check(graph):
    answer1, answer2 = 0, 0 # answer1 맨 위 흰색, answer2 맨 위 검은색
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if graph[i][j] == 'B': answer1 += 1
                elif graph [i][j] == 'W': answer2 += 1
answer = int(1e9)

for i in range(N - 7):
    for j in range(M - 7):
        graph = [data[x][j: j + 8] for x in range(i, i + 8)]
        '''
        graph_alter = []
        for x in range(i, i + 8):
            graph_alter.append(data[x][j: j + 8])
        '''
        answer = min(answer, check(graph))




'''
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

graph 배열에 8줄을 차례대로 넣음.
'''