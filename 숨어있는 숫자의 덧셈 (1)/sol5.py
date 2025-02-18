def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except:
            continue # 다음 for문으로 진행해주세요

    # 문제가 있으면 실행하고 문제가 없으면 넘어가라

    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))