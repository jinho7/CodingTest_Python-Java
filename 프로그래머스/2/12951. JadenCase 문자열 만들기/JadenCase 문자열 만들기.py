# https://chobopark.tistory.com/273
# 파이썬 실기 문제에서 capitalize() 썼었는데 ㄷㄷ
def solution(s):
    return ' '.join(word.capitalize() for word in s.split(' '))