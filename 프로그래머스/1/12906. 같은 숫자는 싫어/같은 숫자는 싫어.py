"""
알고리즘
1. 스택 자료형에 원소를 넣는다
2. 스택 자료형의 최근 원소값이 
"""

def solution(arr):
    answer = []
    bef = -1
    for x in arr:
        if (x != bef):
            answer.append(x)
            bef = x
    return answer