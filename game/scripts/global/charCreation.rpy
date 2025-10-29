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
        "A jaký používáš rod?"
    else:
        "Jaký používáš rod?"
    menu:
        "Mužský":
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
        "Ženský":
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
$ picGender = gender
$ lastPicGender = gender
label looks:
show expression ("mc/char [race][picGender][pic].png") at menuImage
menu:
    "Tohle jsem já!":
        hide expression ("mc/char [race][picGender][pic].png")
        image mcPic = ("mc/char [race][picGender][pic].png")
        image mcPicBeaten = ("mc/char [race][picGender][pic] beaten.png")
    "Další obrázek":
        hide expression ("mc/char [race][picGender][pic].png")
        if pic < 5:
            $ pic += 1
        # elif pic < 7:
        #     $ pic += 1
        #     if picGender != "U":
        #         $ lastPicGender = picGender
        #         $ picGender = "U"
        else:
            $ pic = 1
            $ picGender = lastPicGender
        jump looks
    "Mužské obrázky" if picGender == "F" or (picGender == "U" and lastPicGender == "F"):
        $ lastPicGender = picGender
        $ picGender = "M"
        jump looks
    "Ženské obrázky" if picGender == "M" or (picGender == "U" and lastPicGender == "M"):
        $ lastPicGender = picGender
        $ picGender = "F"
        jump looks
    "Změnit rasu":
        hide expression ("mc/char [race][picGender][pic].png")
        jump race
    "Změnit pohlaví":
        hide expression ("mc/char [race][picGender][pic].png")
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
