label aachimMain:
    $ lastSpokenWith = "aachim"
    $ heinrichHouseholdSpokenWith.append("aachim")
    $ origAsked = son.asked.copy()

    if son in cells:
        call aachimCellsIntro
    elif "spoken alone" not in son.asked:
        call aachimAloneFirst
    else:
        call aachimAloneAgain

    call aachimAloneOptions

    # adjust time spent
    $ time.addMinutes((len(son.asked) - len(origAsked)) * 3)
    if "arrest in progress" not in status:
        jump victimHouseholdConversationEnded
    return

label aachimCellsIntro:
    scene bg cell
    "Aachima najdeš, jak sedí na jednoduché pryčně se sklopenou hlavou a koleny přitaženými skoro pod bradu. Vypadá takhle ještě mladší, než na svých asi patnáct let."
    "Když přijdeš k jeho cele, zvedne hlavu a podívá se na tebe."
    return

label aachimAloneFirst:
    $ son.asked.append("spoken alone")
    "Lisbeth se zarazí a na chvíli vypadá, ze se chce na něco zeptat, ale pak přikývne."
    $ lisbeth.say("Samozřejmě, dojdu pro něj.")
    "Bez svých dvou kamarádů je Aachim viditelně nervózní, a když vám Lisbeth nechá soukromí, ještě se za ní krátce ohlédne."
    $ son.say("Proč... co pro vás můžu udělat?", "surprised")
    return

label aachimAloneAgain:
    "Lisbeth se zarazí a na chvíli vypadá, ze se chce na něco zeptat, ale pak přikývne."
    $ lisbeth.say("Samozřejmě, dojdu pro něj.")
    "Aachim si tě ostražitě změří."
    $ son.say("O co jde? Nemůžu se zdržet moc dlouho...")
    return

