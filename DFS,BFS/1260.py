# 정점, 간선, 시작노드 입력받기
n, m, v = map(int,input().split())
graph = [[0]*(n+1) for i in range(n+1)]

# 간선이 연결하고 있는 노드상태 입력받기
for i in range(m):
    from_, to_ = map(int, input().split())
    graph[from_][to_] = graph[to_][from_] = 1 # 양방향

visited = [0]*(n+1)

def dfs(v):
    #현재 노드를 방문처리
    print(v, end=' ') # 먼저 출력 하고 그다음
    visited[v] = 1   # 방문 처리
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1: # 아직 방문 안했지만 방문할 노드
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.pop(0)
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1: # 아직 방문 안했지만 방문할 노드
                queue.append(i)
                visited[i] = 1




dfs(v)
print()
visited=[0]*(n+1)
bfs(v)

