def solution(nums):
    result = 0
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            for j in range(k+1, len(nums)):
                 if is_prime(nums[i]+nums[k]+nums[j]):
                        result += 1
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True