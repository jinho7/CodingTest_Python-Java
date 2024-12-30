from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
        
    cache = deque(maxlen=cacheSize)
    time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5
            
    return time