from collections import deque

def solution(board):
    # 직선 도로 = 100원, 코너 = 500원
    # 한 칸 이동할 때마다 -> 직선 += 1, 코너인지도 확인
    # 최소비용 = 최대한 코너를 쓰지 않고 가자.
    # 갈 떄마다 해당 칸을 갱신 / 방향을 저장해야 함
    # 먼저 최단 거리를 구해보자.
    
    # n x n
    n = len(board)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    # (x, y), 방향, cost
    q = deque([ [(0, 0), (0, 0), 0] ])
    dist[0][0] = 0

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while (q):
        (cx, cy), (c_dx, c_dy), cost = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and dist[nx][ny] > cost:
                ncost = cost + 100
                # 초기 0, 0이 아니고, 방향 전환이 있는가?
                if (c_dx, c_dy) != (0, 0) and (c_dx, c_dy) != (dx, dy):
                    ncost += 500
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                q.append([(nx, ny), (dx, dy), ncost])
    
    return dist[n-1][n-1]