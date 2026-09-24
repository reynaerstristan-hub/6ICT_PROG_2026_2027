# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}


while True:
    naam = input("wat is je naam: ")
    if naam == "stop":
        break
    
    elif naam in gasten:
        print(f"hallo {gasten.get(naam)} {naam}")
        gasten.pop(naam)

    elif naam not in gasten:
        print("naam niet op lijst")