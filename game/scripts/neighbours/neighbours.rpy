label neighboursController:
    call lieseOptionsRemainingCheck
    call lotteOptionsRemainingCheck
    call neighboursOptionsRemainingCheck
    if optionsRemaining == 0:
        $ lastSpokenWith == ""
        return

    scene bg exterior02
    if liese.alreadyMet == False:
        "Vyjdeš ven před dům a pohled ti padne na dveře vedoucí do Heinrichovy dílny. Jsou vlastně dost na očích. Pokud jimi v noci prošel zloděj, je možné, že by si ho všiml někdo ze sousedů?"
    $ currentLocation = "victim street"

    menu:
        "{i}(Poptat se po okolních domech){/i}" if liese.alreadyMet == False:
            call lieseController
        "{i}(Zkusit ještě další domy){/i}" if liese.alreadyMet == True and lotte.alreadyMet == False:
            call lotteController
        "{i}(Vrátit se za Liese){/i}" if liese.alreadyMet == True and lastSpokenWith != "Liese" and lieseOptionsRemaining != 0:
            call lieseController
        "{i}(Vrátit se za Lotte){/i}" if lotte.alreadyMet == True and lastSpokenWith != "Lotte" and lotteOptionsRemaining != 0:
            call lotteController
        "{i}(Dojít za Eckhardem pro klíč od dílny){/i}" if "retrieving workshop key" in status and "carrying key" not in status and "too late for key" not in status:
            jump eckhardController
        "{i}(Vrátit se na strážnici){/i}":
            $ lastSpokenWith == ""
            return

    jump neighboursController

###

label neighboursOptionsRemainingCheck:
    $ optionsRemaining = 0
    if liese.alreadyMet == False:
        $ optionsRemaining += 1
    if liese.alreadyMet == True and lotte.alreadyMet == False:
        $ optionsRemaining += 1
    if liese.alreadyMet == True and lastSpokenWith != "Liese" and lieseOptionsRemaining != 0:
        $ optionsRemaining += 1
    if lotte.alreadyMet == True and lastSpokenWith != "Lotte" and lotteOptionsRemaining != 0:
        $ optionsRemaining += 1
    return
