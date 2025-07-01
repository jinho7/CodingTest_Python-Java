def solution(board, skill):
    # 누적합 사용
    n, m = len(board), len(board[0])
    
    diff = [[0] * (m+1) for _ in range(m+1)]
    
    for tp, r1, c1, r2, c2, degree in skill:
        add = degree if tp == 2 else -degree
        diff[r1][c1] += add
        diff[r1][c2+1] -= add
        diff[r2+1][c1] -= add
        diff[r2+1][c2+1] += add
    
    # 가로 누적합
    for i in range(len(board)+1):
        for j in range(1, len(board[0])+1):
            diff[i][j] += diff[i][j-1]
    # 세로 누적합
    for j in range(len(board)+1):
        for i in range(1, len(board[0])+1):
            diff[i][j] += diff[i-1][j]
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + diff[i][j] > 0:
                answer += 1    
    
    return answer