def solution(n, k):
    
    # k진수로 전환
    temp = ''
    while n != 0:
        temp += str(n % k)
        n = n//k
    temp = temp[::-1]
    
    num_pack = []
    temp_str = ''
    for i in range(len(temp)):
        if temp[i] == '0':
            num_pack.append(temp_str)
            temp_str = ''
        else:
            temp_str += temp[i]
    num_pack.append(temp_str)
    
    print(num_pack)
    # 0이 없다면
    count = 0
    for i in range(len(num_pack)):
        # 소수라면,
        if num_pack[i] != '' and is_prime(int(num_pack[i])):
            count += 1
    return count

def is_prime(num):
    # 소수인지 판단
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True