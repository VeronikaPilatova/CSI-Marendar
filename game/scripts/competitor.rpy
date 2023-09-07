label kasparController:
    # check if visit makes sense
    call kasparOptionsRemainingCheck
    if optionsRemaining == 0:
        "Nenapadá tě, co dalšího se mistra Kaspara ještě ptát."
        return
    call preludeController

    # walk over
    if kaspar.alreadyMet == False:
        $ time.addMinutes(30)
    else:
        $ time.addMinutes(15)
    $ currentLocation = "kaspar house"
    $ origAsked = kaspar.asked.copy()

    # visit itself
    scene bg kaspar inside
    if kaspar.alreadyMet == False:
        call kasparFirst
    else:
        call kasparAgain
    call kasparOptions
    if "arrest in progress" not in status:
        call leavingKaspar

    # adjust time spent and status
    $ time.addMinutes((len(kaspar.asked) - len(origAsked)) * 3)
    if kaspar.alreadyMet == False:
        $ kaspar.alreadyMet = True
    return

label kasparFirst:
    if "victim house visited" in status and nirevia.alreadyMet == True:
        "Jakmile se představíš, mistr Kaspar tě okamžitě pozve dál. Jeho dům je menší než mistra Heinricha nebo cechmistrův, ale uvnitř je zařízený velmi pohodlně. Krb hoří a před ním je rozvalený pes."
    elif "victim house visited" in status:
        "Jakmile se představíš, mistr Kaspar tě okamžitě pozve dál. Jeho dům je menší než mistra Heinricha, ale uvnitř je zařízený velmi pohodlně. Krb hoří a před ním je rozvalený pes."
    elif nirevia.alreadyMet == True:
        "Jakmile se představíš, mistr Kaspar tě okamžitě pozve dál. Jeho dům je menší než cechmistrův, ale uvnitř je zařízený velmi pohodlně. Krb hoří a před ním je rozvalený pes."
    else:
        "Jakmile se představíš, mistr Kaspar tě okamžitě pozve dál. Jeho dům je menší, ale uvnitř je zařízený velmi pohodlně. Krb hoří a před ním je rozvalený pes."
    $ kaspar.say("Posaďte se. Můžu vám nabídnout pohár medoviny?")
    show mcPic at menuImage
    menu:
        "Omlouvám se, ve službě nepiju.":
            hide mcPic
            $ kaspar.asked.append("no drink")
            $ rauvin.trust += 1
            $ kaspar.say("To samozřejmě chápu. Obdivuhodná zodpovědnost, opravdu.", "happy")
        "Dám si rád, díky. {i}(pořádně si přihnout){/i}" if gender == "M":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
        "Dám si ráda, díky. {i}(pořádně si přihnout){/i}" if gender == "F":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
        "Dám si rád, díky. {i}(předstírat pití){/i}" if gender == "M":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ hayfa.trust += 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
        "Dám si ráda, díky. {i}(předstírat pití){/i}" if gender == "F":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ hayfa.trust += 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
    $ kaspar.say("S čím vám vlastně můžu pomoci?")
    $ mc.say("Vyšetřuji ztrátu mistrovského výrobku z dílny mistra Heinricha.")
    if gender == "M":
        $ kaspar.say("A jste si jistý, že se jedná o krádež?")
    else:
        $ kaspar.say("A jste si jistá, že se jedná o krádež?")
    $ kaspar.say("Nechci roznášet drby nebo pomlouvat kolegu, ale… Heinrich má ve zvyku každý dokončený výrobek opravdu důkladně zapít u Salmy. A pak se může stát ledacos…")
    $ mc.say("Co například?")
    $ kaspar.say("Například bych se nedivil, kdyby Heinrich vzal svůj vzácný výtvor s sebou do hospody a zapomněl na to. Nebo ho třeba omylem nebo ve vzteku zničil. Zeptejte se u Salmy. Nebo ještě lépe jeho ženy, jaký je s ním život, ona ho zná nejlépe.")
    $ mc.say("Zamyslím se nad tím.")
    $ mc.say("Můžu vám ještě položit pár otázek?")
    $ kaspar.say("Samozřejmě, velmi rád pomůžu.")
    return

