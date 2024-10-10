"""
1.주어진 숫자를 배열로 변환한다
2.for문으로 가능한 모든 숫자 조합을 구한다
3.max()로 최댓값을 구한 후 return한다(문자열 형태로)
"""

def solution(number, k):
    target_number = []
    result = []
    for char_element in number: # 1
        target_number.append(char_element)
    
    for x in target_number:
        if result and (result[-1] < x):
            while result and (k>0) and (result[-1] < x):
                k -= 1
                result.pop()
        result.append(x)
    result = result[:len(result) - k]
    result_str = ""
    
    for x in result:
        result_str = result_str + x
    return result_str