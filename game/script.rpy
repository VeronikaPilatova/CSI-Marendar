init python:
    import copy

    class Location(object):
        def __init__(self, name, code):
            self.name = name
            self.code = code
            self.checked = []


    class Note(object):
        def __init__(self, person, x, y, isActive = False):
            self.name = person.name
            self.x = x
            self.y = y
            self.code = person.code
            self.isActive = isActive
        @property
        def buttonImage(self):
            icon = "evidencewall/button " + self.code + ".png"
            return(icon)


    class Event(object):
        def __init__(self, when, code, priority = 2, status = "", checkAfter = 0, checkReason = ""):
            self.when = when
            self.code = code
            self.priority = priority
            self.status = status
            self.checkAfter = checkAfter
            self.checkReason = checkReason


transform center:
    xalign 0.5
    yalign 0.5

transform menuImage:
    xalign 0.5
    yalign 0.2

transform signature:
    xpos 1200
    ypos 800
    xanchor 1.0
    yanchor 0.0

transform sealedParchmentName:
    xpos 800
    ypos 310



label start:
    $ _quit_slot = "quitsave"

    call preparation
    call prepareInterludes
    #call evidenceWall

    # game scripts
    $ persistent.menuOption = "intro"

    call charCreation

    $ persistent.gameProgress = "case in progress"

    call intro # intro + first chosen location
    call guardhouseFirst

    "DEBUG: This is the end for now."
    return

label thrownOut:
    if not achievement.has(achievement_name['fired'].name):
        $ Achievement.add(achievement_name['fired'])
    $ persistent.menuOption = "bad ending"
    $ persistent.gameProgress = "case failed"
    $ renpy.save_persistent()
    $ MainMenu(confirm=False)()
    return

label end:
    $ renpy.unlink_save("quitsave")
    $ _quit_slot = None
    return

###

