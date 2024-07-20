def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id_removed = ''
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in ['-', '_', '.']:
            new_id_removed += char
    new_id = new_id_removed
    
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id += "a"
        
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    
    return new_id


# 참고:
# 시간복잡도 관점에서 볼 때:

# 1. 문자열을 계속 수정하는 방법:
# 매 수정마다 새 문자열을 생성하므로 O(n^2) 시간복잡도를 가질 수 있습니다.
# 여기서 n은 문자열의 길이입니다.

# 2. 리스트로 변환 후 수정하는 방법:
# 리스트 변환: O(n)
# 요소 수정: 각 요소에 대해 O(1), 전체적으로 O(n)
# 다시 문자열로 변환: O(n)
# 총 시간복잡도: O(n)

# 따라서, 시간복잡도 측면에서는 리스트로 변환하여 처리하는 방법이 일반적으로 더 효율적입니다. 특히 여러 번의 수정이 필요한 경우 이 방법이 유리합니다.