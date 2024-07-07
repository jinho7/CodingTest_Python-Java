def solution(price, money, count):
    sum = 0
    for i in range(price, price*count+1, price):
        sum+=i
    return sum - money if money < sum else 0

# return max(0,price*(count+1)*count//2-money)
# 개섹시하다. 
# 등차 수열의 합 공식 활용..
# max() 로 음수나오면 (돈 안부족하면) 0 뽑히게..