# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

def repeat_str():
    test_count = int(input())
    for _ in range(test_count):
        result = []
        data = list(map(str, input().split()))
        repeat_count = int(data[0])
        text = data[1:] 
        for w in text[0]:
            texts = (w * repeat_count)
            result.append(texts)

        results ="".join(result)
        print(results)
        
repeat_str()