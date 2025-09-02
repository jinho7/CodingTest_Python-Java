def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_numbers(current, remaining):
        if current:
            num_set.add(int(current))
        
        for i in range(len(remaining)):
            next_num = current + remaining[i]
            next_remaining = remaining[:i] + remaining[i+1:]
            generate_numbers(next_num, next_remaining)

    num_set = set()
    generate_numbers('', numbers)

    prime_count = sum(1 for num in num_set if is_prime(num))
    return prime_count