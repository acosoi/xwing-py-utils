import json

from itemtype import ItemType
from markdownprinter import MarkdownPrinter

class Inventory:

    ###########
    # Members #
    ###########

    # A map of all known purchasable items, indexed by ID
    purchaseDefinitions = {}

    # A map of all known items, indexed by ItemType and then ID
    itemDefinitions = {}

    # A map of items in the inventory, indexed by ItemType and then ID
    items = {}

    ###########
    # Methods #
    ###########

    # Adds a list of purchaseable items to the list of purchase definitions
    def addPurchaseDefinitions(self, definitions):
        for definition in definitions:
            self.addPurchaseDefinition(definition)

    # Adds a purchasable item to the list of purchase definitions
    def addPurchaseDefinition(self, definition):
        self.purchaseDefinitions[int(definition["id"])] = definition

    # Adds a list of items to the list of item definitions
    def addItemDefinitions(self, type, definitions):
        for definition in definitions:
            self.addItemDefinition(type, definition)

    # Adds a new item to the list of item definitions
    def addItemDefinition(self, type, definition):
        if type not in self.itemDefinitions:
            self.itemDefinitions[type] = {}

        self.itemDefinitions[type][int(definition["id"])] = definition

    # Retrieves the specified item definition
    def getItemDefinition(self, type, id):
        return self.itemDefinitions[type][int(id)]

    # Adds all of the items bundled in the purchase to the inventory
    def addPurchase(self, purchase):
        contents = self.purchaseDefinitions[int(purchase["id"])]["contents"]

        # add items from the purchase to the inventory
        self._addItemsFromPurchase(ItemType.SHIP, contents["ships"])
        self._addItemsFromPurchase(ItemType.PILOT, contents["pilots"])
        self._addItemsFromPurchase(ItemType.UPGRADE, contents["upgrades"])
        self._addItemsFromPurchase(ItemType.REFERENCE_CARD, contents["reference-cards"])

    # Calls addItem for all items in the given list
    def _addItemsFromPurchase(self, type, items):
        for item in items:
            self.addItem(type, item, items[item])

    # Add a single item (ship, upgrade, pilot) to the inventory
    def addItem(self, type, item, count):
        if type not in self.items:
            self.items[type] = {}

        if item not in self.items[type]:
            self.items[type][item] = count
        else:
            self.items[type][item] += count

    # Retrieves all owned items of that type, along with their counts
    def getItemsByType(self, type):
        return self.items[type]

# Go through every item of the specified type and get a Markdown representation
# for each, using MarkdownPrinter
def printItemsList(itemType, inventory):
    printer = MarkdownPrinter('../xwing-data/images')
    output = ""

    items = inventory.getItemsByType(itemType)

    for item in items:
        definition = inventory.getItemDefinition(itemType, item)
        output += printer.printItem(itemType, definition, items[item]) + '\n'

    return output

# When running this script, load up the contents of purchases.js, construct the
# inventory and output inventory.md (a Markdown document with all of the items
# in our collection).
if __name__ == "__main__":

    inv = Inventory()

    # Replace this path with your path to the xwing-data repository
    dataDirectory = '../xwing-data/data/'

    # Read all definitions (that are useful, don't include items such as
    # damage cards or conditions)
    inv.addPurchaseDefinitions(json.load(open(dataDirectory + 'sources.js')))
    inv.addItemDefinitions(ItemType.SHIP, json.load(open(dataDirectory + 'ships.js')))
    inv.addItemDefinitions(ItemType.PILOT, json.load(open(dataDirectory + 'pilots.js')))
    inv.addItemDefinitions(ItemType.UPGRADE, json.load(open(dataDirectory + 'upgrades.js')))
    inv.addItemDefinitions(ItemType.REFERENCE_CARD, json.load(open(dataDirectory + 'reference-cards.js')))

    # Load the purchases JSON
    purchases = json.load(open('purchases.js'))

    # Process each purchase from the loaded JSON
    for purchase in purchases:
        inv.addPurchase(purchase)

    # Print out the entire inventory with Markdown syntax
    output = "# Ships\n\n"
    output += printItemsList(ItemType.SHIP, inv)
    output += "\n\n# Pilots\n\n"
    output += printItemsList(ItemType.PILOT, inv)
    output += "\n\n# Upgrades\n\n"
    output += printItemsList(ItemType.UPGRADE, inv)
    with open("output.md", "w") as outputFile:
        outputFile.write(output)
