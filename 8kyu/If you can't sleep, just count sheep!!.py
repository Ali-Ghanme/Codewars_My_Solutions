def count_sheep(n):
    count = ""
    for i in range(1, n+1):
        count = count + "{} sheep...".format(i)
    return count
