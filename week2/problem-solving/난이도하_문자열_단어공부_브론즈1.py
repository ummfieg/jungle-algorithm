# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

def many_word():
    word = str(input())
    up_word = (word.upper())
    peice = {}
    for w in up_word:
        if w not in peice:
            peice[w] = 1
        else:
            peice[w] += 1

    result = [k for k,v in peice.items() if max(peice.values()) == v]
    if (len(result) > 1):
        print("?")
    else:
        print(result[0])

many_word()

      
