def solution(n):
    answer = []
    for i in range(n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer

print(solution(10))
print(solution(15))