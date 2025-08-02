from Fiets import Fiets


class Ebike(Fiets):
    def __init__(self, merk, model, gewicht, accu_capaciteit):
        super().__init__(merk, model, gewicht)
        self.__accu_capaciteit = accu_capaciteit

    def __str__(self):
        return (f"{super().__str__()}\nCapaciteit accu: "
                f"{self.__accu_capaciteit} Wattuur")

    def get_accu_capaciteit(self) -> int:
        return self.__accu_capaciteit

    def set_accu_capaciteit(self, accu_capaciteit):
        self.__accu_capaciteit = accu_capaciteit
