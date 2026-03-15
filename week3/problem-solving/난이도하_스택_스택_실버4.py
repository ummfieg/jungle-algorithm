# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
def stack_input():
    run_count = int(input())

    stack = []

    data = ([str(input()) for _ in range(run_count)])

    for i in data:
        if "push" in i:
            push_data = i.split()
            stack.append(push_data[1])
        elif i == "top":
            if len(stack) >= 1:
                print(stack[-1])
            else:
                print(-1)
        elif i == "size":
            print(len(stack))
        elif i == "empty":
            if len(stack) <= 0:
                print(1)
            else:
                print(0)
        elif i == "pop":
            if len(stack) >= 1:
                pop_value = stack.pop()
                print(pop_value)
            else:
                print(-1)
stack_input()