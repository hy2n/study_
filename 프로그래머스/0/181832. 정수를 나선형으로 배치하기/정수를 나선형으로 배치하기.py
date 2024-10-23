def solution(n):
    arr_ = [[0] * n for _ in range(n)]
    total_set = 1
    ava_x_L = 0
    ava_x_R = n -1
    ava_y_T = 0
    ava_y_B = n -1
    x=0 # 시작점
    y=0 # 시작점
    
    while total_set <= n*n:
        print(total_set)
        while x <= ava_x_R and total_set <= n*n: #오른쪽으로 이동
            arr_[y][x] = total_set
            total_set += 1
            x += 1
        x -= 1
        y += 1
        ava_y_T +=1
        
        while y <= ava_y_B and total_set <= n*n: #밑으로 이동
            arr_[y][x] = total_set
            total_set += 1
            y += 1
        y -= 1
        x -= 1 
        ava_x_R -=1
        
        while x >= ava_x_L and total_set <= n*n: #왼쪽으로 이동
            arr_[y][x] = total_set
            total_set += 1
            x -= 1
        y -= 1
        x += 1 
        ava_y_B -= 1
        
        while y >= ava_y_T and total_set <= n*n: #위로 이동
            arr_[y][x] = total_set
            total_set += 1
            y -= 1
        y += 1
        x += 1 
        ava_x_L+=1
            
    return arr_

def debug(x,y):
    print(f'{x} , {y}')
