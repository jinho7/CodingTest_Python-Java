import math

def solution(n, words):
    
    used = [words[0]]
    last_turn = 1
    for i in range(1, len(words)) :
        # 1. 한 글자 이상인가
        if len(words[i]) <= 1:
            last_turn = i+1
            break
        # 2. used에 있는 지 체크?
        elif words[i] in used:
            last_turn = i+1
            break
        # 3. 룰 : 끝에 말이랑 첫 말이랑 같은지
        elif used[-1][-1] != words[i][0]:
            last_turn = i+1
            break
        else :
             # 후처리 : used에 담기
            last_turn = i+1
            used.append(words[i])
            
    if len(words) == last_turn and used[-1] == words[-1]:
        return [0,0]
        
    # 가장 먼저 탈락하는 사람의 번호
    eliminated_num = (last_turn - 1) % n + 1
    # 탈락자가 자신의 몇 번째 차례에 탈락
    eliminated_turn = math.ceil(last_turn / n)

    return eliminated_num, eliminated_turn