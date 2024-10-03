def stars_while():
    print("Začátek")
    i = 0
    while i < 5:
        print("*")
        i += 1
    print("Konec")

def stars_for():
    print("zacatek")

    for i in range(5):
        print("*", i)
    print("Konec")

def in_range(min_number, max_number, number):
    if (number < min_number) or (number > max_number):
        print ("Is not in range")
    else:
        print("Is in range")
    

#in_range(100, 1000, 2)

#funkce vypise "Ahoj jméno"
def dopln_jmeno(jmeno):
    pass

jm = input("Zadej jmeno: ")
dopln_jmeno(jm)
print ("Ahoj ", jm)