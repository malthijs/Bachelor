class Voetballer:
    def __init__(self, naam, leeftijd, nationaliteit, punten_algemeen,
                 punten_potentiaal, club, waarde, loon, punten_special,
                 voorkeursvoet, positie, rugnummer, begindatum, lengte,
                 gewicht):
        self.__naam = naam
        self.__leeftijd = leeftijd
        self.__nationaliteit = nationaliteit
        self.__punten_algemeen = punten_algemeen
        self.__punten_potentiaal = punten_potentiaal
        self.__club = club
        self.__waarde = waarde
        self.__loon = loon
        self.__punten_special = punten_special
        self.__voorkeursvoet = voorkeursvoet
        self.__positie = positie
        self.__rugnummer = rugnummer
        self.__begindatum = begindatum
        self.__lengte = lengte
        self.__gewicht = gewicht

    def __str__(self):
        return ("Naam: %s, Club: %s,"
                " Land: %s, Positie: %s."
                % (self.__naam, self.__club,
                   self.__nationaliteit, self.get_linie()))

    def get_naam(self):
        return self.__naam

    def set_naam(self, naam):
        self.__naam = naam

    def get_leeftijd(self):
        return self.__leeftijd

    def set_leeftijd(self, leeftijd):
        self.__leeftijd = leeftijd

    def get_nationaliteit(self):
        return self.__nationaliteit

    def set_nationaliteit(self, nationaliteit):
        self.__nationaliteit = nationaliteit

    def get_punten_algemeen(self):
        return self.__punten_algemeen

    def set_punten_algemeen(self, punten_algemeen):
        self.__punten_algemeen = punten_algemeen

    def get_punten_potentiaal(self):
        return self.__punten_potentiaal

    def set_punten_potentiaal(self, punten_potentiaal):
        self.__punten_potentiaal = punten_potentiaal

    def get_club(self):
        return self.__club

    def set_club(self, club):
        self.__club = club

    def get_waarde(self):
        return self.__waarde

    def set_waarde(self, waarde):
        self.__waarde = waarde

    def get_loon(self):
        return self.__loon

    def set_loon(self, loon):
        self.__loon = loon

    def get_punten_special(self):
        return self.__punten_special

    def set_punten_special(self, punten_special):
        self.__punten_special = punten_special

    def get_voorkeursvoet(self):
        return self.__voorkeursvoet

    def set_voorkeursvoet(self, voorkeursvoet):
        self.__voorkeursvoet = voorkeursvoet

    def get_positie(self):
        return self.__positie

    def set_positie(self, positie):
        self.__positie = positie

    def get_nummer(self):
        return self.__rugnummer

    def set_nummer(self, nummer):
        self.__rugnummer = nummer

    def get_begindatum(self):
        return self.__begindatum

    def set_begindatum(self, begindatum):
        self.__begindatum = begindatum

    def get_lengte(self):
        return self.__lengte

    def set_lengte(self, lengte):
        self.__lengte = lengte

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht

    def get_lengte_cm(self):
        try:
            lengte_split = self.__lengte.split("'")
            feet = float(lengte_split[0].strip())
            inches = float(lengte_split[1].strip())
            cm = feet * 30.48 + inches * 2.54
        except ValueError:
            cm = 175.000000
            print("Lengte van %s is niet bekend." % self.__naam)
        return cm

    def get_linie(self):
        if self.__positie == 'GK':
            linie = 'Keeper'
        elif self.__positie in ['RB', 'CB', 'LB', 'RWB', 'LWB', 'RCB', 'LCB']:
            linie = "Verdediging"
        elif self.__positie in ['CDM', 'CM', 'CAM', 'RM', 'LM', 'RCM', 'LCM',
                                'LDM', 'LAM', 'RDM', 'RAM']:
            linie = "Middenveld"
        elif self.__positie in ['RW', 'LW', 'CF', 'RF', 'LF', 'ST', 'RS',
                                'LS', ]:
            linie = "Aanval"
        else:
            linie = self.__positie
        return linie
