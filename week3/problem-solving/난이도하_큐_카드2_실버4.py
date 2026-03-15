# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

def card_game():
    count = int(input())
    queue = deque()

    for i in range(1,count+1):
        queue.append(i)
    
    while len(queue) > 1:
        queue.popleft()
        value = queue.popleft()
        queue.append(value)

    print(queue.pop())
    
card_game()