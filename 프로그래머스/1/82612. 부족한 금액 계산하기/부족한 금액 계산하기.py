def solution(price, money, count):
    sum = 0
    for i in range(price, price*count+1, price):
        sum+=i
    return sum - money if money < sum else 0