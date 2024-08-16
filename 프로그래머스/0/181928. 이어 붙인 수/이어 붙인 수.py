def solution(num_list):
    answer = 0
    arr_odd = [x for x in num_list if x%2!=0]
    odd_str = ''
    
    arr_even = [x for x in num_list if x%2==0]
    even_str = ''
    for x in arr_odd:
        odd_str = odd_str + str(x)
    for x in arr_even:
        even_str = even_str + str(x)
    return int(even_str) + int(odd_str)
        
        