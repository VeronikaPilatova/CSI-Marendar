label victimHouseholdController:
    # check if visit makes sense
    if lisbethNote.isActive == False:
        pass
    elif chosenChar == "workshop":
        call workshopOptionsRemainingCheck
        if workshopOptionsRemaining == 0:
            "Nenapadá tě, co dalšího v dílně mistra Heinricha ještě prohlížet."
            return
    elif chosenChar == "victim":
        call victimOptionsRemainingCheck
        if "carrying key" not in status and victimOptionsRemaining == 0:
            "Nenapadá tě, na co dalšího se mistra Heinricha ještě ptát."
            return
    elif chosenChar == "lisbeth":
        call lisbethOptionsRemainingCheck
        if lisbethOptionsRemaining == 0:
            "Nenapadá tě, na co dalšího se Lisbeth ještě ptát."
            return
    elif chosenChar == "son":
        call boysOptionsRemainingCheck
        call aachimAloneOptionsRemainingCheck
        if boysOptionsRemaining == 0 and aachimOptionsRemaining == 0:
            "Nenapadá tě, na co dalšího se Aachima ještě ptát."
            return
    elif chosenChar == "ada":
        call adaOptionsRemainingCheck
        if adaOptionsRemaining == 0:
            "Nenapadá tě, na co dalšího se Ady ještě ptát."
            return
    elif chosenChar == "apprentice1" or chosenChar == "apprentice2":
        call boysOptionsRemainingCheck
        if boysOptionsRemaining == 0:
            "Nenapadá tě, na co dalšího se učedníků ještě ptát."
            return
    if chosenChar != "eckhard":
        call preludeController

    # walk over
    if currentLocation != "victim house" and currentLocation != "workshop":
        if "victim house visited" not in status:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
    $ currentLocation = "victim house"

    # visit itself
    $ lastSpokenWith = ""
    $ refusedBy = ""
    call victimHouseIntro

    # adjust time and status
    if "victim house visited" not in status:
        $ status.append("victim house visited")
    $ lisbethNote.isActive = True
    call neighboursController
    $ refusedBy = ""
    if "kaspar and lisbeth ratted out" in status and kaspar.imageParameter != "beaten":
        $ kaspar.imageParameter = "beaten"
        $ lisbeth.imageParameter = "beaten"
    stop music fadeout 0.5
    return

