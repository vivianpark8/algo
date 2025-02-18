def solution(slice, n):
    pizza = 0
    if slice/n >= 1:
        return 1
    elif slice/n < 1:
        if n % slice :
            pizza = n//slice + 1
        else :
            pizza = n//slice
        return pizza

print(solution(7, 10))
print(solution(4, 12))