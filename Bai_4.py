def trituyetdoi (x) :
    mang =[i for i in range(len(x))]
    for i in range(len(x)) :
        mang.append(abs(x[i]))
        total = sum(mang)
    return total