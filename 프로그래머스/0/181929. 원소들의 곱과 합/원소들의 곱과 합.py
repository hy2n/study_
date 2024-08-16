def solution(num_list):
    sum_ = 0
    rex_ = 1
    for a in num_list:
        sum_ = sum_ + a
    for a in num_list:
        rex_ = rex_ * a
    if ((sum_*sum_)<rex_):
        return 0
    else:
        return 1