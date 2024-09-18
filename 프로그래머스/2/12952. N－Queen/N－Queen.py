def solution(n):
    
    # 초기화
    queens = []
    answer = 0
    
    def backtrack(row):
        nonlocal answer
        
        # 모든 퀸을 배치한 경우
        if row == n:
            answer += 1
            return
        
        # 해당 행(row)의 각 열(col)에 퀸을 배치 시도
        for col in range(n):
            # 퀸을 놓을 수 있는지 검사
            if is_safe(row, col):
                # 퀸을 배치하고 다음 행으로 이동
                queens.append((row, col))
                backtrack(row + 1)
                # 백트래킹: 다시 퀸을 제거하고 다른 위치 시도
                queens.pop()
        
    
    # 주어진 위치에 퀸을 놓을 수 있는지 확인하는 함수
    def is_safe(row, col):
        for r, c in queens:
            # 같은 열에 있거나 대각선에 있는지 확인
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True
    
    # 백트래킹 시작: 첫 번째 행부터 시작
    backtrack(0)
    
    return answer