label victimHouseIntro:
    play music audio.heinrich fadeout 0.5 if_changed
    scene bg heinrich outside
    if "victim house visited" not in status:
        "Dům mistra Heinricha najdeš snadno. Je to jeden z nejvýstavnějších v ulici a přiléhá k němu prostorná dílna."
        "Zaklepeš na dveře a otevře ti upravená žena s milým úsměvem."
        $ lisbeth.say("Dobrý den, potřebujete něco?")
        $ mc.say("Jsem %(mcName)s z městské hlídky a vyšetřuji krádež výrobku mistra Heinricha.")
        $ lisbeth.say("Já jsem Lisbeth, jeho žena. Můžu vám nějak pomoct?")
    else:
        "Cestu k domu mistra Heinricha už znáš, a tak ani nemusíš přemýšlet, který z výstavních domů v ulici je ten správný."
        if lisbethNote.isActive == False:
            "Zaklepeš na dveře a otevře ti upravená žena s milým úsměvem."
        elif "fresh flowers" in status:
            "U vchodu tě zase přivítá paní domu s úsměvem, který je v něčem vřelejší a upřímnější než obvykle. Uvnitř si všimneš čerstvých květin ve váze."
            $ lisbeth.say("Vítejte, zrovna peču jablečný závin. Co pro vás můžu udělat?")
            $ status.remove("fresh flowers")
            $ status.append("flowers")
            if not achievement.has(achievement_name['flowers'].name):
                $ Achievement.add(achievement_name['flowers'])
        else:
            $ lisbeth.say("Dobrý den… aha, vy jste ten strážný, co hledá manželův výrobek. Můžu vám nějak pomoct?")
    if lisbethNote.isActive == False:
        call victimHouseholdOptions
    elif chosenChar == "workshop":
        if "workshop visited" in status and gender == "M":
            $ mc.say("Mohl bych se ještě jednou podívat do dílny?")
        elif "workshop visited" in status and gender == "F":
            $ mc.say("Mohla bych se ještě jednou podívat do dílny?")
        elif gender == "M":
            $ mc.say("Mohl bych se podívat do dílny?")
        else:
            $ mc.say("Mohla bych sepodívat do dílny?")
        jump workshopIntro
    elif chosenChar == "victim":
        if gender == "M":
            $ mc.say("Rád bych ještě jednou mluvil s vaším mužem.")
        else:
            $ mc.say("Ráda bych ještě jednou mluvila s vaším mužem.")
        jump victimMain
    elif chosenChar == "lisbeth":
        $ mc.say("Můžu vám položit pár otázek?")
        jump lisbethMain
    elif chosenChar == "son":
        $ mc.say("Můžu mluvit s vaším synem?")
        jump sonIntro
    elif chosenChar == "ada":
        $ mc.say("Můžu mluvit s vaší dcerou?")
        jump adaMain
    elif chosenChar == "apprentice1" or chosenChar == "apprentice2":
        if "gender" == "M":
            $ mc.say("Chtěl bych si promluvit s učedníky.")
        else:
            $ mc.say("Chtěla bych si promluvit s učedníky.")
        jump apprenticesIntro
    elif "carrying key" in status:
        $ mc.say("Nesu vašemu muži klíč od jeho dílny.")
        if gender == "M":
            $ lisbeth.say("To jste hodný. Dojdu pro něj, pojďte zatím dál.", "happy")
        else:
            $ lisbeth.say("To jste hodná. Dojdu pro něj, pojďte zatím dál.", "happy")
        call victimHouseInterior
        jump returningKey
    else:
        call victimHouseholdOptions
    return

label victimHouseInterior:
    if "fresh flowers" in status or "flowers" in status:
        scene bg heinrich flowers
    else:
        scene bg heinrich inside
    return

