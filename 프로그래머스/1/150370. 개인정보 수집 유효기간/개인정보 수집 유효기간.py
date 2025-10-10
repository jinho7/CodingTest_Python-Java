def solution(today, terms, privacies):
    
    term_dict = {}
    for x in terms:
        term, month = x.split()
        # -1 일 까지! 유효
        term_dict[term] = int(month) * 28 - 1
    
    # 날짜 -> 일로 변경 (2000 제외하고 뒤만)
    def date_to_days(date):
        year, month, day = date.split('.')
        # month = (int(year) - 2001) * 12 + int(month)
        return ((int(year) - 2001) * 12 + int(month) - 1) * 28 + int(day)
    
    today_day = date_to_days(today)
    answer = []
    
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        if date_to_days(date) + term_dict[term] < today_day:
            answer.append(idx+1)
        
    return answer