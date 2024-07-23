def solution(friends, gifts):
    
    # 준 사람 : 받은 사람 [list는 friends 수 만큼 0으로 채워줌] 딕셔너리 생성
    gift_history = {friend : [0 for i in range(len(friends))] for friend in friends}
    
    # 주고받은 선물
    for gift in gifts:
        giver , receiver = gift.split()
        # 선물 기록에서 receiver 찾아가서 해당 value list에서 getter의 index에 1 추가
        gift_history[giver][friends.index(receiver)] += 1
    
    # 선물 지수
    # gift_history에서 가로 합 - 세로 합
    gift_point = []
    for giver in friends:
        given = sum(gift_history[giver])
        received = sum(gift_history[receiver][friends.index(giver)] for receiver in friends)
        gift_point.append(given - received)

    # 최종적으로 다음 달에 받을 선물 수 담을 list
    next_month_gift = [0 for i in range(len(friends))]
    
    # 서로 선물을 주고 받았는지 체크
    for A in range(len(friends)):
        for B in range(A+1, len(friends)):
            num_A_to_B = gift_history[friends[A]][friends.index(friends[B])]
            num_B_to_A = gift_history[friends[B]][friends.index(friends[A])]
        
            # 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
            if num_A_to_B > num_B_to_A:
                next_month_gift[A] += 1
            elif num_A_to_B < num_B_to_A:
                next_month_gift[B] += 1
            # 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면
            else:
                # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
                if gift_point[A] > gift_point[B]:
                    next_month_gift[A] += 1
                elif gift_point[A] < gift_point[B]:
                    next_month_gift[B] += 1
                #  선물 지수마저 같다면 선물을 주고 받지 않는다.
                else:
                    None
    # 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수
    return max(next_month_gift)