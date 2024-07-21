from collections import defaultdict

def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)
    
    # 각 사용자가 신고한 사용자 목록
    user_reports = defaultdict(set)
    # 각 사용자별 신고당한 횟수
    report_counts = defaultdict(int)
    
    for r in report:
        reporter, reported = r.split()
        user_reports[reporter].add(reported)
        report_counts[reported] += 1
    
    # k번 이상 신고당한 사용자 목록
    banned = set(user for user, count in report_counts.items() if count >= k)
    
    # 각 사용자가 신고한 사용자 중 정지된 사용자의 수 계산
    result = [len(user_reports[user] & banned) for user in id_list]
    
    return result