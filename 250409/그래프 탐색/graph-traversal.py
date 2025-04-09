# n개의 정점 m개의 간선
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]

for edge in edges:
    x, y = edge
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 0
visited = [False for _ in range(0, n+1)]
visited[1] = True
def dfs(v):
    global cnt
    for curr_v in range(1, n+1):
        if graph[v][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)

dfs(1)
print(cnt)