# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

def bored_qan():
    students = int(input()) 
    
    default = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
    question = '"재귀함수가 뭔가요?"'

    story1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
    story2 ='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
    story3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
    answer1 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
    answer2 = "라고 답변하였지."

    #반복횟수 아님 들여쓰기
    depth = 0 
    
    def ask(depth):
        #base case
        if depth == students:
            print("____" * depth + question)
            print("____" * depth + answer1)
            print("____" * depth + answer2)
            return
        
       
        print("____" * depth + question)
        print("____" * depth + story1)
        print("____" * depth  + story2)
        print("____" * depth + story3)

        ask(depth+1)

        #여기서 depth에 따라 "____" 결정
        print("____"*depth + answer2) 

    print(default)
    ask(depth)

bored_qan()