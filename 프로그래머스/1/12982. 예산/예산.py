def solution(d, budget):
    total_money = 0
    total_ok_teams = 0
    for x in range(0,len(d)):
        total_money += d[x]
    
    if (total_money == budget):
        return len(d)
    else:
        d.sort()
        for x in d:
            if (budget>=x):
                budget -= x
                total_ok_teams += 1
            else:
                return total_ok_teams
    return total_ok_teams