def solution(survey, choices):
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 4를 기준으로 [0] 혹은 [1] 에 해당하는 key의 value에 점수를 저장
    for i in range(len(choices)):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
    
    result = ''
    
    # 크거나 같다로 처리
    result += 'R' if dic['R'] >= dic['T'] else 'T'
    result += 'C' if dic['C'] >= dic['F'] else 'F'
    result += 'J' if dic['J'] >= dic['M'] else 'M'
    result += 'A' if dic['A'] >= dic['N'] else 'N'
    
    return result