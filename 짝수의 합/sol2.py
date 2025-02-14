def solution(n):
    # 1, 2, 3, 4
    sum = 0
    for i in range(0, n+1, 2):
        sum += i
    return sum

print(solution(10))
print(solution(4))