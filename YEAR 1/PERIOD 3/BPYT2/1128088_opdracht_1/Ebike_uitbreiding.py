from Fiets import Fiets


class Ebike(Fiets):
    def __init__(self, merk, model, gewicht, accu_capaciteit):
        super().__init__(merk, model, gewicht)
        self.__accu_capaciteit = accu_capaciteit
        self.__check()

    def __str__(self):
        return (f"{super().__str__()}\nCapaciteit accu: "
                f"{self.__accu_capaciteit} Wattuur")

    def __check(self):
        if type(self.__accu_capaciteit) != int:
            self.__accu_capaciteit = 700

        elif self.__accu_capaciteit > 700:
            self.__accu_capaciteit = 700

        elif self.__accu_capaciteit < 0:
            self.__accu_capaciteit = 700

    def bereken_accuduur(self, snelheid: int) -> float:
        accuduur = self.__accu_capaciteit / (15 + 10 * 1.1 ** snelheid)
        return accuduur

    def bereken_actieradius(self, snelheid: int) -> float:
        actieradius = snelheid * (
                self.__accu_capaciteit / (15 + 10 * 1.1 ** snelheid))
        return actieradius

    def bereken_optimale_snelheid(self, doelafstand: int) -> int:
        optimale_snelheid = 1000
        while True:
            actieradius = optimale_snelheid * (self.__accu_capaciteit /
                                               (15 + 10 * 1.1 **
                                                optimale_snelheid))
            if actieradius > doelafstand:
                return optimale_snelheid

            elif optimale_snelheid < 1 or doelafstand < 0:
                return -1

            else:
                optimale_snelheid -= 1

    def get_accu_capaciteit(self) -> int:
        return self.__accu_capaciteit

    def set_accu_capaciteit(self, accu_capaciteit):
        self.__accu_capaciteit = accu_capaciteit


# voorbeelden
# a = Ebike("Zoom", "Rapido", 25, 500)
# print(a.get_accu_capaciteit())
# b = Ebike("Zoom", "Rapido", 25, -10)
# print(b.get_accu_capaciteit())
# c = Ebike("Zoom", "Rapido", 25, "pepernoot")
# print(c.get_accu_capaciteit())

# stella = Ebike("Stella", "Durante", 25, 400)
# print(stella.bereken_accuduur(34))
# print(stella.bereken_actieradius(34))
# print(stella.bereken_optimale_snelheid(75))
# print(stella.bereken_optimale_snelheid(200))
# print(stella.bereken_optimale_snelheid(25))
