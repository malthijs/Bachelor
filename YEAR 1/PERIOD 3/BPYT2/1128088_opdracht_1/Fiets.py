class Fiets:
    def __init__(self, merk, model, gewicht):
        self.__merk = merk
        self.__model = model
        self.__gewicht = gewicht

    def __str__(self):
        return (f"Een {self.__merk} fiets, model {self.__model}.\n"
                f"Deze fiets weegt {self.__gewicht} kilo")

    def get_gewicht(self) -> int:
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht

    def get_merk(self) -> str:
        return self.__merk

    def set_merk(self, merk):
        self.__merk = merk

    def get_model(self) -> str:
        return self.__model

    def set_model(self, model):
        self.__model = model
