import sys
import csv

def nacti_csv(soubor):
    seznam = []
    with open(soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            seznam.append(print(radek))
    return seznam

# def spoj_data(*data):
#     return [["Tomas","Novak","28","1"], ["Jan","Dvorak","20","1"], ["Alice","Nova","","1"]]



def zapis_csv(soubor, data):
    with open(soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)

    


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledna_data)
    except IndexError:
        print("chyba")
        
data = [["Tomas","Novak","28","1"], ["Jan","Dvorak","20","1"], ["Alice","Nova","","1"]]
nacti_csv("excel.csv")
zapis_csv("novy_excel.csv", data)