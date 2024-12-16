label visitGuardhouseReminder:
    $ random = renpy.random.randint(1, 6)
    scene expression ("bg/bg street0[random].png")
    if melien.alreadyMet == False:
        call visitGuardhouseReminderFirst
    else:
        call visitGuardhouseReminderAgain

    call visitGuardhouseReminderMenu

    $ melien.alreadyMet = True
    "Melien kývne a zmizí ti v ulicích města."
    if "reason" in melien.asked:
        $ melien.asked.remove("reason")
    return

label visitGuardhouseReminderFirst:
    "Při procházení městem tě zastaví mladý elf. Vlastně sis ho ani nevšiml[a] přicházet, dokud nestál přímo před tebou."
    show mcPic at menuImage
    menu:
        "Potřebuješ něco?":
            hide mcPic
            $ melien.say("Já ne. Pro tebe ale mám zprávu.")
        "Nemám žádné peníze...":
            hide mcPic
            $ melien.say("Rozhodně na boháče nevypadáš. Ale naštěstí pro tebe žádné nepotřebuju.")
    $ melien.say("Jsem Melien z hlídky. Chce s tebou mluvit Rauvin a být tebou bych ho nenechával moc dlouho čekat.")
    if visitGuardhouseReminder == "complaint":
        $ melien.say("Vypadal dost naštvaný.")
    return

label visitGuardhouseReminderAgain:
    "Na moment se zastavíš, jen abys zkontroloval[a], že jdeš správnou ulicí, když tě někdo osloví."
    $ melien.say("%(callingMc)s?")
    "Otočíš se za hlasem a díváš se přímo do obličeje mladého elfa. Až po chvilce k němu přiřadíš správné jméno."
    $ melien.say("Máš se zase stavit na strážnici.")
    $ melien.say("A Rauvina bych nenechával dlouho čekat a tak vůbec… to už vlastně znáš.")
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
        "Říkal, co potřebuje?" if melien.alreadyMet == False and "reason" not in melien.asked:
            call melienReason
        "Říkal Rauvin, co potřebuje?" if melien.alreadyMet == True and "reason" not in melien.asked:
            call melienReason
        "Proč nemáš stejnokroj?" if melien.alreadyMet == False and "uniform" not in melien.asked:
            hide mcPic
            $ melien.asked.append("uniform")
            "Melien se usměje."
            $ messeger.say("Proč ho nemáš ty?", "happy")
            $ mc.say("Vlastně mi ho ještě nestihli dát... k hlídce jsem nastoupil[a] teprve dnes.")
            $ melien.say("Na slavnosti ho určitě dostaneš, ale Hayfa velitele a Rauvina přesvědčila, že občas je lepší nebýt vidět až z městských hradeb.")
        "Co si vlastně o Rauvinovi myslíš?" if melien.alreadyMet == True and "Rauvin" not in melien.asked:
            hide mcPic
            $ melien.asked.append("Rauvin")
            $ melien.say("Že není dobrý nápad ho nechat čekat. A že když s tebou chce mluvit, asi to bude důležité.")
            $ melien.say("Je to ale docela správňák. Ke všem spravedlivý a tak. Myslím, že kdyby to bylo potřeba, tak by kohokoli z nás podržel.")
            $ mc.say("Vážně všechny?")
            $ melien.say("Všechny. Kdyby mu za to někdo nestál, tak by ho z hlídky vyhodil.")
        "Rauvin může vyhazovat lidi, když hlídce přímo nevelí?" if "Rauvin" in melien.asked and "Rauvin 2" not in melien.asked:
            hide mcPic
            $ melien.asked.append("Rauvin 2")
            $ melien.say("On jí vlastně celkem velí. A je jenom otázka času, než jí bude velet i oficiálně.")
            $ mc.say("Na co se čeká?")
            $ melien.say("Nevím, možná až bude v hlídce dýl než rok a půl? Ale všichni ví, že Galar jenom drží židli teplou pro toho, kdo přijde po něm.")
        "Co si vlastně myslíš o Hayfě?" if melien.alreadyMet == True and "Hayfa" not in melien.asked:
            hide mcPic
            $ melien.append("Hayfa")
            $ melien.say("Proč zrovna o Hayfě? Každopádně dobře zná město, dobře zná lidi, za mě by to tady klidně mohla jednou převzít, ale myslím, že se jí nechce. Je dobrý nápad ji poslouchat, když něco říká.")
    jump visitGuardhouseReminderMenu

label melienReason:
    hide mcPic
    $ melien.asked.append("reason")
    if visitGuardhouseReminder == "complaint":
        "Melien zavrtí hlavou."
        $ melien.say("Neříkal, jenom se tvářil naštvaně.")
    elif visitGuardhouseReminder == "info":
        $ melien.say("Prý pro tebe něco má něco k tvému případu.")
    else:
        "Melien zavrtí hlavou."
        $ melien.say("Neříkal.")
    return

label visitGuardhouseReminderOptionsRemaining:
    $ optionsRemaining = 0
    if "reason" not in melien.asked:
        $ optionsRemaining += 1
    if melien.alreadyMet == False and "uniform" not in melien.asked:
        $ optionsRemaining += 1
    if melien.alreadyMet == True and "Rauvin" not in melien.asked:
        $ optionsRemaining += 1
    if "Rauvin" in melien.asked and "Rauvin 2" not in melien.asked:
        $ optionsRemaining += 1
    if melien.alreadyMet == True and "Hayfa" not in melien.asked:
        $ optionsRemaining += 1
    return
