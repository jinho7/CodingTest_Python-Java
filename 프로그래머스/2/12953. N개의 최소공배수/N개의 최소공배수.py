import math

def solution(arr):
    temp = 1
    for i in range(len(arr)):
        temp = lcm(temp, arr[i])
    return temp

def lcm(a, b):
    return a*b // math.gcd(a,b)