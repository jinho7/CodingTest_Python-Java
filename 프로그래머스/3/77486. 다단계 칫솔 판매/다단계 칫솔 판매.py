from collections import defaultdict
def solution(enroll, referral, seller, amount):
    # heap tree 활용
    
    # 자식 이익의 10%를 추천인에게 배분 (부모 노드)
    # 본인의 이익 = 모든 자식의 이익 10%들까지 포함
    
    # 개당 100원
    # 10 % => 정수 원 단위에서 절사 = 10 % 가 1원 미만 => 이득 분배 X
    # 꼭 bottom to top 계산?
    # 어차피 각 node들 다 10% 계산하고 나중에 합하면 그것도 다 10%에 포함
    
    # enroll[i] - referral[i] = {자식 - 부모} 1:1 관계
    
    # tree = { 자식 : 부모 }
    tree = defaultdict(str)
    for i in range(len(referral)):
        tree[enroll[i]] = referral[i]
    
    # 수익
    benefits = {e : 0 for e in enroll}
    
    def calculator(name, cost):
        #print('---', name, '의 판매 계산 ---')
        while name != "-":
            x = name
            rest = cost
            name = tree[name]
            tenpersent = int(cost * 0.1)
            rest -= tenpersent
            #print('자식 :', name, '은 나머지', 'cost의 10%인', cost, '수익 예정')
            #print('실제 부모 반영 :', x, '은 나머지', rest, '수익')
            benefits[x] += rest
            cost = tenpersent
            # 10 % => 정수 원 단위에서 절사 = 10 % 가 1원 미만 => 이득 분배 X
            if cost == 0:
                break;
        
    #print(tree)
    for i in range(len(seller)):
         calculator(seller[i], amount[i]*100)

    return list(benefits.values())