def solution(data, ext, val_ext, sort_by):
    answer = []
    mode = 0
    if ext == "code":
        mode = 0
    elif ext == "date":
        mode = 1
    elif ext == "maximum":
        mode = 2
    else:
        mode = 3

    sel_mode = 0
    if sort_by == "code":
        sel_mode = 0
    elif sort_by == "date":
        sel_mode = 1
    elif sort_by == "maximum":
        sel_mode = 2
    else:
        sel_mode = 3
        
    for a in data:
        if (a[mode] < val_ext):
            answer.append(a)

    answer.sort( key=lambda x: x[sel_mode])
    return answer
