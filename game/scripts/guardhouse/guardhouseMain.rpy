label guardhouseAgain:
    $ chosenChar = ""
    if "arrest in progress" not in status:
        if currentLocation != "cells":
            $ currentLocation = "guardhouse"
        call guardhouseIntro

    label guardhouseMainMenu:
        if "arrest in progress" in status:
            scene bg cells entrance
            play music audio.cells fadeout 0.5 if_changed
        else:
            scene bg guardhouse
        call cluesOptionsRemainingCheck
        call guardhouseHelpOptionsAvailable
        call guardhouseArrestOptionsAvailable
        call solianHelpOptionsAvailable

        menu:
            "{i}(Nahlásit pokrok v pátrání){/i}" if optionsRemaining != 0 and "out of office" not in rauvin.status:
                call endArrest
                $ rauvin.say("To vždycky cením, ale teď mám zrovna práci, tak jen rychle. Jaký je nejslibnější nový vývoj?")
                call reportingBack
            "{i}(Požádat Rauvina o pomoc){/i}" if helpOptionsAvailable > 0 and "out of office" not in rauvin.status:
                call endArrest
                $ helpAsked = 0
                call guardhouseHelpMenu
            "{i}(Požádat Soliana o pomoc){/i}" if helpOptionsAvailable > 0 and "out of office" in rauvin.status:
                call endArrest
                $ helpAsked = 0
                call guardhouseHelpMenu
            "{i}(Požádat Soliana o neformální službičku){/i}" if solianHelpOptionsAvailable > 0:
                call endArrest
                "Solian poměrně často opouští strážnici kvůli různým pochůzkám. Teď ho ale najdeš, jak se u malého stolku probírá nějakými záznamy. Rozhlédneš se a ověříš si, že nikdo jiný není v doslechu."
                call solianHelpMenu
            "{i}(Navrhnout Rauvinovi zatčení){/i}" if arrestOptionsAvailable > 0 and "out of office" not in rauvin.status:
                call endArrest
                call guardhouseArrestMenu
            #"{i}(Navrhnout Solianovi zatčení){/i}" if arrestOptionsAvailable > 0 and "out of office" in rauvin.status:
                #call endArrest
                #call guardhouseArrestMenu
            "{i}(Jít k vězeňským celám){/i}" if currentLocation != "cells":
                call cellsController
            "{i}(Vrátit se k vězeňským celám){/i}" if currentLocation == "cells":
                call cellsController
            "{i}(Promluvit si se zatčeným){/i}" if "arrest in progress" in status and len(cells) != 0:
                call cellsController
            "{i}(Flákat se){/i}": #FOR DEBUG PURPOSES
                menu:
                    "{i}Hodinu{/i}":
                        $ time.addHours(1)
                    "{i}Tři hodiny{/i}":
                        $ time.addHours(3)
                    "{i}Pět hodin{/i}":
                        $ time.addHours(5)
                call interludeController
            "{i}(Vrátit se zase k případu){i}":
                call endArrest
                if "out of office" in rauvin.status:
                    "Solian na tebe krátce kývne a vrátí se ke své práci."
                    jump backToEvidenceWall
                elif optionsRemaining != 0:
                    $ rauvin.say("Jak pokračuješ s případem? Nějaký nový vývoj od posledně?")
                    call reportingBack
                else:
                    "Rauvin jen kývne a nechá tě vrátit se k práci."
                jump backToEvidenceWall
        jump guardhouseMainMenu


label guardhouseIntro:
    scene bg guardhouse
    # scenes to witness
    $ sceneWitnessed = False
    if timeOfDay != "standup":
        $ sceneWitnessed = True
    elif time.days == 3 and "Rauvin's health report" not in status:
        call rauvinHealthReport
        $ sceneWitnessed = True
    elif time.days == 2 and "Hayfa's past encounter" not in status:
        call hayfasPastEncounter
        $ sceneWitnessed = True
    elif "Rovien house visited" in status and "racism encounter" not in status and "out of office" not in rauvin.status:
        call racismEncounter
        $ sceneWitnessed = True

    # player approached/intro
    if time.days == 3 and time.hours > 16 and "case progress discussed" not in solian.asked:
        call nervousSolian
    elif victim.trust < -4 and "heinrich complained" not in status:
        call guardhouseHeinrichComplained
    elif "waiting for suspect list" in status:
        call suspectListDelivered
    elif "investigating less deals" in status:
        call AmlCheckResult
    elif "awaiting AML merchant list" in status:
        call AmlMerchantListDelivered
    elif "zeran witnesses" in status:
        call zeranWitnessesChecked
    elif time.hours > 16 and "report given" not in dailyStatus and "out of office" not in rauvin.status and optionsRemaining != 0:
        call reportWantedIntro
    elif sceneWitnessed == False:
        $ intro = renpy.random.choice(guardhouseIntros)
        "[intro]"
    return

