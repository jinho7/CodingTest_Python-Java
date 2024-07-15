def solution(a, b, n):
    total_bottles = 0
    while n >= a:
        exchanged = (n // a) * b
        total_bottles += exchanged
        n = exchanged + (n % a)
    return total_bottles


total_bottles = 0
def my_solution(a, b, n):
    global total_bottles
    if n >= a:
        exchanged = (n // a) * b
        total_bottles += exchanged
        n = exchanged + (n % a)
        return solution(a, b, n)
    else:
        return total_bottles
