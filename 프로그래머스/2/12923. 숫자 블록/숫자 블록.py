def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(func(i))
    
    return answer

def func(i):
    if i == 1:
        return 0
    else:
        d = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                # 블록 번호는 10,000,000 이하
                if i // j <= 10000000:  
                    d = i // j
                    break
                else:
                    d = j
        return d