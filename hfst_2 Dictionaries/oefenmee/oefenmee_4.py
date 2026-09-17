# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
#niveau 1
fruit = input("geef een fruit op: ")
print(f"aantal {fruit} in mand: {fruitmand[fruit]}")

#niveau 2
fruit = input("geef een fruit op: ")
if fruit in fruitmand:
    print(f"aantal {fruit} in mand: {fruitmand[fruit]}")
else: 
    print("fruit niet in mand")