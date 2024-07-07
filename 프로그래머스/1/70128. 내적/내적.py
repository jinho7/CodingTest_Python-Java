def solution(a, b):
    sum = 0
    for i in range(len(a)):
        x = a[i]*b[i]
        sum += x
    return sum