"""
Projectnaam: Eindopdracht

Auteur: Matthijs de Vries

Startdatum: 13-feb-2024

Einddatum: 13-feb-2024

Versienummer: 2
"""

from os import listdir, path
from copy import deepcopy
from random import choice, randint, shuffle


def lees_pokepack():
    """Functie beschrijving:
    Leest de tekstbestanden in map 'pokepack' en verwerkt ze tot een
    dictionary met nummer als key (str) en ASCII-art (str) als value.

    :return art: Info van map 'pokepack'
    :rtype art: Dictionary
    """
    art = {}
    root = "pokepack"
    files = listdir(root)

    for f in files:  # pakt bestandsnamen (zoals "001.txt")
        try:
            with open(path.join(root, f), "r", encoding="utf-8") as file:
                f = "".join([i for i in f if i.isnumeric()])  # nummer
                file = file.read().strip("\n")  # ASCII-art
                art[f] = file

        except FileNotFoundError as e:
            print(f"Fout: {e}.\nZorg ervoor dat de vereiste bestanden en "
                  f"mappen aanwezig zijn.")
            exit()

    return art


def lees_pokemon_150(art):
    """Functie beschrijving:
    Leest het bestand 'pokemon_150.txt' in en verwerkt het tot een dictionary
    met nummer als key (str) en overig als value (list).

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :return data: Info van bestand 'pokemon_150.txt'
    :rtype data: Dictionary
    """

    data = {}
    try:
        with open("pokemon_150.txt", "r", encoding="utf-8") as file:
            file.readline()
            for line in file:
                info = line.strip().split(",")
                nummer = info[0]  # nummer
                overig = info[1::]  # overig

                if nummer in art:
                    data[nummer] = [int(i) if i.isnumeric()
                                    else i for i in overig]

    except FileNotFoundError as e:
        print(f"Fout: {e}.\nZorg ervoor dat de vereiste bestanden en mappen "
              f"aanwezig zijn.")
        exit()

    return data


def lees_combat_moves():
    """Functie beschrijving:
    Leest het bestand 'combat_moves.csv' in en verwerkt het tot een dictionary
    met type als key (str) en move als value (list).

    :return aanvallen: Info van bestand 'combat_moves.csv'
    :rtype aanvallen: Dictionary
    """
    aanvallen = {}
    try:
        with open("combat_moves.csv", "r", encoding="utf-8") as file:
            file.readline()
            for line in file:
                aanval, soort = line.strip().split(";")
                if soort not in aanvallen:
                    aanvallen[soort] = [aanval]  # type
                else:
                    aanvallen[soort] += [aanval]  # move

    except FileNotFoundError as e:
        print(f"Fout: {e}.\nZorg ervoor dat de vereiste bestanden en mappen "
              f"aanwezig zijn.")
        exit()

    return aanvallen


def weergeef_pokemon(art, data, nummer):
    """Functie beschrijving:
    Weergeeft een Pokémon. Eerst wordt geassocieerde ASCII-art getoond, daarna
    nummer en tot slot 'name', 'type 1', 'type 2', 'HP', 'attack', 'defense' en
    'speed'.

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :param data: Info van bestand 'pokemon_150.txt'
    :type data: Dictionary

    :param nummer: Input van gebruiker
    :type nummer: String
    """
    print(f"{art[nummer]}")  # ASCII-art
    print(f"[#:{nummer}]", end="")  # nummer

    kolommen = ["Name", "Type 1", "Type 2", "HP", "Attack", "Defense", "Speed"]
    for index, kolom in enumerate(kolommen):  # itereert over de value van data
        item = data[nummer][index]
        print(f"[{kolom}:{item}]", end="")
    print("\n")


