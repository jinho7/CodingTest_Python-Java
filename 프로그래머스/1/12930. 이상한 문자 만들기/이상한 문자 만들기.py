def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        answer.append(trans(word))
    return ' '.join(answer)

def trans(word):
    new_word = []
    for i in range(len(word)):
        if i % 2 == 0:
            new_word.append(word[i].upper())
        else:
            new_word.append(word[i].lower())
    return ''.join(new_word)