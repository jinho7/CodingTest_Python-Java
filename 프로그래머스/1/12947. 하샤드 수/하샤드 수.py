def sum_digit(number):
    if number < 10:
        return number

    return number % 10 + sum_digit (number//10)

def solution(x):
    if x % sum_digit(x) :
        return False
    return True