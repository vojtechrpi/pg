class BadDataError(Exception):
    pass


class Souradnice:

    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka
    
    @property
    def sirka(self):
        return self.__sirka
    
    @property
    def delka(self):
        return self.__delka
    
    def __str__(self) -> str:
        return f'Souradnice: {self.sirka}, {self.delka}'
    
    @classmethod
    def nacti_z_dat(cls, data):
        if "souradnice" not in data:
            raise BadDataError
        souradnice = data["souradnice"]
        if not isinstance(souradnice, dict):
            raise BadDataError
        if "sirka" not in souradnice or "delka" not in souradnice:
            raise BadDataError
        return cls(souradnice["sirka"], souradnice["delka"])


if __name__ == "__main__":
    # trida Souradnice v konstruktoru (__init__) bere sirku a delka,
    # pokud ale chceme vytvorit novy objekt z dat (data), je dobre
    # implementovat tridni metodu nacti_z_dat
    data = {"souradnice": {"sirka": 50, "delka": 50}}
    s = Souradnice.nacti_z_dat(data)
    print(s)