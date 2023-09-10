init python:
    class Person(object):
        def __init__(self, name, code, imageParameter = "", reputation = 0, trust = 0, pressure = 0, status = ""):
            self.char = Character(name)
            self.name = name
            self.code = code
            self.imageParameter = imageParameter
            self.reputation = reputation
            self.trust = trust
            self.pressure = pressure
            self.relationships = {}
            self.alreadyMet = False
            self.cluesAgainst = 0
            self.asked = []
            self.arrestReason = []
            self.status = []
            self.status.append(status)

        def say(self, input, mood = ""):
            if self.code == "mcPic":
                if self.imageParameter == "beaten":
                    image = "mcPicBeaten"
                else:
                    image = "mcPic"
            else:
                image = "npc " + self.code
                if self.imageParameter != "" and renpy.can_show(image + " " + self.imageParameter):
                    image += " " + self.imageParameter
                if mood != "" and renpy.can_show(image + " " + mood):
                    image += " " + mood

            renpy.show(image, [center])
            renpy.say(self.char, input)
            renpy.hide(image)

        def rename(self, newName):
            self.name = newName
            self.char = Character(newName)
