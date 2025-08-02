from Fiets import Fiets


class Racefiets(Fiets):
    def __init__(self, merk, model, gewicht, aantal_versnellingen):
        super().__init__(merk, model, gewicht)
        self.__aantal_versnellingen = aantal_versnellingen

    def __str__(self):
        return (f"{super().__str__()}\nAantal versnellingen: "
                f"{self.__aantal_versnellingen}")

    def get_versnellingen(self) -> int:
        return self.__aantal_versnellingen

    def set_versnellingen(self, aantal_versnellingen):
        self.__aantal_versnellingen = aantal_versnellingen
