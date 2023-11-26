label arrest:
    python:
        cells.append(arrested[-1])
        newlyArrested = arrested[-1]
        arrestReason = arrested[-1].arrestReason[-1]
        if newlyArrested not in persistent.arrestedPeople:
            persistent.arrestedPeople.append(newlyArrested)

    scene bg guardhouse
    call arrestedEveryoneAchievementCheck
    if newlyArrested == rumelin:
        "TBD: Odvedeš Rumelina do cely."
    elif newlyArrested == eckhard:
        "TBD: Odvedeš Eckharda do cely."
    elif newlyArrested == zeran:
        "TBD: Odvedeš Zerana do cely."
        if arrestReason == "vagrancy":
            call zeranVagrancyArrestReaction

    scene bg cells entrance
    $ currentLocation = "cells"
    if "cells visited" not in status:
        call cellsFirst
        $ status.append("cells visited")

    jump guardhouseAgain

label endArrest:
    if "arrest in progress" in status:
        $ status.remove("arrest in progress")
        scene bg guardhouse
        call guardhouseIntro
    return

###

label zeranVagrancyArrestReaction:
    scene bg cells entrance
    "Když začneš stoupat po schodech od chodby s celami zpět na denní světlo, zjistíš, že dveře zpět do hlavní místnosti jsou zavřené a před nimi, přímo na vrcholku schodiště, stojí Hayfa."
    $ hayfa.say("Vážně jsi právě zahodil[a] svou budoucnost jen proto, aby sis něco dokázal[a]?")
    $ mc.say("... prosím?")
    if gender == "M":
        $ hayfa.say("Zatknul jsi Zerana. Za potulku. Uvnitř domu, ve kterém bydlí. Za takové zneužití moci by se nestyděl ani Velin.", "angry")
    else:
        $ hayfa.say("Zatkla jsi Zerana. Za potulku. Uvnitř domu, ve kterém bydlí. Za takové zneužití moci by se nestyděl ani Velin.", "angry")
    $ mc.say("Neměl žádnou úctu k hlídce! Jak potom můžeme střežit pořádek?")
    $ hayfa.say("My bez zneužívání moci. Ty už nijak.", "angry")
    $ hayfa.say("Teď mi vrať glejt a vypadni z tohohle města.", "angry")
    $ mc.say("Do toho, jestli ve městě zůstanu, přece nemáš, co mluvit.")
    $ hayfa.say("Mám povinnost město chránit před všemi, co mu chtějí ublížit. A o tobě už vím, co jsi zač.")
    "Odevzdáš glejt a hlídkařka ti ustoupí z cesty. Potom tě sleduje pohledem po celou tu nepříjemně dlouhou dobu, dokud nepřejdeš přes strážnici k hlavnímu vchodu a nezazní za tebou bouchnutí pantů."
    scene bg door01
    "Stojíš na ulici a přemýšlíš, kam ještě můžeš jít."
    jump thrownOut
    return
