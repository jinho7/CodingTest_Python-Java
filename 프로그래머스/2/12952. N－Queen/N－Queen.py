# 백트레킹 주요 문제
def solution(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:  # 모든 퀸을 놓았다면
            return 1  # 유효한 방법 1개를 찾음
        count = 0  # 유효한 경우의 수를 세는 변수
        for col in range(n):  # 각 열에 대해 퀸을 놓을 수 있는지 확인
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                # 열과 대각선에 퀸이 없다면
                count += backtrack(row + 1, 
                                   cols | {col}, 
                                   diag1 | {row - col}, 
                                   diag2 | {row + col})  # 다음 행으로 넘어가서 퀸 배치 시도
        return count

    return backtrack(0, set(), set(), set())  # 0행부터 시작, 처음에는 아무 퀸도 없음