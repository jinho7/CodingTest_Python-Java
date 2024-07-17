# 효율성 테스트.. 다걸림
def asolution(participant, completion):
    for i in range(len(completion)):
        participant.remove(completion[i])
    return participant[0]

def bsolution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

def solution(participant, completion):
    hash_dict = {}
    
    # 참가자 이름을 해시에 추가하고 카운트
    for name in participant:
        if name in hash_dict:
            hash_dict[name] += 1
        else:
            hash_dict[name] = 1
    
    # 완주자 이름을 해시에서 제거
    for name in completion:
        hash_dict[name] -= 1
        if hash_dict[name] == 0:
            del hash_dict[name]
    
    # 남은 이름이 완주하지 못한 선수
    return list(hash_dict.keys())[0]