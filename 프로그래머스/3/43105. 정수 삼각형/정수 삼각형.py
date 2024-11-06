def solution(triangle):
    # 1. dp 배열 초기화 (triangle과 같은 크기로)
    dp = [[0] * len(row) for row in triangle]
    
    # 2. 첫 번째 값 설정
    dp[0][0] = triangle[0][0]
    
    # 3. 각 행에 대해
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:  # 각 행의 첫 번째 숫자
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:  # 각 행의 마지막 숫자
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:  # 중간에 있는 숫자들
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    # 4. 마지막 행에서 최대값 찾기
    return max(dp[-1])