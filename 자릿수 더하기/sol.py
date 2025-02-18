def solution(n):

    a = len(str(n)) + 1
    total_sum = 0

    for i in range(a):
        total_sum += (n % 10**i) // (10**(i-1))

    return int(total_sum)
    

print(solution(1234))
