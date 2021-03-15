def getFilteredCsv (csvAsString): 
    unfilteredSubStrings = csvAsString.split(sep=",")  
    return [x for x in unfilteredSubStrings if x != ""]
    


with open("/home/jean/Documents/fuzzySearch/inventory.csv", "r") as inventory: 
    filteredCsv = getFilteredCsv(inventory.read()) 
    inventory.close()

filteredCsv = ",".join(filteredCsv)    
    
with open("/home/jean/Documents/fuzzySearch/filteredInventory.csv", "w") as inventory: 
    inventory.writelines(filteredCsv)
    