def solution(answers):
    first = [1, 2, 3, 4, 5] # 12345 반복
    second = [2, 1, 2, 3, 2, 4, 2, 5] # 21232425 반복 
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3311224455 반복
   
    first = slice(first, answers)
    second = slice(second, answers)
    third = slice(third, answers)
    
    correct = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            correct[0] += 1
        if answers[i] == second[i]:
            correct[1] += 1
        if answers[i] == third[i]:
            correct[2] += 1
            
    max_score = max(correct)
    result = []
    for i in range(3):
        if correct[i] == max_score:
            result.append(i + 1)
    
    return sorted(result)


def slice(arr, answers):
    if len(arr) > len(answers):
        return arr[:len(answers)]
    else:
        while len(arr) < len(answers):
            arr += arr
    return arr[:len(answers)]