def weergeef_team(team):
    """Functie beschrijving:
    Weergeeft het team van de trainer. Eerst worden de kolommen getoond: '#',
    'name', 'type 1', 'type 2', 'attack', 'defense', 'speed'. Daarna wordt
    de bijbehorende informatie van de Pokémon(s) in deze categorieën getoond.

    :param team: Pokémon(s) in team van trainer
    :type team: Dictionary
    """
    kolommen = ["#", "Name", "Type 1", "Type 2", "HP", "Attack", "Defense",
                "Speed"]

    for kolom in kolommen:
        print(f"{kolom.ljust(12)}", end="")
    print("\n" + "-" * 89)

    for key, value in team.items():
        print(f"{key.ljust(12)}", end="")
        for item in value:
            print(f"{str(item).ljust(12)}", end="")
        print()
    print()


def dex_raadplegen(art, data):
    """Functie beschrijving:
    Logic programma dat samenwerkt met weergeef_pokemon(). Zorgt ervoor dat de
    trainer een Pokémon kan bekijken door het invoeren van een nummer of naam
    van een Pokémon.

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :param data: Info van bestand 'pokemon_150.txt'
    :type data: Dictionary
    """
    namen = {value[0]: key for key, value in data.items()}
    for key in data:
        print(f"[{key}] {data[key][0]}")

    while True:
        keuze = input("\nWelke Pokémon wil je bekijken? ")

        if keuze.isalpha() and keuze in namen.keys():  # naam
            weergeef_pokemon(art, data, namen[keuze])
            break

        if keuze.isnumeric() and keuze in namen.values():  # nummer
            weergeef_pokemon(art, data, keuze)
            break

        if keuze.isnumeric():
            print("Dit nummer komt niet voor in deze pokedex.")

        else:
            print("Deze naam komt niet voor in deze pokedex")


def starter(art, data):
    """Functie beschrijving:
    De trainer begint hier zijn avontuur door een start-pokémon te kiezen.
    Indien een incorrecte keuze gegeven wordt, wordt er opnieuw gevraagd
    wat voor start-pokémon hij/zij wil kiezen. Tot slot vraagt het om een
    confirmatie waarbij 'J/j' of 'N/n' op beantwoord moet worden.

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :param data: Info van bestand 'pokemon_150.txt'
    :type data: Dictionary

    :return: Een start-pokémon
    :rtype: Dictionary
    """
    starters = {"b": ["Bulbasaur", "001"], "c": ["Charmander", "004"],
                "s": ["Squirtle", "007"]}

    print("Welkom Pokétrainer!")
    while True:
        keuze = input("\nWelke start-pokémon wil je gaan gebruiken? "
                      "Je kunt een keuze maken uit:\n"
                      "[b] Bulbasaur\n"
                      "[c] Charmander\n"
                      "[s] Squirtle\n\n"
                      "Geef je keuze op: ").lower()

        if keuze in starters:
            naam, nummer = starters[keuze]
            print(f"\nJe hebt gekozen voor {naam}!")
            weergeef_pokemon(art, data, nummer)

            while True:
                stoppen = input("Ben je zeker van je keuze? (j/n) ").lower()
                if stoppen == "j":
                    print(f"\n{naam} is toegevoegd aan je team!\n")
                    return {nummer: data[nummer]}

                if stoppen == "n":
                    break


def vangen(art, data, team):
    """Functie beschrijving:
    Werkt samen met een groot aantal functies:
        1. vangen_spawner()
        2. vangen_kiezen()
        3. vangen_prioriteit()
        4. vangen_weergave()

    Zorgt ervoor dat als de trainer gewonnen heeft de verslagen Pokémon
    in zijn team krijgt.

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :param data: Info van bestand 'pokemon_150.txt'
    :type data: Dictionary

    :param team: Pokémon(s) in team van trainer
    :type team: Dictionary

    :return team: Pokémon(s) in team van trainer
    :rtype team: Dictionary
    """
    wilde_pokemon = vangen_spawner(art, data, team)  # nummer
    gekozen_pokemon = vangen_kiezen(team)  # nummer

    combo = [{wilde_pokemon: data[wilde_pokemon]},
             {gekozen_pokemon: data[gekozen_pokemon]}]

    # zorgt ervoor dat de snelste Pokémon vooraan staat (list --> dict)
    combo = vangen_prioriteit(combo, wilde_pokemon, gekozen_pokemon)

    # substituut dat als onafhankelijk object fungeert
    sub_combo = deepcopy(combo)
    verlies, winst = vangen_weergave(sub_combo, wilde_pokemon, gekozen_pokemon)

    if verlies == wilde_pokemon:
        print(f"De winnaar is {data[winst][0]}!\n"
              f"{data[verlies][0]} is toegevoegd aan je team!\n")
        team[verlies] = data[verlies]

    else:
        print(f"De winnaar is {data[winst][0]}!\n"
              f"Helaas, je hebt niet gewonnen van de wilde pokemon.\n")

    return team


