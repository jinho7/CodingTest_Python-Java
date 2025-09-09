# n개의 요소를 가진 튜플: n-tuple
# 규칙
# 1. 중복된 원소 가능 / 순서 있다.
# 2. 원 소개수는 유한. (무한 X)

# 중복 없는 튜플이 있다면?
# {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
# => 확장의 개념. 전에껄 이용할 수 있지 않을까?
# {튜플} But, 안에서의 순서가 바뀌어도 되고, 밖에 순서가 바뀌어도 됨 (이것 또한 튜플) = 2 Depth의 tuple이 나옴

# 역추론 과정 알고리즘을 -> 정추론 과정을 먼저 살펴보자
# a1 / a1, a2 순으로 탄생 -> a1은 어떤 튜플에나 있고, 추가 시 하나씩 새로운 원소가 추가됨
# => 내부 / 외부적으로 순서 변경 가능하다는 점.
# 핵심: 내부 개수로 정렬 시, 하나씩 추가 된다는 점. => 그 하나가 새로운 원소라는 점.
import re
from collections import Counter

def solution1(s):

    # 1. 문자열 나눠서 숫자만 담기
    lst = []
    cur = set()
    num = ""

    for ch in s[1:len(s)-1]:
        if ch.isdigit():
            num += ch
        else:
            if num:
                cur.add(int(num))
                num = ""
            if ch == '{':
                cur = set()
            elif ch == '}':
                lst.append(cur)
    
    # [사전검증]: 원소 1개라면, 바로 출력
    if len(lst) == 1:
        return list(lst[0])
    
    # 2. 순서 정렬
    lst.sort(key = lambda x:-len(x))
    
    answer = []
    for i in range(len(lst)-1):
        x = list(lst[i] - lst[i+1])

        answer.append(x[0])
    answer.append(list(lst[-1])[0])
    
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

    return answer[::-1]

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))