import math

N, K = map(int, input().split())
divisors = []

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)

divisors.sort()

if K <= len(divisors):
    print(divisors[K - 1])
else:
    print(0)