label backToEvidenceWall:
    if "add investigating less deals" in status:
        $ status.remove("add investigating less deals")
        $ status.append("investigating less deals added")
        $ newEvent = Event(copy.deepcopy(time), "STATUS", 0, "investigating less deals", 3, "info")
        $ newEvent.when.addHours(2)
        $ eventsList.append(newEvent)
    if "add investigating less deals solian" in status:
        $ status.remove("add investigating less deals solian")
        $ status.append("investigating less deals solian added")
        $ newEvent = Event(copy.deepcopy(time), "STATUS", 0, "investigating less deals solian", 3, "info")
        $ newEvent.when.addHours(2)
        $ eventsList.append(newEvent)
    if "add zeran witnesses" in status:
        $ status.remove("add zeran witnesses")
        $ status.append("zeran witnesses added")
        $ newEvent = Event(copy.deepcopy(time), "STATUS", 0, "zeran witnesses", 3, "info")
        $ newEvent.when.addHours(2)
        $ eventsList.append(newEvent)

    jump evidenceWall


label reportWantedIntro:
    "Rauvin na tebe kývne."
    $ rauvin.say("Chtěl jsem se zeptat, jak pokračuješ s případem. Máš nový vývoj nebo slibnou stopu?")
    show mcPic at menuImage
    menu:
        "Něco ano, můžeme to hned probrat.":
            hide mcPic
        "Něco ano, ale zatím to není ucelené, radši bych ještě nějakou dobu věnoval[a] pátrání.":
            hide mcPic
            $ rauvin.say("Pojďme si promluvit o tom, co máš. Chápu, že ještě nemusíš mít rozpletený celý případ, ale potřebuji vědět, jak se věc vyvíjí. A třeba tě dokážu i nějak podpořit.")
        "Zatím vlastně nic nemám.":
            hide mcPic
            $ rauvin.say("Pojďme si tedy promluvit o tom, jaké stopy jsi sledoval[a] a co z nich vzešlo. Třeba jsi ve skutečnosti blíž, než si [sam] myslíš.")
            $ rauvin.say("A jestli ne, tím spíš to potřebuji vědět.")
        "Tím se teď nechci zdržovat.":
            hide mcPic
            $ rauvin.trust -= 2
            $ rauvin.say("Dávat hlášení velícímu důstojníkovi není zdržování, ale nutnost pro to, aby hlídka držela pohromadě.", "angry")
            $ rauvin.say("Takže začni.", "angry")
            show mcPic at menuImage
            menu:
                "No dobře, jestli to půjde rychle...":
                    hide mcPic
                "Já to myslím vážně, na tohle nemám čas.":
                    hide mcPic
                    $ rauvin.trust -= 3
                    $ mc.cluesAgainst += 1
                    if mc.cluesAgainst > 1:
                        $ rauvin.say("To jsme dva. K čemu je mi hlídkař, který se mnou ani nemluví?", "angry")
                        $ rauvin.say("A není to první případ, se chováš způsobem, který je s působením v hlídce neslučitelný. Přinejmenším v hlídce, která opravdu hájí všechny v tomto městě.", "angry")
                        $ rauvin.say("Vrať mi pověřovací listinu a já ti popřeji hodně štěstí při hledání nějakého zaměstnání, kde si budeš moci víc dělat, co tě zrovna napadne.")
                        scene bg door01
                        "Zanedlouho se ocitneš znovu před strážnicí. Stojíš na ulici a přemýšlíš, kam ještě jít."
                        jump thrownOut
                    else:
                        $ rauvin.say("Já také. Dej mi hlášení, nebo vrať pověřovací listinu.", "angry")
                        show mcPic at menuImage
                        menu:
                            "Když to musí být, tak tedy pojďme na to.":
                                hide mcPic
                            "{i}(Vrátit glejt){/i}":
                                hide mcPic
                                "Beze slova podáš Rauvinovi listinu s pečetí a tvým jménem. Rauvin na tebe chvíli zkoumavě hledí a také nic neříká. Poté tvé pověření přijme a schová si ho za pás."
                                $ rauvin.say("Plat si nezasloužíš, protože nemám doklad o žádné vykonané práci. K východu trefíš.")
                                "Otočíš se a bez dalšího loučení vyjdeš ven na ulici vstříc osudu, který už s hlídkou nebude nijak spjatý."
                                jump thrownOut
    call reportingBack
    return

# Options available check #

label guardhouseArrestOptionsAvailable:
    $ arrestOptionsAvailable = 0
    if "confession" in rumelin.asked and rumelin not in allArrested and "arrest Rumelin" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    if "confession" in kaspar.asked and kaspar not in allArrested:
        $ arrestOptionsAvailable += 1
    if zeranNote.isActive and "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason and "arrest Zeran for stolen idea" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    return
