def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            a = (i, n//i)
            answer.append(a)
    return len(answer)
    
print(solution(20))