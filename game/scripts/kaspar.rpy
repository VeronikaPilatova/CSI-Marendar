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
    if kaspar.imageParameter == "beaten" and "assaulted" not in kaspar.asked:
        call kasparBeatenIntro
    elif kaspar.alreadyMet == False:
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
        "Dám si rád[a], díky. {i}(pořádně si přihnout){/i}":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
        "Dám si rád[a], díky. {i}(předstírat pití){/i}":
            hide mcPic
            $ kaspar.asked.append("drink accepted")
            $ hayfa.trust += 1
            $ kaspar.say("Je skvělé potkat hlídkaře, který není tak formální.", "happy")
    $ kaspar.say("S čím vám vlastně můžu pomoci?")
    $ mc.say("Vyšetřuji ztrátu mistrovského výrobku z dílny mistra Heinricha.")
    $ kaspar.say("A jste si jist[y], že se jedná o krádež?")
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

label kasparBeatenIntro:
    "Mistr Kaspar na tebe tentokrát spustí, sotva vkročíš do dveří."
    $ kaspar.say("To je dobře, že jdete. Byl tu Heinrich! Přiřítil se, když jsem poklidně pracoval před domem, začal mi nadávat a vrhl se na mě! Jen tak, hrubián zatracený!", "surprised")
    $ kaspar.say("To se dělá, útočit takhle na řemeslného mistra? Svoje učedníky ať si mlátí, jak chce, a také to očividně dělá, podle toho, kolik mu jich odchází, ale ať aspoň nechá na pokoji slušné dospělé lidi.", "angry")
    $ kaspar.say("Já nejsem odborník na zákony, ale tohle přece nemůžete nechat jen tak!", "angry")
    label kasparBeatenOptions:
    show mcPic at menuImage
    menu:
        "Jaký říkal, že k tomu má důvod?" if "beaten - reasons" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("beaten - reasons")
            $ kaspar.say("Neříkal nic, čemu by příčetný člověk rozuměl. Jen chrlil nadávky.", "angry")
            jump kasparBeatenOptions
        "Nechodil jste mu za ženou?" if "beaten - affair" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("beaten - affair")
            $ kaspar.say("Prosím? Co je tohle za pomluvy? Občas spolu mluvíme, ale to může za cokoli špatného považovat možná tak Heinrich, ale určitě nikdo jiný!", "surprised")
            show mcPic at menuImage
            menu:
                "Souhlasím, mistr Heinrich vás očividně nechápe.":
                    hide mcPic
                    $ kaspar.say("Přesně. Já věděl, že ho prokouknete.", "happy")
                "Kdyby to bylo tak v pořádku, neměli byste s paní Lisbeth důvod to tajit.":
                    hide mcPic
                    $ kaspar.say("Ten důvod je přesně v tom, že Heinrich nic nechápe. Jak se teď jasně ukázalo.", "angry")
            jump kasparBeatenOptions
        "Co vaše návštěva jeho dílny?" if "confession" in kaspar.asked and "beaten - workshop visit" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("beaten - workshop visit")
            $ kaspar.say("O tom přece nemůže nic tušit. Jak by to asi poznal? Na nic jsem ani nesáhnul, natož abych něco rozbil nebo odnesl.", "angry")
            $ kaspar.say("A Lisbeth ví, jaký je. Jedině že byste mu to řekl[a] vy, ale to jste snad neudělal[a], že ne?", "angry")
            show mcPic at menuImage
            menu:
                "Samozřejmě že ne.":
                    hide mcPic
                    $ kaspar.asked.append("not ratted out")
                    $ mc.say("Máte pravdu, byla to špatná úvaha.")
                    $ kaspar.say("To je v pořádku, každý se někdy spleteme. Hlavně aby mu to neprošlo.")
                "Samozřejmě že ano. Měl právo to vědět.":
                    hide mcPic
                    $ kaspar.asked.append("ratted out")
                    $ kaspar.trust -= 3
                    $ kaspar.say("Prosím? A čeho jste tím prosím vás chtěl[a] dosáhnout? Jste se sebou teď spokojen[y]?")
                    show mcPic at menuImage
                    menu:
                        "Je to soukromá záležitost a on ji řešil soukromě. Tak je to v pořádku a já do toho nebudu zasahovat.":
                            hide mcPic
                            $ kaspar.say("Tak to jsem o vás tedy měl jiné mínění.", "angry")
                        "Uznávám, že mě překvapil. Takhle přehnat to neměl.":
                            hide mcPic
                            $ kaspar.trust += 1
                            $ kaspar.say("Tak se hlavně postarejte, aby mu to neprošlo.", "angry")
            jump kasparBeatenOptions
        "Rozhodně to tak nenechám.":
            hide mcPic
            if "ratted out" in kaspar.asked:
                $ kaspar.say("No aspoň že tak.", "angry")
            else:
                $ kaspar.say("Věděl jsem, že se na hlídku mohu spolehnout.", "happy")
            $ kaspar.say("Ale přivedlo vás sem něco jiného. S čím můžu pomoct?")
            $ kaspar.asked.append("promised to deal with Heinrich")
        "Je mi líto, nemůžu s tím nic udělat. Musím se věnovat jiným záležitostem.":
            hide mcPic
            $ kaspar.say("Jako třeba hledání ztracených bot přesně toho hrubiána, který pobíhá po městě a mlátí lidi, kteří chtějí v klidu pracovat? Opravdu je pro vás tohle to hlavní?", "angry")
            $ kaspar.say("Zeptejte se prosím jeho jasnosti, jestli si takto hlídka představuje udržování práva, protože já tedy ne.", "angry")
            $ mc.say("... koho že?")
            $ kaspar.say("Jeho jasnosti svobodného pána Rauvina de Vito, samozřejmě. Kolik šlechticů v tomhle městě znáte?")
            show mcPic at menuImage
            menu:
                "Dobře, zeptám se ho.":
                    hide mcPic
                "Jeho názory znám. A vím, co mi dal za úkol.":
                    hide mcPic
            $ mc.say("Ale přišel[a] jsem za vámi kvůli něčemu jinému.")
            $ kaspar.say("No tak do toho, když to jinak nejde.")
    $ kaspar.asked.append("assaulted")
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
            $ mc.say("Nemáte žádné učedníky? Čekal[a] bych, že mistr vašeho postavení nějaké mít bude.")
            $ kaspar.say("Ne, je pro mne příjemnější mít tu na výpomoc jen tovaryše, kteří už něco umí. Ti u mne samozřejmě nebydlí.")
            $ kaspar.say("Můžu vám ukázat svůj vlastní nedokončený pár bot, pokud by to něco znamenalo.")
            $ mc.say("To asi nebude nutné.")
        "Zeptal[a] jsem se U Salmy a hostinská včera výrobek mistra Heinricha neviděla." if "lost shoes in pub" in salma.asked and "lost shoes in pub" not in kaspar.asked:
            hide mcPic
            call kasparLostShoesInPub
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("join forces")
            $ status.append("join forces survey")
            $ kaspar.say("To by byl velmi nezvyklý počin. Odvážný, chce se mi říct. Muselo by to mít velmi dobré zdůvodnění, většinou přece mistři pracují sami. Ostatně, vy také očividně na vyšetřování vašeho případu stačíte [sam] a nechodíte ve dvojici.")
            $ mc.say("A kdyby to dobré zdůvodnění mělo?")
            $ kaspar.say("Pak by to mohlo být vnímáno dobře, ale těžko soudit takto obecně.")
            $ mc.say("Co kdyby se jednalo například o spojení mistra Heinricha a mistra Njala?")
            $ kaspar.say("Těch dvou? Nerad bych byl nezdvořilý, ale musím se přemáhat, abych se nesmál.")
            $ kaspar.say("Bylo by zřejmé, že ten opilec svoje vlastní dílo ztratil nebo zkazil, a tak se chytil jakékoli záchrany. Proč by mu pomáhal zrovna Njal, to nevím, ale vůbec bych se nedivil, kdyby na ten svátek prostě zapomněl. Všichni víme, že trpaslíci pořád jen vypráví o svých pradědech a na opravdové bohy si nevzpomenou.")
            $ kaspar.say("Rozhodně by se jim městské klepny smály ještě dlouho.")
            $ kaspar.say("Mají snad něco podobného v úmyslu?")
            $ mc.say("Nevím, jestli to skutečně mají v úmyslu. Někdo podobný nápad zmínil a já chtěl[a] zjistit od někoho znalého věci, co by to znamenalo.")
            $ kaspar.say("Jistě, rozumím. Jsem hlídce samozřejmě kdykoli k službám.")
        "Budete ochotný svědčit ve prospěch té tanečnice s ohněm?" if "fireshow" in status and "testify for dancer" not in kaspar.asked:
            hide mcPic
            $ kaspar.asked.append("testify for dancer")
            $ kaspar.say("Jistě, ale proč? Na její usvědčení mě přece nepotřebujete, vždyť to je jasný případ.")
            $ mc.say("Asi jste se přeslechl, mám na mysli v její prospěch. Aby nebyla potrestaná nebo alespoň ne tak přísně.")
            $ kaspar.say("Ve prospěch... Proč? Vždyť je to zločinec!", "surprised")
            $ mc.say("To si právě nemyslím a mám pro to rozumné důvody.")
            $ kaspar.say("Tyhle rozumné důvody vás tam nikdo ani nenechá říct. Do takového podniku se mi vážně jít nechce.", "angry")
            show mcPic at menuImage
            menu:
                "Jestli jí pomůžete, zatknu Heinricha za to, jak vás napadl." if kaspar.imageParameter == "beaten" and victim not in arrested:
                    hide mcPic
                    $ kaspar.say("Ale to je přece vaše povinnost bez ohledu na cokoli. Od čeho bychom hlídku měli, kdyby nebránila slušné lidi před podobně sprostými útoky?", "surprised")
                    $ kaspar.say("Jestli to pořád nechápete, zajděte konečně za tím Rauvinem, ať vám to vysvětlí.", "angry")
                "A co když vám zaručím, že Heinrich nebude mít na slavnostech žádný pořádný výrobek?":
                    hide mcPic
                    $ kaspar.say("To už přece víme, když ho ztratil.", "angry")
                    $ kaspar.say("Bude tam muset dát něco, co mu zrovna leží na polici. To mi docela stačí, po tom, jak se svým úžasným dílem chvástal.")
                "Je to mladá dívka, co nepřeje nikomu nic špatného. A potřebuje vás, protože jiné zastání nemá.":
                    hide mcPic
                    $ kaspar.say("Tedy mám sám bránit cizí holku, co málem znovu zapálila město, proti všem příčetným lidem, se kterými se celý život potkávám na ulici?", "angry")
                    $ kaspar.say("Odpusťte, ale to mi nepřipadá jako nejlepší nápad.", "angry")
                "Byl[a] bych vám potom zavázan[y].":
                    hide mcPic
                    $ kaspar.say("Nic proti tomu mít přítele v hlídce, ale upřímně, nevím, jak moc bych stál o přítele, co mě bude hnát do podniků, ve kterých nejspíš ztratím tvář.", "angry")
                    $ kaspar.say("Naštěstí my přátelé jsme, a tak nic takového dělat nebudete, že ano?")
                "Rozumím, nebudu vás s tím dále zdržovat.":
                    hide mcPic
            $ kaspar.say("Neberte to špatně. Jste ve městě nově, rád vám pomůžu se v něm správně pohybovat. Hlídka se mnou vždy může počítat.", "happy")
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
            if "workshop unlocked" in clues:
                $ mc.say("Myslel[a] jsem, že ke krádeži došlo někdy během noci, kdy byla dílna odemčená. Víte něco, co jste zatím neřekl?")
            else:
                $ mc.say("Myslel[a] jsem, že ke krádeži došlo někdy během noci. Víte něco, co jste zatím neřekl?")
            $ kaspar.say("Určitě jste mluvil[a] o večeru. Jak bych mohl vědět něco, co mi nikdo neřekl?")
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
    if "fireshow" in status and "testify for dancer" not in kaspar.asked:
        $ optionsRemaining += 1
    return
