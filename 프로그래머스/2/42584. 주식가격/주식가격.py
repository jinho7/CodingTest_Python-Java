def solution(prices):
    
    answer = [0] * len(prices)
    stack = []

    for index, price in enumerate(prices):
        for j in range(index+1 , len(prices)):
            # 후에 본인보다 큰 숫자 있으면 = 떨어지지 않은 기간
            if price <= prices[j]:
                answer[index] += 1
            # 후에 본인보다 작은 숫자 있으면 = 떨어진 기간
            # 해당 숫자 초 - 본인 숫자 초 = x
            # 본인 입장에서 x 초 뒤에 가격이 떨어진다는 뜻
            else: 
                answer[index] = j - index
                break 
        
    return answer