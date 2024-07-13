def solution(name, yearning, photo):
    score_dic = dict(zip(name,yearning))
    answer = []
    for i in range(len(photo)):
        sum = 0
        for k in range(len(photo[i])):
            for key, value in score_dic.items():
                if (photo[i][k] == key):
                    sum += value
        answer.append(sum)
            
    

    return answer