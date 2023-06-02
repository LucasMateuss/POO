from enum import Enum


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan" 
    PRS = "prs"
    ANY = "any"


class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"


class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"


class GuitarSpec:
    def __init__(self, builder, model, typeg, backWood, topWood, numStrings):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.backWood = backWood
        self.topWood = topWood
        self.numStrings = numStrings

    def getBuilder(self):
        return self.builder

    def getTypeG(self):
        return self.typeg

    def getModel(self):
        return self.model

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def getNumStrings(self):    
        return self.numStrings

    def matches(self, otherSpec):
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model and self.model.lower() != otherSpec.getModel().lower():
            return False
        if self.typeg != otherSpec.getTypeG():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        if self.numStrings != otherSpec.getNumStrings():
            return False
        return True


class Guitar:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice


class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def searchGuitar(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.spec.matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars


def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)


def main():
    inventory = Inventory()
    initializeInventory(inventory)

    lucas = GuitarSpec(Builder.FENDER, "Stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.searchGuitar(lucas)

    if matchingGuitars:
        print("Lucas, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.spec
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:")
            print(f"{guitarSpec.getBackWood().value} na traseira e laterais,")
            print(f"{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas")
            print(f"Ela pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Lucas, não temos nada para você.")


if __name__ == '__main__':
    main()