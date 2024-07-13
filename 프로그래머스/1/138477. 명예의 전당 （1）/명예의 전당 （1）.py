def solution(k, score):
    temp = []
    answer = []
    for i in range(len(score)):
        temp.append(score[i])
        temp.sort(reverse=True)
        if i < k:
            answer.append(temp[i])
        else :
            answer.append(temp[k-1])
    return answer