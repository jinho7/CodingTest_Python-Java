def solution(board):
    rows = len(board)
    cols = len(board[0])
    
    # DP 테이블 생성
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                # 첫 행이나 첫 열은 그대로 1로 설정
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # dp 테이블 갱신
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # 최대 변의 길이 갱신
                max_side = max(max_side, dp[i][j])
    
    # 정사각형의 넓이 반환
    return max_side * max_side
