import sys, pygame 
import pandas, openpyxl, numpy 
from fuzzywuzzy import fuzz, process
        
class FuzzyEngine: 
    def __init__(self): 
        self.itemsDict = self.getItemsDict('/home/jean/Documents/textInput/filteredInventory.csv')
        self.itemsList = self.itemsDict.keys()
        
    def getItemsDict (self, inventoryPath):
        inventory = pandas.read_csv(inventoryPath, usecols=[2,3,4,5,6])

        itemsDict = {}
        
        for item in inventory.values: 
            itemDetails = numpy.ndarray.tolist(item)
            itemsDict[itemDetails[0]] = itemDetails[3]
            
        return itemsDict

    def search(self, keyword): 
        bruteSearch = process.extract(keyword, self.itemsList, limit=10)
        
        return self.filterSearch(bruteSearch)
    
    def filterSearch(self, bruteSearch):
        items = [] 
        
        for tup in bruteSearch: 
            items.append([tup[0], self.itemsDict[tup[0]]])
        
        return items

class Ui: 
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption('Catálogo de Preços')
        
        self.searchEngine = FuzzyEngine()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([400, 600]) 
        self.baseFont = pygame.font.Font(None, 32) 
        
        self.searchText = ''
        self.searchList = []
    
    def render(self): 
        self.screen.fill((2,132,132))
        
        self.renderSearchBox()
        self.renderSearchresults()
        
        pygame.display.flip()
        self.clock.tick(60)
    
    def renderSearchBox(self):
        textSurface = self.baseFont.render(self.searchText, True, (255,253,250)) 
        self.screen.blit(textSurface, (0,0))
        
    def handleEvents (self, events):
        for event in events: 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE: 
                    self.removeLastLetter()
                else:    
                    self.addsearchText(event.unicode)

                self.searchList = self.searchEngine.search(self.searchText)
            
    def addsearchText(self, text): 
        self.searchText += text
    
    def removeLastLetter(self): 
        self.searchText = self.searchText[0:-1]


GUI = Ui()


while True:
    GUI.handleEvents(pygame.event.get())
    GUI.render()
  