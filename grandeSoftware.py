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


class Style(Enum):
    A = "a"
    F = "f"


class InstrumentSpec:
    def __init__(self, builder, model, typeg, backWood, topWood):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.backWood = backWood
        self.topWood = topWood

    def matches(self, otherSpec):
        return (
            self.builder == otherSpec.builder
            and self.model.lower() == otherSpec.model.lower()
            and self.typeg == otherSpec.typeg
            and self.backWood == otherSpec.backWood
            and self.topWood == otherSpec.topWood
        )


class GuitarSpec(InstrumentSpec):
    def __init__(self, builder, model, typeg, backWood, topWood, numStrings):
        super().__init__(builder, model, typeg, backWood, topWood)
        self.numStrings = numStrings

    def getNumStrings(self):
        return self.numStrings

    def matches(self, otherSpec):
        return (
            super().matches(otherSpec)
            and self.numStrings == otherSpec.getNumStrings()
        )


class MandolinSpec(InstrumentSpec):
    def __init__(self, builder, model, typeg, backWood, topWood, style):
        super().__init__(builder, model, typeg, backWood, topWood)
        self.style = style

    def getStyle(self):
        return self.style

    def matches(self, otherSpec):
        return (
            super().matches(otherSpec)
            and self.style == otherSpec.getStyle()
        )


class Instrument:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec


class Guitar(Instrument):
    def __init__(self, serialNumber, price, spec):
        super().__init__(serialNumber, price, spec)


class Mandolin(Instrument):
    def __init__(self, serialNumber, price, spec):
        super().__init__(serialNumber, price, spec)


class Inventory:
    def __init__(self):
        self.inventory = []

    def addInstrument(self, serialNumber, price, spec):
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serialNumber, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serialNumber, price, spec)
        self.inventory.append(instrument)

    def getInstrument(self, serialNumber):
        for instrument in self.inventory:
            if instrument.serialNumber == serialNumber:
                return instrument
        return None

    def search(self, searchSpec):
        if isinstance(searchSpec, GuitarSpec):
            return [
                guitar
                for guitar in self.inventory
                if isinstance(guitar, Guitar) and guitar.spec.matches(searchSpec)
            ]
        elif isinstance(searchSpec, MandolinSpec):
            return [
                mandolin
                for mandolin in self.inventory
                if isinstance(mandolin, Mandolin) and mandolin.spec.matches(searchSpec)
            ]
        return []


def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addInstrument("V95693", 1499.95, spec1)
    inventory.addInstrument("V99999", 1599.95, spec1)
    spec2 = MandolinSpec(Builder.FENDER, "stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, Style.A)
    inventory.addInstrument("M12345", 1000.00, spec2)


def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)
    if matchingGuitars:
        print("Erin, talvez você goste destas:")
        for guitar in matchingGuitars:
            guitarSpec = guitar.spec
            print(
                "Guitarra:",
                guitar.serialNumber,
                guitarSpec.builder.value,
                guitarSpec.model,
                guitarSpec.typeg.value,
                "guitar:",
                guitarSpec.backWood.value,
                "na traseira e laterais,",
                guitarSpec.topWood.value,
                "no tampo,",
                guitarSpec.numStrings,
                "cordas. Ela pode ser sua por apenas $",
                guitar.price,
                "!",
            )
    else:
        print("Desculpe Erin, não temos nada para você.")

    whatBobLikes = MandolinSpec(Builder.FENDER, "stratocaster", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, Style.A)
    matchingMandolins = inventory.search(whatBobLikes)
    if matchingMandolins:
        print("Bob, talvez você goste destas:")
        for mandolin in matchingMandolins:
            mandolinSpec = mandolin.spec
            print(
                "Mandolin:",
                mandolin.serialNumber,
                mandolinSpec.builder.value,
                mandolinSpec.model,
                mandolinSpec.typeg.value,
                "mandolin:",
                mandolinSpec.backWood.value,
                "na traseira e laterais,",
                mandolinSpec.topWood.value,
                "no tampo,",
                mandolinSpec.style.value,
                "estilo. Ela pode ser sua por apenas $",
                mandolin.price,
                "!",
            )
    else:
        print("Desculpe Bob, não temos nada para você.")


if __name__ == "__main__":
    main()