dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']
]
#niveau 1
# rij = int(input("geef een rij op"))
# kolom = int(input("geef een kolom op"))

# print(dambord_2D[rij][kolom])

#niveau 2 : je krijg een out of range error

#niveau 3 
rij = int(input("geef een rij op"))
kolom = int(input("geef een kolom op"))


if (rij > len(dambord_2D)) or (kolom > len(dambord_2D[kolom])):
    print("rij niet in dambord")
    
else:
    print(dambord_2D[rij][kolom])