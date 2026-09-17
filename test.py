# nummers = ["+32 470 998301", "+32 483 313220", "+ 32 453 876532"]
# namen = ["jan", "piet", "kapper korneel"]

# naam_gebr = input("geef een naam: ")

# for index,naam in enumerate(namen):
#     if naam_gebr == naam:
#         print(nummers[index])


telefoonboek = {"jan" : "+32 454 456767",
                "piet" : "+32 696 696969",
                "kapper korneel" : "+32 676 76767"
}

naam = input("geef naam: ")
if naam in telefoonboek:
    print(telefoonboek[naam])
else:
    print('naam bestaat niet')