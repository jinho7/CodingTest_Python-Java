def solution(n):
    next_n = n
    while 1:
        next_n += 1
        if bin(n)[2:].count('1') == bin(next_n)[2:].count('1'):
            break
    return next_n