# 시간 줄이기 위해 최적화
# 대칭 구조라는 점 이용하기
# 루트만큼 나눈 후 좌우 대칭
# 루트: import math, 혹은 n ** 05 -> n의 2분의 1승 -> 제곱 -> int(n**0.5)+1

from math import sqrt

def solution(n):
    answer = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            answer += 2

            if i * i == n:
                answer -= 1

    return answer
    
print(solution(20))
print(solution(100))
