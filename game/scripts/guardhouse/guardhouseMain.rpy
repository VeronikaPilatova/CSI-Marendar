label guardhouseAgain:
    $ chosenChar = ""
    if "arrest in progress" not in status:
        if currentLocation != "cells":
            $ currentLocation = "guardhouse"
        call guardhouseIntro

    label guardhouseMainMenu:
        if "arrest in progress" in status:
            scene bg cells entrance
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
            "{i}(Promluvit si se zatčeným){/i}" if "arrest in progress" in status:
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

label guardhouseHelpMenu:
    call guardhouseHelpOptionsAvailable
    if helpOptionsAvailable == 0:
        if gender == "M":
            $ mc.say("Děkuji, to je všechno, co jsem chtěl.")
        else:
            $ mc.say("Děkuji, to je všechno, co jsem chtěla.")
        return

    show mcPic at menuImage
    menu:
        "Mohla by hlídka prověřit nějaké obchody?" if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status:
            hide mcPic
            call helpWithAml
            $ helpAsked += 1
        "Potřeboval bych ověřit, jestli Zeran včera v noci opravdu pracoval." if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status) and gender == "M":
            hide mcPic
            call helpWithZeranWitnesses
            $ helpAsked += 1
        "Potřebovala bych ověřit, jestli Zeran včera v noci opravdu pracoval." if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status) and gender == "F":
            hide mcPic
            call helpWithZeranWitnesses
            $ helpAsked += 1
        "Vlastně si to ještě nechám projít hlavou." if helpAsked == 0:
            hide mcPic
            return
        "Děkuji, to je všechno, co jsem chtěl." if helpAsked > 0 and gender == "M":
            hide mcPic
            return
        "Děkuji, to je všechno, co jsem chtěla." if helpAsked > 0 and gender == "F":
            hide mcPic
            return
    jump guardhouseHelpMenu

label solianHelpMenu:
    call solianHelpOptionsAvailable
    if solianHelpOptionsAvailable == 0:
        "Vrátíš se zas k jiným záležitostem."
        return

    show mcPic at menuImage
    menu:
        "Jak snadné je dostat se k záznamům o clech? Hodilo by se mi do nich občas nakouknout." if "offered favour" in "lotte asked" and "industrial espionage" not in solian.asked:
            hide mcPic
            call industrialEspionage
        "{i}(Vrátit se k jiným záležitostem.){/i}":
            return
    jump solianHelpMenu

