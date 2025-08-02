from Voetballer import Voetballer


def bereken_gemiddelde_salaris_club(voetballer_lijst: list["Voetballer", ...]):
    salaris_per_club, spelers_per_club = {}, {}
    for voetballer in voetballer_lijst:
        if (voetballer.get_club() not in salaris_per_club and
                voetballer.get_club() not in salaris_per_club):
            salaris_per_club[voetballer.get_club()] = (
                int(voetballer.get_loon()[0:-1]))
            spelers_per_club[voetballer.get_club()] = 1

        else:
            salaris_per_club[voetballer.get_club()] += (
                int(voetballer.get_loon()[:-1]))
            spelers_per_club[voetballer.get_club()] += 1

    for key, value in salaris_per_club.items():
        print(f"{key}: {(value/spelers_per_club[key]):.2f}")


def diversiteit(land: str, voetballer_lijst: list["Voetballer", ...]) -> int:
    posities = set()
    linies = set()
    for voetballer in voetballer_lijst:
        if voetballer.get_nationaliteit() == land:
            posities.add(voetballer.get_positie())
            linies.add(voetballer.get_linie())

    if len(posities) + len(linies) == 0:
        return 0
    else:
        return len(posities) * len(linies)


def goedkoopste_team(voetballer_lijst: list["Voetballer", ...],
                     aantal_verdedigers: int,
                     aantal_middenvelders: int,
                     aantal_aanvallers: int) -> int:
    verdedigers, middenvelders, aanvallers, keepers = [], [], [], []
    team = [verdedigers, middenvelders, aanvallers, keepers]

    voetballer_lijst.reverse()
    for voetballer in voetballer_lijst:
        if (voetballer.get_linie() == "Verdediging" and len(verdedigers) <
                aantal_verdedigers):
            verdedigers.append(voetballer)

        elif (voetballer.get_linie() == "Middenveld" and len(middenvelders) <
              aantal_middenvelders):
            middenvelders.append(voetballer)

        elif (voetballer.get_linie() == "Aanval" and len(aanvallers) <
              aantal_aanvallers):
            aanvallers.append(voetballer)

        elif voetballer.get_linie() == "Keeper" and len(keepers) < 1:
            keepers.append(voetballer)

    salaris = 0
    for linie in team:
        for speler in linie:
            salaris += int(speler.get_loon()[0:-1])

    return salaris


def main():
    voetballer_lijst = []
    with open("top100_fifa.txt", "r", encoding="utf-8") as file:
        file.readline()
        inhoud = file.readlines()
        for line in inhoud:
            line = line.strip("\n").split(",")
            voetballer_lijst.append(Voetballer(*line))

    # voorbeelden
    bereken_gemiddelde_salaris_club(voetballer_lijst)
    print(diversiteit("Brazil", voetballer_lijst))
    print(goedkoopste_team(voetballer_lijst, 4, 3, 3))


if __name__ == "__main__":
    main()
