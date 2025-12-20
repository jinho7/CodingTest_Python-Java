from collections import defaultdict

def solution(genres, plays):
    genres_plays = defaultdict(int)
    genres_dict = defaultdict(list)
    
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        
        genres_dict[genre].append([play, i])
        genres_plays[genre] += play
        
    sorted_genres_plays = sorted(genres_plays.items(), key=lambda x: x[1], reverse = True)
    
    answer = []
    for genre, play in sorted_genres_plays:
        genres_dict[genre].sort(key=lambda x: (x[0], -x[1]), reverse = True)
        print(genres_dict[genre])
        for _, i in genres_dict[genre][:2]:
            answer.append(i)
    return answer