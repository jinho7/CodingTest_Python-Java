# map을 사용한 풀이
# 문자열의 각 문자에 int 함수를 적용 -> 이는 각 문자를 정수로 변환
# 이후 변환된 정수들의 합을 계산
def sum_digit(number):
    return sum(map(int, str(number)))

# Test
print("결과 : {}".format(sum_digit(123)));