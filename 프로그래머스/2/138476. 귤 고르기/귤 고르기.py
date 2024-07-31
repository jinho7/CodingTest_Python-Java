def solution(k, tangerine):
    size_count_dict = {}
    # size_count_dict = { size : tangerine.count(size) for size in tangerine }
    for i in set(tangerine):
        size_count_dict[i] = 0 # 딕셔너리 생성
    
    for i in tangerine:
        size_count_dict[i] += 1 # 딕셔너리에 값 생성, 저장
    # 뭐 실제 크기가 중요한 것은 아님. 그냥 몇가지 종류로 나눌 수 있는지가 중요.
    # key는 날리자
    counts = sorted((i for i in size_count_dict.values()), reverse = True) 
    # 큰 수부터 개수만 남음
    
    for index, count in enumerate(counts): # 인덱스와 같이 for문으로 돌리기
        k -= count
        if k <= 0:
            return index + 1 # 종류 개수