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

# Intros #

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

###

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

# Options available check #

label guardhouseArrestOptionsAvailable:
    $ arrestOptionsAvailable = 0
    if "confession" in rumelin.asked and rumelin not in arrested and "arrest Rumelin" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    if "confession" in kaspar.asked and kaspar not in arrested:
        $ arrestOptionsAvailable += 1
    if zeranNote.isActive and "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason and "arrest Zeran for stolen idea" not in rauvin.asked:
        $ arrestOptionsAvailable += 1
    return
