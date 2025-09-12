from collections import deque

def solution(rows, columns, queries):
    # 0. [사전작업] 인덱스 변환
    queries = [[x-1 for x in query] for query in queries]

    # 1. 행렬 만들기
    board = [[c + (columns * r) + 1 for c in range(columns)] for r in range(rows)]
    
    # 2. 실제 회전
    def rotation(query):
        # x1, y1: 왼쪽 위 / x2, y2: 오른쪽 아래
        x1, y1, x2, y2 = query

        # 2-1. 기존 숫자 담아두기
        temp = deque([])
        for i in range(y1, y2):
            temp.append(board[x1][i])
        for i in range(x1, x2):
            temp.append(board[i][y2])
        for i in range(y2, y1, -1):
            temp.append(board[x2][i])
        for i in range(x2, x1, -1):
            temp.append(board[i][y1])
            
        # 2-2. 한칸 밀기
        temp.appendleft(temp.pop())
        
        # 2-3. 그대로 덮어 씌우기
        new_board = board.copy()
        
        j = 0
        for i in range(y1, y2):
            new_board[x1][i] = temp[j]
            j += 1
        for i in range(x1, x2):
            new_board[i][y2] = temp[j]
            j += 1
        for i in range(y2, y1, -1):
            new_board[x2][i] = temp[j]
            j += 1
        for i in range(x2, x1, -1):
            new_board[i][y1] = temp[j]
            j += 1
            
        return min(temp), new_board
    
    answer = []
    
    for query in queries:
        minimum, new_board = rotation(query)
        answer.append(minimum)
        board = new_board
    
    return answer