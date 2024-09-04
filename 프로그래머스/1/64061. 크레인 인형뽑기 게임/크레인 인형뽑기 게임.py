def solution(board, moves):
    answer = 0
    box = [0]
    for i in moves:
        Moved = False
        for x in board:
            if (x[i-1] > 0) and (Moved==False):
                Moved = True #더 밑으로 안내려가게 막음
                if (box[-1] == x[i-1]): #만약 전 요소와 현 요소가 같으면
                    answer = answer + 2 # 2더하고
                    print(box)
                    print(x[i-1])
                    box.pop() #없애
                    print(box)
                else:
                    box.append(x[i-1]) #바구니에 요소 담기
                x[i-1] = 0
    return answer