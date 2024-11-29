from collections import deque

def solution(m, n, puddles):
    distance = [[[float('inf'), 0] for _ in range(m+1)] for _ in range(n+1)]
    distance[1][1] = [0, 1]
    queue = deque([(1, 1)])
    directions = [(1, 0), (0, 1)]
    while queue:
        x, y = queue.popleft()
        current_distance = distance[x][y][0]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 범위 체크를 먼저 하고
            if 1 <= nx <= n and 1 <= ny <= m and [ny, nx] not in puddles:
                next_distance = current_distance + 1
                
                if next_distance < distance[nx][ny][0]:
                    distance[nx][ny] = [next_distance, distance[x][y][1]]
                    queue.append((nx, ny))
                elif next_distance == distance[nx][ny][0]:
                    distance[nx][ny][1] += distance[x][y][1]
    
    return distance[n][m][1] % 1000000007