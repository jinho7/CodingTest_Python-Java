from collections import deque

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x, start_y = i, j
    
    def bfs(start_x, start_y, board):
        rows = len(board)
        cols = len(board[0])

        # 방향 벡터 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS를 위한 큐 초기화
        queue = deque([(start_x, start_y, 0)])  # (x, y, 거리)
        visited = [[False] * cols for _ in range(rows)]
        visited[start_x][start_y] = True

        while queue:
            x, y, distance = queue.popleft()

            # 목표 지점에 도달한 경우
            if board[x][y] == "G":
                return distance

            # 네 방향으로 이동
            for dx, dy in directions:
                next_x, next_y = x, y

                # 다음에 벽을 만나거나, 장애물을 만날 때까지 이동
                while True:
                    # 다음 위치가 보드 범위를 벗어나거나, 장애물(D)을 만나면 중단
                    if not (0 <= next_x + dx < rows and 0 <= next_y + dy < cols) or board[next_x + dx][next_y + dy] == "D":
                        break
                    next_x += dx
                    next_y += dy

                # 방문하지 않은 위치라면 큐에 추가하고 방문 처리
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, distance + 1))
        
        # 목표 지점에 도달하지 못한 경우
        return -1

    answer = bfs(start_x, start_y, board)
    return answer
