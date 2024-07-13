def solution(number, limit, power):
    list = []
    for i in range(1, number+1):
        list.append(count_divisors(i))
    
    for x in range(len(list)):
        if (list[x] > limit):
            list[x] = power
            
    return sum(list)

def count_divisors(num):
    count = 0
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            if i * i == num:
                count += 1
            else:
                count += 2
    return count