from collections import deque

def solution(begin, target, words):
    # 변환할 수 없는 경우에는 0를 return 합니다.
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, count = queue.popleft()
        print("현재 단어:" , current_word)
        if current_word == target:
            return count

        # words에서 변환 가능한 단어 찾기
        for word in words:
            if word not in visited and can_change(current_word, word):
                # 다음 단어 큐에 추가
                queue.append([word, count+1])
                # 방문 체크
                visited.add(word)           
    return 0

# 한 글자만 다른지 확인하는 함수
def can_change(x, y):
    diff = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False