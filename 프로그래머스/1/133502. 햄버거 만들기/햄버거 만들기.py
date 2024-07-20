def solution(ingredient):
    # 아래부터 빵 – 야채 – 고기 - 빵
    # 1, 2, 3  = 빵, 야채, 고기 의미
    # 1 2 3 1 만나면 -> pop & count 증가
    # 스택 느낌으로 
    stack = []
    count = 0
    
    for item in ingredient:
        stack.append(item)
        if len(stack) >= 4 and check_set(stack):
            del stack[-4:]
            count += 1
    
    return count

def check_set(arr):
    return True if arr[-4:] == [1, 2, 3, 1] else False
        