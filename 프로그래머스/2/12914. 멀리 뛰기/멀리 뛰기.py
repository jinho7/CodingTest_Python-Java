def my_solution(n):
    # k x 2 + 1 로 나타낼 수 있고, k 는 0 ~ n//2
    # k에 따라 1의 개수는 n - 2k
    sum = 0
    for k in range(n//2 + 1):
        num_2 = k
        num_1 = n - 2*k
        total = n - k
        result = factorial(total) // ( factorial(num_1) * factorial(num_2) )
        sum += result
    return sum % 1234567

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# 하..결국 그냥 피보나치 수열이었구나..........>
# n번째 칸에 도달하는 방법은 두 가지
# 1) (n-1)번째 칸에서 1칸 뛰기
# 2) (n-2)번째 칸에서 2칸 뛰기
def solution(n):
    MOD = 1234567
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]