class ImutableInteger:
    def __init__(self, number):
        self.__number = number
        self.imutable = True
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number
    
    
if __name__ == "__main__":
    ii = ImutableInteger(5)
    print(ii.number)

    ii.imutable = True
    ii.number = 60


    