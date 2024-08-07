def solution(word):
    answer = 0
    # 5진수?
    # A 0, E 1, I 2, O 3, U 4순서
    alpha_to_num = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    # 자리에 대해 x 5, x 5^2 ... 가중치
    # 마지막 자리에서 알파벳이 하나 올라가면 1개의 새로운 단어가 생김
    # 네번째 -> 5^1 + (5^0) ... // 첫째자리 5^0 더해서
    # 첫 째 자리에서 알파벳 하나 올라가면 5^4 + 5^3 + 5^2 + 5^1 + 5^0 
    weights = []
    temp = 0
    for i in range(5):
        temp += 5**i
        weights.append(temp)
    weights.reverse()
    
    for index, item in enumerate(word):
        answer += alpha_to_num[item] * weights[index] + 1
        # 본인 차례도 세줘야해서 +1
    
    return answer





    