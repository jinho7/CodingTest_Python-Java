def solution(clothes):
    dictionary = {i[1]: set() for i in clothes}
    
    # 각 항목을 해당하는 집합에 추가
    for i in clothes:
        dictionary[i[1]].add(i[0])
    
    # 각 set에 착용x (none) 추가해주고, 착용x로만 조합된 케이스 -1
    for key in dictionary.keys():
        dictionary[key].add('none')
    
    temp = 1
    for key in dictionary.keys():
        temp *= len(dictionary[key])
        
    return temp - 1