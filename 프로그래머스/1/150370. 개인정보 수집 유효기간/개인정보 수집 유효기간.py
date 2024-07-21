def solution(today, terms, privacies):
    # dic {약관 종류 : 유효기간}
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}

    answer = []
    for index, item in enumerate(privacies):
        # 해당 약관 종류 = item.split()[1]
        if item.split()[1] in terms_dict:
            # 해당 약관 종류가 있다면, 그 key의 value를 찾아옴 = terms_dict[item.split()[1]]
            
            # 개인정보 수집 일자 + 약관종류의 유효기간 * 28 보다 오늘 일자가 더 크면
            if replace(item.split()[0]) + terms_dict[item.split()[1]] * 28 <= replace(today):
                answer.append(index+1)
            
    return answer

# 'yyyy.mm.dd' 형식의 stirng -> 몇 일인지 치환하는 코드
def replace(yyyymmdd):
    result = 0
    # (년-1)x12x28
    result += (int(yyyymmdd.split('.')[0])-1) * 12 * 28
    # (월-1)x28
    result += (int(yyyymmdd.split('.')[1])-1) * 28
    result += int(yyyymmdd.split('.')[2]) 
    
    return result