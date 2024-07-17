# for문 4개 돌리면서 끙끙대다가 그냥 찾아봄..

def solution(keymap, targets):
    # 각 문자를 입력하는데 필요한 최소 키 입력 횟수를 알아야 한다!

    # 각 문자에 대한 최소 키 입력 횟수를 저장하는 딕셔너리
    # 각 문자의 최소 입력 횟수를 저장하기 위해 딕셔너리를 사용
    # 키는 문자, 값은 최소 입력 횟수
    char_min_presses = {}
    
    # keymap을 순회하며 각 문자의 최소 입력 횟수 계산
    for key in keymap:
        for i, char in enumerate(key, 1):
            if char not in char_min_presses or i < char_min_presses[char]:
                char_min_presses[char] = i
    
    print(char_min_presses)
    

    result = []
    # targets의 각 문자열을 순회
    # 각 문자에 대해 저장된 최소 입력 횟수를 더한다.
    # 만약 문자가 keymap에 없다면, 그 문자열은 만들 수 없으므로 -1로 처리한다.
    for target in targets:
        total_presses = 0
        for char in target:
            if char not in char_min_presses:
                total_presses = -1
                break
            total_presses += char_min_presses[char]
        result.append(total_presses)
    
    return result