label kasparAgain:
    "Mistr Kaspar tě pozve dál téměř jako starého přítele a tentokrát ti bez ptaní rovnou podá plný pohár."
    if "drink accepted" in kaspar.asked:
        $ kaspar.say("Na posilněnou. Stejná lahev jako minule, zdálo se mi, že vám chutnala.", "happy")
    else:
        $ kaspar.say("Na osvěžení. Bezová šťáva, protože vím, že vaše práce je náročná a potřebujete si zachovat čistou hlavu.", "happy")
    $ kaspar.say("Nějaké pokroky ve vyšetřování?")
    $ mc.say("Sleduji teď jednu stopu, můžu se vás ještě na pár věcí zeptat?")
    $ kaspar.say("Ale samozřejmě, rád pomůžu.")
    return

label kasparOptions:
    call kasparOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Děkuji vám za pomoc.")
        $ kaspar.say("Rádo se stalo. Pomáhat hlídce je přece naše povinnost.", "happy")
        return

    show mcPic at menuImage
    menu:
        "Je pravda, že máte s mistrem Heinrichem spory?" if "enemies" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("enemies")
            $ kaspar.say("Spíš bych řekl, že spory má on se mnou.")
            $ kaspar.say("Vzal si do hlavy, že bude novým cechmistrem a já mu v tom mám bránit. Přitom je pravděpodobné, že Rumelin svou pozici obhájí.")
        "Takže vy o pozici hlavy cechu neusilujete?" if "enemies" in kaspar.asked and "ambitions" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("ambitions")
            $ kaspar.say("Tak samozřejmě, kdyby se ta pozice přeci jen uvolnila…")
            $ kaspar.say("Myslím, že Rumelin je v čele cechu už příliš dlouho a všichni si zasloužíme změnu. Zvlášť teď, s novou městskou radou s velkými ambicemi. Rumelin měl koneckonců velmi blízko k Velinovi, nejsem si jistý, jak snadno bude s novou radou vycházet.")
            $ mc.say("Všiml jste si nějakých rozporů mezi nimi?")
            $ kaspar.say("Zatím ne, ale městská rada se změnami teprve začíná.")
        "Je někdo jiný, kdo by chtěl mistru Heinrichovi uškodit?" if "enemies" in kaspar.asked and "enemies2" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("enemies2")
            $ kaspar.say("Krádeží jeho mistrovského výrobku? Nikdo takový mne nenapadá. Nebo…")
            "Mistr Kaspar se zamyslí."
            $ kaspar.say("Je hrozné něco takového jen pomyslet, ale pokud bych musel v našem cechu na někoho ukázat… pak by to byl Rumelin.")
            $ kaspar.say("Dalo by se říct, že Heinrich svým pitím a výbušnou povahou nedělá dobré jméno cechu. A Rumelin se netají tím, že pro dobré jméno cechu udělá cokoli.")
        "Kde jste byl včera v noci?" if "alibi" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("alibi")
            "Mistr Kaspar na moment zaváhá."
            $ kaspar.say("Doma. Sám. Můj vlastní výrobek ještě není dokončený, tak jsem pracoval dlouho do noci.")
            $ mc.say("Může vám to někdo dosvědčit?")
            $ kaspar.say("Obávám se, že jen můj pes. Toho asi vyslechnout nemůžete, předpokládám?")
            if gender == "M":
                $ mc.say("Nemáte žádné učedníky? Čekal bych, že mistr vašeho postavení nějaké mít bude.")
            else:
                $ mc.say("Nemáte žádné učedníky? Čekala bych, že mistr vašeho postavení nějaké mít bude.")
            $ kaspar.say("Ne, je pro mne příjemnější mít tu na výpomoc jen tovaryše, kteří už něco umí. Ti u mne samozřejmě nebydlí.")
            $ kaspar.say("Můžu vám ukázat svůj vlastní nedokončený pár bot, pokud by to něco znamenalo.")
            $ mc.say("To asi nebude nutné.")
        "Zeptal jsem se U Salmy a hostinská včera výrobek mistra Heinricha neviděla." if "lost shoes in pub" in salma.asked and "lost shoes in pub" not in kaspar.asked and gender == "M":
            hide mcPic
            call kasparLostShoesInPub
        "Zeptala jsem se U Salmy a hostinská včera výrobek mistra Heinricha neviděla." if "lost shoes in pub" in salma.asked and "lost shoes in pub" not in kaspar.asked and gender == "F":
            hide mcPic
            call kasparLostShoesInPub
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("join forces")
            $ status.append("join forces survey")
            if gender == "M":
                $ kaspar.say("To by byl velmi nezvyklý počin. Odvážný, chce se mi říct. Muselo by to mít velmi dobré zdůvodnění, většinou přece mistři pracují sami. Ostatně, vy také očividně na vyšetřování vašeho případu stačíte sám a nechodíte ve dvojici.")
            else:
                $ kaspar.say("To by byl velmi nezvyklý počin. Odvážný, chce se mi říct. Muselo by to mít velmi dobré zdůvodnění, většinou přece mistři pracují sami. Ostatně, vy také očividně na vyšetřování vašeho případu stačíte sama a nechodíte ve dvojici.")
            $ mc.say("A kdyby to dobré zdůvodnění mělo?")
            $ kaspar.say("Pak by to mohlo být vnímáno dobře, ale těžko soudit takto obecně.")
            $ mc.say("Co kdyby se jednalo například o spojení mistra Heinricha a mistra Njala?")
            $ kaspar.say("Těch dvou? Nerad bych byl nezdvořilý, ale musím se přemáhat, abych se nesmál.")
            $ kaspar.say("Bylo by zřejmé, že ten opilec svoje vlastní dílo ztratil nebo zkazil, a tak se chytil jakékoli záchrany. Proč by mu pomáhal zrovna Njal, to nevím, ale vůbec bych se nedivil, kdyby na ten svátek prostě zapomněl. Všichni víme, že trpaslíci pořád jen vypráví o svých pradědech a na opravdové bohy si nevzpomenou.")
            $ kaspar.say("Rozhodně by se jim městské klepny smály ještě dlouho.")
            $ kaspar.say("Mají snad něco podobného v úmyslu?")
            if gender == "M":
                $ mc.say("Nevím, jestli to skutečně mají v úmyslu. Někdo podobný nápad zmínil a já chtěl zjistit od někoho znalého věci, co by to znamenalo.")
            else:
                $ mc.say("Nevím, jestli to skutečně mají v úmyslu. Někdo podobný nápad zmínil a já chtěla zjistit od někoho znalého věci, co by to znamenalo.")
            $ kaspar.say("Jistě, rozumím. Jsem hlídce samozřejmě kdykoli k službám.")
        "Jste zatčen za krádež výrobku mistra Heinricha." (badge="handcuffs") if "confession" in kaspar.asked and kaspar not in arrested:
            hide mcPic
            $ kaspar.say("Vždyť jsem jasně řekl, že jsem v dílně ty boty ani nenašel.", "angry")
            $ mc.say("To je ale přesně to, co by řekl zloděj.")
            $ kaspar.say("Zloděj by se hlavně nepřiznal, že v té dílně vůbec byl. Koho to dnes do té hlídky berou?", "angry")
            $ mc.say("Půjdete se mnou.")
            $ kaspar.arrestReason.append("stolen shoes")
            $ arrested.append(kaspar)
            $ status.append("arrest in progress")
            return
        "Jste zatčen za zničení výrobku mistra Heinricha." (badge="handcuffs") if "confession" in kaspar.asked and kaspar not in arrested:
            hide mcPic
            $ kaspar.say("Vždyť jsem jasně řekl, že jsem v dílně ty boty ani nenašel.", "angry")
            $ mc.say("To je ale přesně to, co by řekl pachatel.")
            $ kaspar.say("Ten by se hlavně nepřiznal, že v té dílně vůbec byl. Koho to dnes do té hlídky berou?", "angry")
            $ mc.say("Půjdete se mnou.")
            $ kaspar.arrestReason.append("destroyed shoes")
            $ arrested.append(kaspar)
            $ status.append("arrest in progress")
            return
        "Jste zatčen za úmysl poškodit výrobek mistra Heinricha." (badge="handcuffs") if "confession" in kaspar.asked and kaspar not in arrested:
            hide mcPic
            $ kaspar.say("Vždyť jsem jasně řekl, že... cože? Zatčen za úmysl? Co je zase tohle za pitomost?", "surprised")
            $ mc.say("Půjdete se mnou.")
            $ kaspar.arrestReason.append("destroyed shoes")
            $ arrested.append(kaspar)
            $ status.append("arrest in progress")
            return
        "Děkuji vám za pomoc.":
            hide mcPic
            $ kaspar.say("Rádo se stalo. Pomáhat hlídce je přece naše povinnost.", "happy")
            return
    jump kasparOptions

