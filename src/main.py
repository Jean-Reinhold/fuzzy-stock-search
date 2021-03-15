from getItemsDict import getItemsDict 
from fuzzywuzzy import fuzz, process
from printItems import printItems
import os 

itemsDict = getItemsDict('/home/jean/Documents/fuzzySearch/filteredInventory.csv')
itemsList = itemsDict.keys()

os.system("clear")

while True: 
    print("digite o nome do item:")
    matchItem = input(str()) 
    
    ratios = process.extract(matchItem, itemsList, limit=10)
    
    printItems(ratios, itemsDict)
    
    s = input(str())
    os.system("clear")