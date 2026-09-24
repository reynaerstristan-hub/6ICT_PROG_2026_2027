# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 8,
    "Werk":  6,
    "Ontspanning": 8
}


print("planning van morgen")
tijd_over = 0
for activieit,duur in planner.items():
    tijd_over = tijd_over + duur
    print(f"- {activieit} : {duur}u ")
    print(f"je hebt nog {24-tijd_over}")