def solution(cards1, cards2, goal):
    i1, i2 = 0, 0  # cards1과 cards2의 현재 인덱스
    
    for word in goal:
        if i1 < len(cards1) and word == cards1[i1]:
            i1 += 1
        elif i2 < len(cards2) and word == cards2[i2]:
            i2 += 1
        else:
            return "No"
    
    return "Yes"


# goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있습니다.
# 마지막 테스트만 통과안함.. 뭐가 문제?
def my_solution(cards1, cards2, goal):
    for x in range(len(goal)-1):
        # x번째를 cards1에서 연속적으로 찾음
        if (this_index(cards1, goal[x]) != -1 and this_index(cards1, goal[x+1]) != -1):
            if (this_index(cards1, goal[x]) > this_index(cards1, goal[x+1])) :
                return "No"
        elif (this_index(cards2, goal[x]) != -1 and this_index(cards2, goal[x+1]) != -1):
            if (this_index(cards2, goal[x]) > this_index(cards2, goal[x+1])) :
                return "No"
    return "Yes"

# 해당 문자열이 배열의 몇 번째 index에 있는지
def this_index(cards, string):
    for index, item in enumerate(cards):
        if (item == string):
            return index
    return -1