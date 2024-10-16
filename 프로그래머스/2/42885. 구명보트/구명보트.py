from collections import deque
"""

1.작은 수부터 정렬
2.인덱스별로 진행하며, 한 인덱스가 올라가면서 보트를 Queue로 구현
3.모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return
"""
def solution(people, limit):
    people.sort()
    boat_current = deque(people)
    boat_used = 0
    
    
    while boat_current:
        if (len(boat_current) < 2):
            boat_used += 1
            break;
        if ((boat_current[0] + boat_current[-1]) <= limit):
            print(boat_current[0] + boat_current[-1])
            boat_current.pop()
            boat_current.popleft()
        else:
            print(boat_current[0] + boat_current[-1])
            boat_current.pop()
        boat_used += 1
    return boat_used
        