import pandas 
import openpyxl
import numpy 

def getItemsDict (inventoryPath):
    inventory = pandas.read_csv(inventoryPath, usecols=[2,3,4,5,6])

    itemsDict = {}
    
    for item in inventory.values: 
        itemDetails = numpy.ndarray.tolist(item)
        itemsDict[itemDetails[0]] = itemDetails[2]
    
    return itemsDict

