def solution(survey, choices):
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(choices)):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
    
    result = ''
    result += 'R' if dic['R'] >= dic['T'] else 'T'
    result += 'C' if dic['C'] >= dic['F'] else 'F'
    result += 'J' if dic['J'] >= dic['M'] else 'M'
    result += 'A' if dic['A'] >= dic['N'] else 'N'
    
    return result