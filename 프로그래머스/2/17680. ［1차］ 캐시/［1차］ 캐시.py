def solution(cacheSize, cities):
    running_time = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            running_time += 1
            cache.remove(city)
        else:
            running_time += 5
            if len(cache) >= cacheSize:
                cache = cache[1:]
        
        if cacheSize > 0:
            cache.append(city)
    
    return running_time