label victimHouseholdOptions:
    call victimOptionsRemainingCheck
    call lisbethOptionsRemainingCheck
    call boysOptionsRemainingCheck
    call aachimAloneOptionsRemainingCheck
    call adaOptionsRemainingCheck
    call workshopOptionsRemainingCheck

    show mcPic at menuImage
    menu:
        "Nesu vašemu muži klíč od jeho dílny." if "carrying key" in status and lastSpokenWith == "":
            hide mcPic
            if gender == "M":
                $ lisbeth.say("To jste hodný. Dojdu pro něj, pojďte zatím dál.", "happy")
            else:
                $ lisbeth.say("To jste hodná. Dojdu pro něj, pojďte zatím dál.", "happy")
            call victimHouseInterior
            jump returningKey
        "Rád bych ještě jednou mluvil s vaším mužem." if victimOptionsRemaining != 0 and lastSpokenWith != "victim" and gender == "M":
            hide mcPic
            if refusedBy == "victim":
                $ lisbeth.say("Nevím, co jste si předtím řekli, ale možná bych to na vašem místě radši nedělala. Zkuste přijít později, až Heinricha přejde vztek.")
                jump victimHouseholdOptions
            else:
                jump victimMain
        "Ráda bych ještě jednou mluvila s vaším mužem." if victimOptionsRemaining != 0 and lastSpokenWith != "victim" and gender == "F":
            hide mcPic
            if refusedBy == "victim":
                $ lisbeth.say("Nevím, co jste si předtím řekli, ale možná bych to na vašem místě radši nedělala. Zkuste přijít později, až Heinricha přejde vztek.")
                jump victimHouseholdOptions
            else:
                jump victimMain
        "Můžu vám položit pár otázek?" if lisbethOptionsRemaining != 0 and lastSpokenWith != "lisbeth":
            hide mcPic
            jump lisbethMain
        "Chtěl bych si promluvit s učedníky." if boysOptionsRemaining != 0 and (apprentice1Note.isActive == True or apprentice2Note.isActive == True) and lastSpokenWith != "boys" and gender == "M":
            hide mcPic
            jump apprenticesIntro
        "Chtěla bych si promluvit s učedníky." if boysOptionsRemaining != 0 and (apprentice1Note.isActive == True or apprentice2Note.isActive == True) and lastSpokenWith != "boys" and gender == "F":
            hide mcPic
            jump apprenticesIntro
        "Můžu mluvit s vaším synem?" if boysOptionsRemaining != 0 and aachimOptionsRemaining != 0 and sonNote.isActive == True and aachim not in cells and lastSpokenWith != "boys" and lastSpokenWith != "aachim":
            hide mcPic
            jump sonIntro
        "Můžu mluvit s vaší dcerou?" if adaOptionsRemaining != 0 and adaNote.isActive == True and lastSpokenWith != "ada":
            hide mcPic
            jump adaMain
        "Bylo by možné podívat se ještě jednou do dílny?" if workshopOptionsRemaining != 0 and lastSpokenWith != "workshop" and "workshop visited" in status:
            hide mcPic
            jump workshopIntro
        "Bylo by možné podívat se do dílny?" if workshopOptionsRemaining != 0 and lastSpokenWith != "workshop" and "workshop visited" not in status:
            hide mcPic
            jump workshopIntro
        "Nebudu vás už zdržovat." if lastSpokenWith != "":
            hide mcPic
            $ lisbeth.say("Na shledanou a hodně štěstí.")
            return
    return

label sonIntro:
    if lastSpokenWith == "":
        $ lisbeth.say("Bude myslím někde s učedníky. Zatím pojďte dál, zavolám vám ho.")
        call victimHouseInterior
    else:
        $ lisbeth.say("Bude myslím někde s učedníky, zavolám vám ho.")
    if "boys met" not in status:
        if time.days == 1:
            "Paní Lisbeth odejde a za krátký okamžik přivede hned tři chlapce, kteří se drží u sebe. Všichni vypadají dost unaveně a vystresovaně."
        else:
            "Paní Lisbeth odejde a za krátký okamžik přivede hned tři chlapce, kteří se drží u sebe."
    else:
        "Paní Lisbeth přivede Aachima a spolu s ním i dva učedníky."
    jump boysMain
    return

label apprenticesIntro:
    if lastSpokenWith == "":
        $ lisbeth.say("Zatím pojďte dál a já vám je zavolám.")
        call victimHouseInterior
    else:
        $ lisbeth.say("Zavolám vám je.")
    if time.days == 1:
        "Paní Lisbeth odejde a za krátký okamžik přivede tři kluky kolem patnácti let, kteří vypadají, jako by toho moc nenaspali."
    else:
        "Paní Lisbeth odejde a za krátký okamžik přivede tři kluky kolem patnácti let."
    jump boysMain
    return

label workshopIntro:
    $ lisbeth.say("Tam vás musí pustit manžel, já tam nesmím ani uklízet. Dojdu mu říct.")
    $ lastSpokenWith = "workshop"
    jump workshopController
    return

label victimHouseholdConversationEnded:
    if lastSpokenWith != "lisbeth":
        "Když ukončíš rozhovor, z vedlejší místnosti se vynoří Lisbeth. Přichází zcela přirozeně a v pravou chvíli, pravděpodobně buď poslouchala za dveřmi, nebo je jednoduše dobrá a pozorná hostitelka."
    $ lisbeth.say("Můžu pro vás ještě něco udělat?")
    call victimHouseholdOptions
    return

###
