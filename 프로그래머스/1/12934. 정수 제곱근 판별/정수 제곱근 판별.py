import math

def solution(n):
    n_sqrt = math.sqrt(n)

    if int(n_sqrt) == n_sqrt:
        return (n_sqrt + 1) * (n_sqrt + 1)
    else :
        return -1

# impprt math 없이 코드 짜기 
def solution2(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else :
        return -1
