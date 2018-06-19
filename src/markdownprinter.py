from itemtype import ItemType

# Takes a definition and count of the given ItemType type and describes it using
# Markdown. Needs a path to the images folder in xwing-data
class MarkdownPrinter:

    artPath = ""
    shipArtPath = None

    def __init__(self, artPath, shipArtPath):
        self.artPath = artPath
        self.shipArtPath = shipArtPath

    # Constructs a Markdown representation of an item. The exact layout varies
    # depending on the item type
    def printItem(self, type, itemDefinition, count):
        if type == ItemType.SHIP:
            factions = ', '.join(itemDefinition["faction"])
            actions = ', '.join(itemDefinition["actions"])

            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
                '<img src="' + self.shipArtPath + '/ships/' + itemDefinition["xws"] + '.png" width="300px" />\n\n' +
                ' **Factions** ' + factions + '\n\n' +
                ' **Attack** ' + str(itemDefinition["attack"]) +
                ' **Agility** ' + str(itemDefinition["agility"]) +
                ' **Hull** ' + str(itemDefinition["hull"])  +
                ' **Shields** ' + str(itemDefinition["shields"]) + '\n\n' +
                ' **Actions** ' + actions + '\n'
            )

        if type == ItemType.PILOT:
            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
                '<img src="' + self.artPath + '/' + itemDefinition["image"] + '" width="240px" />\n'
            )

        if type == ItemType.UPGRADE:
            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
                '<img src="' + self.artPath + '/' + itemDefinition["image"] + '" width="240px" />\n'
            )

        return "MarkdownPrinter::printItem - unsupported item type " + str(type)
