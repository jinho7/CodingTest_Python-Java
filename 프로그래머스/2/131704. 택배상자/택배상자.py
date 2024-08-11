def solution(order):
    answer = 0
    temp = []
    origin = [i for i in range(len(order), 0, -1)]
    idx = 0
    # order 에 있는 순서대로 들어가야함
    while idx < len(order):
        # order[idx]가 origin의 마지막 상자와 일치
        if len(origin) > 0 and order[idx] == origin[-1]:
            origin.pop()
            answer += 1
            idx += 1
        # order[idx]가 temp의 맨 위 상자와 일치
        elif len(temp) > 0 and order[idx] == temp[-1]:
            temp.pop()
            answer += 1
            idx += 1
        # origin에서 상자를 꺼내 temp에 임시 보관
        else:
            if len(origin) > 0:
                temp.append(origin.pop())
            else:
                break

    return answer