label aachimAloneOptions:
    call aachimAloneOptionsRemainingCheck
    if aachimOptionsRemaining == 0:
        $ mc.say("To je všechno, můžeš zase jít.")
        return

    show mcPic at menuImage
    menu:
        "Jak jsme spolu mluvili včera v dílně..." if "Aachim met during break-in" in status and "met during break-in" not in son.asked:
            hide mcPic
            $ son.asked.append("met during break-in")
            "Aachim se nervózně rozhlédne, jestli není někdo v doslechu."
            $ son.say("Já o tom nikomu neřekl. Spoléhám na to, že vy taky ne.")
        "Co vyrábíš?" if "working on" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
            hide mcPic
            $ son.asked.append("working on")
            if "WIP shoes seen" in status:
                $ mc.say("Nepodobná se to botám, které tvůj otec vyráběl na slavnosti?")
            $ son.say("Je to taková lehká taneční bota.")
            $ son.say("Na co si to vůbec hraju. Takhle jemný střih nemůžu zvládnout a táta stejně říká, že nejdůležitější je umět udělat poctivou dobře padnoucí holínku a zbytek je jen pozlátko.", "sad")
            $ son.say("Ale pak se taky kasal, jak zrovna touhle botou všem vytře zrak, tak já nevím.", "sad")
        "Můžu nějak pomoct?" if "help" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
            hide mcPic
            $ son.asked.append("help")
            $ son.say("Jestli neumíte zařídit, aby se z téhle zatracené hromady krámů stalo něco ohromujícího, tak těžko.", "sad")
        "Vyráběl jsi i předevčírem v noci?" if "yesterday" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
            hide mcPic
            $ son.asked.append("yesterday")
            $ son.say("Ne.", "angry")
            $ son.say("Předevčírem v noci jsem toho měl dost, a tak jsem šel spát. Vůbec nevím, co se tady v noci dělo.", "angry")
            $ mc.say("Takže jsi začal někdy ještě dřív?")
            $ son.say("...jo. Jsou to asi tři dny. Přemýšlel jsem nad tím už dřív, ale začal jsem až tehdy.")
            $ son.say("Táta mi zase jednou vynadal, jak jsem švec na nic, a mával mi před očima tou svojí úžasnou novou botou.", "angry")
            $ son.say("Já to přece vím, že jsem švec na nic, tak proč mě nutí, abych jím byl?", "sad")
        "Myslíš, že tvou botu na slavnosti vezmou?" if "work accepted" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
            hide mcPic
            $ son.asked.append("work accepted")
            $ son.say("Myslíš, že tvou botu na slavnosti vezmou?")
            $ son.say("Ale máte pravdu, asi ji nedodělám a nikdo se o ní nedozví. Kromě teď vás.", "sad")
            $ son.say("A táta mě zabije tak jako tak...", "sad")
        "Není to potom zbytečná práce?" if "work accepted" in son.asked and "work useless" not in son.asked:
            hide mcPic
            $ son.asked.append("work useless")
            $ son.say("Je to naprosto zbytečná práce, ale co mám podle vás dělat?", "sad")
            show mcPic at menuImage
            menu:
                "Neuvažoval jsi o změně řemesla?" if "change trade" not in son.asked:
                    hide mcPic
                    $ son.asked.append("change trade")
                    $ son.say("Uvažoval. Dost často. A taky o změně města a ideálně i obličeje, aby mě táta nemohl přitáhnout zpátky.", "sad")
                    "Aachim nešťastně potřese hlavou."
                    $ son.say("Táta mi život naplánoval dopředu a žádné změny v něm nedovolí. Jenom si holt představoval větší talent a nadšení pro tu jeho zatracenou ševcovinu.", "sad")
                "Řekl bych změnit řemeslo, ale..." if "change trade" in son.asked and gender == "M":
                    hide mcPic
                    $ son.say("Ale to mě táta nenechá. Jo.", "sad")
                "Řekla bych změnit řemeslo, ale..." if "change trade" in son.asked and gender == "M":
                    hide mcPic
                    $ son.say("Ale to mě táta nenechá. Jo.", "sad")
                "Nechat tátu, ať si nadává. Dílnu ti jednou předá stejně, nebo ne?":
                    hide mcPic
                    $ son.say("To mi zatím řekl každý, komu jsem se zkusil svěřit.", "sad")
                    $ son.say("Asi jo, ale kdy to bude? A jak mám do té doby žít s těmi neustálými výčitkami a připomínáním, jak jsem strašně k ničemu?", "sad")
                    $ son.say("A navíc, s tátou člověk nikdy neví. Řemeslo je pro něj důležitější než rodina a všem nám to dává najevo, ten ještě může udělat cokoli.", "sad")
        "Proč by tě měl zabíjet?" if "work accepted" in son.asked and "father angry" not in son.asked:
            hide mcPic
            $ son.asked.append("father angry")
            $ son.say("Protože... no, protože jsem jsem švec na nic. A nikdy se mu nezavděčím.", "surprised")
        "Jenom kvůli tomu by tě přece nechtěl zabít zrovna teď." if "father angry" in son.asked and "why now" not in son.asked:
            hide mcPic
            $ mc.say("Stalo se mezi vámi něco?")
            $ son.say("Nestalo!", "surprised")
            $ son.say("Ale ztratily se mu jeho mistrovské boty, tak zuří na celý svět. Zrovna teď bude chtít zabít kohokoli, kdo ho nějak vyprovokuje.", "sad")
        "Nepřemýšlel jsi někdy o změně řemesla?" if "change trade" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
            hide mcPic
            $ son.asked.append("change trade")
            $ son.say("Uvažoval. Dost často. A taky o změně města a ideálně i obličeje, aby mě táta nemohl přitáhnout zpátky.", "sad")
            "Aachim nešťastně potřese hlavou."
            $ son.say("Táta mi život naplánoval dopředu a žádné změny v něm nedovolí. Jenom si holt představoval větší talent a nadšení pro tu jeho zatracenou ševcovinu.", "sad")
        "Zatýkám tě pro zničení výrobku tvého otce." (badge="handcuffs") if "confession" in son.asked:
            hide mcPic
            "Aachim vytřeští oči a chvíli na tebe jen vyděšeně zírá."
            $ mc.say("Půjdeš se mnou.")
            $ son.say("A... co bude potom?", "surprised")
            show mcPic at menuImage
            menu:
                "Soud určitě vezme v úvahu, že to byla jenom nehoda." if "thief punishment" in colleaguesAsked:
                    hide mcPic
                    $ son.say("Určitě? Co když ne a něco mi useknou nebo mě dají do pranýře a všichni po mně budou házet kameny?", "surprised")
                    $ son.say("A i kdyby mě pustili, stejně budu před celým městem za zloděje. Jak se na mě potom budou lidi dívat? A na tátu? Na Adu?", "surprised")
                    $ mc.say("To už nemůžu ovlivnit.")
                "Co se obvykle děje zlodějům?":
                    hide mcPic
                    $ son.say("Ale tohle nebyla krádež! To byla jen nešťastná nehoda!", "surprised")
                    $ mc.say("Odnesl jsi z dílny něco, co nebylo tvoje. Jestli tohle není krádež, musí to říct soud, ne já.")
                "To bude nejspíš na tvém otci.":
                    hide mcPic
                    $ son.say("A proč mě potom potřebujete zatýkat?", "surprised")
                    $ mc.say("Když mu to jen řeknu, tak tě nejspíš zmlátí, a jestli to přežene, půjde před soud také. Takhle bude trest podle zákona, ať už bude jakýkoli.")
                    $ son.say("No to je opravdu útěcha.", "sad")
                "To už není moje věc.":
                    hide mcPic
                    $ hayfa.trust -= 1
                    $ son.trust -= 3
                    $ son.say("Jasně, hlavně splnit úkol, proč se zajímat o lidi.", "angry")
            $ newlyArrested.append(son)
            $ status.append("arrest in progress")
            return

        "{i}(Vrátit se k prohledávání dílny){/i}" if currentLocation == "workshop night":
            hide mcPic
            $ actionsTaken = 4
            "Aachim na chvíli zaváhá."
            $ son.say("Vlastně bych vás asi neměl nechat moc se ve věcech hrabat... kdybyste je nevrátil[a] na přesně správné místo a tak...", "surprised")
            $ mc.say("Umím se chovat hodně opatrně.")
            $ son.say("O tom nepochybuju, ale... já nevím...", "sad")
        "Asi bych měl zase jít" if currentLocation == "workshop night" and gender == "M":
            hide mcPic
            $ mc.say("Vážně nechci, aby mě tady někdo chytil.")
            $ son.say("To jsme dva.")
            "Aachim ti posvítí na cestu ke dveřím ven na ulici a zavře za tebou, spíš z nervozity než kvůli tomu, že bys to opravdu potřeboval."
            scene bg heinrich outside dark
            "Zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
        "Asi bych měla zase jít" if currentLocation == "workshop night" and gender == "F":
            hide mcPic
            $ mc.say("Vážně nechci, aby mě tady někdo chytil.")
            $ son.say("To jsme dva.")
            "Aachim ti posvítí na cestu ke dveřím ven na ulici a zavře za tebou, spíš z nervozity než kvůli tomu, že bys to opravdu potřebovala."
            scene bg heinrich outside dark
            "Zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
        "To je všechno, můžeš zase jít.":
            hide mcPic
            return

    if currentLocation == "workshop night":
        $ status.append("Aachim met during break-in")
        return
    else:
        jump aachimAloneOptions

label aachimAloneOptionsRemainingCheck:
    $ aachimOptionsRemaining = 0
    if "working on" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
        $ optionsRemaining += 1
    if "help" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
        $ optionsRemaining += 1
    if "yesterday" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
        $ optionsRemaining += 1
    if "work accepted" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
        $ optionsRemaining += 1
    if "work accepted" in son.asked and "work useless" not in son.asked:
        $ optionsRemaining += 1
    if "work accepted" in son.asked and "father angry" not in son.asked:
        $ optionsRemaining += 1
    if "change trade" not in son.asked and (currentLocation == "workshop night" or "met during break-in" in son.asked):
        $ optionsRemaining += 1
    if "Aachim met during break-in" in status and "met during break-in" not in son.asked:
        $ optionsRemaining += 1
    return
