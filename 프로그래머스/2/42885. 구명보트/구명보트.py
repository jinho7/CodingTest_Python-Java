def solution(people, limit):

    first = 0
    last = len(people)-1
    boat = 0
    
    people.sort(reverse = True)
    # 약간 포인터 양 끝에서 오는 느낌
    
    while first <= last:
        if people[first] + people[last] <= limit:
            last -= 1
        first += 1
        boat +=1
        
    return boat

def first_solution(people, limit):
    # 한명 최대 2명
    # 꾹꾹 눌러담기 뭔가 greedy 하게 무거운거 부터 채우면 될 거 같은데
    # 그리고 남는 공간에서 가벼운 사람 중에 탐색해서 가장 
    
    boat = 0
    sum = 0
    
    people.sort()
    
    # people 빌 때 까지
    while people:
        # 최고 몸무게가 타 있는 상태에서 계속 체크
        sum += max(people)
        
        temp = 0
        # temp를 갱신하며 limit 안넘는 최대값을 찾음
        for i in range(0, len(people)-1):
            if sum + people[i] <= limit:
                temp = people[i]
        # 또 태울 사람 찾았다면 그 놈도 제거
        if temp != 0:
            sum += temp
            people.remove(temp)
        people.remove(max(people))
        # sum 초기화
        sum = 0
        boat += 1
        
    return boat

