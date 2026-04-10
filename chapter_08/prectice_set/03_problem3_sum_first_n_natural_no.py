
def sum_first_n_natural_no(n:int):
    if (n== 1): return 1
    return n + sum_first_n_natural_no(n-1)


print(sum_first_n_natural_no(4))
