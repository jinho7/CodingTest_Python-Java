# 실행시간을 전역으로 관리
running_time = 0

class Queue:
    # 생성자 배열 생성
    def __init__(self):
        self.items = []

    # 비어 있는지
    def isEmpty(self):
        return len(self.items) == 0
    # 넣기
    def enqueue(self, item):
        self.items.append(item)
    
    # 처음꺼 빼기
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    
def solution(cacheSize, cities):
    global running_time
    # 만약에 cacheSize가 0이면 그냥 모두 cache_miss
    if cacheSize == 0:
        return len(cities) * 5

    cache = Queue()
    # 전처리 (대소문자 구문 X)
    cities = [city.lower() for city in cities]
    
    for city in cities:
        #print("----------------------------------------")
        #print("캐싱 작업 이전 상태 : ", cache.items)
        # 해당 도시가 캐시에 있을 때
        if city in cache.items:
            #print(city, "가 cache에 있습니다.")
            cache_hit()
            # 씁. 이거 Queue 쓰는 이유가 있낰ㅋㅋㅋㅋㅋㅋㅋㅋ
            cache.items.remove(city)
            cache.enqueue(city)
        # 해당 도시가 캐시에 없을 때
        else:
            # 캐시가 차 있으면 가장 오래된 놈을 빼고 넣는다.
            if cache.size() >= cacheSize:
                #print(city, "가 cache에 없습니다.", cache.size(), "가", cacheSize, "보다 크거나 같습니다.")
                cache_miss()
                cache.dequeue()
                cache.enqueue(city)
            # 캐시가 안 차 있으면 그대로 넣는다.
            else:
                #print(city, "가 cache에 없습니다.", cache.size(), "가", cacheSize, "보다 작습니다.")
                cache_miss()
                cache.enqueue(city)
        #print("캐싱 작업 이후 상태 : ", cache.items)
    return running_time

# 뭔가 hit 했다고 기능적으로 표현하기 위해 빼놓음 ㅎㅎ
def cache_hit():
    global running_time
    running_time += 1
    
# 뭔가 hit 했다고 기능적으로 표현하기 위해 빼놓음 ㅎㅎ
def cache_miss():
    global running_time
    running_time += 5
