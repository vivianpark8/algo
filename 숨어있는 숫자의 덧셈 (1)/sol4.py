def solution(my_string):
    answer = 0
    numbers = '123456789'

    for num in numbers:
        answer += int(num)

    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))