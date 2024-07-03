import math

def solution(n):
    n_sqrt = math.sqrt(n)

    if int(n_sqrt) == n_sqrt:
        return (n_sqrt + 1) * (n_sqrt + 1)
    else :
        return -1