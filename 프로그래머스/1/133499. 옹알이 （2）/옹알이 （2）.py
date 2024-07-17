def solution(babbling):
    count = 0
    for word in babbling:
        if check_word(word):
            count += 1
    return count

def check_word(word):
    possible = ["aya", "ye", "woo", "ma"]
    # 글자를 한 글자씩 탐색
    i = 0
    # 이전에 반복된 글자를 캐싱
    last = ""
    while i < len(word):
        found = False
        for sound in possible:
            if word[i:].startswith(sound) and sound != last:
                i += len(sound)
                # 캐싱
                last = sound
                found = True
                break
        # 다 돌아봤는데 한 번도 found = True가 안됨
        if not found:
            return False
    return True