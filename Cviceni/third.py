def je_prvocislo(cislo):
    delitel = 2
    while delitel < cislo:
        if cislo % delitel == 0:
            break
        delitel = delitel + 1

    if delitel == cislo:
        return True
    else:
        return False


def vrat_prvocisla(maximum):
    seznam = []
    for i in range(1, maximum + 1):
        if je_prvocislo(i):
            seznam.append(i)
 
    return(seznam)


print(je_prvocislo(5))
print(vrat_prvocisla(10))