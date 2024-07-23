# 아으 또 런타임 에러야. HashMap? dictionary?

fibo_dict = {'fibo0' : 0, 'fibo1' : 1}

def solution(n):
    for i in range(2, n):
        fibo(i)
    return fibo(n) % 1234567

def fibo(n):
    if n == 0:
        return fibo_dict['fibo0']
    elif n == 1:
        return fibo_dict['fibo1']
    else:
        # 사전 저장
        temp_str1 = 'fibo' + str(n)
        temp_str2 = 'fibo' + str(n-1)
        temp_str3 = 'fibo' + str(n-2)
        fibo_dict[temp_str1] = fibo_dict[temp_str2] + fibo_dict[temp_str3]
        return fibo_dict[temp_str1]