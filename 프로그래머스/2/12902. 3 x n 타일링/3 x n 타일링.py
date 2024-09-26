# https://s2choco.tistory.com/24 참고
import math

def solution(n):
    MOD = 1000000007

    # 일단 홀수가 되면 0
    if n % 2 != 0:
        return 0
    # 짝수가 되면 ?
    # n = 0 : 1 개
    # n = 2 : 3 개
    # n = 4 : 11 개
    # (보면 3가지 타일가지고 양쪽 permutations 나옴 >> 3*3 + 그리고 새로운 문양 2가지 >> 2 = 11)
    # n = 6 : 41개 (11 * 3 + >> 4 * 2)
    # n = 8 : 153개 (41 * 3 + >> 15 * 2)
    else:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[2] = 3

        # n이 2일 때부터 n까지 점화식 계산
        for i in range(4, n+1, 2):
            dp[i] = (3 * dp[i-2]) % MOD
            for j in range(4, i+1, 2):
                dp[i] = (dp[i] + 2 * dp[i-j]) % MOD

    return dp[n]