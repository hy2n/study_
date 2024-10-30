from collections import OrderedDict
"""
1. 신고받을 MAP자료형을 만든다
2. 중복 신고 상황이 아니라면 MAP자료형의 숫자를 ++ 한다
3. 반복하고 출력한다
"""

def solution(id_list, report, k):
    REPORT_USER_LIST=OrderedDict()
    REPORT_LOG=OrderedDict()
    for x in id_list: #초기화 (1)
        REPORT_USER_LIST[x] = 0
        REPORT_LOG[x] = []
    for x in report:
        reporter = x.split(" ")[0]
        bad_user = x.split(" ")[1]
        if bad_user in REPORT_LOG[reporter]: # 중복신고시 continue
            continue
        else:
            REPORT_USER_LIST[bad_user] += 1
            REPORT_LOG[reporter].append(bad_user)
    answer = []
    #print(REPORT_LOG)
    for x in REPORT_USER_LIST:
        if (REPORT_USER_LIST[x]>=k):# 차단시 알림
            REPORT_USER_LIST[x]= -1 #차단되었다고 표식
    for x in id_list:
        #print(x)
        notifycount = 0
        for y in REPORT_LOG[x]: # 신고한 사용자기 있으면
            if y and REPORT_USER_LIST[y] == -1:# 그 신고한 사용자가 차단당했다면
                notifycount += 1
        answer.append(notifycount)
    return answer
