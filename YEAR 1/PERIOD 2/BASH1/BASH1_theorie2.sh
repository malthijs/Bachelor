#!/bin/bash
# ssh s1128088@145.97.18.235
# password: telehack
# logout (beëindigt connectie met server)

# nano (teksteditor; voor complexe programma's)
# ./ (voor het executeren van een script)

# >    --> schrijf naar een bestand
# >>   --> voeg toe aan een bestand
# <    --> de inhoud van een bestand wordt gebruikt als invoer
# |    --> geeft uitvoer van een commando door naar een andere

# head -nx (toont x aantal regels vanaf het begin; standaard is 10)
# tail -nx (toont x aantal regels van het eind; standaard is 10)
# head -nx | tail -n+y (toont x aantal regels minus y aantal regels vanaf het
# begin)

# sort (sorteert; standaard is alfabetisch)
# sort -n (sorteert numeriek)
# sort -r (sorteert andersom)
# sort -R (sorteert willekeurig)
# sort -k (sorteert op basis van een gespecificeerde range van kolommen)
# sort -t (hiermee kan gespecificeerd worden hoe kolommen gescheiden worden)

# nl (nummert de opgegeven regels)
# nl -s (plaatst opgegeven karakters na nummering)
# nl -w (plaatst x aantal spaties voor nummering)

# wc (weergeeft aantal lijnen, woorden, bytes en bestandsnaam)
# wc -l (aantal lijnen en bestandsnaam)
# wc -w (aantal woorden en bestandsnaam)
# wc -m (aantal karakters en bestandsnaam)

# cut -f -d
# -f (snijdt op basis van een gespecificeerde range van kolommen)
# -d (hiermee kan gespecificeerd worden hoe kolommen gescheiden worden)

# sed 's/regex/replace/g'

# * voorbeeld *
# sed 's/.$//g' (laatste karakter van string wordt "verwijderd")
# sed 's/^.//g' (eerste karakter van string wordt "verwijderd")

# uniq (voegt alle regels samen die met elkaar overeenkomen)
# uniq -d (toont alleen de herhaalde regels)
# uniq -c (toont de herhaalde regels, met het aantal herhalingen voor elk
# unieke regel)

# fold (plaatst een enter na gespecificeerde hoeveelheid karakters)

# tr (verplaatst gespecificeerde substring met een andere substring)
# tr -d (verwijdert de gespecificeerde tekens)

# LET OP:
# 'tr' commando is ontworpen voor het vertalen of verwijderen van individuele
# tekens en niet voor complexe patronen

# more (toont inhoud van een file; gaat er met grotere stappen doorheen)
# less (toont inhoud van een file; gaat er met kleinere stappen doorheen)
