# 재귀함수를 이용한 풀이

def sum_digit(number):
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)

# Test
print("결과 : {}".format(sum_digit(123)));