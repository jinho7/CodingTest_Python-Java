from collections import deque

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x, start_y = i, j
    
    rows = len(board)
    cols = len(board[0])
        
    # 방문 배열
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start_x][start_y] = True
    
    def bfs(start_x, start_y, board):

        # 방향 벡터 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS를 위한 큐 초기화
        queue = deque([(start_x, start_y, 0)])
        
        while queue:
            x, y, distance = queue.popleft()

            # G 도착
            if board[x][y] == "G":
                return distance

            # 네 방향 이동
            for dx, dy in directions:
                next_x, next_y = x, y

                # 다음에 벽을 만나거나, 장애물을 만날 때까지
                while True:
                    # 다음 위치가 보드 범위를 벗어나거나, D을 만나면 break
                    if not (0 <= next_x + dx < rows and 0 <= next_y + dy < cols) or board[next_x + dx][next_y + dy] == "D":
                        break
                    next_x += dx
                    next_y += dy

                # 방문하지 않은 위치 -> 큐에 추가 + 방문 처리
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, distance + 1))
        
        return -1

    answer = bfs(start_x, start_y, board)
    return answer
