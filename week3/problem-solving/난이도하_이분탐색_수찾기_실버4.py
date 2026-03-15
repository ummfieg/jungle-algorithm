# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

def binary_search():
    default_count = int(input())
    nums_list = list(map(int, input().split()))
    second_count = int(input())
    find_nums = list(map(int, input().split()))

    nums_list.sort()
 
    # print(nums_list,find_nums)

    # 기준 리스트를 먼저 정렬한다.
   #디폴트 카운트만큼 for문 돌려서
   #nums_list 애들을 바깥 for문으로 두고
   #second_count만큼 안쪽 for문 두고
   # nums_list의 각 원소를 기준 타겟을 두고 for in find_nums 가 있으면 


    for target in find_nums:
        left = 0
        right = len(nums_list)-1

        while left <= right:
            mid =(left+right)//2
            if target > nums_list[mid]:
                left = mid+1
            elif target == nums_list[mid]:
                print(1)
                break
            elif target <  nums_list[mid]:
                right = mid-1
       
        else:
           print(0)
    
binary_search()
    