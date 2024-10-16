def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }
    teen = {
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }
    desitky = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát",
        6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
    }

    if cislo in jednotky:
        return jednotky[cislo]
    elif cislo in teen:
        return teen[cislo]
    elif 20 <= cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + jednotky[jednotka]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo je mimo rozsah"

print(cislo_text(45))  
