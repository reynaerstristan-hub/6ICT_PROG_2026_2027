# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}


while True:
    naam = input("wat is je naam")
    if naam in gasten:
        for naam,job in gasten.items():
            print(f"welkom {job} {naam}")

        