def vangen_spawner(art, data, team):
    """Functie beschrijving:
    De trainer komt een willekeurige Pokémon tegen dat niet in zijn team zit.

    :param art: Info van map 'pokepack'
    :type art: Dictionary

    :param data: Info van bestand 'pokemon_150.txt'
    :type data: Dictionary

    :param team: Pokémon(s) in team van trainer
    :type team: Dictionary

    :return: Random geselecteerde nummer
    :rtype: String
    """
    while True:
        spawn = choice(list(art))  # pakt een nummer
        if spawn not in team:
            break

    print("Je gaat op weg om nieuwe Pokémon te vangen.")
    weergeef_pokemon(art, data, spawn)

    print(f"Je komt een wilde {data[spawn][0]} tegen! "
          f"Welke pokemon wil je tegen de wilde "
          f"{data[spawn][0]} gebruiken?\n")

    weergeef_team(team)
    return spawn


def vangen_kiezen(team):
    """Functie beschrijving:
    De trainer kiest een Pokémon om tegen de andere Pokémon in te zetten.

    :param team: Pokémon(s) in team van trainer
    :type team: Dictionary

    :return: Nummer van gekozen Pokémon
    :rtype: String
    """
    namen = {value[0]: key for key, value in team.items()}

    while True:  # elif niet nodig door 'return' keywords
        keuze = input("Kies je teampokémon uit met een nummer of naam: ")

        if keuze.isalpha() and keuze in namen.keys():  # naam
            return namen[keuze]

        if keuze.isnumeric() and keuze in namen.values():  # nummer
            return keuze

        if keuze.isnumeric():
            print("Dit nummer komt niet voor in dit team.\n")

        else:
            print("Deze naam komt niet voor in dit team.\n")


def vangen_prioriteit(combo, wilde_pokemon, gekozen_pokemon):
    """Functie beschrijving:
    Zorgt ervoor dat de snelste Pokémon begint, en verandert combo van een
    list naar een dictionary waar beide Pokémon inzitten.

    :param combo: Bezit twee dictionaries; afkomstig van de twee Pokémon's
    :type combo: List

    :param wilde_pokemon: De vijandige Pokémon
    :type wilde_pokemon: Dictionary

    :param gekozen_pokemon: De vriendelijke Pokémon
    :type gekozen_pokemon: Dictionary

    :return combo: Hierin zitten beide Pokémon's
    :rtype combo: Dictionary
    """
    if combo[0][wilde_pokemon][-1] < combo[1][gekozen_pokemon][-1]:
        combo.reverse()

    elif combo[0][wilde_pokemon][-1] == combo[1][gekozen_pokemon][-1]:
        shuffle(combo)

    return {key: value for d in combo for key, value in d.items()}


