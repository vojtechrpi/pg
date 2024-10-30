def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    pozice = figurka["pozice"]
    typ_figurky = figurka["typ"]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    def je_cesta_volna(pocatek, cil):
        x1, y1 = pocatek
        x2, y2 = cil
        dx = 1 if x2 > x1 else -1 if x2 < x1 else 0
        dy = 1 if y2 > y1 else -1 if y2 < y1 else 0
        x, y = x1 + dx, y1 + dy
        while (x, y) != (x2, y2):
            if (x, y) in obsazene_pozice:
                return False
            x, y = x + dx, y + dy
        return True

    if typ_figurky == "pěšec":
        if pozice[1] != cilova_pozice[1]:
            return False
        if pozice[0] >= cilova_pozice[0]:
            return False
        if pozice[0] == 2:
            if cilova_pozice[0] - pozice[0] <= 2:
                return je_cesta_volna(pozice, cilova_pozice)
        else:
            return cilova_pozice[0] - pozice[0] == 1 

    elif typ_figurky == "jezdec":
        dx = abs(pozice[0] - cilova_pozice[0])
        dy = abs(pozice[1] - cilova_pozice[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    elif typ_figurky == "věž":
        if pozice[0] != cilova_pozice[0] and pozice[1] != cilova_pozice[1]:
            return False
        return je_cesta_volna(pozice, cilova_pozice)

    elif typ_figurky == "střelec":
        if abs(pozice[0] - cilova_pozice[0]) != abs(pozice[1] - cilova_pozice[1]):
            return False
        return je_cesta_volna(pozice, cilova_pozice)

    elif typ_figurky == "dáma":
        je_pohyb_spravny = (
            pozice[0] == cilova_pozice[0] or 
            pozice[1] == cilova_pozice[1] or  
            abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]) 
        )
        return je_pohyb_spravny and je_cesta_volna(pozice, cilova_pozice)

    elif typ_figurky == "král":
        return max(abs(pozice[0] - cilova_pozice[0]), abs(pozice[1] - cilova_pozice[1])) == 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True