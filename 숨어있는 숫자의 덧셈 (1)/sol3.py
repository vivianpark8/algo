# 아스키코드 활용 -> 문자와 숫자의 범위

def solution(my_string):
    answer = 0

    for char in my_string:

        if not (ord('A') <= ord(char) <= ord('z')): # 글자가 아닌가요?
            answer += int(char)

    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))