def solution(A, B):
    # 최대한 적은 수로 이기기
    A.sort(reverse=True)
    B.sort(reverse=True)
    # 이기면 이기고, 못이기면 가장 작은수로 져버리기
    answer = 0
    i = 0
    j = 0
    while j != len(B):
        if B[j] > A[i]:
            j += 1
            answer += 1
        else:
            B.pop()
        i += 1

    return answer