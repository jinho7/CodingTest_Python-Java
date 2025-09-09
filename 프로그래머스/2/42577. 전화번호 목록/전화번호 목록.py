def solution(phone_book):
    n = len(phone_book)
    phone_book.sort()
    # 사전순 정렬에서 인접한 요소만 생각
    # 사전순 정렬에서 인접 요소 중 비교 필요 2개는 짧음 < 큼
    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True