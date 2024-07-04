def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer

    # 한 줄로 해결가능 : list(range(x, n*x+1, x))
