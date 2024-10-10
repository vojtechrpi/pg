# funkce vrati treti prvek ze seznamu
#def vrat_treti(seznam):
#    if len(seznam) < 3:
#        return None
#    else: 
#       return seznam[2]

# funkce spocita prumer z hodnot v seznamu
#def udelej_prumer(seznam):
#    vysledek = sum(seznam)
#    delka = int(len(seznam))
#    prumer = vysledek/delka
#    return prumer
# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(student):
    jmeno = student["jmeno"]
    prijmeni = student["prijmeni"]
    vek = student["vek"]
    prumer = round(sum(student["znamky"])/int(len(student["znamky"])),2)
    return f"Jmeno: {jmeno}, Prijmeni: {prijmeni}, Vek: {vek}, Prumerna znamka: {prumer}"


if __name__ == "__main__":
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))