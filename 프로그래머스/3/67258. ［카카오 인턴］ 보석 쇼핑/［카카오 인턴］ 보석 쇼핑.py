from collections import defaultdict

def solution(gems):
    # 모든 보석의 종류를 파악
    gems_set = set(gems)
    total_types = len(gems_set)  # 보석 종류의 개수
    
    # 슬라이딩 윈도우를 위한 변수 초기화
    gem_count = defaultdict(int)
    s, e = 0, 0  # 투 포인터
    answer = [0, len(gems) - 1]  # 최소 구간 (시작, 끝)

    gem_count[gems[0]] = 1  # 첫 보석 추가

    while e < len(gems):
        # 모든 종류의 보석을 포함하는지 확인
        # print(gem_count)
        if len(gem_count) == total_types:
            # 현재 구간 길이가 더 짧으면 정답 갱신
            if (e - s) < (answer[1] - answer[0]):
                answer = [s, e]
            # 구간을 줄이기 위해 시작 포인터 이동
            gem_count[gems[s]] -= 1
            if gem_count[gems[s]] == 0:  # 보석 개수가 0이 되면 제거
                del gem_count[gems[s]]
            s += 1
        else:
            # 끝 포인터를 이동해 구간 확장
            e += 1
            if e < len(gems):
                gem_count[gems[e]] += 1

    # 정답은 1-based index로 반환
    return [answer[0] + 1, answer[1] + 1]
