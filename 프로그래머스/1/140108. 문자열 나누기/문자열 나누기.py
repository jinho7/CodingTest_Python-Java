def solution(s):
    answer = 0
    while s:
        s = devide(s)
        answer += 1
        if s is None:
            break
    return answer

def devide(string):
    for k in range(2, len(string) + 1, 2):
        if len(string[:k]) // 2 == string[:k].count(string[0]):
            return string[k:]
    return None
    
        