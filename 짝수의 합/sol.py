def solution(n):
    # 1, 2, 3, 4
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum

print(solution(10))
print(solution(4))