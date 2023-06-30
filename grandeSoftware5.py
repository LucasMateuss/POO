from enum import Enum
from typing import TypedDict, List


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"


class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"


class Style(Enum):
    A = "a"
    F = "f"


class Type(Enum):
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


class Properties(TypedDict):
    instrument_type: InstrumentType
    builder: Builder
    model: str
    type: Type
    num_strings: int
    top_wood: Wood
    back_wood: Wood
    style: Style


class InstrumentSpec:
    def __init__(self, properties: Properties = None):
        if properties is None:
            self.properties: Properties = {}
        else:
            self.properties = properties.copy()

    def get_property(self, property_name: str):
        return self.properties.get(property_name)

    def get_properties(self) -> Properties:
        return self.properties

    def matches(self, other_spec) -> bool:
        for property_name, property_value in other_spec.get_properties().items():
            if property_name not in self.properties or self.properties[property_name] != property_value:
                return False
        return True


class Instrument:
    def __init__(self, serial_number: str, price: float, spec: InstrumentSpec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_price(self) -> float:
        return self.price

    def set_price(self, new_price: float) -> None:
        self.price = new_price

    def get_spec(self) -> InstrumentSpec:
        return self.spec


class Inventory:
    def __init__(self):
        self.inventory: List[Instrument] = []

    def add_instrument(
        self, serial_number: str, price: float, spec: InstrumentSpec
    ):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

    def get_instrument(self, serial_number: str):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec: InstrumentSpec) -> List[Instrument]:
        matching_instruments: List[Instrument] = []
        for instrument in self.inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments


def initialize_inventory(inventory):
    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.COLLINGS,
        "model": "CJ",
        "type": Type.ACOUSTIC,
        "num_strings": 6,
        "top_wood": Wood.INDIAN_ROSEWOOD,
        "back_wood": Wood.SITKA,
    }
    inventory.add_instrument("11277", 3999.95, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.GIBSON,
        "model": "Les Paul",
        "type": Type.ELECTRIC,
        "num_strings": 6,
        "top_wood": Wood.MAPLE,
        "back_wood": Wood.MAPLE,
    }
    inventory.add_instrument("70108276", 2295.95, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.MANDOLIN,
        "builder": Builder.GIBSON,
        "model": "F5-G",
        "type": Type.ACOUSTIC,
        "top_wood": Wood.MAPLE,
        "back_wood": Wood.MAPLE,
        "style": Style.A,
    }
    inventory.add_instrument("9019920", 5495.99, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.BANJO,
        "builder": Builder.GIBSON,
        "model": "RB-3",
        "type": Type.ACOUSTIC,
        "num_strings": 5,
        "back_wood": Wood.MAPLE,
    }
    inventory.add_instrument("8900231", 2945.95, InstrumentSpec(properties))

def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    properties = {
        "builder": Builder.GIBSON,
        "back_wood": Wood.MAPLE,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)
    if matching_instruments:
        print("Erin, talvez você goste desta(s):")
        print("\n----- Lista de instrumentos encontrados -----\n")
        for instrument in matching_instruments:
            instrument_spec = instrument.get_spec()
        for property_name, property_value in instrument_spec.get_properties().items():
            if property_name == "instrument_type":
                continue
            if isinstance(property_value, Enum):
                print(property_name.capitalize() + ":", property_value.value)
            else:
                print(property_name.capitalize() + ":", property_value)
        print("Ele pode ser seu por apenas $", instrument.get_price(), "\n")
        return
    print("Não foram encontradas guitarras com as especificações desejadas.")


if __name__ == "__main__":
    main()