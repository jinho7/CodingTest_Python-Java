def solution(n):
    answer = 1
    for answer in range(1,n):
        if (n % answer == 1):
            break;
    return answer