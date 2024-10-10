import sys

def main(parametr):
    print(f"Parametr obsahuje {parametr}")

if __name__ == "__main__":
    jmeno = input("Zadej jmeno: ")
    main(jmeno)
    prijmeni = input("Zadej prijmeni: ")
    main(prijmeni)