from collections import deque

def solution(maps):
    
    # bfs 를 만들껀데, maps, start, target 파라미터로 만들자.
    # bfs 2번 사용 : S -> L & L -> E
    answer = 0
    
    s_to_l = bfs(maps, "S", "L")
    l_to_e = bfs(maps, "L", "E")
    return s_to_l + l_to_e if s_to_l != -1 and l_to_e != -1 else -1

# 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
# 즉, S -> L 일 때, E는 지나갈 수 있음 (제한 구역이 아님)
# 또한, visited도 두 Step에서 매번 초기화
def bfs(maps, start, target):
    n , m = len(maps), len(maps[0])
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    visited = [[False] * m for _ in range(n)]
    
    # start의 위치 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                start_x, start_y = i, j
        
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    
    while queue:
        x, y, distance = queue.popleft()
        if maps[x][y] == target:
            return distance
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
                
    return -1