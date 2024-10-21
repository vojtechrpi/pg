vloz = int(input("Zadej cislo: "))
vloz2 = int(input("Zadej konecne cislo: "))

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
 
    print(seznam)


if je_prvocislo(vloz):
    print("True")
else:
    print("False")


je_prvocislo(vloz)
vrat_prvocisla(vloz2)