label leavingKaspar:
    $ kaspar.say("Pokud bych mohl ještě nějak pomoci, určitě se stavte znovu.", "happy")
    $ mc.say("Budu na to myslet. Zatím na shledanou.")
    return

###

label kasparLostShoesInPub:
    $ kaspar.asked.append("lost shoes in pub")
    if "alcoholic" in salma.asked and "alcoholic" in lisbeth.asked:
        $ mc.say("A o záchvatech vzteku také neví ani hostinská Salma, ani paní Lisbeth.")
    elif "alcoholic" in salma.asked:
        $ mc.say("A o záchvatech vzteku také neví.")
    elif "alcoholic" in lisbeth.asked:
        $ mc.say("A paní Lisbeth popírá, že by mistr Heinrich býval po alkoholu vzteklý.")
    $ kaspar.say("A kam se ty střevíce potom ztratily, když nebyly večer v jeho dílně?")
    show mcPic at menuImage
    menu:
        "To právě hlídka vyšetřuje.":
            hide mcPic
            $ kaspar.say("Samozřejmě, hlídka má mou plnou důvěru. Jen mám strach o pověst mistra Heinricha, slavnosti začínají už za čtyři dny.")
        "Večer?":
            hide mcPic
            if gender == "M":
                if "workshop unlocked" in clues:
                    $ mc.say("Myslel jsem, že ke krádeži došlo někdy během noci, kdy byla dílna odemčená. Víte něco, co jste zatím neřekl?")
                else:
                    $ mc.say("Myslel jsem, že ke krádeži došlo někdy během noci. Víte něco, co jste zatím neřekl?")
                $ kaspar.say("Určitě jste mluvil o večeru. Jak bych mohl vědět něco, co mi nikdo neřekl?")
            else:
                if "workshop unlocked" in clues:
                    $ mc.say("Myslela jsem, že ke krádeži došlo někdy během noci, kdy byla dílna odemčená. Víte něco, co jste zatím neřekl?")
                else:
                    $ mc.say("Myslela jsem, že ke krádeži došlo někdy během noci. Víte něco, co jste zatím neřekl?")
                $ kaspar.say("Určitě jste mluvila o večeru. Jak bych mohl vědět něco, co mi nikdo neřekl?")
            $ mc.say("Byl jste včera v Heinrichově dílně?")
            $ kaspar.say("A jak bych se do té dílny měl dostat? Ani jsem nevěděl, že Heinrich šel zase pít.")
    return

label kasparOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "enemies" not in kaspar.asked:
        $ optionsRemaining += 1
    if "enemies" in kaspar.asked and "ambitions" not in kaspar.asked:
        $ optionsRemaining += 1
    if "enemies" in kaspar.asked and "enemies2" not in kaspar.asked:
        $ optionsRemaining += 1
    if "alibi" not in kaspar.asked:
        $ optionsRemaining += 1
    if "lost shoes in pub" in salma.asked and "lost shoes in pub" not in kaspar.asked:
        $ optionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in kaspar.asked:
        $ optionsRemaining += 1
    return
