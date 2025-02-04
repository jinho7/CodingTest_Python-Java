def solution(genres, plays):
    # 총 재생수 dictionary 와
    # 장르 별로 dictionary = { genres : [[고유번호, 재생횟수], ..] 로 들어감}
    genres_all_play_time = {genre : 0 for genre in genres }
    genres_plays = {genre : [] for genre in genres }
    for i in range(len(plays)):
        genres_all_play_time[genres[i]] += plays[i]
        genres_plays[genres[i]].append([i, plays[i]])
    
    # 장르 별로 재생횟수별로 정렬함. (이미 고유번호 순으로 들어갔음)
    for value in genres_plays.values():
        value.sort(key=lambda x: x[1], reverse=True)
    
    # 속한 노래가 많이 재생된 장르를 먼저 수록_ 위해서 정렬
    genres_all_play_time_list = []
    for x, y in genres_all_play_time.items():
        genres_all_play_time_list.append([x, y])
    genres_all_play_time_list.sort(key=lambda x: x[1], reverse=True)
    
    answer = []
    # 장르 내에서 많이 재생된 노래를 먼저 수록
    for genres, all_play_time in genres_all_play_time_list:
        play_time = genres_plays[genres]
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
        if len(play_time) == 1:
            answer.append(play_time[0][0])
        else:
            answer.append(play_time[0][0])
            answer.append(play_time[1][0])
    return answer