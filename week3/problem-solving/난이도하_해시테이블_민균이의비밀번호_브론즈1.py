# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933


# 입력한 원래의 단어 저장
# 원래의 단어를 뒤집은 후 입력 list에서 일치하는 단어 찾기
# 자기자신도 포함할 수 있음.
# 일치하는 단어가 있으면 해당 단어의 가운데 글자 출력하기

def revers():
    count = int(input())
    data = ([str(input()) for _ in range(count)])

   
    for pw in data:
        revers_pw  = pw[::-1]
        if revers_pw in data:
            mid = len(revers_pw) // 2
            return print(len(revers_pw), revers_pw[mid])
            
revers()