def vangen_weergave(sub_combo, wilde_pokemon, gekozen_pokemon):
    """Functie beschrijving:
    Doet een aantal berekeningen; hier wordt het gevecht gesimuleerd. Geeft
    uiteindelijk de Pokémon's terug aan vangen().

    :param sub_combo: Collectie van vriendelijke en vijandige Pokémon
    :type sub_combo: Dictionary

    :param wilde_pokemon: De vijandige Pokémon
    :type wilde_pokemon: Dictionary

    :param gekozen_pokemon: De vriendelijke Pokémon
    :type gekozen_pokemon: Dictionary

    :return: Nummers van de Pokémon
    :rtype: Tuple
    """
    sub_combo[gekozen_pokemon].append("")
    sub_combo[wilde_pokemon].append("")

    print(f"\nHet gevecht tussen {sub_combo[gekozen_pokemon][0]} "
          f"en {sub_combo[wilde_pokemon][0]} begint!")

    while True:
        for pokemon in sub_combo:
            andere_pokemon = next(key for key in sub_combo.keys()
                                  if key != pokemon)  # pakt de andere Pokémon

            aanval, schade = vangen_aanval(sub_combo, pokemon, andere_pokemon)
            sub_combo[andere_pokemon][3] -= schade

            print(f"{sub_combo[pokemon][0]} valt aan met {aanval}!\n"
                  f"Dit doet {schade} schade!\n"
                  f"{sub_combo[andere_pokemon][0]} heeft "
                  f"nu {max(0, sub_combo[andere_pokemon][3])} hp over.\n")

            if sub_combo[pokemon][3] <= 0:
                return pokemon, andere_pokemon

            if sub_combo[andere_pokemon][3] <= 0:
                return andere_pokemon, pokemon


def vangen_aanval(sub_combo, pokemon, andere_pokemon):
    """Functie beschrijving:
    Pikt een random aanval voor 'pokemon'. Een aanval kan niet twee keer
    achterelkaar plaatsvinden. Tot slot wordt de schade van de aanval berekent.

    :param sub_combo: Collectie van vriendelijke en vijandige Pokémon
    :type sub_combo: Dictionary

    :param pokemon: Een van de twee Pokémon's
    :type pokemon: String

    :param andere_pokemon: Een van de twee Pokémon's
    :type andere_pokemon: String

    :returns:
        - aanval (str): Random geselecteerde aanval
        - schade (int): Schade van de random geselecteerde aanval
    """
    aanvallen = lees_combat_moves()
    pokemon_aanvallen = []

    for i in sub_combo[pokemon][1:3]:
        if len(str(i)) != 0:
            pokemon_aanvallen.extend(aanvallen[i])

    while True:
        aanval = choice(pokemon_aanvallen)
        if aanval != sub_combo[pokemon][-1]:
            sub_combo[pokemon][-1] = aanval
            break

    schade = max(1, (round((sub_combo[pokemon][4] -
                            sub_combo[andere_pokemon][5]) / 6) +
                     randint(2, 20)))

    return aanval, schade


def opties():
    """Functie beschrijving:
    Presenteert aan de gebruiker een keuzemenu waarbij hij/zij tussen 1 en 5
    kan kiezen. Als de gebruiker een verkeerde input geeft, wordt de vraag
    opnieuw gesteld.

    :return optie: Input van de gebruiker
    :rtype optie: Int
    """
    while True:
        optie = input("[1] Pokédex raadplegen\n"
                      "[2] Nieuw Pokémon team starten\n"
                      "[3] Nieuwe Pokémon vangen\n"
                      "[4] Team tonen\n"
                      "[5] Stoppen\n\n"
                      "Wat wil je doen? ")
        print()

        if optie.isnumeric() and optie in "12345":
            break

    return int(optie)


def main():
    """Functie beschrijving:
    Hoofdprogramma van het spel Pokémon.

    Gebruikte functies:
        1. lees_pokepack()
        2. lees_pokemon_150()
        3. opties()
        4. dex_raadplegen()
        5. starter()
        6. vangen()
        7. weergeef_team()
    """
    art = lees_pokepack()
    data = lees_pokemon_150(art)
    team = {}

    while len(team) != 4 and (optie := opties()) != 5:
        if optie == 1:
            dex_raadplegen(art, data)

        elif optie == 2:
            team = starter(art, data)  # reset team

        elif (optie in {3, 4}) and len(team) == 0:
            print("Stel eerst een team samen voor"
                  " dat je deze keuze kunt maken.\n")

        elif optie == 3:
            team = vangen(art, data, team)  # update team
            if len(team) == 4:
                print("Gefeliciteerd! Je hebt een team van 4 Pokémon!")

        elif optie == 4:
            weergeef_team(team)

    print("Tot de volgende keer!")


if __name__ == "__main__":
    main()
