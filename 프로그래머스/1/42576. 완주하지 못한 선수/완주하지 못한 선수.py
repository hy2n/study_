import collections

def solution(participant, completion):
    usersHashMap = collections.Counter(participant) - collections.Counter(completion)
    
    for key, value in usersHashMap.items():
        if value > 0:
            return key