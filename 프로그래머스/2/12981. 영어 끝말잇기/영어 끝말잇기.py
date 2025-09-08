def solution(n, words):
    
    queue = [words[0]]

    def validation(word):
        # 1. 한 단어인지, 2. 끝말잇기
        print(queue[-1], word)
        if len(word) > 1 and queue[-1][-1] == word[0]:
            # 3. 이전에 사용한 단어인지
            if word not in queue:
                return True
        return False
    
    for i in range(1, len(words)):
        if validation(words[i]):
            queue.append(words[i])
            continue
        else:
            return [(i + 1) % n or n, (i + n) // n]
    return [0, 0]