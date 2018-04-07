from itemtype import ItemType

# Takes a definition and count of the given ItemType type and describes it using
# Markdown. Needs a path to the images folder in xwing-data
class MarkdownPrinter:

    artPath = ""

    def __init__(self, path):
        self.artPath = path

    # Constructs a Markdown representation of an item. The exact layout varies
    # depending on the item type
    def printItem(self, type, itemDefinition, count):
        if type == ItemType.SHIP:
            factions = ', '.join(itemDefinition["faction"])
            actions = ', '.join(itemDefinition["actions"])

            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
               '* Factions: ' + factions + '\n' +
               '* Attack: ' + str(itemDefinition["attack"]) + '\n' +
               '* Agility: ' + str(itemDefinition["agility"]) + '\n' +
               '* Hull: ' + str(itemDefinition["hull"]) + '\n' +
               '* Shields: ' + str(itemDefinition["shields"]) + '\n' +
               '* Actions: ' + actions + '\n'
            )

        if type == ItemType.PILOT:
            slots = ', '.join(itemDefinition["slots"])

            unique = "false"
            if "unique" in itemDefinition:
                unique = itemDefinition["unique"]

            text = "-"
            if "text" in itemDefinition:
                text = itemDefinition["text"]

            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
                '![](' + self.artPath + '/' + itemDefinition["image"] + ')\n'
                '* Unique: ' + str(unique) + '\n' +
                '* Ship: ' + str(itemDefinition["ship"]) + '\n' +
                '* Skill: ' + str(itemDefinition["skill"]) + '\n' +
                '* Points: ' + str(itemDefinition["points"]) + '\n' +
                '* Slots: ' + slots + '\n' +
                '* Text: ' + text + '\n' +
                '* Faction: ' + str(itemDefinition["faction"]) + '\n'
            )

        if type == ItemType.UPGRADE:
            unique = "false"
            if "unique" in itemDefinition:
                unique = itemDefinition["unique"]

            attack = "-"
            if "attack" in itemDefinition:
                attack = itemDefinition["attack"]

            rangeStr = "-"
            if "range" in itemDefinition:
                rangeStr = itemDefinition["range"]

            return (
                '### ' + itemDefinition["name"] + ' x ' + str(count) + '\n' +
                '![](' + self.artPath + '/' + itemDefinition["image"] + ')\n'
                '* Slot: ' + str(itemDefinition["slot"]) + '\n' +
                '* Unique: ' + str(unique) + '\n' +
                '* Points: ' + str(itemDefinition["points"]) + '\n' +
                '* Attack: ' + str(attack) + '\n' +
                '* Range: ' + str(rangeStr) + '\n' +
                '* Text: ' + str(itemDefinition["text"]) + '\n'
            )

        return "MarkdownPrinter::printItem - unsupported item type " + str(type)
