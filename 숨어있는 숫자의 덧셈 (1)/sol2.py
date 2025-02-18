# 쉬운 풀이

def solution(my_string):
    numbers = []

    for char in my_string:
        # if char = 숫자인가요?
        # string 메소드 쓰면 됨

        if char.isdigit():
            numbers.append(int(char))

    return sum(numbers)


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))