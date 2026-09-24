# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}

#niveau 1
# print("recept voor worst met wortelen en erwten")

# for voeding,hoeveelheid in recept.items():
#     print(voeding, ":" , hoeveelheid)

#niveau 2
print("recept voor worst met wortelen en erwten")
personen = int(input("voor hoeveel personen wil je? : "))


for voeding,hoeveelheid in recept.items():
    recept[voeding] = (hoeveelheid / 4) * personen
print(recept)
    