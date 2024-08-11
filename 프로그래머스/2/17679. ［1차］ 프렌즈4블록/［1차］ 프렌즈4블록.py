def solution(m, n, board):
    # board를 2차원 리스트로 변환
    board = [list(row) for row in board]
    total_removed = 0
    
    while True:
        to_remove = set()  # 지워질 블록들의 위치를 저장
        
        # 2x2 블록 체크
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '0':
                    to_remove.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
        
        if not to_remove:
            break
        
        # 블록 제거 및 카운팅
        total_removed += len(to_remove)
        for i, j in to_remove:
            board[i][j] = '0'
        
        # 블록 떨어뜨리기
        for j in range(n):
            empty_row = m - 1  # 가장 아래 행을 가리키는 포인터
            for i in range(m - 1, -1, -1):
                # 0이 아닐 때만, empty_row 올린다.
                # 0일땐 안올리다가, 다시 0이 아니면, empty_row는 빈 칸 중아래인 놈이 된다.
                if board[i][j] != '0':
                    # 그대로 두기
                    board[empty_row][j] = board[i][j]
                    # empty_row가 현재 i줄이 아니면 0으로 채움
                    if empty_row != i:
                        board[i][j] = '0'
                    # empty_row 포인터 하나 올림
                    empty_row -= 1
    
    return total_removed
