label visitGuardhouseReminder:
    $ random = renpy.random.randint(1, 5)
    scene expression ("bg/bg street0[random].png")
    if messenger.alreadyMet == False:
        call visitGuardhouseReminderFirst
    else:
        call visitGuardhouseReminderAgain

    call visitGuardhouseReminderMenu

    $ messenger.alreadyMet = True
    "Melien kývne a zmizí ti v ulicích města."
    if "reason" in messenger.asked:
        $ messenger.asked.remove("reason")
    return

label visitGuardhouseReminderFirst:
    if gender == "M":
        "Při procházení městem tě zastaví mladý elf. Vlastně sis ho ani nevšiml přicházet, dokud nestál přímo před tebou."
    else:
        "Při procházení městem tě zastaví mladý elf. Vlastně sis ho ani nevšimla přicházet, dokud nestál přímo před tebou."
    show mcPic at menuImage
    menu:
        "Potřebuješ něco?":
            hide mcPic
            $ messenger.say("Já ne. Pro tebe ale mám zprávu.")
        "Nemám žádné peníze...":
            hide mcPic
            $ messenger.say("Rozhodně na boháče nevypadáš. Ale naštěstí pro tebe žádné nepotřebuju.")
    $ messenger.say("Jsem Melien z hlídky. Chce s tebou mluvit Rauvin a být tebou bych ho nenechával moc dlouho čekat.")
    if visitGuardhouseReminder == "complaint":
        $ messenger.say("Vypadal dost naštvaný.")
    return

label visitGuardhouseReminderAgain:
    if gender == "M":
        "Na moment se zastavíš, jen abys zkontroloval, že jdeš správnou ulicí, když tě někdo osloví."
    else:
        "Na moment se zastavíš, jen abys zkontrolovala, že jdeš správnou ulicí, když tě někdo osloví."
    $ messenger.say("%(callingMc)s?")
    "Otočíš se za hlasem a díváš se přímo do obličeje mladého elfa. Až po chvilce k němu přiřadíš správné jméno."
    $ messenger.say("Máš se zase stavit na strážnici.")
    $ messenger.say("A Rauvina bych nenechával dlouho čekat a tak vůbec… to už vlastně znáš.")
    return

label visitGuardhouseReminderMenu:
    call visitGuardhouseReminderOptionsRemaining
    if optionsRemaining == 0:
        $ mc.say("Díky, hned za ním zajdu.")
        return

    show mcPic at menuImage
    menu:
        "Díky, hned za ním zajdu.":
            hide mcPic
            return
        "Říkal, co potřebuje?" if messenger.alreadyMet == False and "reason" not in messenger.asked:
            call messengerReason
        "Říkal Rauvin, co potřebuje?" if messenger.alreadyMet == True and "reason" not in messenger.asked:
            call messengerReason
        "Proč nemáš stejnokroj?" if messenger.alreadyMet == False and "uniform" not in messenger.asked:
            hide mcPic
            $ messenger.asked.append("uniform")
            "Melien se usměje."
            $ messeger.say("Proč ho nemáš ty?", "happy")
            if gender == "M":
                $ mc.say("Vlastně mi ho ještě nestihli dát… k hlídce jsem nastoupil teprve dnes.")
            else:
                $ mc.say("Vlastně mi ho ještě nestihli dát… k hlídce jsem nastoupila teprve dnes.")
            $ messenger.say("Na slavnosti ho určitě dostaneš, ale Hayfa velitele a Rauvina přesvědčila, že občas je lepší nebýt vidět až z městských hradeb.")
        "Co si vlastně o Rauvinovi myslíš?" if messenger.alreadyMet == True and "Rauvin" not in messenger.asked:
            hide mcPic
            $ messenger.asked.append("Rauvin")
            $ messenger.say("Že není dobrý nápad ho nechat čekat. A že když s tebou chce mluvit, asi to bude důležité.")
            $ messenger.say("Je to ale docela správňák. Ke všem spravedlivý a tak. Myslím, že kdyby to bylo potřeba, tak by kohokoli z nás podržel.")
            $ mc.say("Vážně všechny?")
            $ messenger.say("Všechny. Kdyby mu za to někdo nestál, tak by ho z hlídky vyhodil.")
        "Rauvin může vyhazovat lidi, když hlídce přímo nevelí?" if "Rauvin" in messenger.asked and "Rauvin 2" not in messenger.asked:
            hide mcPic
            $ messenger.asked.append("Rauvin 2")
            $ messenger.say("On jí vlastně celkem velí. A je jenom otázka času, než jí bude velet i oficiálně.")
            $ mc.say("Na co se čeká?")
            $ messenger.say("Nevím, možná až bude v hlídce dýl než rok a půl? Ale všichni ví, že Galar jenom drží židli teplou pro toho, kdo přijde po něm.")
        "Co si vlastně myslíš o Hayfě?" if messenger.alreadyMet == True and "Hayfa" not in messenger.asked:
            hide mcPic
            $ messenger.append("Hayfa")
            $ messenger.say("Proč zrovna o Hayfě? Každopádně dobře zná město, dobře zná lidi, za mě by to tady klidně mohla jednou převzít, ale myslím, že se jí nechce. Je dobrý nápad ji poslouchat, když něco říká.")
    jump visitGuardhouseReminderMenu

label messengerReason:
    hide mcPic
    $ messenger.asked.append("reason")
    if visitGuardhouseReminder == "complaint":
        "Melien zavrtí hlavou."
        $ messenger.say("Neříkal, jenom se tvářil naštvaně.")
    elif visitGuardhouseReminder == "info":
        $ messenger.say("Prý pro tebe něco má něco k tvému případu.")
    else:
        "Melien zavrtí hlavou."
        $ messenger.say("Neříkal.")
    return

label visitGuardhouseReminderOptionsRemaining:
    $ optionsRemaining = 0
    if "reason" not in messenger.asked:
        $ optionsRemaining += 1
    if messenger.alreadyMet == False and "uniform" not in messenger.asked:
        $ optionsRemaining += 1
    if messenger.alreadyMet == True and "Rauvin" not in messenger.asked:
        $ optionsRemaining += 1
    if "Rauvin" in messenger.asked and "Rauvin 2" not in messenger.asked:
        $ optionsRemaining += 1
    if messenger.alreadyMet == True and "Hayfa" not in messenger.asked:
        $ optionsRemaining += 1
    return
