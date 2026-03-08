# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

def sad_truth():
    n = int(input())

    for _ in range(n):
        data = list(map(int, input().split()))
        
        student = data[0]
        scores = data[1:]
        
        avg = sum(scores) / student
        
        count = 0
        for score in scores:
            if score > avg:
                count += 1
        
        percent = (count / student) * 100
        print(f"{percent:.3f}%")
    
sad_truth()