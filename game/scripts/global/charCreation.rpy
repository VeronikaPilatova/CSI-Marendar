label charCreation:
play music "audio/music/adventure awaits.mp3" fadeout 0.5 if_changed
scene bg intro
show bg intro dark with dissolve

label race:
    if race == "":
        "Tohle může být v Marendaru citlivá otázka, ale... jaké jsi rasy?"
    else:
        "Jaké jsi rasy?"
    menu:
        "Člověk":
            $ race = "human"
        "Elf":
            $ race = "elf"
        "Hobit":
            $ race = "hobbit"
        "Trpaslík":
            $ race = "dwarf"
    if gender != "":
        jump looks
    else:
        jump gender

label gender:
    if gender == "":
        "A co tvoje pohlaví?"
    else:
        "Jaké je tvoje pohlaví?"
    menu:
        "Muž":
            $ gender = "M"
            $ a = ""
            $ e = ""
            $ y = "ý"
            $ pronoun3 = "mu"
            $ pronoun4 = "ho"
            $ pronoun7 = "ním"
            $ sel = "šel"
            $ sam = "sám"
            $ pronounPossessive = "jeho"
        "Žena":
            $ gender = "F"
            $ a = "a"
            $ e = "e"
            $ y = "á"
            $ pronoun3 = "jí"
            $ pronoun4 = "ji"
            $ pronoun7 = "ní"
            $ sel = "šla"
            $ sam = "sama"
            $ pronounPossessive = "její"

$ pic = 1
label looks:
show expression ("mc/char [race][gender][pic].png") at menuImage
menu:
    "Tohle jsem já!":
        hide expression ("mc/char [race][gender][pic].png")
        image mcPic = ("mc/char [race][gender][pic].png")
        image mcPicBeaten = ("mc/char [race][gender][pic] beaten.png")
    "Další obrázek":
        hide expression ("mc/char [race][gender][pic].png")
        if pic < 5:
            $ pic += 1
        else:
            $ pic = 1
        jump looks
    "Změnit rasu":
        hide expression ("mc/char [race][gender][pic].png")
        jump race
    "Změnit pohlaví":
        hide expression ("mc/char [race][gender][pic].png")
        jump gender

label naming:
$ mcName = renpy.input("Jak se jmenuješ?", length=25, exclude="0123456789+=,.?!<>").strip()
if mcName == "":
    "Jak se jmenuješ?"
    jump naming

label calling:
$ callingMc = renpy.input("Jak ti máme říkat? (5. pád jména)")
if callingMc == "":
    "Jak ti máme říkat? (5. pád jména)"
    jump calling

$ mc = Person(mcName, "mcPic")
return
