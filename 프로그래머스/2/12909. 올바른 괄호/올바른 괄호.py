"""
1 . 문자열이 ( 라면 값을 1 추가한다
2 . 문자열이 ) 라면 값을 1 지운다
3 . 만약 마지막 코드에서 STACK변수 안에 아무것도 들었으면 TRUE, 아니면 FALSE로..
"""
def solution(s):
    stack = []
    if(s[0] == ')'): #예외처리
        return False
    elif len(s)%2 == 1:
        return False
    
    for x in range(0,len(s)):
        if (s[x] == '('):
            stack.append('(')
        elif (s[x] == ')') and (len(stack)>0):
            if(stack[-1] == '('):
                stack.pop()
    if (len(stack) == 0):
        return True
    else:
        return False