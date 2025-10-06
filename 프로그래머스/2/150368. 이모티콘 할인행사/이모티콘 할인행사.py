from itertools import product

def solution(users, emoticons):
    
    answer = [0, 0]
    
    # 이모티콘 관점으로 다시 생각
    for comb in product([i for i in range(10, 50, 10)], repeat= len(emoticons)):
        total_subscriber, total_price = 0, 0
        
        # 1. 각 사용자에 대해
        for user_min_discount_percent, user_min_price in users:
            cost = 0
            
            # 2. 현재 comb의 각 이모티콘 가격 계산
            for emo_price, emo_discount_percent in zip(emoticons, comb):
                # 조건 만족하는 이모티콘만 구매
                if emo_discount_percent >= user_min_discount_percent:
                    cost += emo_price * (100 - emo_discount_percent) // 100
                
            # 3. 구매한 이모티콘 합이 기준 가격 이상 -> 구독
            if cost >= user_min_price:
                total_subscriber += 1
            else:
                total_price += cost
        # print(f'{comb} 할인율일 때, 구독자 수: {total_subscriber}, 판매액: {total_price}')
        
        # 최적해 갱신
        # 1. 구독자 수가 더 많아지는 케이스
        if total_subscriber > answer[0]:
            answer = [total_subscriber, total_price]
        # 2. 구독자 수가 같다면, 최대값 갱신
        elif total_subscriber == answer[0]:
            answer[1] = max(answer[1], total_price)
            
    return answer