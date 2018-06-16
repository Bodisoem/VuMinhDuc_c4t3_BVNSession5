def phantu (n):
    day = [2]
    congsai = 0
    for i in range(n):
        if i % 2 == 0 and i != 0:
            congsai += 0.5
            day.append( day[0] - congsai)
        if i % 2 == 1  :
            day.append( -1 )
    return day

