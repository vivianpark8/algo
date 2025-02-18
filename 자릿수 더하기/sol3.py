# 글자로 바라보기

def solution(n):
    answer = 0

    # for i in n -> 여기서 n은 시퀀스 형태가 아니라 단순한 숫자 데이터 하나라 for문에 넣을 수 없음
    
    for i in str(n): # 글자로 쓰면 str 시퀀스 형태로 바뀌므로 for문에서 사용 가능
        answer += int(i)


    return answer
    

print(solution(1234))