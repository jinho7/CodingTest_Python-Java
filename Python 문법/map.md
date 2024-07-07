# map

## map이란
- map(function, list): 각 요소에 함수 적용
- 문자열의 각 문자에 int 함수를 적용 -> 이는 각 문자를 정수로 변환
- 이후 변환된 정수들의 합을 계산

```python
def sum_digit(number):
    return sum(map(int, str(number)))
```

## 관련 문제
- 12925. 문자열을 정수로 바꾸기
