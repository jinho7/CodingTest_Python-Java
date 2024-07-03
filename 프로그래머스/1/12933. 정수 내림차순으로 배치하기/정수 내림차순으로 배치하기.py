def solution(n):
    answer = list(str(n))
    for i in range(len(answer) - 1):
        for j in range(len(answer) - 1 - i):
            if answer[j] < answer[j+1]:
                answer[j], answer[j+1] = answer[j+1], answer[j]
    return int("".join(answer))
