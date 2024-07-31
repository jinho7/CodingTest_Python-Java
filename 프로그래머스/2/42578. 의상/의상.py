def solution(clothes):
    dictionary = {i[1]: set() for i in clothes}
    
    # 각 항목을 해당하는 집합에 추가
    for i in clothes:
        dictionary[i[1]].add(i[0])
    
    # 착용 x 추가해주고, 착용 x만 있는 조합 -1
    for key in dictionary.keys():
        dictionary[key].add('none')
    
    temp = 1
    for key in dictionary.keys():
        temp *= len(dictionary[key])
        
    return temp - 1