lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("rij,kolom,getal")
#niveau 1

# for rij,lijst in enumerate(lijst_2D):
#     for kolom , getal in enumerate(lijst):
#         if (rij == 0) or (rij == 2):
#             print(rij,kolom,getal)

#niveau 2

for rij,lijst in enumerate(lijst_2D):
    for kolom , getal in enumerate(lijst):
        if rij == kolom:
            print(rij,kolom,getal)