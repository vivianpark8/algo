# 정석 풀이
# 10으로 계속 나눴을 때 나머지를 구함 -> 몫이 0이 될 때까지
# divmod(무엇을, 몇으로 나누는가) -> (몫, 나머지) 튜플로 결과를 줌

def solution(n):
    answer = 0

    while n > 0:
        a, b = divmod(n, 10) # 튜플로 결과를 묶어서 줌 -> b: 나머지

        # a = divmod(n, 10)[0]
        # b = divmod(n, 10)[1]

        # a = n // 10
        # b = n % 10
        
        answer += b
        n = a
    
    return answer
    

print(solution(1234))