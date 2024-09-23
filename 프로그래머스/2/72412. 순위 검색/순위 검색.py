from itertools import product
from bisect import bisect_left

def solution(info, query):
    lang = ["cpp", "java", "python", "-"]
    job = ["backend", "frontend", "-"]
    career = ["junior", "senior", "-"]
    food = ["chicken", "pizza", "-"]
    
    all_dict = { ' '.join(combination): [] for combination in product(lang, job, career, food) }
    
    # 각 지원자 정보를 모든 경우의 수에 매핑
    for applicant in info:
        applicant_lang, applicant_job, applicant_career, applicant_food, applicant_score = applicant.split()
        applicant_score = int(applicant_score)
        for l in [applicant_lang, "-"]:
            for j in [applicant_job, "-"]:
                for c in [applicant_career, "-"]:
                    for f in [applicant_food, "-"]:
                        key = ' '.join([l, j, c, f])
                        all_dict[key].append(applicant_score)
    
    # 각 리스트 정렬 (이진 탐색을 위해)
    for key in all_dict:
        all_dict[key].sort()
    
    answer = []
    for q in query:
        lang_query, job_query, career_query, food_and_score_query = q.split(' and ')
        food_query, score_query = food_and_score_query.split()
        score_query = int(score_query)
        query_key = ' '.join([lang_query, job_query, career_query, food_query])
        
        # 이진 탐색을 사용해 효율적으로 점수 찾기
        scores = all_dict[query_key]
        idx = bisect_left(scores, score_query)
        answer.append(len(scores) - idx)
    
    return answer