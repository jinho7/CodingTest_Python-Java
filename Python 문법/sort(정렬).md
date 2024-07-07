# sort(정렬)

## 정렬 관련 여러 메서드

1. `list.sort()` 메서드:
   - 리스트 자체를 정렬합니다 (in-place 정렬).
   - 원본 리스트를 변경합니다.
   - 반환값은 None입니다.

   기본 사용:
   ```python
   numbers = [3, 1, 4, 1, 5, 9, 2]
   numbers.sort()
   print(numbers)  # [1, 1, 2, 3, 4, 5, 9]
   ```

2. `sorted()` 함수:
   - 정렬된 새 리스트를 반환합니다.
   - 원본 리스트를 변경하지 않습니다.
   - 리스트뿐만 아니라 모든 이터러블에 사용 가능합니다.

   기본 사용:
   ```python
   numbers = [3, 1, 4, 1, 5, 9, 2]
   sorted_numbers = sorted(numbers)
   print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
   print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본 유지)
   ```

3. 공통 매개변수:
   - `key`: 정렬 기준을 지정하는 함수
   - `reverse`: True로 설정하면 역순으로 정렬

   예시:
   ```python
   # 문자열 길이로 정렬
   words = ['apple', 'banana', 'cherry', 'date']
   sorted_words = sorted(words, key=len)
   print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']

   # 두 번째 요소로 정렬
   pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
   pairs.sort(key=lambda pair: pair[1])
   print(pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]

   # 역순 정렬
   numbers = [3, 1, 4, 1, 5, 9, 2]
   numbers.sort(reverse=True)
   print(numbers)  # [9, 5, 4, 3, 2, 1, 1]
   ```


## 관련 문제
- 12933. 정수 내림차순으로 배치하기