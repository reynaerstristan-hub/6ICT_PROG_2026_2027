lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]
aparte_sommen = []
for index_hoofd, sublijst in enumerate(lijst):
    som = (sum(sublijst))
    aparte_sommen.append(som)
print(sum(aparte_sommen))

    
