label njalHouseController:
    # check if visit makes sense
    if "njal house visited" not in status:
        pass
    elif chosenChar == "njal":
        call njalOptionsRemainingCheck
        if njalOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se mistra Njala ještě ptát."
            return
    elif chosenChar == "gerd":
        call gerdOptionsRemainingCheck
        if gerdOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se Gerda ještě ptát."
            return
    call preludeController

    # walk over
    if currentLocation != "njal house" or currentLocation != "njal house inside":
        if "njal house visited" not in status:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        $ currentLocation = "njal house"

    # visit itself
    if gerd in cells and chosenChar == "gerd":
        jump gerdController
    elif njal in cells and chosenChar == "njal":
        jump njalController
    else:
        play music audio.njal fadeout 0.5 if_changed
        scene bg njal outside
        if "njal house visited" not in status:
            call njalHouseFirst
        else:
            call njalHouseAgain

    # adjust status
    $ njalNote.isActive = True
    $ gerdNote.isActive = True
    if "njal house visited" not in status:
        $ status.append("njal house visited")
    stop music fadeout 0.5
    return

label njalHouseFirst:
    if time.hours < 18:
        "Po chvíli hledání se zastavíš před menším kamenným domem, ze kterého je otevřeným oknem slyšet spokojené pohvizdování. Před domem sedí na ševcovské trojnožce asi čtrnáctiletý kluk, plně zabraný do šití elegantně tvarované boty."
        $ mc.say("Bydlí tady mistr Njal?")
        "Kluk zvedne hlavu od práce."
    else:
        "Po chvíli hledání se zastavíš před menším kamenným domem. Okno je otevřené a když se zastavíš přede dveřmi, dolétne k tobě tlumený zvuk smíchu."
        "Zaklepeš a otevře ti asi čtrnáctiletý kluk."
        $ mc.say("Bydlí tady mistr Njal?")
    $ gerd.say("Jo, jste tu správně. Co potřebujete?")

    call gerdOptionsRemainingCheck
    menu:
        "Mluvit s ním. Můžeš ho místo těch otázek rovnou zavolat?":
            $ hayfa.trust -= 1
            $ gerd.trust -= 1
            "Kluk chvíli vypadá, že by měl chuť odmlouvat, ale pak si to zřejmě rozmyslí."
            $ gerd.say("Můžu.")
            "Kluk zmizí v domě a za pár minut přivede trpaslíka s šedivějícími tmavými vlasy a vráskami od smíchu v obličeji. Na tebe se ale trpaslík dívá spíš chladně."
            $ njal.say("Potřebujete něco?")
            $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v dílně mistra Heinricha. Můžu vám položit několik otázek?")
            "Mistr Njal pozvedne obočí a chvíli si tě prohlíží. Pak ti rukou naznačí, že máš jít za ním."
            $ njal.say("Pojďte dál, pokusím se vám odpovědět, na co budu moci.")
            call njalHouseInside
            jump njalController
        "Jsem z městské hlídky a vyšetřuji krádež u mistra Heinricha. Rád[a] bych mistrovi položil[a] několik otázek.":
            jump speakToNjal
        "Ty jsi Gerd?" if "fired apprentices" in clues:
            $ gerd.say("Jo. Proč se ptáte?")
            jump gerdController
        "Ty jsi učedník mistra Njala?" if gerdNote.isActive == False and gerdOptionsRemaining > 0:
            $ gerd.say("Jo. Proč se ptáte?")
            jump gerdController

label speakToNjal:
    $ gerd.say("Dojdu mu to říct.")
    "Kluk zmizí v domě, ale za pár minut je zpátky a podrží ti dveře."
    $ gerd.say("Mistr říkal, že máte jít rovnou dál.")
    call njalHouseInside
    jump njalController

label njalHouseAgain:
    if gerd in cells:
        "Před domem tentokrát nikoho nepotkáš a ani neslyšíš žádné zvuky zevnitř. Když ale zabušíš na dveře, ozve se brzy zaskřípění pantů a před tebou se objeví mistr Njal."
        jump njalController
    elif njal in cells:
        "Před domem tentokrát nikoho nepotkáš a dům je tichý. Zabušíš na dveře a po chvíli ti otevře Gerd a ostražitě si tě změří."
        jump gerdController
    elif time.hours < 18:
        "Dům mistra Njala vypadá stejně, jako když jsi tu byl[a] poprvé. Učedník Gerd sedí na trojnožce před domem a napíná na kopyto připravený základ budoucí boty. Z domu je slyšet tlumené prozpěvování, ale konkrétní slova se ti nedaří zachytit."
        "Gerd zvedne hlavu od práce."
    else:
        "Dům mistra Njala vypadá stejně příjemně, jako když jsi tu byl[a] poprvé. Okno je stále otevřené, a když se zastavíš přede dveřmi, dolétne k tobě tlumený zvuk smíchu."
        "Zaklepeš a otevře ti Njalův učedník Gerd se svým typickým bezstarostným úsměvem."
    $ gerd.say("Potřebujete ještě něco?")
    if chosenChar == "gerd":
        if gerd.alreadyMet == False:
            $ mc.say("Vlastně bych si chtěl[a] promluvit s tebou.")
            $ gerd.say("Se mnou? Proč vlastně?")
        jump gerdController
    elif chosenChar == "njal":
        if njal.alreadyMet == True:
            $ mc.say("Chtěl[a] bych ještě jednou mluvit s tvým mistrem.")
            "Gerd kývne a na chvíli zmizí v domě. Netrvá dlouho a jsi zase pozván dovnitř."
            call njalHouseInside
            jump njalController
        else:
            $ mc.say("Chtěl[a] bych si promluvit s tvým mistrem.")
            "Gerd kývne a na chvíli zmizí v domě. Netrvá dlouho a jsi pozvána dovnitř."
            call njalHouseInside
            jump njalController

label njalHouseInside:
    scene bg njal inside
    if "njal house visited" not in status:
        "Dům má i uvnitř neomítnuté stěny a i přes zapálené svíčky je dost tmavý, přesto ale působí útulně. V jednom rohu stojí ševcovská trojnožka a stolek s rozdělanou prací."
        $ status.append("njal house visited")
        $ currentLocation = "njal house inside"
    return

###
