def solution(n, k):
    a = n * 12000
    
    b = (k - n // 10) * 2000
        
    return a + b

print(solution(10, 3))
print(solution(64, 6))