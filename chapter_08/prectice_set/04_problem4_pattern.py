def pattern(n):
    if(n==0):return 0
    print("*"*n)
    return pattern(n-1)

pattern(4)