def solution(numbers):
    num = 0
    for i in numbers:
        num += i
    return num / len(numbers)

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