label guardhouseArrestMenu:
    show mcPic at menuImage
    menu:
        "Chci zatknout mistra Kaspara, za krádež Heinrichova výrobku." if "confession" in kaspar.asked and kaspar not in arrested:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for theft")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            if gender == "M":
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčený, že lže a buď je zničil, nebo odnesl a někde schoval.")
            else:
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčená, že lže a buď je zničil, nebo odnesl a někde schoval.")
            $ rauvin.say("Máš na to důkazy?")
            $ mc.say("Mistr Kaspar se v podstatě přiznal…")
            $ rauvin.say("Potřebujeme buď plné přiznání nebo nezvratný důkaz.")
            $ rauvin.say("Neříkám, že nemáš pravdu, ale pokračuj v pátrání, dokud toho nebudeš mít v rukou víc.")
            if gender == "M":
                $ rauvin.say("A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Kaspara, za zničení Heinrichova výrobku." if "confession" in kaspar.asked and kaspar not in arrested and "burned evidence" in clues:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for sabotage")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            if gender == "M":
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčený, že lže. Navíc mám důkaz, že se někdo pokusil Heinrichovy střevíce spálit v jeho vlastním krbu.")
            else:
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčená, že lže. Navíc mám důkaz, že se někdo pokusil Heinrichovy střevíce spálit v jeho vlastním krbu.")
            $ rauvin.say("Máš na to důkaz, který by ukazoval přímo na mistra Kaspara?")
            $ mc.say("V podstatě se přiznal.")
            $ rauvin.say("Potřebujeme buď plné přiznání nebo nezvratný důkaz.")
            $ rauvin.say("Neříkám, že nemáš pravdu, ale pokračuj v pátrání, dokud toho nebudeš mít v rukou víc.")
            if gender == "M":
                $ rauvin.say("A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Kaspara, za úmysl poškodit Heinrichův výrobek." if "confession" in kaspar.asked and kaspar not in arrested and "burned evidence" in clues:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for intentions")
            "Rauvin se zamračí."
            $ rauvin.say("Co myslíš tím úmyslem?")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            $ rauvin.say("Ale neudělal to?")
            $ mc.say("Tvrdí, že ty střevíce nenašel, a já mu spíš věřím.")
            $ rauvin.say("Nemyslím si, že je možné zatknout váženého mistra jen za úmysl něco udělat, i kdybychom pro ten úmysl měli naprosto nezvratný důkaz. A já si moc nedokážu představit, jak by takový důkaz mohl vypadat, Kaspar může kdykoli všechno popřít.")
            $ rauvin.say("Kdyby něco skutečně udělal, třeba se do té dílny vloupal nebo si na to ničení aspoň přinesl nějaké nástroje, mělo by to větší pádnost, ale ani potom by se tím soudce nemusel chtít vůbec zabývat.")
            if gender == "M":
                $ rauvin.say("Pokračuj tedy prosím v pátrání, jestli najdeš něco dalšího, co proti mistru Kasparovi směřuje. A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("Pokračuj tedy prosím v pátrání, jestli najdeš něco dalšího, co proti mistru Kasparovi směřuje. A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Rumelina, za podvod a snahu poškodit jiného mistra jeho cechu." if "confession" in rumelin.asked and rumelin not in arrested:
            hide mcPic
            $ rauvin.asked.append("arrest Rumelin")
        "Chci zatknout Zerana, za krádež střihu mistra Njala." if zeranNote.isActive and "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason:
            hide mcPic
            $ rauvin.asked.append("arrest Zeran for stolen idea")
            if "stolen idea" in rauvin.asked:
                $ rauvin.say("Zerana? Takže ten střih mistru Heinrichovi donesl on?")
                $ mc.say("Ano, pravděpodobně aby ho mistr Heinrich vzal zpátky.")
            else:
                $ rauvin.say("O jaký střih se jedná?")
                $ mc.say("O střih na ukradené boty mistra Heinricha. Původně ho vytvořil mistr Njal a Zeran mu ho ukradl. Pravděpodobně doufal, že ho pak mistr Heinrich vezme zpátky.")
            $ rauvin.say("A máš na to důkazy?")
            show mcPic at menuImage
            menu:
                "Ne, ale jsem si jistý, že to udělal." if gender == "M":
                    call arrestZeranStolenIdeaConvinced
                "Ne, ale jsem si jistá, že to udělal." if gender == "F":
                    call arrestZeranStolenIdeaConvinced
                "Ne, ale Njal požaduje, abychom někoho zatkli.":
                    hide mcPic
                "Ve skutečnosti ne, možná to není dobrý nápad.":
                    hide mcPic
                    $ rauvin.say("Zatýkat někoho bez důkazů rozhodně dobrý nápad není.")
                    if gender == "M":
                        $ rauvin.say("Vrať se k pátrání a stav se, kdybys potřeboval s něčím pomoct.")
                    else:
                        $ rauvin.say("Vrať se k pátrání a stav se, kdybys potřeboval s něčím pomoct.")
    return

label guardhouseIntro:
    scene bg guardhouse
    # scenes to witness
    $ sceneWitnessed = False
    if time.days == 2 and "Killian encounter" not in status:
        call kilianEncounter
        $ sceneWitnessed = True
    elif "Rovien house visited" in status and "racism encounter" not in status and "out of office" not in rauvin.status:
        call racismEncounter
        $ sceneWitnessed = True

    # player approached/intro
    if victim.trust < -4 and "heinrich complained" not in status:
        call guardhouseHeinrichComplained
    elif "waiting for suspect list" in status:
        call suspectListDelivered
    elif "investigating less deals" in status:
        call AmlCheckResult
    elif "awaiting AML merchant list" in status:
        call AmlMerchantListDelivered
    elif "zeran witnesses" in status:
        call zeranWitnessesChecked
    elif time.hours > 16 and "report given" not in dailyStatus and "out of office" not in rauvin.status:
        "Rauvin na tebe kývne."
        $ rauvin.say("Chtěl jsem se zeptat, jak pokračuješ s případem. Máš nový vývoj nebo slibnou stopu?")
        call reportingBack
    elif sceneWitnessed == False:
        "Rauvin sedí u stolu a prochází nějaké papíry, ale když se přiblížíš, zvedne hlavu a otočí se na tebe."
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

###

label suspectListDelivered:
    if "out of office" not in rauvin.status:
        "Jakmile si tě Rauvin všimne, mávne na tebe listem papíru."
        if gender == "M":
            $ rauvin.say("Hostinská Salma ti posílá seznam hostů ze včerejška, prý sis ho vyžádal.")
            $ mc.say("To je pravda. Myslel jsem, že by nám pomohlo vědět, kdo všechno mohl slyšet o dokončených střevících.")
        else:
            $ rauvin.say("Hostinská Salma ti posílá seznam hostů ze včerejška, prý sis ho vyžádala.")
            $ mc.say("To je pravda. Myslela jsem, že by nám pomohlo vědět, kdo všechno mohl slyšet o dokončených střevících.")
        "Rauvin se mírně zamračí."
        $ rauvin.say("Ta úvaha dává smysl, ale nejsem si jistý, jestli na procházení celého seznamu máme čas. Einionovy slavnosti jsou už za čtyři dny a jen obejít všechny tyhle lidi by mohlo zabrat celý den, možná víc.")
        $ rauvin.say("Zkus se zaměřit na jiné stopy a pokud by žádná z nich nikam nevedla, k seznamu hostů se můžeš vrátit později.")
    else:
        "Dojde k tobě Solian a podá ti list papíru."
        if gender == "M":
            $ solian.say("Tady ti Salma posílá seznam hostů ze včerejška, prý jsi chtěl vědět, kdo mohl slyšet o Heinrichově dokončeném díle. Znamená to, že nemáš žádnou konkrétní stopu?")
        else:
            $ solian.say("Tady ti Salma posílá seznam hostů ze včerejška, prý jsi chtěla vědět, kdo mohl slyšet o Heinrichově dokončeném díle. Znamená to, že nemáš žádnou konkrétní stopu?")
        show mcPic at menuImage
        menu:
            "Konkrétní stopy mám, ale chtěl jsem být důkladný." if gender == "M":
                hide mcPic
                $ solian.say("Tak se zaměř spíš na ně. Einionovy slavnosti jsou za čtyři dny a už jenom oběhnout celý tenhle seznam může zabrat víc času, než vůbec máš.", "angry")
            "Konkrétní stopy mám, ale chtěla jsem být důkladná." if gender == "F":
                hide mcPic
                $ solian.say("Tak se zaměř spíš na ně. Einionovy slavnosti jsou za čtyři dny a už jenom oběhnout celý tenhle seznam může zabrat víc času, než vůbec máš.", "angry")
            "Zatím méně, než by se mi líbilo.":
                hide mcPic
                $ solian.say("Tak zkus co nejrychleji nějaké najít. Einionovy slavnosti jsou za čtyři dny a už jenom oběhnout celý tenhle seznam může zabrat víc času, než vůbec máš.", "angry")
        $ solian.say("A v nejhorším případě na tom seznamu začni u nějakých potulných tovaryšů a jiné pakáže, někdo takový tam určitě bude.")
    $ status.remove("waiting for suspect list")
    $ status.append("suspect list delivered")
    $ time.addMinutes(5)
    return

label AmlCheckResult:
    if "out of office" not in rauvin.status:
        "Dojde k tobě Rauvin."
        if gender == "M":
            $ rauvin.say("Vypadá to, že se změnou v obchodování ševcovských mistrů jsi měl pravdu. Nechal jsem to prověřit a v ostatních hospodách to vypadá přesně stejně.")
        else:
            $ rauvin.say("Vypadá to, že se změnou v obchodování ševcovských mistrů jsi měla pravdu. Nechal jsem to prověřit a v ostatních hospodách to vypadá přesně stejně.")
        $ rauvin.say("Mistra Njala několik obchodníků odmítlo i jinde a mistra Rumelina nikdo neviděl nakupovat luxusní materiál, přestože ho podle všeho má a používá.")
        $ mc.say("Pokusím se zjistit, kdo za tím stojí.")
        "Rauvin krátce kývne."
        $ rauvin.say("Postupuj opatrně, a pokud něco zjistíš, určitě mi to nahlaš.")
    else:
        "Přijde k tobě Solian se zamračeným výrazem."
        if gender == "M":
            $ solian.say("Jak jsi řešil ty změny v obchodování...", "angry")
            $ mc.say("Přišlo mi to podezřelé, a tak jsem chtěl vědět, jestli se to změnilo opravdu i v jiných hospodách než u Salmy.")
        else:
            $ solian.say("Jak jsi řešila ty změny v obchodování...")
            $ mc.say("Přišlo mi to podezřelé, a tak jsem chtěla vědět, jestli se to změnilo opravdu i v jiných hospodách než u Salmy.")
        $ solian.say("Nechali jsme to prověřit a mistra Njala prý opravdu několik obchodníků odmítlo i jinde. Ale...")
        $ mc.say("A co mistr Rumelin? Viděl ho někdo v poslední době nakupovat luxusní materiál?")
        $ solian.say("Pokud vím, tak ne. Ale souvisí to nějak s tvým případem?", "angry")
        $ mc.say("Mohlo by. Co kdyby krádež Heinrichových střevíců byla součást snahy poškodit nějak celý cech?")
        $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc. Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.", "angry")
        show mcPic at menuImage
        menu:
            "Budu na to myslet.":
                hide mcPic
            "Pokud tu dochází ke zločinu, budu ho řešit.":
                hide mcPic
                $ solian.trust -= 1
                if gender == "M":
                    $ solian.say("Hlavně buď opatrný a nestrkej do ničeho zbytečně prsty.", "angry")
                else:
                    $ solian.say("Hlavně buď opatrná a nestrkej do ničeho zbytečně prsty.", "angry")
        $ mc.say("V každém případě díky za ověření, že Salma měla pravdu.")
        "Solian jen kývne a vrátí se k vlastní práci."
        $ solian.asked.append("less deals")
    $ status.remove("investigating less deals")
    $ status.append("less deals checked")
    $ time.addMinutes(5)
    return

label AmlMerchantListDelivered:
    if "out of office" not in rauvin.status:
        "Přijde k tobě Rauvin s listem papíru v ruce."
        if "less deals checked" in status:
            if gender == "M":
                $ rauvin.say("Mistr Njal ti tady posílá seznam jmen. Týká se to myslím těch podezřelých obchodů, které jsi prověřoval.")
            else:
                $ rauvin.say("Mistr Njal ti tady posílá seznam jmen. Týká se to myslím těch podezřelých obchodů, které jsi prověřovala.")
        else:
            $ rauvin.say("Mistr Njal ti tady posílá nějaký seznam jmen.")
        if "AML" in lotte.asked:
            $ mc.say("Už ho možná nebudu potřebovat, ale díky.")
        else:
            $ mc.say("Výborně, díky.")
        if "less deals checked" not in status:
            "Rauvin povytáhne obočí."
            $ rauvin.say("O co vlastně jde?")
            if gender == "M":
                $ mc.say("Mistr Njal má v poslední době zvláštní problémy s nákupy materiálu, tak jsem chtěl prověřit, jestli to není snaha poškodit ševcovský cech jako celek. Njal mi slíbil seznam obchodníků, kteří mu odmítli něco prodat.")
            else:
                $ mc.say("Mistr Njal má v poslední době zvláštní problémy s nákupy materiálu, tak jsem chtěla prověřit, jestli to není snaha poškodit ševcovský cech jako celek. Njal mi slíbil seznam obchodníků, kteří mu odmítli něco prodat.")
            if "AML" in lotte.asked:
                if gender == "M":
                    $ rauvin.say("To rozhodně za prověření stojí. Co jsi zatím zjistil?")
                else:
                    $ rauvin.say("To rozhodně za prověření stojí. Co jsi zatím zjistila?")
            else:
                $ rauvin.say("To rozhodně za prověření stojí. Můžu ten seznam rovnou předat našim lidem, ať se nezdržuješ obcházením většího množství lidí.")
        else:
            if "AML" in lotte.asked:
                if gender == "M":
                    $ rauvin.say("Co jsi zatím zjistil?")
                else:
                    $ rauvin.say("Co jsi zatím zjistila?")
        if "AML" in lotte.asked:
            show mcPic at menuImage
            menu:
                "Podle Karstenovy ženy Lotte šlo o instrukce cechmistra Rumelina.":
                    hide mcPic
                    $ rauvin.say("Zmínila i jeho důvody?")
                    $ mc.say("Prý mělo jít o společné nákupy pro cech, ale moc tomu nevěřím. Vůbec to nesedí dohromady.")
                "Vlastně na tom ještě pracuji.":
                    hide mcPic
                    $ rauvin.say("V téhle věci určitě nedělej nic ukvapeného.")
        $ rauvin.say("Hlavně buď v pátrání diskrétní a informuj mě o pokroku. Nekalé obchody většinou vedou k bohatým a vlivným lidem.")
    else:
        "Přijde k tobě Solian s papírem v ruce."
        if "less deals checked" in status:
            if gender == "M":
                $ solian.say("Chápu správně, že jsi otravoval mistra Njala tím podezřením na změny v obchodech?", "angry")
            else:
                $ solian.say("Chápu správně, že jsi otravovala mistra Njala tím podezřením na změny v obchodech?", "angry")
            if "less deals" in solian.asked:
                $ solian.say("Neříkal jsem ti, že by to měl řešit především cech samotný?", "angry")
            show mcPic at menuImage
            menu:
                "Rauvin by to chtěl vyšetřit." if "less deals" in solian.asked:
                    hide mcPic
                    if gender == "M":
                        $ solian.say("Říká někdo, kdo ho zná dva dny. Rauvin by ti hlavně řekl, abys byl opatrný a nešlápnul někomu na kuří oko.", "angry")
                    else:
                        $ solian.say("Říká někdo, kdo ho zná dva dny. Rauvin by ti hlavně řekl, abys byla opatrná a nešlápla někomu na kuří oko.", "angry")
                    $ solian.say("A především, Rauvin tu teď není a my ostatní musíme řešit nejdřív ty případy, na kterých záleží někomu důležitému. Jinak bychom taky mohli mít ještě míň lidí a zdrojů, než máme teď.")
                "Rauvin mě pověřil, ať to vyšetřím." if "less deals" not in solian.asked:
                    hide mcPic
                    if gender == "M":
                        $ solian.say("To je možné. A také ti určitě řekl, že máš být opatrný a nešlápnout někomu na kuří oko.", "angry")
                    else:
                        $ solian.say("To je možné. A také ti určitě řekl, že máš být opatrná a nešlápnout někomu na kuří oko.", "angry")
                    $ solian.say("A především, Rauvin tu teď není a my ostatní musíme řešit nejdřív ty případy, na kterých záleží někomu důležitému. Jinak bychom taky mohli mít ještě míň lidí a zdrojů, než máme teď.")
                "Mistr Njal mne požádal o pomoc.":
                    hide mcPic
                    "Solian se zamračí."
                    $ solian.say("Pak měl radši požádat hlídku jako celek.", "angry")
                    if gender == "M":
                        $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrný, abys proti hlídce nepoštval někoho důležitého. Nebo abys nezanedbával ztracené dílo mistra Heinricha.", "angry")
                    else:
                        $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrná, abys proti hlídce nepoštvala někoho důležitého. Nebo abys nezanedbávala ztracené dílo mistra Heinricha.", "angry")
        else:
            $ solian.say("Mistr Njal ti tady posílá seznam jmen. Nechápu ale, jak to souvisí s krádeží u mistra Heinricha.", "angry")
            show mcPic at menuImage
            menu:
                "Vyšetřuji podezřelé změny v obchodech týkající se celého ševcovského cechu.":
                    hide mcPic
                    $ mc.say("Je možné, že ta krádež je součástí snahy poškodit celý cech.")
                    $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc. Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.", "angry")
                    show mcPic at menuImage
                    menu:
                        "Budu na to myslet.":
                            hide mcPic
                            "Solian kývne, podá ti list se jmény a vrátí se zas ke své práci."
                        "Pokud tu dochází ke zločinu, budu ho řešit.":
                            hide mcPic
                            if gender == "M":
                                $ solian.say("Hlavně buď opatrný a nestrkej do ničeho zbytečně prsty.", "angry")
                            else:
                                $ solian.say("Hlavně buď opatrná a nestrkej do ničeho zbytečně prsty.", "angry")
                "Nejspíš nijak, ale mistr Njal mne požádal o pomoc.":
                    hide mcPic
                    "Solian se zamračí."
                    $ solian.say("Pak měl radši požádat hlídku jako celek.", "angry")
                    if gender == "M":
                        $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrný, abys proti hlídce nepoštval někoho důležitého. Nebo abys nezanedbával ztracené dílo mistra Heinricha.", "angry")
                    else:
                        $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrná, abys proti hlídce nepoštvala někoho důležitého. Nebo abys nezanedbávala ztracené dílo mistra Heinricha.", "angry")
    $ status.remove("awaiting AML merchant list")
    $ status.append("AML merchant list delivered")
    $ time.addMinutes(5)
    return

label guarhouseHeinrichComplained:
    if "out of office" not in rauvin.status:
        $ status.append("heinrich complained")
        if gender == "M":
            "Rauvin na tebe ještě z dálky mávne a ukáže směrem k té místnosti, ve které jsi dřív mluvil s mistrem Heinrichem. Tváří se ještě vážněji než obvykle a už to samo o sobě tě dokáže znervóznit."
        else:
            "Rauvin na tebe ještě z dálky mávne a ukáže směrem k té místnosti, ve které jsi dřív mluvila s mistrem Heinrichem. Tváří se ještě vážněji než obvykle a už to samo o sobě tě dokáže znervóznit."
        scene bg interviewroom
        if gender == "M":
            $ rauvin.say("Měl bys vědět, že tady byl mistr Heinrich a stěžoval si na tebe.", "angry")
        else:
            $ rauvin.say("Měla bys vědět, že tady byl mistr Heinrich a stěžoval si na tebe.", "angry")
        $ heinrichComplaint = "Prý se k němu nechováš s dostatečným respektem"

        python:
            if "not reliable" in status:
                heinrichComplaint += ", nedá se na tebe spolehnout"
            if "alcoholic" in eckhard.asked or "alcoholic" in salma.asked or "alcoholic" in lisbeth.asked:
                heinrichComplaint += ", kladeš naprosto zbytečné otázky"
            if "secret lover" in victim.asked or "relationship" in victim.asked:
                heinrichComplaint += ", strkáš nos do věcí, do kterých ti nic není,"
            if gender == "M":
                heinrichComplaint += " a měl by sis víc hledět své práce."
            else:
                heinrichComplaint += " a měla by sis víc hledět své práce."

        $ rauvin.say("%(heinrichComplaint)s.")
        if rauvin.trust > 4:
            $ rauvin.say("Já jsem s tebou zatím spokojený, ale i tak bych ti radil mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
        elif hayfa.trust > 4:
            $ rauvin.say("Hayfa je přesvědčená, že pro nás budeš cenná posila, ale tím spíš bych ti radil mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
        elif rauvin.trust < -4:
            $ rauvin.say("A abych byl upřímný, já sám s ním zatím musím spíš souhlasit. Čekal jsem od tebe výrazně lepší práci. Máš ještě čas s tím něco udělat, ale městská hlídka si potřebuje pověst zlepšit a ne ještě zbytečně provokovat vlivné mistry.")
        else:
            $ rauvin.say("Radil bych ti mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
    else:
        if gender == "M":
            "Solian rázným krokem přijde až k tobě, popadne tě za paži a odvede tě do hloubi strážnice. Na krátký okamžik zaváháš, zda to má být zatčení, dojdete však pouze do místnosti, v níž jsi předtím mluvil s Heinrichem."
        else:
            "Solian rázným krokem přijde až k tobě, popadne tě za paži a odvede tě do hloubi strážnice. Na krátký okamžik zaváháš, zda to má být zatčení, dojdete však pouze do místnosti, v níž jsi předtím mluvila s Heinrichem."
        scene bg interviewroom
        $ solian.say("Byl tady mistr Heinrich. Jak se to k němu prosím tě chováš?", "angry")
        $ heinrichComplaint = "Prý vůbec nemáš respekt"

        python:
            if "not reliable" in status:
                heinrichComplaint += ", není na tebe spolehnutí"
            if "alcoholic" in eckhard.asked or "alcoholic" in salma.asked or "alcoholic" in lisbeth.asked:
                heinrichComplaint += ", ptáš se na úplné zbytečnosti"
            if "secret lover" in victim.asked or "relationship" in victim.asked:
                heinrichComplaint += ", strkáš nos do věcí, do kterých ti nic není,"
            if gender == "M":
                heinrichComplaint += " a měl by sis víc hledět své práce."
            else:
                heinrichComplaint += " a měla by sis víc hledět své práce."

        $ solian.say("%(heinrichComplaint)s.")
        $ solian.say("Uvědomuješ si, že ten člověk si velmi dobře rozumí s purkmistrem a sám se možná za pár dní stane cechmistrem? Vážně chceš, aby zrovna on měl pocit, že nestojíme za nic a přesně tolik by nám město mělo platit?", "angry")
        $ solian.say("Tohle musíš nějak napravit. Zkus se mu omluvit nebo pro něj něco udělat, nebo pokud možno konečně najdi ty zatracené boty nebo aspoň toho, kdo mu je sebral. A hlavně si prosím dávej pořádný pozor na pusu.", "angry")
    $ status.append("victim expects apology")
    return

label zeranWitnessesChecked:
    if "out of office" not in rauvin.status:
        "Dojde za tebou Rauvin."
        $ rauvin.say("Nechal jsem prověřit Zeranovu práci v noc krádeže a nevidím v jeho výpovědi žádné nesrovnalosti.")
        $ rauvin.say("Janis ho na tu noc skutečně najal na čištění žump a do rána byla práce odvedená. Francek skutečně pracoval nedaleko a matně si vzpomíná, že Zerana v noci potkal, i když spolu nemluvili.")
    else:
        "Dojde za tebou Solian."
        if gender == "M":
            $ solian.say("Jak jsi chtěl prověřit Zeranovy údajné svědky, tak nejsou schopní říct nic konkrétního.")
        else:
            $ solian.say("Jak jsi chtěla prověřit Zeranovy údajné svědky, tak nejsou schopní říct nic konkrétního.")
        $ solian.say("Janis ho na tu noc opravdu najal na čištění žump a do rána byla práce odvedená, nic jiného neví. Francek skutečně pracoval poblíž a prý Zerana možná v noci potkal, ale nemluvili spolu.")
        $ mc.say("Takže jeho výpověď se potvrdila?")
        $ solian.say("Možná. Ale pevný důkaz to není. Francek si není úplně jistý a stejně není dost důvěryhodný, aby jen jeho slovo stačilo.")
        show mcPic at menuImage
        menu:
            "To je dobré vědět, díky.":
                hide mcPic
                "Solian kývne a vrátí se ke své práci."
            "Zajímá mě pravda, ne důvěryhodnost.":
                hide mcPic
                $ solian.trust -= 1
                $ solian.say("Tak zkus nezapomenout, že pravda pak musí ještě obstát u soudu.")
    $ status.remove("zeran witnesses")
    $ status.append("zeran witnesses checked")
    return

label helpWithAml:
    $ helpAsked += 1
    $ rauvin.trust += 1
    $ hayfa.trust += 1

    if "out of office" not in rauvin.status: # asking Rauvin
        $ rauvin.say("Pravděpodobně ano, ale teď před slavnostmi je spousta práce. O jaké obchody jde a proč by měly být důležité?")
    else: # asking Solian
        $ solian.say("O jaké obchody jde a jak souvisí se ztracenými botami mistra Heinricha?", "angry")


        if "less deals" in njal.asked:
            $ mc.say("Mistr Njal má v posledních dvou týdnech problém uzavřít obchod na nákup materiálu, který potřebuje na výrobu vlastního díla na Einionovy slavnosti. Několik obchodníků mu potřebné věci odmítlo prodat dost náhle, po slibně působícím rozhovoru.")
            show mcPic at menuImage
            menu:
                "Mistr Njal navíc pracoval na stejném typu bot jako mistr Heinrich." if "police business" in njal.asked:
                    hide mcPic
                "Je to už druhý mistr, kterému někdo brání se na slavnostech prezentovat.":
                    hide mcPic
                    $ mc.say("Mohla by to být snaha poškodit celý cech.")
                "Svoje obchody navíc skrývá nebo přesouvá i cechmistr Rumelin.":
                    hide mcPic
                    $ mc.say("Podle Salmy uzavírá méně smluv na drahý materiál, ale smlouvy na prodej zůstávají stejné.")

            if "out of office" not in rauvin.status: # Rauvin
                $ rauvin.say("Je pravda, že to by mohlo stát za prověření. Nechám někoho zjistit, jestli ti obchodníci odmítají prodávat materiál i jiným ševcovským mistrům. Víš, o které by mělo jít?")
                if "awaiting AML merchant list" in status:
                    if gender == "M":
                        $ mc.say("Ano, požádal jsem mistra Njala o seznam.")
                    else:
                        $ mc.say("Ano, požádala jsem mistra Njala o seznam.")
                    $ rauvin.say("Výborně, někdo ty obchodníky prověří.")
                else:
                    $ mc.say("Z hlavy si mistr Njal vzpomněl na Karstena a Roviena.")
                    $ rauvin.trust -=1
                    $ hayfa.trust -= 1
                    $ rauvin.say("Kdybychom je znali všechny, usnadnilo by to našim lidem práci, ale dva jsou asi lepší než nic. Nechám někoho, aby se poptal.")
                $ status.append("add investigating less deals")
            else: # Solian
                "Solian se zamračí."
                $ solian.say("A mistr Njal chce, aby to řešila hlídka? Neměl by to spíš řešit cech sám?", "angry")
                show mcPic at menuImage
                menu:
                    "Ano, Njal mne požádal, abychom to prověřili.":
                        hide mcPic
                        $ solian.say("Pak měl ideálně jít za hlídkou jako celkem, ale možná měl takhle před slavnostmi spoustu práce.")
                        $ solian.say("Dobře, zkusím se nějak opatrně poptat. Víš, kteří obchodníci Njala odmítli?")
                    "Já myslím, že bychom to řešit měli.":
                        hide mcPic
                        $ mc.say("Tohle by snadno mohla být cílená snaha Njala poškodit a to je určitě zločin.")

        else:
            $ mc.say("Mistr Njal má podle Salmy najednou problém uzavřít obchody a mistr Rumelin uzavírá méně smluv na drahý materiál. Zajímavé je, že smlouvy na prodej zůstávají stejné.")
            $ mc.say("Tak přemýšlím, jestli to spolu s krádeží výrobku, který chtěl mistr Heinrich představit na slavnostech, nemůže ukazovat na snahu poškodit ševcovský cech jako celek.")

            if "out of office" not in rauvin.status: # Rauvin
                "Rauvin se zamračí a zamyslí."
                $ rauvin.say("To opravdu zní trochu zvláštně. Možná to nic neznamená, ale pro jistotu nechám někoho zjistit, jestli se jen nepřesunuli do jiné hospody. A jestli mistr Rumelin pořád prodává zboží, které drahý materiál potřebuje.")
                $ status.append("add investigating less deals")
            else: # Solian
                "Solian se zamračí."
                $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc.", "angry")
                $ solian.say("Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.")
                show mcPic at menuImage
                menu:
                    "To dává smysl, radši do toho nebudu šťourat.":
                        hide mcPic
                        $ solian.say("Jsem rád, že to chápeš.", "happy")
                    "Pokud tu dochází ke zločinu, měli bychom to řešit.":
                        hide mcPic
                        $ solian.trust -= 1
                        $ solian.say("Já bych měl radši jistotu, že budeme mít možnost řešit zločiny i za měsíc. Mimo jiné proto, že nechci přijít o práci. Samozřejmě nevím, jak to vidíš ty...")
                        show mcPic at menuImage
                        menu:
                            "Máš pravdu, radši to nechám být.":
                                hide mcPic
                                $ solian.say("Výborně, jsem rád, že jsme se shodli.", "happy")
                            "Máš jistotu, že až se vrátí Rauvin, uvidí to stejně?":
                                hide mcPic
                                $ solian.say("Rauvin je občas zatracený...", "angry")
                                $ solian.say("No dobře, nějak to ověřím. Hlavně do té doby neudělej žádnou hloupost, která by někoho naštvala.")
                                $ status.append("add investigating less deals solian")
                    "I tak mi přijde bezpečnější to prověřit.":
                        hide mcPic
                        $ mc.say("Už kvůli tomu, aby to nevypadalo, že jsme něco zanedbali.")
                        $ mc.say("Nebo máš naprostou jistotu, že by to Rauvin nechal být?")
                        $ solian.say("Rauvin je občas zatracený...", "angry")
                        $ solian.say("No dobře, nějak to ověřím. Hlavně do té doby neudělej žádnou hloupost, která by někoho naštvala.")
                        $ status.append("add investigating less deals solian")

    $ time.addMinutes(10)
    return

label helpWithZeranWitnesses:
    $ mc.say("Janis ho prý najal na čištění žump nedaleko západní brány.")
    $ mc.say("A spolu s ním tam měl pracovat ještě Francek.")
    if "out of office" not in rauvin.status:
        $ rauvin.say("To by mělo být snadné ověřit. Pošlu někoho, aby se jich zeptal.")
    else:
        $ solian.say("To nebude problém ověřit, zařídím to.")
    $ status.append("add zeran witnesses")
    $ time.addMinutes(3)
    return

label industrialEspionage:
    $ solian.asked.append("industrial espionage")
    $ solian.say("Záznamy se pečlivě uchovávají. Ale není dovolené si je jen tak prohlížet, někomu by mohlo vadit, kdybychom jen tak pro zábavu štourali do jeho obchodů. Proč se o ně zajímáš?")
    show mcPic at menuImage
    menu:
        "Kvůli dobrým vztahům s jednou osobou, se kterou jsem se seznámil." if gender == "M":
            call industrialEspionageGoodRelations
        "Kvůli dobrým vztahům s jednou osobou, se kterou jsem se seznámila." if gender == "F":
            call industrialEspionageGoodRelations
        "Požádala mě o to Lotte, žena obchodníka Karstena.":
            hide mcPic
            $ solian.say("S tou je určitě dobré se přátelit. Dobře, zjistím, co potřebuje, a předám jí to.")
            $ solian.say("Ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "Potřebuji to, abych dokázal pomoct té tanečnici s ohněm." if gender == "M":
            call industrialEspionageHelpKatrin
        "Potřebuji to, abych dokázala pomoct té tanečnici s ohněm." if gender == "F":
            call industrialEspionageHelpKatrin
    $ time.addMinutes(10)
    return

label industrialEspionageGoodRelations:
    hide mcPic
    $ solian.say("Chápu. O koho jde?")
    show mcPic at menuImage
    menu:
        "O Lotte, ženu obchodníka Karstena.":
            hide mcPic
            $ solian.say("S tou je určitě dobré se přátelit. Dobře, zjistím, co potřebuje, a předám jí to.")
            $ solian.say("Ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "To bych si radši nechal pro sebe." if gender == "M":
            hide mcPic
            $ solian.say("Jak myslíš. V tom případě ale nemám důvod ti s něčím takhle nebezpečným pomáhat.", "angry")
        "To bych si radši nechala pro sebe." if gender == "F":
            hide mcPic
            $ solian.say("Jak myslíš. V tom případě ale nemám důvod ti s něčím takhle nebezpečným pomáhat.", "angry")
    return

label industrialEspionageHelpKatrin:
    hide mcPic
    $ solian.say("Vážně chceš kvůli ní dělat něco podobně nebezpečného? Jestli se na to přijde, velitel Galar tě okamžitě vyhodí z hlídky a nejspíš skončíš přinejmenším na pranýři. On velitel nebývá moc vidět, ale zrovna překračování pravomocí opravdu nestrpí.", "angry")
    $ solian.say("A jak jí to vůbec pomůže? Chceš tím někoho uplatit, aby se jí zastal?", "angry")
    show mcPic at menuImage
    menu:
        "Ano, Lotte z ulice, kde bydlí mistr Heinrich.":
            hide mcPic
            $ solian.trust += 1
            $ solian.say("No dobře, zrovna ta to snad vezme spíš jako začátek přátelského vztahu, než aby zůstala u té jedné pomoci a pak nás už nechtěla znát.")
            $ solian.say("Zjistím, co potřebuje, a předám jí to. A ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "Do toho ti nic není.":
            hide mcPic
            $ solian.trust -= 2
            $ solian.say("Jak myslíš. V tom případě ale nemám důvod ti s něčím takhle nebezpečným pomáhat.", "angry")
        "Máš pravdu, nestojí to za to.":
            hide mcPic
            $ solian.trust += 1
            $ solian.say("Těší mě, že to tak vidíš. Když už podstupovat podobné nebezpečí, mělo by to být pro něco odpovídajícího.")
            $ solian.say("Nemůžeme pomoct každému, kdo to potřebuje. Na to nás není dost a příliš pozorně nás hlídají.")
    return

label arrestZeranStolenIdeaConvinced:
    hide mcPic
    $ rauvin.trust -= 3
    $ mc.cluesAgainst += 1
    "Rauvin se zamračí."
    $ rauvin.say("A to ti připadá jako dostatečný důvod?", "angry")
    if gender == "M":
        $ rauvin.say("Jestli nemáš důkazy, proč si jsi tak jistý?")
    else:
        $ rauvin.say("Jestli nemáš důkazy, proč si jsi tak jistá?")
    $ mc.say("Kdo jiný by to udělal? Zeran měl důvod si Heinricha chtít udobřit a neměl moc jiných možností, jak to udělat.")
    $ mc.say("Navíc jeho noví kamarádi mu něco podobného klidně mohli vnuknout.")
    $ rauvin.say("Jací noví kamarádi?")
    $ mc.say("No vždyť víte. V dočasné čtvrti je určitě spousta pochybných osob.")
    $ mc.say("My víme, že Zeran přijal útočiště u Sabriho, který na něj podle všeho má velký vliv. Ten říká, že když člověk něco chce, má si to prostě vzít.")
    $ rauvin.say("To říká i Hayfa.")
    $ mc.say("No ano, ale u ní to hlavně znamenalo dostat se do hlídky a získat si její důvěru. Ale Zeran hlídce každým slovem nadává. Od toho těžko můžeme čekat, že najde zápal pro nějakou dobrou věc.")
    $ rauvin.say("A jak vysvětluješ, že Heinrich měl střih v rukou, ale Zerana zpátky nepřijal?")
    $ mc.say("Jednoduše, je na Zerana opravdu naštvaný, dceru chce ze všech sil chránit.")
    $ rauvin.say("Takže když to shrnu, chceš zatknout Zerana, protože se ti nelíbí, kdo mu jako jediný nabídl střechu nad hlavou. Důkazy nemáš, ale předpokládáš, že mu po dvou letech v Heinrichově učení nedošlo, jestli pro něj bude důležitější ukradený střih, nebo bezpečí jeho dcery.")
    $ rauvin.say("Pochopil jsem to správně?")
    $ mc.say("No, ano. My nad tím můžeme uvažovat s chladnou hlavou, ale Zeran je na to příliš v zajetí pocitu, jak mu všichni ublížili.")
    $ rauvin.say("Chápu.")
    $ rauvin.say("Aby tedy bylo jasno, my tu nejsme od toho, abychom posílali lidi k soudu jen na základě pocitů nebo domněnek. Potřebujeme pořádné důkazy. Ty tvoje by nám soud smetl se stolu, a jestli ne, bylo by to jeho selhání a jeho ostuda úplně stejně jako naše.", "angry")
    $ rauvin.say("Už vůbec potom nikoho neposíláme k soudu za to, že někdo má určitě podezřelé kamarády. To není důkaz, to by bylo souzení ostatních jen proto, že se nám na nich něco nelíbí. A toho už v Marendaru bylo dost.", "angry")
    if mc.cluesAgainst > 1:
        $ rauvin.say("O něčem podobném už jsme ale mluvili. Doufal jsem, že se poučíš, ale nestalo se. Někoho takového si v hlídce nemůžu dovolit držet.")
        $ rauvin.say("Prosím, vrať svůj glejt.")
        $ rauvin.say("Hodně štěstí při hledání jiné práce.")
        jump thrownOut
    $ rauvin.say("Ve skutečnosti nemám radost z toho, že to vůbec navrhuješ. Uvědom si, že by to mělo následky. V lepším případě by se u soudu ukázalo, že se nám nedá důvěřovat a nejsme o nic lepší než hlídka za Velina, a v horším by to Zeranovi zničilo život ještě víc.", "angry")
    $ rauvin.say("Podobného způsobu přemýšlení se musíš co nejdřív zbavit. Ten do hlídky nepatří.", "angry")
    show mcPic at menuImage
    menu:
        "Díky za vysvětlení. Polepším se.":
            hide mcPic
            $ rauvin.say("O tom nepochybuji.")
        "Připadá mi, že si toho o sobě nějak moc myslíš.":
            hide mcPic
            $ rauvin.trust -= 3
            $ rauvin.say("Myslím si o sobě, že jsem tvůj velitel. Můžeš to přijmout, nebo odejít.")
            show mcPic at menuImage
            menu:
                "Jistě, omlouvám se.":
                    hide mcPic
                    $ rauvin.say("V pořádku.")
                "S takovýmto velitelem v jedné hlídce být nechci.":
                    hide mcPic
                    $ rauvin.say("Dobrá, v tom případě prosím vrať glejt a já ti popřeji hodně štěstí při hledání jiné práce.")
                    jump thrownOut
    if gender == "M":
        $ rauvin.say("Samozřejmě ale oceňuji, že ses nejdřív přišel zeptat, jestli zatknout Zerana je dobrý nápad. To je správný postup.")
    else:
        $ rauvin.say("Samozřejmě ale oceňuji, že ses nejdřív přišla zeptat, jestli zatknout Zerana je dobrý nápad. To je správný postup.")
    $ rauvin.say("Potřebujeme ještě něco probrat, nebo se teď vrátíš k případu?")
    return

label arrestZeranStolenNjalInsists:
    hide mcPic
    $ rauvin.trust -= 3
    $ mc.cluesAgainst += 1
    "Rauvin se zamračí."
    $ rauvin.say("A to ti připadá jako dostatečný důvod?", "angry")
    $ mc.say("Ne u každého, ale tady mluvíme o řemeslnickém mistru a Zeran to klidně mohl udělat. Dost pochybuji, že bude mít nějaké důkazy o své nevině.")
    $ rauvin.say("A právě proto nikoho nezatýkáme bez důkazů!", "angry")
    show mcPic at menuImage
    menu:
        "Proč ne? Tak se to přece dělá všude.":
            hide mcPic
            $ rauvin.say("Ale ne tady! A jestli to tak bylo vždycky, tak teď už ne. Teď platí rovnost před zákonem!", "angry")
            if gender == "M":
                $ mc.say("Tomu nerozumím. Všiml jsem si, jak moc je pro vás důležité dobré jméno u vážených osob. Už jenom ten rozdíl, jak jste hned první den mluvil se mnou a potom s mistrem Heinrichem, byl opravdu výrazný.")
            else:
                $ mc.say("Tomu nerozumím. Všimla jsem si, jak moc je pro vás důležité dobré jméno u vážených osob. Už jenom ten rozdíl, jak jste hned první den mluvil se mnou a potom s mistrem Heinrichem, byl opravdu výrazný.")
            $ rauvin.say("Ctít něčí společenské postavení přece neznamená ohýbat kvůli nim zákony!", "angry")

            if any("careful of the rich" in str for str in status):
                if "careful of the rich - lover" in status:
                    $ mc.say("Když jsme ale mluvili o možném milenci paní Lisbeth, kladl jste mi na srdce, že mám na jejich postavení brát ohled. U nikoho jiného jste po mně takovou opatrnost nechtěl.")
                $ mc.say("Jestli mám někoho vyšetřovat obzvlášť opatrně a u jiného to je jedno, tak to přece jasně říká, že na každého platí zákony jinak.")
                $ rauvin.say("Neříká! Vždycky chceme případ pochopit tak do hloubky, jak to jen jde. Jediný rozdíl je v tom, že bohatší lidé mají víc možností, jak nám v tom překážet.", "angry")

            $ rauvin.say("Zatýkat lidi jen proto, že to klidně mohli udělat, to si nemůžeme dovolit. A nemůžeme si dovolit hlídkaře, kteří to navrhují.", "angry")
            $ rauvin.say("“Prosím, vrať svůj glejt.")
            $ rauvin.say("Zkus štěstí v nějaké práci, kde nerozhoduješ o ostatních.")
            jump thrownOut
        "Chápu. Asi bych měl jít hledat důkazy." if gender == "M":
            call goFindEvidence
        "Chápu. Asi bych měla jít hledat důkazy." if gender == "F":
            call goFindEvidence

    return

label goFindEvidence:
    hide mcPic
    if mc.cluesAgainst < 2:
        if gender == "M":
            $ rauvin.say("To bys měl. Opravdové důkazy, ne to, že někdo nebude nikomu chybět nebo se ti nelíbí.", "angry")
        else:
            $ rauvin.say("To bys měla. Opravdové důkazy, ne to, že někdo nebude nikomu chybět nebo se ti nelíbí.", "angry")
        $ rauvin.say("A prosím, přemýšlej příště nad tím, jestli tvůj návrh nemůže ublížit někomu, kdo je možná nevinný. My nejsme utlačovatelská hlídka. A nemůžeme si tu dovolit nikoho, kdo jako utlačovatel přemýšlí.")
    else:
        $ rauvin.say("Ve skutečnosti ne.", "angry")
        $ rauvin.say("Tohle není první případ, kdy spolu o něčem podobném mluvíme. Doufal jsem, že si z toho napoprvé něco vezmeš, ale nestalo se. Někoho takového si v hlídce nemůžeme dovolit mít.", "angry")
        $ rauvin.say("“Prosím, vrať svůj glejt.")
        $ rauvin.say("Hodně štěstí při hledání nové práce.")
        jump thrownOut
    return

label nervousSolian:
    "Strážnicí prostupuje výrazný pocit nejistoty. Ačkoli se hlídkaři snaží plnit své každodenní povinnosti, často na sebe navzájem vrhají tázavé pohledy a pak je hned odvrací. Znepokojení je znát i z tichých rozhovorů, které občas zaslechneš."
    "Jakmile tě spatří Solian, pokyne ti, abys ho následoval do jedné z menších místností."
    scene bg interviewRoom
    "Nesedne si, jen zavře a rovnou se začne vyptávat."
    $ solian.say("Jak postupuje tvůj případ? Slavnosti jsou skoro tady, potřebujeme někoho zatknout nejpozději zítra v poledne. Máme někoho?")

    label nervousSolianOptions:
    show mcPic at menuImage
    menu:
        "Neměl by se mnou tohle řešit Rauvin?" if "nervous - Rauvin" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Rauvin")
            $ solian.say("Měl, ale ten tady není a kdo ví, kdy se zase vrátí. Já ti budu muset stačit.", "angry")
            $ solian.say("Jestli se ti nelíbí, že mi všechno budeš muset vysvětlovat od začátku, můžeš si na něj stěžovat u velitele.", "angry")
            jump nervousSolianOptions
        "Co se stalo s Rauvinem?" if "nervous - Rauvin 2" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Rauvin 2")
            $ solian.say("To pořád ještě nikdo pořádně neví. Prostě tady není.", "angry")
            $ solian.say("Starají se o něj v hospici a je u něj jeho sestra, takže my se můžeme soustředit na naši práci.")
            jump nervousSolianOptions
        "Kam vlastně jela Hayfa?" if "nervous - Hayfa" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Hayfa")
            $ solian.say("Nevím a nezajímá mě to. Pro mě je důležité zajistit, aby hlídka splnila svoje povinnosti, a to dokážeme i bez ní.", "angry")
            jump nervousSolianOptions
        "Proč to tak spěchá? Nemůžeme vyšetřovat ještě pár dní?" if "nervous - hurry" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - hurry")
            $ solian.trust -= 2
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ solian.say("Proč asi. Jestli začnou slavnosti a mistr Heinrich ani nebude mít výrobek, ani nebude probíhat soud za jeho krádež nebo zničení, bude všem pro smích. A tomu chceme zabránit.", "angry")
            jump nervousSolianOptions
        "Pořád nemám dokonale přesvědčivé důkazy.":
            hide mcpic
            $ solian.asked.append("nervous - no proof")
            $ soliansay("Na přesvědčivé důkazy už nemáme čas. Ty současné budou muset stačit.")
            $ mc.say("Rauvin ale vždycky říkal...")
            $ solian.say("Rauvin tady není. Jsme tady my a my s tím musíme něco provést. Takže koho můžeme zatknout?", "angry")
            $ mc.say("No, jestli ti stačí i částečné důkazy...")
        "Pachatele už naštěstí znám. Věřím, že mám dobré důkazy.":
            hide mcPic
            $ solian.say("No to je skvělá zpráva. Kdo to je?")

    show mcPic at menuImage
    menu:
        "...tak mně tedy ne." if "nervous - no proof" in solian.asked:
            hide mcPic
            $ rauvin.trust += 3
            $ hayfa.trust += 2
            $ solian.trust -= 2
            $ solian.say("A co tedy chceš dělat? Říct mistru Heinrichovi, že jsme to nezvládli?", "angry")
            $ mc.say("Lepší než zatknout někoho, proti komu nemáme dostatečné důkazy.")
            $ solian.say("V tom případě se běž vrátit k případu a koukej ty svoje dostatečné důkazy hodně rychle najít.", "angry")
            if gender == "M":
                $ solian.say("Jestli mi do zítřejšího poledne nedokážeš říct, koho můžeme zatknout, bude to znamenat, že ses neosvědčil. Určitě dokážeš domyslet, co to pro tvoje další působení v hlídce znamená.")
            else:
                $ solian.say("Jestli mi do zítřejšího poledne nedokážeš říct, koho můžeme zatknout, bude to znamenat, že ses neosvědčila. Určitě dokážeš domyslet, co to pro tvoje další působení v hlídce znamená.")
            show mcPic at menuImage
            menu:
                "Vynasnažím se.":
                    hide mcPic
                    $ solian.say("To je dobře. A teď už se nenech zdržovat.")
                "Co když se ty důkazy prostě nedají najít? Nemůžete mě přece vyhodit z hlídky kvůli jednomu případu.":
                    hide mcPic
                    $ solian.say("Věř tomu, že můžeme.", "angry")
                    $ solian.say("A teď už se nenech zdržovat.", "angry")
                "O tom, kdo zůstane v hlídce, ty přece nijak nerozhoduješ.":
                    hide mcPic
                    $ solian.trust -= 1
                    $ solian.say("Já jsem v hlídce dva roky. Ty dva nebo tři dny. Troufám si tvrdit, že rozumím lépe než ty tomu, jak to tady chodí.", "angry")
                    $ solian.say("Přijmi teď tedy mou dobrou radu a nenech se už zdržovat.", "angry")
        "Můžeme zatknout mistra Kaspara." if "confession" in kaspar.asked:
            hide mcPic
            if gender == "M":
                $ solian.say("Jseš si jistý? Je to vážený mistr a navíc se možná bude ucházet o místo cechmistra. Musíme si být opravdu jistí, než ho z čehokoli obviníme.")
            else:
                $ solian.say("Jseš si jistá? Je to vážený mistr a navíc se možná bude ucházet o místo cechmistra. Musíme si být opravdu jistí, než ho z čehokoli obviníme.")
            $ mc.say("Sám se mi přiznal, že v dílně mistra Heinricha byl a že jeho boty zničit chtěl. Doufal, že ho tím znemožní právě před tou volbou cechmistra, do které se chtěli hlásit oba.")
            $ solian.say("To ale před soudem nezopakuje. Vždyť tím by znemožnil hlavně sám sebe. Je proti němu i jiný důkaz?", "angry")
            $ mc.say("Paní Lisbeth ho do té dílny sama pustila. Namluvil jí, že si boty chce jen prohlédnout.")
            $ solian.say("Tohle ale nemůžeme vzít k soudu. Uvědomuješ si, co by z toho bylo za řeči? To by popudilo nejen Kaspara a Heinricha, ale ve výsledku možná i Rumelina, protože by celý cech byl městu pro smích.", "angry")
            $ solian.say("Trochu času ještě zbývá. Najdi někoho jiného, na kom je dost silné podezření.")
            $ solian.say("Mistra Kaspara zatknout nemůžeme. Ostatně to, že v dílně byl, ještě neznamená, že s botami opravdu něco určitě provedl.", "angry")
        "Můžeme zatknout Gerda." if ("fired apprentices" in clues and "which apprentice" in liese.asked) or "workshop visit" in gerd.asked:
            hide mcPic
            $ mc.say("To je učedník mistra Njala, který byl dřív v učení u mistra Heinricha.")
            if "workshop visit" in gerd.asked:
                $ mc.say("Přiznal se, že v té dílně tu noc byl.")
            else:
                $ mc.say("Mám svědka, že byl tu noc v dílně.")
            $ solian.say("To je dobré! Ale proč by to dělal?", "surprised")
            $ mc.say("Protože ho Heinrich vyhodil. Sice mu k tomu dal na cestu zbytek peněz zaplacených za vyučení, ale stejně kolem toho určitě bylo hodně zlé krve.")
            $ mc.say("Navíc je Gerd pořádný drzoun, který chce mít vždy poslední slovo.")
            $ solian.say("Dobře, to by mělo obstát. Můžeš ho sebrat.", "happy")
            $ solian.say("Mistr Njal se sice bude vztekat, ale všichni ostatní jen mávnou rukou, že to je stejně jen podivínský trpaslík. To nás nemusí trápit.")
        "Můžeme zatknout mistra Njala s jeho učedníkem." if "workshop visit" in gerd.asked and "workshop visit" in njal.asked:
            hide mcPic
            $ solian.say("Mistra Njala? Je to sice podivínský trpaslík, ale na zatčení mistra potřebujeme hodně pádné důkazy.", "surprised")
            $ mc.say("Oba přiznali, že Gerd tu noc šel do Heinrichovy dílny na Njalův příkaz. Tvrdí, že si hlavně chtěli vzít zpátky střih, podle kterého jsou ty kradené boty ušité a které jim mistr Heinrich prý ukradl.")
            $ mc.say("Ale k čemu je brát mistru Heinrichovi střih, když už má hotové boty? Každý bude předpokládat, že ho má, a on ho podle nich může sestavit znovu.")
            $ mc.say("Mysleli si, že si jen zjednávají spravedlnost, kterou jim městské zákony nikdy nedají.")
            $ solian.say("A myslíš, že to samé budou říkat i před soudem?", "surprised")
            $ mc.say("Myslím, že ano. Oba o tom vypadali hodně přesvědčení.")
            $ solian.say("Nu dobrá. Je pravda, že mistru Heinricha to velmi potěší.")
            $ solian.say("Jen ještě poslední otázka, ví o tom cechmistr Rumelin?")
            if "police business" in njal.asked:
                $ mc.say("Částečně. Njal s ním o ukradeném střihu mluvil, ale o vloupání do dílny už ne, pokud vím.")
            else:
                if gender == "M":
                    $ mc.say("To nevím. Njal to neříkal a s Rumelinem jsem o tom nemluvil.")
                else:
                    $ mc.say("To nevím. Njal to neříkal a s Rumelinem jsem o tom nemluvila.")
            $ solian.say("V tom případě za ním zajdu, aby z toho soudu nebyl překvapený. Mohlo by ho to ukázat ve špatném světle.")
        "Můžeme zatknout Zerana." if zeranNote.isActive == True and zeran.status != "cleared":
            hide mcPic
            $ solian.say("To je kdo?")
            $ mc.say("Bývalý učedník mistra Heinricha. Mistr ho před několika měsíci vyhodil, protože měl podezření, že mu chodí za dcerou.")
            $ solian.say("Jo tenhle! O tom se ve městě hodně mluvilo. Takovéhle zneužití důvěry jsme tady už nějakou dobu neměli.")
            $ solian.say("Ten se určitě chtěl pomstít. Už jednou mistru Heinrichovi zkusil ublížit, taková verbež jako on to ráda zkusí znovu.")
            $ solian.say("To před soudem obstojí a mistr Heinrich bude spokojený.", "happy")
            $ solian.say("Běž ho rovnou zatknout.")
        "Můžeme zatknout žebračku Erle." if "stolen shoes found" in status:
            hide mcPic
            $ solian.say("A uvěří nám to někdo? Ta si nevezme víc peněz než na jídlo na den, i když jí je někdo dává. Proč by něco kradla?", "angry")
            $ mc.say("To nevím, ale měla u sebe lahve s vínem a pálenkou, které se mistru Heinrichovi ztratily také. Možná chtěla ukrást něco k pití a boty vzala z okamžitého nápadu, protože se jí prostě líbily.")
            $ mc.say("Krádež alkoholu si u ní představit dokážu. Co jiného by ji pořád drželo v tak povznesené náladě?")
            $ mc.say("A hlavně věděla, kde ty boty jsou.")
            $ solian.say("No, možná. Pořád se bojím, že by to u soudu mohlo vyvolat podezření. Ale jestli to nemohl udělat nikdo jiný, ona určitě ano.", "angry")
            $ solian.say("Zkus se zamyslet, jestli nenarazíš ještě na něco užitečného. A jestli ne, tak ji zítra seber.")
    return

###

label guardhouseHelpOptionsAvailable:
    $ helpOptionsAvailable = 0
    if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status:
        $ helpOptionsAvailable += 1
    if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status):
        $ helpOptionsAvailable += 1
    return

label solianHelpOptionsAvailable:
    $ solianHelpOptionsAvailable = 0
    if "offered favour" in "lotte asked" and "industrial espionage" not in solian.asked:
        $ solianHelpOptionsAvailable += 1
    return

label guardhouseArrestOptionsAvailable:
    $ arrestOptionsAvailable = 0
    if "confession" in rumelin.asked and rumelin not in arrested and "arrest Rumelin" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    if "confession" in kaspar.asked and kaspar not in arrested:
        $ arrestOptionsAvailable += 1
    if zeranNote.isActive and "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason and "arrest Zeran for stolen idea" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    return
