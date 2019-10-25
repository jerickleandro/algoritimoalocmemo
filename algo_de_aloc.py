def best_fit(memoria, processos):
    for p in processos:
        l = acha_pos_best(memoria, p)
        if(l > 0):
            memoria[l] = memoria[l] - p
    return memoria


def acha_pos_best(memoria, p):
    best = 0
    menor = 10000
    flag = False
    for m in memoria:
        if(p <= m):
            sub = m-p
            if(sub <= menor):
                menor = sub
                best = memoria.index(m)
            flag = True
    if flag:
        return best
    else:
        return -1


def wost_fit(memoria, processos):

    for p in processos:
        l = acha_pos_wost(memoria, p)
        if(l > 0):
            memoria[l] = memoria[l] - p
    return memoria


def acha_pos_wost(memoria, p):
    best = 0
    maior = 0
    flag = False
    for m in memoria:
        if(p <= m):
            sub = m-p
            if(sub >= maior):
                maior = sub
                best = memoria.index(m)
            flag = True
    if flag:
        return best
    else:
        return -1


def first_fit(memoria, processos):
    for p in processos:
        for m in memoria:
            if(p <= m):
                l = memoria.index(m)
                memoria[l] = memoria[l]-p
                break
    return memoria


def next_fit(memoria, processos):
    for p in processos:
        for m in memoria:
            if(p <= m):
                l = memoria.index(m)
                memoria[l] = memoria[l]-p
                break
    return memoria


memoria = [8, 12, 5, 20, 15, 9]
processos = [16, 3, 15, 2]
print(memoria)
print(best_fit(memoria.copy(), processos))
print(wost_fit(memoria.copy(), processos))
print(first_fit(memoria.copy(), processos))
