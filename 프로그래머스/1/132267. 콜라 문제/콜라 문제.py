def solution(a, b, n):
    total_bottles = 0
    while n >= a:
        exchanged = (n // a) * b
        total_bottles += exchanged
        n = exchanged + (n % a)
    return total_bottles