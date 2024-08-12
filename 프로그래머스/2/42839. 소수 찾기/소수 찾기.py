from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 모든 가능한 숫자 조합 생성
    num_set = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num_set.add(int(''.join(perm)))

    # 소수 개수 세기
    prime_count = sum(1 for num in num_set if is_prime(num))

    return prime_count