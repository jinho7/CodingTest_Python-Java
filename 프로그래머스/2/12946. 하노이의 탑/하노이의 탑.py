def solution(n):
    
    # 재귀
    def move(n, s, d):
        a = 6 - s - d
        if n == 1:
            return [s, d]
        
        answer = []
        if n == 2:
            answer.extend([move(n-1, s, a)])
            answer.append([s, d])
            answer.extend([move(n-1, a, d)])
        else:
            answer.extend(move(n-1, s, a))
            answer.append([s, d])
            answer.extend(move(n-1, a, d))
        return answer

    return move(n, 1, 3)