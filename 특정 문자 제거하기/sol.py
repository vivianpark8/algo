def solution(my_string, letter):
    answer = []
    for a in my_string:
        if a not in letter:
            answer.append(a)       
    return ''.join(answer)

print(solution('abcdef', 'f'))