def printItems (ratios, itemsDict): 
    for ratio in ratios: 
        print("{}  ----------------  Valor: {}".format(ratio[0], itemsDict[ratio[0]]))