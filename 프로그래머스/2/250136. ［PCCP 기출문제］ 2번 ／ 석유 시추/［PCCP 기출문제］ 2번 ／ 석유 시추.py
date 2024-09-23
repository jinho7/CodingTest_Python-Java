from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    oil_chunks = []
    visited = [[False] * m for _ in range(n)]
    
    def bfs(i, j):
        queue = deque([(i, j)])
        chunk = set([(i, j)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    chunk.add((nx, ny))
        return chunk
    
    # 석유 덩어리 식별
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                oil_chunks.append(bfs(i, j))
    
    # 각 열별 석유량 계산
    column_oil = [0] * m
    for chunk in oil_chunks:
        columns = set()
        for x, y in chunk:
            columns.add(y)
        for col in columns:
            column_oil[col] += len(chunk)
    
    # 최대 석유량 찾기
    return max(column_oil)