laptop_info = [
    253,
    [2, "HP ProBook 445 G8"],
    [6, "Huur30", "deployed", "deployed", [3, "LAPTOPS-ZONDERTOUCH"] ],

]

#niveau 1
print(laptop_info[0],laptop_info[1][1],laptop_info[2][4][1])
#niveau 2
laptop_info[2][0] = laptop_info[2][0] + 2

#niveau 3
laptop_info.append(1)
laptop_info[3].append("campus")
print(laptop_info)