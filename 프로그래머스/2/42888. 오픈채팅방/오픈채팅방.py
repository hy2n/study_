"""
1. 각 record를 split해서 명령어를찾는다
2. UID로 만들어진 MAP함수 
"""
from collections import OrderedDict

def solution(record):
    UidList = OrderedDict()
    PrintList = []
    for x in record:
        command = x.split(' ')[0]
        UID = x.split(' ')[1]
        if (len(x.split(' '))<3):
            continue
        nickname = x.split(' ')[2]
        
        UidList[UID] = nickname
            
    for x in record:
        command = x.split(' ')[0]
        UID = x.split(' ')[1]
        
        if (command == 'Enter'):
            PrintList.append([True,UID])
        elif (command == 'Leave'):
            PrintList.append([False,UID])
    #print(PrintList)
    answer = []
    for x in PrintList:
        if x[0] == True:
            answer.append(f'{UidList[x[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{UidList[x[1]]}님이 나갔습니다.')
    return answer