label preparation:
    default persistent.gameProgress = "new"
    default persistent.menuOption = "intro"

    $ time = Calendar(0, 13)

    default dayOfCrime = "včera"
    default investigationStart = "dnes"
    default festivalStart = "za čtyři dny"

    # characters - watch
    default hayfa = Person("Hayfa", "hayfa")
    default rauvin = Person("Rauvin", "rauvin")
    default runa = Person("Runa", "runa")
    default solian = Person("Solian", "solian")
    default melien = Person("Melien", "melien")
    # characters - case 1
    default ada = Person("Ada", "ada")
    default eckhard = Person("Eckhard", "eckhard", "hungover")
    default erle = Person("Žebračka Erle", "erle")
    default gerd = Person("Gerd", "gerd")
    default kaspar = Person("Mistr Kaspar", "kaspar")
    default laris = Person("Laris", "laris")
    default liese = Person("Liese", "liese")
    default lisbeth = Person("Lisbeth", "lisbeth")
    default lotte = Person("Lotte", "lotte")
    default merchant = Person("Karsten", "merchant")
    default nirevia = Person("Nirevia", "nirevia")
    default njal = Person("Mistr Njal", "njal")
    default optimist = Person("Ferdi", "apprentice1", "hungover")
    default rovien = Person("Rovien", "rovien")
    default rumelin = Person("Cechmistr Rumelin", "rumelin")
    default sabri = Person("Sabri", "sabri")
    default salma = Person("Hostinská Salma", "salma")
    default son = Person("Aachim", "son", "hungover")
    default victim = Person("Mistr Heinrich", "victim")
    default yesman = Person("Rudi", "apprentice2", "hungover")
    default zairis = Person("Zairis", "zairis")
    default zeran = Person("Zeran", "zeran")
    # characters - other
    default angryWoman = Person("Žena", "angry woman")
    default assistant = Person("Pomocník v knihovně", "assistant")
    default racist = Person("Obchodník", "angry merchant")
    default katrin = Person("Tanečnice", "katrin")
    default kilian = Person("Hráč na lyru", "kilian")
    default anon1 = Person("Měšťan", "anon1")
    default anon2 = Person("Mešťan", "anon2")
    default anon3 = Person("Měšťanka", "anon3")
    default locksmith = Person("Zámečník", "locksmith")

    # character initial relationships
    $ lisbeth.relationships["victim"] = 2
    $ lisbeth.relationships["kaspar"] = 5
    $ victim.relationships["lisbeth"] = 5

    # evidence wall notes
    default seeMeNote = False
    default apprentice1Note = Note(optimist, 1335, 240, False)
    default apprentice2Note = Note(yesman, 1300, 425, False)
    default erleNote = Note(erle, 250, 700, False)
    default kasparNote = Note(kaspar, 640, 55, False)
    default adaNote = Note(ada, 1160, 80, False)
    default eckhardNote = Note(eckhard, 1020, 750, False)
    default gerdNote = Note(gerd, 1550, 600, False)
    default rumelinNote = Note(rumelin, 320, 180, True)
    default rovienNote = Note(rovien, 200, 400, False)
    default zairisNote = Note(zairis, 30, 480, False)
    default nireviaNote = Note(nirevia, 150, 120, False)
    default njalNote = Note(njal, 1710, 720, False)
    default lotteNote = Note(lotte, 500, 500, False)
    default merchantNote = Note(merchant, 500, 500, False)
    default pub = Location("Hospoda U Salmy", "pub")
    default pubNote = Note(pub, 700, 650, True)
    default sonNote = Note(son, 1140, 290, False)
    default victimNote = Note(victim, 850, 300, True)
    default lisbethNote = Note(lisbeth, 1000, 150, False)
    default workshop = Location("Heinrichova dílna", "workshop")
    default workshopNote = Note(workshop, 970, 400, True)
    default zeranNote = Note(zeran, 1650, 60, False)
    default sabriNote = Note(sabri, 1730, 270, False)
    default library = Location("Knihovna", "library")
    default libraryNote = Note(library, 1250, 750, False)
    default notes = [workshopNote, apprentice1Note, apprentice2Note, erleNote, kasparNote, adaNote, gerdNote, zeranNote, eckhardNote, rumelinNote, rovienNote, zairisNote, nireviaNote, njalNote, lotteNote, merchantNote, pubNote, sonNote, victimNote, lisbethNote, sabriNote, libraryNote]

    # variables - mc
    default race = "" # human / elf / hobbit / dwarf
    default gender = "" # M / F
    default origin = "" # born here / family / newcomer
    default reasons = "" # altruist / order / personal
    default skill =  "" # combat / observation / diplomacy
    default personality = []
    default cultistMaterial = 0

    # variables - gender distinction
    default a = "/a" # additional letter for female
    default e = "/e" # additional letter for female
    default y = "ý/á" # gendering some adjectives
    default pronoun3 = "mu/jí" # personal pronoun, 3rd case
    default pronoun4 = "ho/ji" # personal pronoun, 4th case
    default pronoun7 = "ním/ní" # personal pronoun, 7th case
    default pronounPossessive = "jeho/její" # personal pronoun, possessive
    default sel = "šel/šla"
    default sam = "sám/sama"

    # variables - guardhouse and watch
    default watchScores = {}
    $ watchScores["rauvin"] = 0
    $ watchScores["hayfa"] = 0
    $ watchScores["solian"] = 0
    $ guardhouseIntros = []
    $ guardhouseIntros.append("Rauvin sedí u stolu a prochází nějaké papíry, ale když se přiblížíš, zvedne hlavu a otočí se na tebe.")
    $ guardhouseIntros.append("V místnosti téměř nikdo není, jen Hayfa právě něco probírá s Rauvinem a jeden z hlídkařů u stolu sepisuje cosi o clech.")
    # variables - investigation progress
    default clues = []
    default globalClues = []
    default status = []
    default dailyStatus = []
    default globalStatus = []
    default cluesReported = []
    default boysAsked = []
    default colleaguesAsked = []
    default mcAsked = []
    default evidenceWallCount = 0
    default newlyArrested = []
    default allArrested = []
    default cells = []
    default gerdInWorkshopDiscovered = False
    # variables - gameplay helpers
    call libraryPreparation
    default chosenChar = ""
    default heinrichHouseholdSpokenWith = []
    default chosenTopic = ""
    default readingTopic = ""
    default currentLocation = ""
    default lastSpokenWith = ""
    default refusedBy = ""
    default leaveOption = "normal"
    default visitGuardhouseReminder = ""
    default njalOptionsRemaining = 1
    default gerdOptionsRemaining = 1
    default adaAngry = False
    default timeOfDay = "day"
    # variables - achievement helpers
    default persistent.zeranArrestReasons = []
    default persistent.arrestedPeople = []
    # variables - time constants
    default keySlightlyLateAfter = Calendar(20, 17)
    default keyVeryLateAfter = Calendar(30, 18)
