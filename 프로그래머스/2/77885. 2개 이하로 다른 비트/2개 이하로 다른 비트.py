def f(x):
    # 짝수는 그냥 1 더하면 됨
    if x % 2 == 0:
        return x + 1
    # 문제는 홀수
    else:
        # 맨 앞에서 01을 만날 수도 있기 때문에 앞에 0을 추가해줌
        bin_x = '0' + bin(x)[2:]
        # 01을 만나는 지점에서 10으로 바꿔준다.
        idx = bin_x.rfind('01')
        bin_x = bin_x[:idx] + '10' + bin_x[idx+2:]
        return int(bin_x, 2)
    
def solution(numbers):
    return [f(num) for num in numbers]