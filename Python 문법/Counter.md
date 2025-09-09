# 📝 `collections.Counter` 정리

## 📌 기본 사용법

```python
from collections import Counter

c = Counter(['a', 'b', 'a', 'c', 'a', 'b'])
print(c)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

* `Counter`는 사실상 **dict의 특수 버전**
* 요소 → key, 등장 횟수 → value

---

## 📌 주요 메서드 & 속성

### 1. `most_common([n])`

등장 빈도 순으로 정렬된 리스트 반환

```python
c = Counter("banana")
print(c.most_common())    # [('a', 3), ('n', 2), ('b', 1)]
print(c.most_common(2))   # [('a', 3), ('n', 2)]
```

---

### 2. `elements()`

각 원소를 횟수만큼 반복하는 이터레이터

```python
c = Counter(a=2, b=1)
print(list(c.elements()))  # ['a', 'a', 'b']
```

---

### 3. `update(iterable or mapping)`

새로운 요소 추가 카운트

```python
c = Counter("banana")
c.update("band")   
print(c)  # Counter({'a': 4, 'n': 3, 'b': 2, 'd': 1})
```

---

### 4. `subtract(iterable or mapping)`

카운트를 빼줌 (음수 가능)

```python
c = Counter("banana")
c.subtract("an")
print(c)  # Counter({'a': 2, 'n': 1, 'b': 1})
```

---

### 5. 산술 연산

Counter는 **집합처럼 연산** 지원합니다.

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)  # Counter({'a': 4, 'b': 3}) (음수 제거)
print(c1 - c2)  # Counter({'a': 2}) (음수는 무시)
print(c1 & c2)  # Counter({'a': 1, 'b': 1}) (교집합: 최소값)
print(c1 | c2)  # Counter({'a': 3, 'b': 2}) (합집합: 최대값)
```

---

## 📌 dict와의 차이

```python
c = Counter("banana")
print(c['a'])   # 3
print(c['z'])   # 0  (dict였다면 KeyError)
```

* Counter는 없는 키 조회 시 `0` 반환 → 에러 안 남.

---

## 📌 실전 활용 예시

### 1) 문자열 문자 빈도수 세기

```python
word = "hello world"
cnt = Counter(word)
print(cnt.most_common(1))  # [('l', 3)]
```

### 2) 리스트 요소 빈도수 세기

```python
nums = [1,2,2,3,3,3,4,4,4,4]
print(Counter(nums))  # Counter({4: 4, 3: 3, 2: 2, 1: 1})
```

### 3) 튜플 문제 (카카오)

```python
import re
from collections import Counter

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
nums = re.findall(r'\d+', s)
cnt = Counter(nums)
print([int(k) for k, _ in cnt.most_common()])  # [2,1,3,4]
```

---

✅ 정리

* **Counter = dict 기반 카운터**
* `most_common`, `elements`, `update`, `subtract` 자주 사용
* 산술 연산(`+ - & |`) 지원 → 집합 연산 느낌
* 없는 키 접근 시 `0` 반환
