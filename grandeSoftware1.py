from enum import Enum

class builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan" 
    PRS = "prs"
    ANY = "any"


class typeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"


class wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"


class Guitar:
    def __init__(self, serialNumber, price, builder, model, typeg, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.backWood = backWood
        self.topWood = topWood

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getBuilder(self):
        return self.builder

    def getTypeg(self):
        return self.typeg

    def getModel(self):
        return self.model

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood
    
class inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, builder, model, typeg, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, typeg, backWood, topWood)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None
    

    def searchGuitar(self, searchGuitar):
        for guitar in self.guitars:
            if searchGuitar.getBuilder() != guitar.getBuilder():
                continue
            model = searchGuitar.getModel().lower()
            if model and model != "" and model != guitar.getModel().lower():
                continue
            if searchGuitar.getTypeg() != guitar.getTypeg():
                continue
            if searchGuitar.getBackWood() != guitar.getBackWood():
                continue
            if searchGuitar.getTopWood() != guitar.getTopWood():
                continue
            return guitar
        return None


inventory = inventory()
inventory.addGuitar("12345", 1500, builder.RYAN, "Stratocastor", typeG.ACOUSTIC, wood.MAPLE, wood.ADIRONDACK)

lucas = Guitar(" ", 0, builder.RYAN,"Stratocastor", typeG.ACOUSTIC, wood.MAPLE, wood.ADIRONDACK)

guitar = inventory.searchGuitar(lucas)

if guitar is not None:
  print(f'Olá, talvez você goste desta: {guitar.getBuilder()} {guitar.getModel()} {guitar.getTypeg()} guitar:\n {guitar.getBackWood()} na traseira e laterais, \n{guitar.getTopWood()} no tampo. \n Ela pode ser sua por apenas R${guitar.getPrice()}')
else:
  print("Desculpe Erin, não temos nada para você")