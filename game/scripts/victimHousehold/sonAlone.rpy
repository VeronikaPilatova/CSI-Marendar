label aachimAloneOptions:
show mcPic at menuImage
menu:
    "Co vyrábíš?" if "working on" not in son.asked:
        hide mcPic
        $ son.asked.append("working on")
        if "WIP shoes seen" in status:
            $ mc.say("Nepodobná se to botám, které tvůj otec vyráběl na slavnosti?")
        $ son.say("Je to taková lehká taneční bota.")
        $ son.say("Na co si to vůbec hraju. Takhle jemný střih nemůžu zvládnout a táta stejně říká, že nejdůležitější je umět udělat poctivou dobře padnoucí holínku a zbytek je jen pozlátko.", "sad")
        $ son.say("Ale pak se taky kasal, jak zrovna touhle botou všem vytře zrak, tak já nevím.", "sad")
    "Můžu nějak pomoct?" if "help" not in son.asked:
        hide mcPic
        $ son.asked.append("help")
        $ son.say("Jestli neumíte zařídit, aby se z téhle zatracené hromady krámů stalo něco ohromujícího, tak těžko.", "sad")
    "Vyráběl jsi i předevčírem v noci?" if "yesterday" not in son.asked:
        hide mcPic
        $ son.asked.append("yesterday")
        $ son.say("Ne.", "angry")
        $ son.say("Předevčírem v noci jsem toho měl dost, a tak jsem šel spát. Vůbec nevím, co se tady v noci dělo.", "angry")
        $ mc.say("Takže jsi začal někdy ještě dřív?")
        $ son.say("...jo. Jsou to asi tři dny. Přemýšlel jsem nad tím už dřív, ale začal jsem až tehdy.")
        $ son.say("Táta mi zase jednou vynadal, jak jsem švec na nic, a mával mi před očima tou svojí úžasnou novou botou.", "angry")
        $ son.say("Já to přece vím, že jsem švec na nic, tak proč mě nutí, abych jím byl?", "sad")
    "Myslíš, že tvou botu na slavnosti vezmou?" if "work accepted" not in son.asked:
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
    "Nepřemýšlel jsi někdy o změně řemesla?" if "change trade" not in son.asked:
        hide mcPic
        $ son.asked.append("change trade")
        $ son.say("Uvažoval. Dost často. A taky o změně města a ideálně i obličeje, aby mě táta nemohl přitáhnout zpátky.", "sad")
        "Aachim nešťastně potřese hlavou."
        $ son.say("Táta mi život naplánoval dopředu a žádné změny v něm nedovolí. Jenom si holt představoval větší talent a nadšení pro tu jeho zatracenou ševcovinu.", "sad")
    "{i}(Vrátit se k prohledávání dílny){/i}" if currentLocation == "workshop night":
        hide mcPic
        $ actionsTaken = 4
        "Aachim na chvíli zaváhá."
        if gender == "M":
            $ son.say("Vlastně bych vás asi neměl nechat moc se ve věcech hrabat... kdybyste je nevrátil na přesně správné místo a tak...", "surprised")
        else:
            $ son.say("Vlastně bych vás asi neměl nechat moc se ve věcech hrabat... kdybyste je nevrátila na přesně správné místo a tak...", "surprised")
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

if currentLocation == "workshop night":
    return
else:
    jump aachimAloneOptions


label aachimAloneOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "working on" not in son.asked:
        $ optionsRemaining += 1
    if "help" not in son.asked:
        $ optionsRemaining += 1
    if "yesterday" not in son.asked:
        $ optionsRemaining += 1
    if "work accepted" not in son.asked:
        $ optionsRemaining += 1
    if "work accepted" in son.asked and "work useless" not in son.asked:
        $ optionsRemaining += 1
    if "work accepted" in son.asked and "father angry" not in son.asked:
        $ optionsRemaining += 1
    if "change trade" not in son.asked:
        $ optionsRemaining += 1
    return
