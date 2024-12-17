label victimMain:
    if lastSpokenWith == "":
        $ lisbeth.say("Dojdu pro něj, pojďte zatím dál.")
        call victimHouseInterior
    else:
        $ lisbeth.say("Dojdu pro něj.")

    $ lastSpokenWith = "victim"
    $ heinrichHouseholdSpokenWith.append("victim")
    call victimIntro

    label victimQuestions:
    $ origAsked = victim.asked.copy()
    call victimOptions

    label victimEnd:
    $ time.addMinutes((len(victim.asked) - len(origAsked)) * 3)
    if leaveOption == "none":
        $ leaveOption = "normal"
    else:
        jump victimHouseholdConversationEnded
    return


label victimIntro:
    "Mistr Heinrich vejde do místnosti s výrazem jako by se napil kyselého piva."

    if "firefighter" in status and "firefighter" not in victim.asked:
        $ victim.asked.append("firefighter")
        "Když tě ale uvidí, jeho výraz se trochu projasní."
        $ victim.say("Včera jsi kolem toho ohně udělal[a] spoustu dobré práce. Kdyby byla hlídka vždycky takhle užitečná, možná bychom si tu na ni zvykli.", "happy")
        $ victim.say("Ale nepři[sel] jsi, abych ti mazal med kolem huby.")
        show mcPic at menuImage
        menu:
            "Ve skutečnosti bych si s vámi o tom ohni rád[a] promluvil[a].":
                hide mcPic
                $ victim.asked.append("fireshow")
                $ victim.say("No dobře, o co jde?")
                call heinrichFireshow
            "Ve skutečnosti jsem se vám přišel omluvit, pokud jsem vás nějak urazil." if "victim expects apology" in status and gender == "M":
                hide mcPic
                $ victim.trust += 1
                $ victim.say("No co si budeme povídat, choval ses jako hulvát. Ale po včerejšku ti jsem ochotný dát ještě šanci.")
                call afterApologyReactionPositive
            "Ve skutečnosti jsem se vám přišla omluvit, pokud jsem vás nějak urazila." if "victim expects apology" in status and gender == "F":
                hide mcPic
                $ victim.trust += 1
                $ victim.say("No co si budeme povídat, chovala ses jako hulvát. Ale po včerejšku ti jsem ochotný dát ještě šanci.")
                call afterApologyReactionPositive
            "To je pravda. Můžu vám ještě položit pár otázek?":
                hide mcPic
                $ victim.say("Bez toho to asi vyšetřit nemůžeš, tak do toho.")
        if "victim expects apology" in status:
            $ status.remove("victim expects apology")
    else:
        if "burned evidence seen" in victim.asked:
            $ victim.say("Už víš, kdo se opovážil hodit moje dílo do mého vlastního krbu?")
        else:
            $ victim.say("Neseš mi zpátky můj ztracený výrobek?")
        if "carrying key" in status:
            $ mc.say("Zatím ne, ale nesu vám od Eckharda zpět klíč od vaší dílny.")
            call returningKey
        elif "victim expects apology" in status:
            $ status.remove("victim expects apology")
            $ mc.say("Zatím ne, ale dělám vše pro to, abych ho na[sel].")
            show mcPic at menuImage
            menu:
                "Jdu se vám omluvit, pokud jsem vás nějak urazil[a].":
                    hide mcPic
                    $ victim.trust += 1
                    if "burned evidence seen" in victim.asked:
                        $ victim.say("No co si budeme povídat, choval[a] ses jako hulvát. Chci jenom základní respekt a aby sis hleděl[a] své práce. Tak hlavně najdi toho zatraceného vandala.")
                    else:
                        $ victim.say("No co si budeme povídat, choval[a] ses jako hulvát. Chci jenom základní respekt a aby sis hleděl[a] své práce. Tak hlavně najdi můj mistrovský výrobek.")
                    show mcPic at menuImage
                    call afterApologyReaction
                "Můžu vám ještě položit pár otázek?":
                    hide mcPic
                    if victim.trust > -2:
                        $ victim.say("Když to musí být... tak se ptej.")
                    else:
                        $ victim.say("Mám sto chutí tě rovnou vyhodit... ale ptej se.", "angry")
        else:
            $ mc.say("Zatím ne, ale dělám vše pro to, abych ho na[sel]. Můžu vám ještě položit pár otázek?")

        if "retrieving workshop key" in status:
            $ victim.say("A co ten klíč, který jsi slíbil donést?")
            $ mc.say("Ještě jsem se pro něj nedostal[a]...")
            if time.isBefore(keyVeryLateAfter):
                $ victim.say("A to si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co? Kdybys to nesliboval[a], mohl jsem si za Eckhardem dojít sám.", "angry")
                $ victim.trust -= 1
            else:
                $ victim.say("Tak už se neobtěžuj. Už jsem si za Eckhardem došel sám a vyzvedl si ho osobně.", "angry")
                $ victim.say("To si myslíš, že když se ztratil můj mistrovský výrobek, můžu teď nechat svou dílnu odemčenou celý den, nebo co?", "angry")
                $ victim.trust -= 3
                $ status.remove("retrieving workshop key")
                $ status.append("not reliable")
            $ mc.say("Těch pár otázek…?")
            $ victim.say("Mám sto chutí tě rovnou vyhodit… ale ptej se.", "angry")
        else:
            if victim.trust > -2:
                $ victim.say("Když to musí být... tak se ptej.")
            else:
                $ victim.say("Mám sto chutí tě rovnou vyhodit... ale ptej se.", "angry")
    return

label returningKey:
    $ lastSpokenWith = "victim"
    $ heinrichHouseholdSpokenWith.append("victim")
    if "retrieving workshop key" in status:

        if time.isBefore(keySlightlyLateAfter):
            $ victim.trust += 1
            $ solian.trust += 1
            "Mistr Heinrich si klíč převezme s úsměvem, za kterým je vidět mírné překvapení."
            if "burned evidence seen" in victim.asked:
                $ victim.say("Vida, hlídka přeci jen k něčemu je. Za ušetření cesty děkuju, ale teď se vrať ke své práci a přines mi toho vandala v zubech.", "happy")
            else:
                $ victim.say("Vida, hlídka přeci jen k něčemu je. Za ušetření cesty děkuju, ale teď se vrať ke své práci a najdi toho zloděje.", "happy")
            call rumelinReminder

        elif time.isBefore(keyVeryLateAfter):
            $ solian.trust += 1
            "Mistr Heinrich si klíč převezme, ale jeho výraz se velmi brzy změní zpět na zamračený."
            if "burned evidence seen" in victim.asked:
                $ victim.say("No ale že ti to trvalo. A teď se vrať ke své práci a přines mi toho vandala v zubech.")
            else:
                $ victim.say("No ale že ti to trvalo. A teď se vrať ke své práci a najdi toho zloděje.")
            call rumelinReminder
        else:

            $ victim.trust -= 3
            "Když vidí klíč v tvé ruce, mistr Heinrich se zamračí ještě víc než předtím."
            $ victim.say("Kde všude ses s klíčem od mé dílny poflakoval[a]? Když jsem tě pro něj poslal, myslel jsem, že mi ho opravdu přineseš.", "angry")
            $ victim.say("Dokonce jsem za Eckhardem zašel sám, ale ten mi řekl, že už jsi tam byl[a]. A jenom ses neobtěžoval[a] dojít až za mnou. To si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            call apologyForLateness from _call_apologyForLateness
    else:

        if time.isBefore(keyVeryLateAfter):
            $ victim.trust += 1
            "Mistr Heinrich vejde do místnosti s mírně zmateným výrazem, ale jakmile zahlédne klíč, téměř ti ho vytrhne z ruky."
            $ victim.say("To je klíč od mé dílny! Jak ses k němu dostal[a]?")
            $ mc.say("Posílá mě s ním Eckhard. Prý by přišel sám, ale je mu špatně.")
            if "burned evidence seen" in victim.asked:
                $ victim.say("No dobře. Tak děkuju, ale teď se vrať ke své práci a přines mi toho vandala v zubech.", "happy")
            else:
                $ victim.say("No dobře. Tak děkuju, ale teď se vrať ke své práci a najdi toho zloděje.", "happy")
            call rumelinReminder
        else:

            $ victim.trust -= 2
            "Mistr Heinrich ti klíč skoro vytrhne z ruky, ale pak se zamračí ještě víc."
            $ victim.say("Co děláš s klíčem od mojí dílny?", "angry")
            $ mc.say("Eckhard ho měl u sebe a napadlo mě…")
            $ victim.say("A kdo se tě prosil o takové nápady? Když jsem konečně našel čas za Eckhardem dojít, řekl mi, že můj klíč předal náhodnému strážnému. Který se očividně neobtěžoval dojít až za mnou.", "angry")
            $ victim.say("To si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            call apologyForLateness

    $ status.remove("carrying key")
    if "retrieving workshop key" in status:
        $ status.remove("retrieving workshop key")
    $ status.append("key delivered")

    show mcPic at menuImage
    menu:
        "Vrátím se k případu.":
            hide mcPic
            $ victim.say("To je to nejlepší, co můžeš udělat.")
            $ time.addMinutes(5)
            jump victimEnd
        "Můžu vám ještě položit pár otázek?":
            hide mcPic
            if victim.trust > -2:
                $ victim.say("Když to musí být... tak se ptej.")
            else:
                $ victim.say("Mám sto chutí tě rovnou vyhodit... ale ptej se.", "angry")
            jump victimQuestions
    return

label victimOptions:
    call zeranInnocentOptionsRemainingCheck
    call victimOptionsRemainingCheck
    if victimOptionsRemaining == 0:
        $ mc.say("Děkuji, to je všechno.")
        $ victim.say("Tak hlavně pohni, slavnosti jsou už za chvíli a já tam pořád nemám co představit.")
        return

    if victim.trust > 5 and "relationship upgrade" not in victim.asked:
        "Mistr Heinrich se na tebe dlouze podívá a pak se k tvému překvapení trochu usměje."
        $ victim.say("Nečekal bych, že to někdy řeknu, ale na hlídkaře vlastně nejsi úplně nejhorší.", "happy")
        $ victim.asked.append("relationship upgrade")

    show mcPic at menuImage
    menu:
        "Můžete mi popsat ztracenou věc?" if "shoes description" not in clues:
            hide mcPic
            $ clues.append("shoes description")
            $ victim.asked.append("shoes description")
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
        "Máte ve městě s někým spory?" if "enemies" not in victim.asked:
            hide mcPic
            $ victim.asked.append("enemies")
            $ victim.say("S každým, kdo si dostatečně neváží mé práce. Rumelin ví, že ho chci nahradit v čele cechu a bojí se o svoje teplé místečko, Kaspar si brousí zuby na tu samou židli, i když na to nemá schopnosti… no a potom kdokoli mi hází klacky pod nohy.")
            $ victim.say("Ale největší důvod znemožnit mě na slavnostech mají myslím tihle dva.")
            $ kasparNote.isActive = True
        "Slyšel[a] jsem, že jste vyhodil několik učedníků?" if "enemies" in rumelin.asked and "fired apprentices" not in victim.asked:
            hide mcPic
            $ victim.asked.append("fired apprentices")
            $ victim.say("A co jiného jsem s nimi měl dělat, když nebyli schopní žádné pořádné práce? Tak dobře mi jejich rodiče nezaplatili.")
        "Co přesně provedli?" if "fired apprentices" in victim.asked and "fired apprentices offense" not in victim.asked:
            hide mcPic
            $ victim.asked.append("fired apprentices offense")
            $ victim.say("Škoda mluvit.")
            $ victim.say("Gerd si myslel, že rozumí řemeslu líp než já. Tak teď může plýtvat materiálem u Njala, ten se v nesmyslných nápadech a rádoby vylepšeních vyžívá. Jako by bylo něco špatně na tom, když někdo udělá poctivou, obyčejnou, prověřenou botu.")
            $ victim.say("Sigi byl prostě neschopný. Nejspíš rozmazlený mazánek bohatého tatínka, ale proč bych se s tím měl mazat já?")
            $ victim.say("A Zeran...")
            "Mistr Heinrich se zamračí."
            $ victim.say("Chodil mi za dcerou. Kluk, který by měl skládat tovaryšské zkoušky a bude svádět mou malou holčičku. Myslím, že z toho vyvázl ještě dost snadno.")
            $ victim.say("A to už bylo mnohem víc slov, než si kterýkoliv z nich zaslouží.")
            $ clues.append("Zeran offense")
            $ adaNote.isActive = True
        "Víte, kde je najít?" if "fired apprentices" in victim.asked and "fired apprentices" not in clues:
            hide mcPic
            $ victim.asked.append("fired apprentices location")
            $ clues.append("fired apprentices")
            $ victim.say("Gerda si vzal k sobě Njal. Vážně nevím, co z toho má, je dost schopný na to, aby si mohl vybírat.")
            $ victim.say("Ty druhé dva nikdo rozumný nechtěl. Jeden šel pryč z města, teď je myslím v Sehnau, nebo někde tím směrem. A ten zmetek Zeran… zkuste to v dočasné čtvrti, mezi ostatními budižkničemy.")
            $ gerdNote.isActive = True
            $ zeranNote.isActive = True
        "Jak vlastně víte, že mezi Zeranem a vaší dcerou něco bylo?" if "fired apprentices offense" in victim.asked and "proof against Zeran" not in victim.asked:
            hide mcPic
            $ victim.asked.append("proof against Zeran")
            $ victim.say("Kromě toho, že je spolu hned několik lidí vidělo? Našel jsem pár dopisů, které ten zmetek Adě psal. Samé sladké řečičky a sliby, dokonce ji chtěl vzít z města.")
        "Mohl bych vidět ty dopisy, které Zeran psal vaší dceři?" if "proof against Zeran" in victim.asked and "Zeran's letters" not in victim.asked and gender == "M":
            hide mcPic
            $ victim.asked.append("Zeran's letters")
            call zeranLettersResponse
        "Mohla bych vidět ty dopisy, které Zeran psal vaší dceři?" if "proof against Zeran" in victim.asked and "Zeran's letters" not in victim.asked and gender == "F":
            hide mcPic
            $ victim.asked.append("Zeran's letters")
            call zeranLettersResponse
        "Tohle vypadá jako drahý papír. Mohl by si ho učedník jako Zeran dovolit?" if "letters for Ada seen" in status and "expensive paper" not in victim.asked:
            hide mcPic
            $ victim.asked("expensive paper")
            $ mc.say("Nebo tady podobné papíry máte?")
            $ victim.say("To opravdu nemám. Co bych dělal s papírem s kudrlinkami? Taková zbytečnost.", "angry")
            $ mc.say("A jak by se k němu tedy Zeran dostal?")
            $ victim.say("To nevím a vůbec mě to nezajímá. Je mi jedno, na co ty svoje nesmysly psal, mojí malé holčičce je nemá co psát vůbec.")
        "Nemáte na práci i tovaryše?" if "journeymen" not in victim.asked:
            hide mcPic
            $ victim.asked.append("journeymen")
            $ victim.say("Ne od té doby, co se Eckhard stal mistrem.")
            $ victim.say("Tovaryši jsou nevděčná cháska. Neposlouchají, pořád si na něco stěžují a dožadují se nějakých práv a přitom buď běhají za děvčaty a posedávají po hospodách, nebo si stěžují na věk a špatné oči. Učedníky si aspoň můžu kdykoli srovnat.")
        "Takže Eckhard býval váš tovaryš?" if "journeymen" in victim.asked and "Eckhard relationship" not in victim.asked:
            hide mcPic
            $ victim.asked.append("Eckhard relationship")
            $ victim.say("Nějakou dobu, ale známe se už od učednických let.")
            $ victim.say("Oba jsme začínali z ničeho. Já jsem si svou dílnu vydupal ze země a Eckhard čekal, že ho cech nechá tovaryšem celý život.")
            $ victim.say("Za Velina byly pro lidské mistry tvrdší podmínky a většina míst byla stejně vyhrazená jenom pro elfy a hobity. Až po požáru se to uvolnilo a Eckhard měl šanci na vlastní dílnu.")
            $ victim.say("Rumelin možná tvrdí, že způsob vedení cechu změnil, ale dokud bude v čele on, nebudu tomu věřit.", "angry")
        "Takhle se vypracovat určitě nebylo snadné." if "Eckhard relationship" in victim.asked and "flattery" not in victim.asked:
            hide mcPic
            $ victim.asked.append("flattery")
            $ victim.trust += 1
            $ victim.say("To nebylo.")
            $ victim.say("Mistr, u kterého jsme byli v učení, nám nic neodpustil. Vstávali jsme ještě za tmy, pracovali až do noci, a netoleroval nám žádné lajdáctví. Ale kromě řemesla nás to naučilo vážit si poctivé práce.")
            $ victim.say("Během cesty na zkušenou jsem se naučil nové postupy a co nejvíc svoje schopnosti zdokonalil. To by mělo být normální, ale ne všichni to tak dělají.")
            $ victim.say("Znal jsem jednoho, co cestoval spíš po hospodách než po dílnách a z města odcházel když nadělal moc velké dluhy... ten bude třeba tovaryš celý život, pokud neskončí ještě hůř.")
            $ victim.say("Stát se mistrem v elfím městě znamenalo muset být lepší, než všichni místní elfové dohromady, když jsem nechal za sebe mluvit svou práci, nikdo mi nemohl upřít.")
            $ victim.say("Já vždycky říkám, že pokud se někdo nedokáže vyhrabat z bídy, tak asi nepracuje dost tvrdě.")
        "Kde by se vaše ukradené boty daly nejlépe prodat?" if "best sale" not in victim.asked:
            hide mcPic
            $ victim.asked.append("best sale")
            $ victim.say("V jiném městě. Tady mou práci všichni znají, každý kupec by měl otázky.")
            $ victim.say("Ale jsem si dost jistý, že o peníze nešlo. V dílně mám drahý materiál, spoustu dalších bot a jiných věcí a to všechno tam zůstalo.")
        "Jaký máte vlastně vztah se svou ženou?" if lotte.alreadyMet == True and "relationship" not in victim.asked:
            hide mcPic
            $ victim.asked.append("relationship")
            call heinrichMaritalRelationship
        "Je někdo, s kým si vaše žena obzvlášť rozumí?" if lotte.alreadyMet == True and "lisbeth friends" not in victim.asked:
            hide mcPic
            $ victim.asked.append("lisbeth friends")
            $ victim.say("To se zeptejte jí, ne?")
            $ victim.say("Ve městě nějaké kamarádky má, ale pořád se to mění, někdo má dítě, někdo se provdá někam daleko, někdo se začne chovat hrozně, už jsem dávno ztratil přehled.")
            $ victim.say("Tyhle ženské záležitosti nejsou nic pro mě.")
        "Je možné, že by vaše žena měla milence?" if lotte.alreadyMet == True and "secret lover" not in victim.asked:
            hide mcPic
            $ victim.asked.append("secret lover")
            $ victim.say("Cože?! Co má tahle otázka znamenat? Proč by moje žena měla mít milence? Doufám, že máš opravdu dobrý důvod, proč o tom začínáš.", "angry")
            show mcPic at menuImage
            menu:
                "Já se jen tak ptal[a]...":
                    hide mcPic
                    $ victim.trust -= 3
                    $ victim.say("Tak se přestaň jen tak ptát a hleď si své opravdové práce.")
                "Snažím se myslet na všechno.":
                    hide mcPic
                    $ victim.trust -= 1
                    $ mc.say("Kdyby někdo takový byl, byl by to způsob, jak se dostat do domu.")
                    $ mc.say("Ostatně kdyby někdo chodil třeba za někým z kluků, bylo by to totéž.")
                    $ victim.say("Jednou pro vždy si prosím zapamatuj, že my jsme slušný dům a žádné pochybné osoby sem nechodí.", "angry")
                "Jedna ze sousedek viděla, jak se vaše žena u dveří vítá s cizím mužem a pak jdou oba dovnitř.":
                    hide mcPic
                    $ victim.say("To musela kecat. Nebo se fakt blbě plést. Znáte ženský, klevetí, pomlouvá a kdo ví, co vlastně viděla.")
                    "Mistr Heinrich se otočí k odchodu, ale po chvíli se obrátí zpátky k tobě."
                    $ victim.say("Která sousedka to vlastně byla?", "angry")
                    $ mc.say("Lotte, bydlí na konci ulice.")
                    $ victim.say("Ta Lotta, jejíž manžel mi dodal šmejd? No to se dalo čekat. Budu muset Karstenovi vysvětlit, že ji má zfackovat, ať s těmi pomluvami přestane.")
                    $ victim.say("Kdyby radši přemýšlela, jak sehnat pořádné zboží a nedělat si ostudu.")
        "Ada se mnou odmítá mluvit, nemohl byste jí domluvit?" if "Ada closed door" in status and "Ada closed door" not in victim.asked:
            hide mcPic
            $ victim.asked.append("Ada closed door")
            $ victim.say("A co od ní potřebuješ? Do dílny nechodí a v noci spí, těžko si mohla něčeho všimnout.", "angry")
            show mcPic at menuImage
            menu:
                "Máte pravdu, asi to nebude tak důležité.":
                    hide mcPic
                    $ victim.say("Přemýšlej taky trochu, než se začneš vyptávat, slavnosti jsou za rohem a svoje boty pořád nevidím.", "angry")
                "Zajímaly mě podrobnosti o tom, jak to ve vašem domě chodí.":
                    hide mcPic
                    $ victim.trust -= 2
                    $ victim.say("Proč se vyptáváš na moji rodinu? Nemáš snad pátrat po mém mistrovském výrobku? Co má tohle znamenat?", "angry")
                    $ mc.say("Mohlo by to osvětlit některé okolnosti té krádeže.")
                    $ victim.say("Tak aby bylo jasno, my jsme slušná domácnost a nikdo tady nekrade, a jestli ten bídák Zeran, Kaspar nebo někdo podobný něco spáchal, nikdo z nás o tom nic neví.", "angry")
                    $ victim.say("Tak nech moji dceru napokoji a mě neotravuj s podobnými nesmysly.", "angry")
        "Mohl by tenhle kousek stuhy být od vašich střevíců?" if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in victim.asked:
            hide mcPic
            "Mistr Heinrich si ohořelý útržek prohlédne a zamračí se."
            call burnedEvidenceSeenVictim
        "Máte nějaký spor s mistrem Njalem?" if "join forces clueless" in njal.asked and "stolen idea" not in clues and "conflict with Njal" not in victim.asked:
            hide mcPic
            $ victim.asked.append("conflict with Njal")
            $ victim.say("S Njalem? Ne, o ničem nevím. Proč bych měl mít spor zrovna s ním?", "angry")
            $ mc.say("Mluvil[a] jsem s ním o vás a působil vůči vám nepřátelsky.")
            $ victim.say("Co já vím, co se mu v té jeho trpasličí palici mohlo vylíhnout. Všichni ho mají za podivína z nějakého důvodu.", "angry")
            $ victim.say("Třeba o mně ten budižkničemu Gerd vykládal nějaké pomluvy. Nebo měl prostě zrovna špatnou náladu. Je to důležité?")
            $ mc.say("To zatím nevím. Dám vědět, jestli se to s něčím spojí.")
        "Ohledně toho odstřižku z krbu..." if "burned evidence seen" in victim.asked and "calm Heinrich" in status and "burned evidence not as bad" not in victim.asked:
            hide mcPic
            $ victim.asked.append("burned evidence not as bad")
            $ status.remove("calm Heinrich")
            $ son.trust += 1
            $ optimist.trust += 1
            $ yesman.trust += 1
            $ ada.trust += 1
            $ victim.say("Už jsi na[sel] toho zmetka, co to má na svědomí?", "angry")
            show mcPic at menuImage
            menu:
                "Nemohl by to být odstřižek nebo zbytek z výroby?":
                    hide mcPic
                    $ victim.say("Všechny podobné odstřižky by měly být už dávno uklizené. A to rozhodně ne v krbu.", "angry")
                    $ mc.say("Ale možné to je?")
                    $ victim.say("Možné asi. Ale to neznamená, že tomu věřím.")
                "Nemohla z něčeho podobného vaše manželka nebo dcera vyšívat?" if adaNote.isActive == True:
                    hide mcPic
                    $ victim.trust -= 1
                    $ victim.say("I kdyby z nějakého nepochopitelného důvodu chtěly házet drahé látky do krbu, tak do mé dílny ani jedna z nich nesmí.")
                "Chci jen říct, že věřím, že se vaše střevíce najdou celé.":
                    hide mcPic
                    $ victim.say("Tak se přestaň zdržovat zbytečnými řečmi a přines mi je.")
        "Nechci zbytečně plašit, ale je možné, že vaše střevíce nenajdeme neporušené." if time.days > 1 and "plan B" not in victim.asked:
            hide mcPic
            $ victim.asked.append("plan B")
            $ clues.append("plan B")
            $ victim.trust -= 1
            $ mc.say("Máte pro jistotu připravený nějaký náhradní výrobek na slavnosti?")
            $ victim.say("Jak to myslíš, že je možná nenajdeš? Od čeho tady hlídku máme, když nedokáže ani najít zloděje a jenom se vymlouvá?", "angry")
            $ mc.say("Ne, zloději jsem na stopě. Jen si nemůžeme být jistí, co s vaším výrobkem provedl.")
            $ victim.say("Spoléhám na to, že mi ty střevíce v pořádku přineseš.")
            $ victim.say("Náhradní výrobek nemám, ale ať vezmu ve své dílně cokoli, bude to lepší práce, než přinese půlka cechu.")
        "Zjistil[a] jsem, kdo vám vypil velkou část vašich zásob vína." if "confession" in boysAsked and "lost bottles solved rumelin" not in victim.asked and "lost bottles solved boys" not in victim.asked:
            call victimLostBottlesSolved
            if leaveOption == "none":
                return
        "Zjistil[a] jsem, že cechmistr Rumelin se snažil poškodit jednoho z ostatních mistrů." if "confession" in rumelin.asked and "rumelin exposed" not in victim.asked:
            hide mcPic
            call rumelinExposedVictim
        "Zajímalo by mne, jak jste se dostal ke střihu mistra Njala." if "stolen idea" in clues and "stolen idea" not in victim.asked:
            hide mcPic
            $ victim.asked.append("stolen idea")
            $ victim.say("Jaký střih myslíte?")
            if "break-in" in clues:
                $ mc.say("Ten, který byl ve vylomené zásuvce vašeho stolu.")
            $ mc.say("Mistr Njal přiznal, že si ho včera v noci spolu s Gerdem vzali zpátky.")
            $ victim.say("Tak to byl on! Přemýšlel jsem, kdo mohl...")
            $ mc.say("Jak se k vám ten střih dostal?")
            show mcPic at menuImage
            menu:
                "Ukradl jste ho sám, nebo pro něj někoho poslal?":
                    hide mcPic
                    $ victim.trust -= 2
                    $ victim.say("Takhle se nenechám urážet. Nikdy v životě jsem nic neukradl a rozhodně bych neokradl jiného mistra svého cechu.", "angry")
                "Věděl jste, že je kradený?":
                    hide mcPic
            $ victim.say("Přinesl mi ho Eckhard. Prý se s ním Njal chlubil u Salmy a já bych ho dokázal zpracovat daleko lépe.")
            $ mc.say("Věděl jste, že je kradený?")
            $ victim.say("Na podrobnosti jsem se neptal.")
            $ victim.say("Původně jsem si ho ani nechtěl vzít, ale pak jsem si ho prohlédl a musel jsem dát Eckhardovi za pravdu. Opravdu skvělá práce. A velmi náročná práce, opravdu dobře to ušít by nezvládl hned tak někdo.")
        "Víte, že za krádež střihu bych měl[a] Eckharda zatknout?" if "stolen idea" in victim.asked and "should arrest eckhard" not in victim.asked:
            call victimArrestEckhard
            if leaveOption == "none":
                return
        "Nechtěl byste se na Einionovy slavnosti spojit s mistrem Njalem?" if "own work" in njal.asked and "plan B" in clues and "join forces" not in victim.asked:
            call victimJoinForces
        "Zjišťoval[a] jsem, jak by se lidi ve městě tvářili, kdybyste na slavnosti přinesl výrobek společně s mistrem Njalem." if "join forces victim pending" in status and "join forces survey" in status:
            call joinForcesSurveyResults
        "Mluvil[a] jsem s mistrem Njalem ohledně vaší spolupráce." if "join forces victim approves" in status and "join forces" in njal.asked and "join forces go-ahead" not in victim.asked:
            $ victim.asked.append("join forces go-ahead")
            call joinForcesGoAhead
        "Mluvil[a] jsem s mistrem Njalem ohledně vaší spolupráce." if "join forces victim approves" in status and "join forces clueless" in njal.asked and "join forces" not in njal.asked and "join forces go-ahead clueless" not in victim.asked:
            $ victim.asked.append("join forces go-ahead clueless")
            call joinForcesGoAhead
        "Rád bych s vámi mluvil[a] o tom, jak kousek odtud byl oheň na ulici." if "fireshow" in status and "fireshow" not in victim.asked:
            hide mcPic
            $ victim.asked.append("fireshow")
            $ victim.say("No dobře, o co jde?")
            call heinrichFireshow
        "Mám důkaz, že Zeran vaši dceru nesváděl." if "zeran innocent" not in victim.asked and "zeran cleared" not in status and zeranInnocentOptionsRemaining > 0:
            hide mcPic
            $ victim.asked.append("zeran innocent")
            if "Ada confronts Zairis":
                $ status.append("zairis confessed")
            if "zairis confessed" in status:
                $ victim.say("To už vím. Byl tady ten holomek od Roviena a přiznal se k tomu.", "angry")
                $ victim.say("Tak jsem mu vysvětlil, ať už se k tomuhle domu ani nikomu z mojí rodiny ani nepřibližuje. Jestli má v té svojí palici aspoň trochu rozumu, tak to udělá.", "angry")
                $ victim.say("Prý že si chtěl promluvit jako chlap s chlapem. Tak dostal, co chtěl.", "angry")
                $ victim.say("Víc se tím špinavcem nemíním zabývat.", "angry")
                $ status.append("zeran cleared")
            else:
                $ victim.say("Neříkal jsem ti, že jméno toho zmetka v tomhle domě už nechci nikdy slyšet?", "angry")
                $ mc.say("I když je nevinný?")
                $ victim.say("Nevinný nebo ne, málem zničil život mojí malé holčičce.", "angry")
                call zeranInnocentOptions
                if leaveOption == "none":
                    return
        "Mám důkaz, že ty milostné dopisy psal vaší dceři Rovienův syn Zairis."  if "zairis guilty" not in victim.asked and "zeran cleared" not in status and zairisGuiltyOptionsRemaining > 0:
            label zairisGuilty:
            hide mcPic
            $ victim.asked.append("zairis guilty")
            if "Ada confronts Zairis":
                $ status.append("zairis confessed")
            if "zairis confessed" in status:
                $ victim.say("To už vím. Byl tady a přiznal se, vypadal na to skoro hrdý, holomek jeden.", "angry")
                $ victim.say("Tak jsem mu vysvětlil, ať už se k tomuhle domu ani nikomu z mojí rodiny ani nepřibližuje. Jestli má v té svojí palici aspoň trochu rozumu, tak to udělá.", "angry")
                $ victim.say("Prý že si chtěl promluvit jako chlap s chlapem. Tak dostal, co chtěl.", "angry")
                $ victim.say("Víc se tím špinavcem nemíním zabývat.", "angry")
                $ status.append("zeran cleared")
            else:
                $ victim.say("On se k tomu přiznal?")
                if "confession" in zairis.asked:
                    $ mc.say("Když viděl všechny důkazy, tak nakonec ano.")
                    $ victim.say("A tomu mám jako věřit? To by mohl říct každý.", "angry")
                    $ mc.say("Můžu ty důkazy vysvětlit i vám, jestli chcete.")
                else:
                    $ mc.say("Zatím ne, ale mám důkazy.")
                $ victim.say("Tak to si chci poslechnout.")

                python:
                    patience = max(victim.trust - 4, 0)

                call zairisGuiltyOptions
                if leaveOption == "none":
                    return
        "Takže když je teď Zeran očištěný..." if "zeran cleared" in status and "zeran cleared" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zeran cleared")
            $ victim.say("Tak co?", "angry")
            label heinrichZeranClearedMenu:
            show mcPic at menuImage
            menu:
                "Neměl by dostat možnost pokračovat v učení?" if "Zeran should continue apprenticeship" not in victim.asked:
                    hide mcPic
                    $ victim.asked.append("Zeran should continue apprenticeship")
                    $ victim.say("No zpátky ho brát nebudu, jestli myslíš tohle. To by nedělalo dobrotu.")
                    $ victim.say("Ale... no... dobře, asi mu můžu vrátit jeho peníze. Ať to zkusí jinde.")
                    $ status.append("Zeran got his money back")
                    show mcPic at menuImage
                    menu:
                        "To mu určitě pomůže a mělo by mu to stačit.":
                            hide mcPic
                            $ victim.say("Doufám, že to bude stačit i mně, abych už měl od toho holomka jednou pro vždy pokoj.")
                        "To mi přijde málo, pořád má neprávem zkaženou pověst.":
                            hide mcPic
                            $ victim.say("A jak to asi mám udělat? Vypadám snad jako mág mysli, abych mu ji změnil?", "angry")
                            $ victim.say("Může začít znova a spravit si ji sám, to by mu mělo stačit.")
                            show mcPic at menuImage
                            menu:
                                "Aspoň mu můžete dát peníze navíc jako odškodné.":
                                    hide mcPic
                                    $ victim.trust -= 1
                                    $ victim.say("Co je tohle za nesmysl? Peníze se mají vydělávat poctivou prací, ne jen tak dostávat za nic.", "angry")
                                    $ victim.say("Jako učedník si bude mít živobytí a bude si moct vydělat malé kapesné.")
                                    $ victim.say("Aspoň bude mít důvod se snažit.")
                                "Mohl byste mu aspoň domluvit jiného mistra.":
                                    hide mcPic
                                    $ mc.say("Musíte mít v cechu spoustu známých, od vás to vezmou lépe, než od Zerana.")
                                    $ victim.say("Dobře, asi můžu za někým zajít a říct mu, že ten lunt je sice nemehlo jako všichni učedníci, ale vzít si ho pod střechu není nic nebezpečného.")
                                    $ victim.say("Vanya teď myslím někoho hledá, je to elfka a v tomhle městě je z těch lepších. Můžeš Zeranovi říct, ať se za ní staví.")
                                    $ status.append("Vanya can take Zeran")
                                "Na veřejnou omluvu mág mysli být nemusíte.":
                                    hide mcPic
                                    $ victim.trust -= 1
                                    $ victim.say("Ne, na to bych musel být šašek, abych dělal představení pro celé město.", "angry")
                        "To mi přijde málo, pořád je bez mistra. Jestli má nějaký talent, takhle přijde vniveč.":
                            hide mcPic
                            $ victim.trust += 1
                            $ victim.say("Talent... No, už jsem viděl i horší packaly. Kdyby nepřišel o rodinu i s dílnou, možná by z něj jednou mistr byl.")
                            $ victim.say("Můžu mu někoho domluvit, ať se ukáže. A pak to bude na něm.")
                            $ victim.say("Vanya teď myslím někoho hledá, je to elfka a v tomhle městě je z těch lepších. Můžeš Zeranovi říct, ať se za ní staví.")
                            $ status.append("Vanya can take Zeran")
                "Možná byste se mu měl omluvit." if "apologise to Zeran" not in victim.asked:
                    hide mcPic
                    $ victim.asked.append("apologise to Zeran")
                    $ victim.trust -= 1
                    $ victim.say("A k čemu mu to bude? Navíc já si za svými činy stojím.", "angry")
                    $ victim.say("Že to nebyl on, to jsem tehdy nemohl vědět a rozhodně nemohl jsem ho ve svém domě nemohl nechat, když to také on klidně být mohl.", "angry")
                    jump heinrichZeranClearedMenu
                "Kdyby ta omluva byla veřejná, spravilo by mu to pověst." if "apologise to Zeran" in victim.asked and "public apology" not in victim.asked:
                    hide mcPic
                    $ victim.asked.append("public apology")
                    $ victim.trust -= 1
                    $ victim.say("Tak tím si nejsem jistý. Ale jsem si jistý tím, že bych byl celému městu pro smích. To opravdu nemám v úmyslu.", "angry")
                    $ victim.say("Jsem řemeslník, ne komediant.", "angry")
                    jump heinrichZeranClearedMenu
                "Máte pravdu, nemá to smysl.":
                    hide mcPic
                    $ victim.say("Jsem rád, že máš aspoň trochu rozum.")

        "Děkuji, to je všechno.":
            hide mcPic
            $ victim.say("Tak hlavně pohni, slavnosti jsou už za chvíli a já tam pořád nemám co představit.")
            return
    if refusedBy == "victim":
        return
    jump victimOptions

label zairisGuiltyOptions:
    call zairisGuiltyOptionsRemainingCheck
    if zairisGuiltyOptionsRemaining == 0:
        $ mc.say("To je všechno, co mám.")
        $ victim.trust -= 1
        $ victim.say("To jsi mě tedy nepřesvědčil[a]. Doufal bych, že když už do mě chceš hučet, budeš aspoň mít něco v rukávu. Ale to bych asi od hlídky čekal moc.", "angry")
        $ victim.say("Pořád jsi mi nena[sel] moje boty. Zkus zase chvíli dělat svoji skutečnou práci. A lépe, než ti šlo orodování za toho všiváka.", "angry")
        return

    show mcPic at menuImage
    menu:
        "Zairisovo písmo odpovídá tomu na dopisech pro vaši dceru." if "Zairis handwriting checked" in status and "zairis guilty handwriting" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zairis guilty handwriting")
            $ zeran.cluesAgainst += 1
            if "zeran handwriting checked" in status:
                $ mc.say("Zeranovo vypadá úplně jinak.")
            if "zeran innocent handwriting" not in victim.asked:
                $ victim.say("Zeran škrábe jako kočka, ale i on by se snad v milostném dopise trochu snažil.", "angry")
                $ mc.say("Vy přece také dokážete rozlišit, co jste psal vy a co paní Lisbeth, například.")
                $ mc.say("Jde o sklon písma, úhlednost, tvar některých písmen... Překvapivě hodně těchto znaků zůstává stejných, i když třeba píšete ve spěchu.")
                if gender == "M":
                    $ victim.say("Ty jsi teda chytrej. No dobře, dobře. Ale také přece mohl Zeran schválně napodobit Zairisovo písmo. To není žádný důkaz.", "angry")
                else:
                    $ victim.say("Ty jsi teda chytrá. No dobře, dobře. Ale také přece mohl Zeran schválně napodobit Zairisovo písmo. To není žádný důkaz.", "angry")
                $ mc.say("To ve skutečnosti není tak jednoduché.")
                $ victim.say("Nepodceňuj toho špinavce.")
            else:
                $ victim.say("Jo, to je ta tvoje teorie, že každý píše úplně jinak.", "angry")
                $ mc.say("To není jenom moje teorie...")
                $ victim.say("Ale také přece mohl Zeran schválně napodobit Zairisovo písmo. To není žádný důkaz.", "angry")
                $ mc.say("To ve skutečnosti není tak jednoduché.")
                $ victim.say("Nepodceňuj toho špinavce.")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "Dopisy se hodně odkazují na Amadise a popisují návštěvu jeho hrobu. Zairis Amadise velmi obdivuje a u jeho hrobu byl." if "Amadis grave" in zairis.asked and "zairis guilty amadis grave" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zairis guilty amadis grave")
            $ patience -= 1
            $ victim.say("Tam ale mohla být spousta elfů. A obdivuje ho taky každý lajdák a nekňuba, co místo práce chodí koukat na komedianty.", "angry")
            $ victim.say("A potom o tom velmi rádi povykládají každému podvodníkovi, co se chce tvářit, že tam byl také.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "V těch dopisech jsou docela dobré básně. Ty by nedokázal napsat každý, ale Zairis se o poezii hodně zajímá." if "letters for Ada seen" and "poetry" in zairis.asked and "zairis guilty poetry" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zairis guilty poetry")
            $ patience -= 1
            $ victim.say("Mně přišly jako snůška nesmyslů a sladkých řečiček. Jak víš, že jsou tak zvláštní?", "angry")
            if "letters for Ada checked in library" in status:
                $ zeran.cluesAgainst += 1
                $ mc.say("Ptal[a] jsem se na ně v knihovně a tu báseň prý v žádném spisu nemají. Naopak prý už od Zairise několik básní četli a jeho stylu je to podobné.")
                $ victim.say("Tak to Zeran ukradl přímo Zairisovi. Nebo si to od něj nechal napsat na zakázku. To tě nenapadlo?", "angry")
                $ mc.say("To by mohlo vysvětlit jednu, dvě básně. Kolik jich Ada dostala?")
                $ victim.say("I kdyby jen jednu, je to víc, než měla, holomek zatracený.", "angry")
            else:
                $ mc.say("Vím o poezii dost, abych to poznal[a].")
                if race == "elf":
                    $ mc.say("My elfové si na vzdělání zakládáme a znalost staré poezie k tomu neodmyslitelně patří.")
                elif race == "dwarf":
                    $ mc.say("Ságy o předcích se u nás trpaslíků vypráví velmi často a všechny musí být co nejkrásnější, aby jim dělaly čest.")
                elif race == "hobbit":
                    $ mc.say("Snažím se ve městě zapadnout, a tak jsem se často přichomýtl[a] k poslechu nějakého pěvce, ať už lidského, nebo elfího.")
                else:
                    $ mc.say("Na jarmarcích jsem slyšel[a] už spoustu písní od různých pěvců.")
                $ victim.say("To je ale něco dost jiného než tohle hloupé cukrování. To neberu.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "Ty dopisy jsou psané vytříbeným stylem, který vyžaduje určité vzdělání. Zairis ho má, ale kde by k němu přišel Zeran? " if "letters for Ada seen" and "zairis guilty style" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zairis guilty style")
            $ patience -= 1
            $ victim.say("Se vzděláním se tady vytahuje každý druhý elf, oni si na to potrpí. A hlavně rodina toho špinavce bývala dřív docela bohatá.", "angry")
            $ victim.say("Ten si mohl sehnat všechny knížky, co potřeboval, aby mohl slušným mladým holkám plést hlavu.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "Ty dopisy jsou psané na velmi drahém papíře, který si Zeran těžko může dovolit. Zairis mi ale napsal nějakou poznámku na přesně stejný druh papíru."  if "Zairis handwriting checked" in status and "zairis guilty paper" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zairis guilty paper")
            $ zeran.cluesAgainst += 1
            $ victim.say("Ten kašpar mohl ten papír ukradnout, nepotřeboval ho tolik. Ani to nemuselo být od Zairise, tolik druhů zdobeného papíru se přece ve městě sehnat nedá.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "To je všechno, co mám.":
            hide mcPic
            $ victim.trust -= 1
            $ victim.say("To jsi mě tedy nepřesvědčil[a]. Doufal bych, že když už do mě chceš hučet, budeš aspoň mít něco v rukávu. Ale to bych asi od hlídky čekal moc.", "angry")
            if "case solved" not in status:
                $ victim.say("Pořád jsi mi nena[sel] moje boty. Zkus zase chvíli dělat svoji skutečnou práci. A lépe, než ti šlo orodování za toho všiváka.", "angry")
            return

    if zeran.cluesAgainst == 3:
        $ victim.say("Zatracená práce, takže abych si to ujasnil, ty říkáš...", "surprised")
        $ mc.say("...že ty dopisy jsou psané Zairisovým písmem na papíře, který Zairis používá, a že v něm jsou básně, které by tímto způsobem moc jiných lidí nenapsalo, jestli vůbec někdo.")
        $ victim.say("Takže to byl on.", "angry")
        $ mc.say("Všechno tomu nasvědčuje.")
        $ victim.say("Mizera jeden. To si s ním vyřídím.", "angry")
        $ mc.say("A Zeran...")
        $ victim.say("...mu posloužil jako obětní beránek. Zbabělec jeden. To mu neprojde.", "angry")
        $ victim.say("Musím teď z domu. Lisbeth tě vyprovodí.", "angry")
        $ mc.say("Nebylo by...")
        $ victim.say("Jindy.")
        "Mistr Heinrich zavolá manželku, řekne jí pár slov a zmizí v domě. Paní Lisbeth si vás oba přeměří tázavým a poněkud znepokojeným pohledem, nenaléhá však a způsobně ti ukáže cestu ke dveřím."
        scene bg heinrich outside
        "Venku před domem potom znovu spatříš mistra Heinricha, jak vyrazí ze dveří a rázným krokem se vydá pryč. Na tebe se ani nepodívá."
        $ status.append("zairis dealt with")
        $ leaveOption = "none"
        jump victimEnd
    elif patience < 1:
        $ victim.say("Upřímně, mám dojem, že jsme těmi dopisy už ztratili až moc času.", "angry")
        if zeran.cluesAgainst == 2:
            $ victim.say("Něco, co říkáš, by možná znělo rozumně, ale zapomínáš, že tady se bavíme o Zeranovi. Ten je schopný každé podlosti.", "angry")
        else:
            $ victim.trust -= 1
            $ victim.say("A tedy doufal jsem, že když už mě nutíš se bavit o tom špinavci Zeranovi, budeš mít aspoň připravené nějaké rozumné důvody, ale těch jsem tedy moc neslyšel.", "angry")
        $ victim.say("Takže mě ušetři toho utrpení v tomhle dál pokračovat a jdi zase chvíli dělat něco, za co tě město platí. Jako třeba věnovat se té zatracené krádeži.", "angry")
        $ victim.say("Slavnosti budou brzy.", "angry")

    jump zairisGuiltyOptions

label zeranInnocentOptions:
    call zeranInnocentOptionsRemainingCheck
    if zeranInnocentOptionsRemaining == 0:
        $ mc.say("To je všechno, co mám.")
        $ victim.say("Takže pořádný důkaz žádný.", "angry")
        $ victim.say("Někdo za Adou chodil a psal jí dopisy. Zjisti, kdo jiný to teda byl, a pak se můžeme bavit. Ale Zeran je jediný elf, se kterým jsem ji viděl já.", "angry")

    show mcPic at menuImage
    menu:
        "Jeho písmo vůbec neodpovídá tomu na dopisech." if "zeran handwriting checked" in status and "zeran innocent handwriting" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zeran innocent handwriting")
            $ victim.say("Jak může písmo neodpovídat? Písmo je písmo, ne? I kdyby tam měl třeba chyby.", "angry")
            $ mc.say("Vy přece také dokážete rozlišit, co jste psal vy a co paní Lisbeth, například.")
            $ mc.say("Jde o sklon písma, úhlednost, tvar některých písmen... Překvapivě hodně těchto znaků zůstává stejných, i když třeba píšete ve spěchu.")
            if gender == "M":
                $ victim.say("Ty jsi teda chytrej. No dobře, dobře. Ale přece mohl schválně psát jinak. To není žádný důkaz.", "angry")
            else:
                $ victim.say("Ty jsi teda chytrá. No dobře, dobře. Ale přece mohl schválně psát jinak. To není žádný důkaz.", "angry")
            $ mc.say("To ve skutečnosti není tak jednoduché.")
            $ victim.say("Nepodceňuj toho špinavce.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "V jednom z dopisů se mluví o Amadisově hrobě, tam se přece Zeran nemohl nikdy dostat." if "Amadis grave" in zeran.asked and "zeran innocent amadis grave" not in victim.asked:
            hide mcPic
            $ victim.asked.append("zeran innocent amadis grave")
            $ victim.say("A tebe překvapuje, že ten zmetek Adě lhal? Stejně jako nám všem ostatním?", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
            else:
                $ mc.say("Já si myslím, že nelhal...")
                $ victim.say("A máš i nějaký opravdový důkaz? Nebo si to jenom myslíš?", "angry")
        "Ty dopisy jsou psané na velmi drahém papíře, který si Zeran těžko může dovolit." if "letters for Ada seen" in status and "expensive paper" not in victim.asked:
            hide mcPic
            $ victim.asked.append("expensive paper")
            $ victim.say("Mohl ho ukrást. Nebo mu stálo za to si na něj našetřit.")
            $ victim.say("Nezapomeň, že ten špinavec dal všanc svoje učednické místo a porušil zákony pohostinství a veškerou slušnost. Dát si práci se sehnáním papíru už je to nejmenší.", "angry")
            if "letters for Ada shown" not in victim.asked and "letters for Ada slip up" not in victim.asked:
                call lettersForAdaSlipUp
                if leaveOption == "none":
                    return
        "Navíc vím, kdo za Adou chodil opravdu - byl to Rovienův syn Zairis." if "zairis guilty" not in victim.asked and "zeran cleared" not in status and zairisGuiltyOptionsRemaining > 0:
            jump zairisGuilty
        "To je všechno, co mám.":
            hide mcPic
            $ victim.say("Takže pořádný důkaz žádný.", "angry")
            $ victim.say("Někdo za Adou chodil a psal jí dopisy. Zjisti, kdo jiný to teda byl, a pak se můžeme bavit. Ale Zeran je jediný elf, se kterým jsem ji viděl já.", "angry")
            return
    jump zeranInnocentOptions

label lettersForAdaSlipUp:
    $ victim.asked.append("letters for Ada slip up")
    $ victim.say("O jakých dopisech to vlastně mluvíš?", "angry")
    $ mc.say("O těch pro vaši dceru...")
    $ victim.say("A ty jsi měl[a] dopisy pro Adu někdy v ruce?", "angry")
    $ victim.say("Nebo se ze mě snažíš dělat vola?")
    show mcPic at menuImage
    menu:
        "Adě jeden nebo dva dopisy zůstaly a ukázala mi je.":
            hide mcPic
            $ victim.say("Ona si ještě něco schovává? Nebo si s tím kašparem pořád dopisuje?", "angry")
            $ victim.say("Jasně jsem přece řekl, ať na toho prolhaného floutka zapomene.", "angry")
            $ victim.say("Tohle si s ní ještě vyřídím.", "angry")
            $ mc.say("Počkejte alespoň, než se celá věc vyjasní.")
            $ victim.say("Na tom není, co vyjasňovat. Ada na toho chlípníka nemá, co vzpomínat. Jestli to nepochopila na poprvé, musím jí to zopakovat.", "angry")
            $ mc.say("Ty dopisy jsou ale právě důkaz, že to nebyl Zeran.")
            $ victim.say("I kdyby, je to jedno. Je moc malá na to, aby se nechávala takhle obelhávat od kohokoli.", "angry")
            $ victim.asked.append("angry at Ada")
        "Náhodou jsem je na[sel] ve vaší dílně.":
            hide mcPic
            $ victim.say("Cože? A to jako kdy? Vždycky jsem tě v dílně hlídal.", "surprised")
            show mcPic at menuImage
            menu:
                "Pustili mě tam učedníci.":
                    hide mcPic
                    $ victim.trust -= 2
                    $ ada.trust -= 3
                    $ son.trust -= 4
                    $ victim.say("Učedníci. Tomu se těžko věří.", "angry")
                    $ mc.say("Nejdřív nechtěli, že byste byl proti, ale vysvětlil[a] jsem jim, že to je v zájmu vyšetřování a hledání vašeho výrobku.")
                    $ victim.say("... ti holomci. Vědí přece moc dobře, že v dílně se nesmí dít nic, o čem bych nevěděl.", "furious")
                    $ victim.say("Těm to ještě spočítám.", "furious")
                    $ victim.say("Jestli máš něco dalšího, tak radši zrychli, než mi dojde sebeovládání, protože tímhle mě vážně rozčílili.", "angry")
                    $ status.append("Heinrich angry apprentices opened workshop")
                    if "apprentices in trouble" not in status:
                        $ status.append("apprentices in trouble")
                "Pustila mě tam paní Lisbeth.":
                    hide mcPic
                    $ victim.trust -= 4
                    $ victim.say("Co je tohle za nesmysl?", "angry")
                    $ victim.say("Ta ví, že tam nesmí ani ona, natož pak nějaký chytrák s glejtem. Ta by tohle nikdy neudělala.", "angry")
                    $ victim.say("Tak mi přestaň lhát do očí a koukej konečně dělat svoji práci.", "angry")
                    $ victim.say("Mimo můj dům.", "angry")
                    "Mistr Heinrich velmi nesmlouvavě ukáže na dveře a tobě nezbyde, než se poroučet a doufat, že další rozhovor bude úspěšnější."
                    $ refusedBy = "victim"
                    $ leaveOption = "none"
                "Dal jste mi přece klíč." if "key delivered" in status:
                    hide mcPic
                    $ victim.say("... jaký klíč?", "surprised")
                    $ victim.say("Jo ty myslíš... a to myslíš vážně?", "angry")
                    $ victim.say("Ten jsem ti nedal a už vůbec ne proto, aby ses mi vloupal[a] do dílny!", "furious")
                    call mcAdmitsBurglary
                "No dobře, ve skutečnosti jsem nic nena[sel].":
                    hide mcPic
                    $ victim.trust -= 3
                    $ victim.say("... to jsem si mohl myslet. Tak už nic nezkoušej a koukej konečně dělat svoji práci.", "angry")
                    $ victim.say("Mimo můj dům.", "angry")
                    "Mistr Heinrich velmi nesmlouvavě ukáže na dveře a tobě nezbyde, než se poroučet a doufat, že další rozhovor bude úspěšnější."
                    $ refusedBy = "victim"
                    $ leaveOption = "none"
        "Náhodou jsme se s tím ctitelem potkali ve městě.":
            hide mcPic
            $ victim.trust -= 3
            # already talking about Zairis
            if "zairis guilty" in victim.asked:
                call adasLoverRandomMeetingZairis
            # talking about Zeran, but knows about Zairis
            elif zairisGuiltyOptionsRemaining > 0:
                $ victim.say("A kdo to tedy byl?", "angry")
                show mcPic at menuImage
                menu:
                    "Na jméno nebyla příležitost se vyptat.":
                        hide mcPic
                        call adasLoverRandomMeetingUnknown
                    "Zairis, syn obchodníka Roviena.":
                        hide mcPic
                        call adasLoverRandomMeetingZairis
            # no idea who else it could be
            else:
                $ victim.say("A kdo to tedy byl?", "angry")
                $ mc.say("Na jméno nebyla příležitost se vyptat.")
                call adasLoverRandomMeetingUnknown
        "Odhalil jste mě, jen jsem to zkusil[a].":
            hide mcPic
            $ victim.trust -= 3
            $ victim.say("... to jsem si mohl myslet. Tak už nic nezkoušej a koukej konečně dělat svoji práci.", "angry")
            $ victim.say("Mimo můj dům.", "angry")
            "Mistr Heinrich velmi nesmlouvavě ukáže na dveře a tobě nezbyde, než se poroučet a doufat, že další rozhovor bude úspěšnější."
            $ refusedBy = "victim"
            $ leaveOption = "none"
    return

label adasLoverRandomMeetingUnknown:
    $ victim.say("Aha, takže ty náhodou potkáš elfa, kterého ani neznáš, on ti vypráví o tvojí tajné lásce, ale ani se nepředstaví.", "angry")
    $ victim.say("Nevím, jestli jsi tak špatn[y] ve vyšetřování, nebo ve lhaní, ale je mi to jedno.", "angry")
    $ victim.say("Jestli pro mě máš něco důležitého, koukej to vysypat. Jestli ne, přestaň mě konečně zdržovat hloupostmi.", "angry")
    return

label adasLoverRandomMeetingZairis:
    $ victim.say("A to jste se prostě jenom tak potkali a on ti začal jenom tak ukazovat milostné dopisy, které zrovna psal?", "angry")
    $ mc.say("Měl[a] jsem podezření a zeptal[a] se... mám opravdu přesvědčivé důkazy.")
    $ victim.say("Které jsi s sebou měl[a] náhodou s sebou. A podezření jsi měl[a] předtím, než ty dopisy ukázal. Určitě.", "angry")
    $ victim.say("Jestli se mi ten floutek přijde sám přiznat, můžeme se o něčem bavit, ale do té doby o něm už nechci slyšet.", "angry")
    return


label heinrichFireshow:
    $ mc.say("Viděl jste vystoupení té tanečnice s ohněm?")
    $ victim.say("Té, jak málem zapálila město?", "angry")
    $ mc.say("Té, jak potom bylo potřeba hasit. Ale jak moc je na vině, to se teprve snažím zjistit.")
    $ victim.say("Vystoupení jsem neviděl, s podobnou verbeží se nezahazuju a mám krásnou manželku.")
    $ victim.say("Viděl jsem hořící vůz a jiskry unášené větrem. Co víc potřebuješ zjišťovat?", "angry")
    show mcPic at menuImage
    menu:
        "Jestli měla něco zapálit opravdu v úmyslu.":
            hide mcPic
            $ victim.say("Mně nezáleží, co měla v úmyslu, záleží mi na tom, že tady málem shořel dům. Jeden požár jsme tu už měli a stačil.", "angry")
            $ victim.say("A vůbec, úmysl nebo ne, měla mít rozum. Mávat něčím zapáleným na ulici je hrozná neopatrnost, to si o něco podobného přímo říká.", "angry")
            $ victim.say("Na tom opravdu není, čím se dál zabývat.", "angry")
        "Jak přesně k tomu zapálení došlo.":
            hide mcPic
            $ mc.say("Víte, jak jsou tady všichni na oheň citliví. Nepřekvapilo by mě, kdyby jí ten ohnivý vějíř někdo zkusil vyrvat z rukou a k požáru došlo jen kvůli tomu.")
            $ mc.say("Mrzelo by mě, kdyby byla odsouzená jen proto, že se někdo jiný neovládl.")
            $ victim.say("Je pravda, že to se asi mohlo stát. Sousedi často blázní kvůli každé hlouposti.", "angry")
            $ victim.say("Potom bys ale měl[a] najít někoho, kdo u toho opravdu byl. Já v tomhle bohužel nepomůžu.")
            $ mc.say("Je možné, že u toho byl někdo z vašich učedníků. Ale jejich slovo bude před soudem mít mnohem větší váhu, když je podpoříte.")
            if "apprentices in trouble" in status:
                $ victim.say("Tyhle raubíře? Těm se nedá věřit nos mezi očima, [sam] jsi mě přece upozornil[a], co provedli.", "angry")
                $ victim.say("To po mně chtít nemůžeš. Moje slovo má pořád nějakou váhu a chci, aby to tak zůstalo.")
            else:
                $ victim.say("No to je jim podobné, že jakmile vidí holku, zapomenou na všechno ostatní.")
                $ victim.say("No co, práci hotovou měli a vzpomenout si, kdo s těmi pochodněmi jak mával, snad zvládnou i oni.")
                $ victim.say("Jestli u soudu přijdou s něčím, co má hlavu a patu, rád se postarám, aby si to ostatní poslechli.")
                $ status.append("Heinrich supports boys' testimony")
                if convincingWitness > 0:
                    $ katrin.cluesAgainst += 1
    return

label afterApologyReaction:
    show mcPic at menuImage
    menu:
        "Samozřejmě. Jdu se zas vrátit k případu.":
            hide mcPic
            $ time.addMinutes(5)
            jump victimEnd
        "Samozřejmě. Můžu vám ještě položit pár otázek?":
            hide mcPic
            $ victim.say("Když to musí být... tak se ptej.")
            return
    return

label afterApologyReactionPositive:
    show mcPic at menuImage
    menu:
        "Toho si vážím. Jdu se zas vrátít k případu.":
            hide mcPic
            $ time.addMinutes(5)
            jump victimEnd
        "Toho si vážím. Můžu vám ještě položit pár otázek?":
            hide mcPic
            $ victim.say("Bez toho to asi vyšetřit nemůžeš, tak do toho.")
            return
    return

label rumelinReminder:
    $ victim.say("Už jsi vyslechl[a] Rumelina?")
    if rumelin.alreadyMet == True:
        $ mc.say("Ano, ale sleduji všechny stopy, na které narazím.")
    else:
        $ mc.say("Nejdřív se na něj chci pořádně připravit.")
    return

label apologyForLateness:
    $ mc.say("Omlouvám se, zabral[a] jsem se do vyšetřování…")
    $ victim.say("Znamená to, že zloděje už máš?", "angry")
    $ mc.say("Ještě ne, ale...")
    $ victim.say("Tak se přestaň flákat a najdi ho.", "angry")
    return

label zeranLettersResponse:
    if victim.trust < 5:
        $ victim.say("Spálil jsem je.")
        $ mc.say("Proč? Mohl to být důkaz…")
        $ victim.say("A taky to mohlo mé holčičce zničit život a na tom mi záleží víc, než na nějakých důkazech.", "angry")
    else:
        "Mistr Heinrich se dlouze zamyslí."
        $ victim.say("Dobře, přinesu je. Ale ber je jako přísně důvěrnou věc, která může zničit život nevinné holce. Jestli zjistím, že se o nich dozvěděl někdo další, ještě o tom uslyšíš.")
        $ mc.say("To samozřejmě chápu a budu na to myslet.")
        "Mistr Heinrich přikývne a po chvíli ti přinese několik listů papíru svázaných tenkou koženou šňůrkou."
        call loveLetters
        $ victim.asked.append("letters for Ada shown")
        label loveLettersVictimMenu:
        menu:
            "{i}(Přečíst si dopisy znovu){i}":
                call loveLetters
                jump loveLettersVictimMenu
            "{i}(Nechat si dopisy u sebe){i}":
                $ victim.trust -= 2
                $ rauvin.trust -= 1
                "Než stihneš dopisy schovat, přeruší tě mistr Heinrich."
                $ victim.say("A teď děláš co? Ukázal jsem ti něco, co by mohlo mé holčičce zničit život. Vážně si myslíš, že ti dovolím si je odnést?", "angry")
                label heinrichLoveLettersReaction:
                show mcPic at menuImage
                menu:
                    "{i}(Vrátit dopisy mistru Heinrichovi){i}":
                        hide mcPic
                        $ victim.say("No proto.", "angry")
                        "Mistr Heinrich dopisy převezme a schová u sebe."
                        $ victim.say("A rozumíme si. Jestli Adě zkusíš jakkoli poškodit pověst, vyřídím si to s tebou.", "angry")
                    "Jestli je mám použít jako důkaz, potřebuji mít u sebe originál." if "need original letters" not in victim.asked:
                        hide mcPic
                        $ victim.asked.append("need original letters")
                        $ victim.say("Důkaz čeho? Jaký je Zeran zmetek? Nebo že jsme si tady hřáli na prsou hada? Nic jiného ta snůška lží nedokazuje.", "angry")
                        $ victim.say("A jestli bys je chtěl[a] někomu ukázat, tak na to rovnou zapomeň.")
                        call heinrichLoveLettersReaction
                    "Můžu si aspoň opsat tu báseň?":
                        call heinrichLoveLettersCopyPoem
            "Můžu si tu báseň opsat?":
                label heinrichLoveLettersCopyPoem:
                hide mcPic
                $ mc.say("Jenom pro případ, že by mohla být nějak důležitá.")
                $ victim.say("Důležitá? Mně přijde prostě jako hloupé cukrování.")
                $ victim.say("Ale pro mě za mě... můžeš si to i vydávat za vlastní, to je mi jedno.")
                $ victim.say("Ale jestli mojí holčičce zkusíš jakkoli poškodit pověst, vyřídím si to s tebou.", "angry")
                "Rychle si báseň opíšeš a pak vrátíš celý balíček dopisů mistru Heinrichovi."
                $ status.append("poem for Ada copied")
            "{i}(Vrátit dopisy mistru Heinrichovi){i}":
                "Mistr Heinrich dopisy převezme a schová u sebe."
                $ victim.say("A rozumíme si. Jestli Adě zkusíš jakkoli poškodit pověst, vyřídím si to s tebou.", "angry")
    return

label heinrichMaritalRelationship:
    $ victim.say("Co je tohle za otázky? Je to moje žena. Kdybychom spolu neměli dobrý vztah, nejsme manželé.", "angry")
    if victim.trust > 0 and "affair revealed" not in status:
        $ victim.say("Navíc bez ní a toho, jak vede domácnost, bych možná nebyl nejlepší švec v celém Marendaru.")
        show mcPic at menuImage
        menu:
            "Omlouvám se, nechtěl[a] jsem vás urazit.":
                hide mcPic
                $ victim.say("Tak se koukej vrátit k vyšetřování a přestaň řešit moje soukromí.", "angry")
            "Jak často jí to říkáte?":
                hide mcPic
                $ victim.asked.append("think about relationship")
                if victim.trust < 5:
                    $ victim.say("Co je ti do toho? Jsi tady jenom od toho, abys na[sel] můj ztracený výrobek, tak sebou pohni a nenavážej se do mého soukromí, nebo si budu stěžovat u tvého velitele.", "angry")
                else:
                    "Mistr Heinrich se zamračí a chvíli nad odpovědí přemýšlí."
                    $ victim.say("Možná...")
                    if "burned evidence seen" in victim.asked:
                        $ victim.say("Do toho ti nic není. Vrať se k pátrání a přines mi moje ztracené střevíce. Nebo aspoň toho vandala v zubech.")
                    else:
                        $ victim.say("Do toho ti nic není. Vrať se k pátrání a přines mi moje ztracené střevíce. Nebo aspoň toho zloděje v zubech.")
                    $ lisbeth.relationships["victim"] += 1
                    $ ada.trust += 1
                    $ status.append("fresh flowers")
                    $ status.append("flowers achievement")
    else:
        $ mc.say("Omlouvám se, nechtěl[a] jsem vás urazit.")
        $ victim.say("Ale urazil[a], tak se koukej vrátit k vyšetřování a nenavážej se do mého soukromí.", "angry")
    return

label rumelinExposedVictim:
    $ victim.asked.append("rumelin exposed")
    $ victim.trust += 5
    "Heinrichovy oči se rozzáří škodolibou radostí."
    if "burned evidence seen" in victim.asked:
        $ victim.say("Kromě zničení mých střevíců? To mě velmi zajímá. Našel se někdo další, kdo ohrožuje jeho pozici?", "happy")
    else:
        $ victim.say("Kromě krádeže mých střevíců? To mě velmi zajímá. Našel se někdo další, kdo ohrožuje jeho pozici?", "happy")
    $ mc.say("Mistr Njal chtěl na slavnostech představit stejný typ střevíců jako vy a mistr Rumelin se bál skandálu.")
    $ victim.say("To si myslel, že moje práce neobstojí v tom srovnání?", "angry")
    $ mc.say("Myslím, že mu šlo spíš o…")
    $ victim.say("Takové urážky si nenechám líbit. Rumelin sám sotva ušije obyčejný škrpál, brání v práci někomu stokrát lepšímu, a ještě si bude brát do huby moje výrobky?", "angry")
    $ victim.say("Postarám se, aby odteď ve městě nikomu nestál ani za pozdrav.", "happy")
    $ status.append("rumelin exposed")
    return

label victimJoinForces:
    hide mcPic
    $ victim.asked.append("join forces")
    $ mc.say("Pracovali jste na stejném typu bot a ty jeho kvůli snaze mistra Rumelina ještě nejsou hotové.")
    if "rumelin exposed" in status:
        show mcPic at menuImage
        menu:
            "Celý cech by to pochopil jako reakci na cechmistrovy špinavé machinace.":
                hide mcPic
                $ victim.say("To je pravda… spojit se proti němu by ke slovům přidalo i jasné gesto.")
                $ victim.say("Zajdu za ním a nabídnu mu pomoc.")
                call joinForcesVictimApproves
                return
            "Před slavnostmi už není moc času a oba na nich potřebujete něco představit...":
                hide mcPic
    else:
        $ mc.say("Před slavnostmi už není moc času a oba na nich potřebujete něco představit...")
    $ victim.say("Takže bych za ním měl jít ze zoufalství, s prosbou o pomoc?", "angry")
    $ mc.say("Tak jsem to nemyslel[a].")
    if victim.trust > 4:
        $ victim.say("A jak tedy?", "angry")
        $ mc.say("Že by v této situaci mohlo být pro vás oba výhodnější spojit síly a vytvořit společně něco mimořádného.")
        $ victim.say("A vzali by to lidi opravdu tak? Nechtěl bych, aby mě pomlouvali, že jsem líný přijít s vlastním výrobkem.")
        $ mc.say("Tak by to určitě nevypadalo...")
        if gender == "M":
            $ victim.say("Hele, jsi na hlídkaře celkem správný chlap, ale promiň, tomuhle nerozumíš.")
        else:
            $ victim.say("Hele, jsi na hlídkaře celkem správná ženská, ale promiň, tomuhle nerozumíš.")
        $ victim.say("Radši mi najdi moje boty. Nebo toho prevíta, co mi je sebral.")
        $ status.append("join forces victim pending")
    else:
        $ victim.say("Tak přestaň přemýšlet nad věcmi, které s tebou vůbec nesouvisí, a věnuj se své práci.", "angry")
    return

label joinForcesSurveyResults:
    hide mcPic
    $ victim.say("Opravdu? ... a jak to dopadlo?", "surprised")
    show mcPic at menuImage
    menu:
        "Nepřijali by to." if "join forces" in rumelin.asked or "join forces" in nirevia.asked or "join forces" in kaspar.asked:
            hide mcPic
            $ victim.say("Přesně to jsem čekal. Každý musí Einiona uctít sám svou vlastní prací, žádné zkratky a zjednodušení.")
            $ victim.say("S kým jsi vlastně mluvil[a]?")
            show mcPic at menuImage
            menu:
                "Říkal to cechmistr Rumelin." if "join forces" in rumelin.asked:
                    hide mcPic
                    $ victim.trust -= 2
                    $ victim.say("Vážně se chceš spoléhat na toho, kdo mi nejspíš ukradl ten první výrobek a kdo mě pomlouvá, kudy chodí?", "angry")
                "Říkala to paní Nirevia." if "join forces" in nirevia.asked:
                    hide mcPic
                    $ victim.trust -= 1
                    $ victim.say("Té tak budu věřit. Tváří se jako dáma, ale je jedna ruka s manželem a všichni víme, co ten je zač.", "angry")
                "Říkal to mistr Kaspar." if "join forces" in kaspar.asked:
                    hide mcPic
                    if "affair exposed" in status:
                        $ victim.trust -= 4
                        $ victim.say("Tohle jméno přede mnou ani nevyslovuj, nebo za ním půjdu znovu a tentokrát mu všechno vysvětlím pořádně.", "angry")
                        $ victim.say("Vůbec nechápu, proč s ním ztrácíš čas, a už vůbec ne, proč s ním mluvíš o mně.", "angry")
                    else:
                        $ victim.trust -= 1
                        $ victim.say("Kaspar je budižkničemu, co umí jen pomlouvat a lichotit a doufá, že to z něj udělá cechmistra. Tomu, co řekne, nepřikládám žádnou váhu.", "angry")
        "Vážili by si toho." if "join forces" in eckhard.asked or "join forces" in salma.asked:
            hide mcPic
            $ victim.say("Opravdu?", "surprised")
            $ victim.say("To jsem nečekal. To bych asi mohl...")
            $ victim.say("Kdo to vlastně říkal?")
            show mcPic at menuImage
            menu:
                "Říkal to mistr Eckhard." if "join forces" in eckhard.asked:
                    hide mcPic
                    $ victim.say("No jo, Eckhard. Na toho je spoleh. Jeden z mála lidí, co mě opravdu uznává. Takových kamarádů bych klidně měl víc.", "happy")
                    "Mistr Heinrich se na chvíli zamyslí a pak zavrtí hlavou."
                    $ victim.say("V tomhle na něj ale dát nemůžu. Ne všichni vidí věci jako on a on si to často neuvědomuje.")
                "Říkala to Salma." if "join forces" in salma.asked:
                    hide mcPic
                    $ victim.trust += 3
                    $ victim.say("Proč Salma? Ta přece není v cechu...", "surprised")
                    $ victim.say("Hm...", "angry")
                    $ victim.say("Je pravda, že nás všechny zná už dlouho, ale zároveň nemá důvod hrát nějaké hry.")
                    $ victim.say("Co že přesně říkala?")
                    $ mc.say("Že z lenosti nebo pohodlnosti by zrovna vás rozhodně nikdo nepodezříval, ale naopak by spolupráce s mistrem Njalem udělala velmi dobrý dojem.")
                    $ victim.say("Po těch letech, co k ní chodíme, už by mohla vědět, co říká...")
                    $ victim.say("Hned za Njalem zajdu, ať můžeme začít co nejdřív.")
                    call joinForcesVictimApproves
        "Nikdo nic užitečného neví.":
            hide mcPic
            $ victim.say("Tak to potom nemá smysl zkoušet.")
    $ status.remove("join forces victim pending")
    $ status.remove("join forces survey")
    return

label joinForcesVictimApproves:
    if "join forces njal approves" in status:
        $ mc.say("S mistrem Njalem už jsem mluvil a vypadá tomu nakloněný. Nemělo by být těžké se dohodnout.")
        $ victim.say("Ty mě pořád překvapuješ. V tom případě se hned pustíme do práce.")
        $ mc.say("Budu vám držet palce.")
        if not achievement.has(achievement_name['jointMasterpiece'].name):
            $ Achievement.add(achievement_name['jointMasterpiece'])
    else:
        $ mc.say("Možná raději chvíli počkejte. Zkusím nejdřív zjistit, jestli by souhlasil i on, ať víte, na čem jste.")
        $ victim.say("Dobře, ale pospěš si prosím. Slavnosti jsou brzy nesmíme ztrácet čas.")
        $ mc.say("Spolehněte se.")
    $ status.append("join forces victim approves")
    return

label joinForcesGoAhead:
    hide mcPic
    if "join forces go-ahead clueless" in victim.asked and "join forces go-ahead" in victim.asked:
        $ victim.asked.append("join forces go-ahead")
        $ victim.say("Znova? A řekl k tomu něco nového?")

    if "join forces njal approves" in status:
        $ victim.trust += 1
        $ mc.say("Vypadá tomu nakloněný. Pokud za ním zajdete, určitě se domluvíte.")
        $ victim.say("To rád slyším. V tom případě se hned pustíme do práce.")
        $ mc.say("Budu vám držet palce.")
    else:
        if "join forces njal pending" in status:
            show mcPic at menuImage
            menu:
                "Mistr Njal bude ochotný spolupracovat, jen pokud dostane spravedlnost za krádež svého střihu.":
                    hide mcPic
                    $ victim.say("Jak to myslíš, pokud dostane spravedlnost? To chce na oplátku nějaký střih ode mě, nebo co?", "angry")
                    $ mc.say("Chce zloděje toho střihu před soudem.")
                    "Mistr Heinrich se zamračí."
                    $ victim.say("Pak je to očividně ještě větší blázen, než se o něm říká. A s blázny já spolupracovat nebudu.", "angry")
                    $ mc.say("Pořád si myslím, že by vám ta spolupráce pomohla ohromit celé město. Pravděpodobně byste se pak konečně stal cechmistrem…")
                    $ victim.say("Nejsem jako Rumelin, abych kvůli jedné židli podrážel jiné lidi.", "angry")
                    $ victim.say("Máš ještě něco, nebo se konečně vrátíš k pátrání po tom zatraceném zloději?", "angry")
                "Bohužel to vypadá, že on o spolupráci nemá zájem.":
                    hide mcPic
                    $ victim.say("Já si od začátku myslel, že to nemá smysl...", "angry")
                    $ victim.say("Tak se vrať ke své opravdové práci a aspoň najdi toho zatraceného zloděje.", "angry")
        else:
            $ mc.say("Bohužel to vypadá, že on o spolupráci nemá zájem.")
            $ victim.say("Já si od začátku myslel, že to nemá smysl...", "angry")
            $ victim.say("Tak se vrať ke své opravdové práci a aspoň najdi toho zatraceného zloděje.", "angry")
    return

label victimLostBottlesSolved:
    hide mcPic
    $ victim.say("Tak to mě opravdu zajímá. Nech mě hádat, byl to Rumelin, aby mě o to víc naštval, když už tady byl pro ty boty, že ano?", "angry")
    show mcPic at menuImage
    menu:
        "Ano, byl to Rumelin.":
            hide mcPic
            $ victim.asked.append("lost bottles solved rumelin")
            $ victim.say("A proč jsi to ještě nezatkl[a]?", "angry")
            $ mc.say("Zatím proti němu sbírám důkazy.")
            $ victim.say("Tak s tím pohni, ať ho stihnou odsoudit ještě před slavnostmi.", "angry")
        "Byl to váš syn a učedníci.":
            hide mcPic
            $ victim.asked.append("lost bottles solved boys")
            $ mc.say("S botami to zřejmě vůbec nesouvisí, jenom chtěli upít a pak se nezastavili.")
            $ victim.say("Tak já je vezmu pod svou střechu, chovám se k nim jako k vlastním a oni mě za tu dobrotu ještě okradou? Ti poletí z domu. A ještě předtím je přerazím. A Aachima dvojnásob, holomka nevděčného.", "angry")
            if "apprentices in trouble" not in status:
                $ status.append("apprentices in trouble")
            show mcPic at menuImage
            menu:
                "To už je záležitost vaší domácnosti, ve které vám nechci nijak radit. Chtěl[a] jsem jenom, abyste o tom věděl.":
                    call victimPunishBoysForDrinking
                    return
                "Nemohl byste si to ještě rozmyslet?":
                    hide mcPic
                    $ victim.say("Co bych si na tom měl rozmýšlet?", "angry")
                    $ mc.say("Jsou to mladí kluci, kteří jednou zapomněli přemýšlet. Vyhodit je z domu je velmi přísný trest.")
                    $ victim.say("Kradli pod mou střechou! Celé město by v tom stálo za mnou, jakkoli mě nemají rádi.", "angry")
                    $ mc.say("Určitě. Ale pořád to znamená, že by skončili jako věční nádeníci kvůli jednomu nerozumu. Možná si zaslouží dostat ještě příležitost.")
                    $ victim.say("Aby to nebyla příležitost k další krádeži.", "angry")
                    $ mc.say("Myslím, že rychle poznáte, jestli se učedníci snaží sekat dobrotu.")
                    $ victim.say("Hm. Budiž, dám tomu pár dní. Aby se neřeklo.")
                    $ victim.say("Doufám, že to aspoň Rumelinovi vezme vítr z plachet, až mě zase někde bude pomlouvat.")
    return

label victimPunishBoysForDrinking:
    hide mcPic
    $ status.append("boys punished for drinking")
    $ victim.trust += 2
    $ son.trust -= 2
    $ optimist.trust -= 2
    $ yesman.trust -= 2
    $ ada.trust -= 1
    $ lisbeth.trust -= 1
    $ victim.say("To je také v pořádku. Teď mě ale omluv, jdu si to s nimi vyřídit.")
    "Mistr Heinrich ti pokyne a ty vyjdeš ven na ulici. Krátce zahlédneš paní Lisbeth, která tě chtěla vyprovodit, jak se překvapeně a znepokojeně dívá na svého manžela. Pak za tebou dveře domu zapadnou."
    $ leaveOption ="none"
    return

label victimArrestEckhard:
    hide mcPic
    $ victim.asked.append("should arrest eckhard")
    $ victim.trust -= 1
    $ victim.say("Za krádež střihu? A kdo ho za něco takového bude žalovat?", "surprised")
    $ mc.say("Mistr Njal. Vypadal, že na tom bude trvat.")
    $ victim.say("Zatracený trpasličí přivandrovalec.", "angry")
    $ victim.say("Myslím tím, nedalo by se mu domluvit, že v Marendaru máme jiné zákony než u nich na severu... nebo odkud přišel?")
    show mcPic at menuImage
    menu:
        "Krádež je krádež, tam moc rozdílů nevidím.":
            hide mcPic
            $ rauvin.trust += 1
            $ victim.say("Ale přece jste říkal, že už má ten svůj střih zase zpátky, takže se nestala žádná škoda.")
        "Pokusím se s ním promluvit.":
            hide mcPic
            $ victim.trust += 2
            $ victim.say("Výborně, aspoň někdo tady má rozum. Tak s ním promluv a nějak to urovnej.")
        "Můžu se o to pokusit, ale musel byste také prokázat dobrou vůli.":
            hide mcPic
            if victim.trust < 4:
                $ victim.say("Dobrou vůli? A to má jako znamenat co? To mě ten trpaslík chce vydírat, nebo jak to mám chápat?", "angry")
                $ mc.say("Tak jsem to nemyslel[a]...")
                $ victim.say("A jak tedy?", "angry")
                $ victim.say("Nebo víš co? Radši přestaň myslet na blbosti a začni konečně dělat svou práci.", "angry")
                $ victim.say("A to je hledání zloděje, ne zatýkání slušných lidí.", "angry")
            else:
                $ victim.say("No dobře, dobrou vůli, ale jak? Mám mu zase já půjčit nějaký svůj střih?")
                show mcPic at menuImage
                menu:
                    "Já můžu zapomenout na krádež a přesvědčit o tom i Njala, pokud vy zapomenete na jednu hloupou klukovinu." if "confession" in boysAsked or "confession" in son.asked:
                        hide mcPic
                        $ victim.say("O čem to mluvíš? Jakou klukovinu?", "angry")
                        label heinrichDealMischiefOptions:
                        show mcPic at menuImage
                        menu:
                            "Myslím tu jejich malou pitku." if "lost bottles solved boys" in victim.asked and "someone got drunk..." not in victim.asked:
                                hide mcPic
                                $ victim.say("Tu, za kterou je chci vyhodit? To není žádná klukovina, to je krádež pod střechou jejich mistra.", "angry")
                                $ mc.say("Co kdyby se z vašich soukromých zásob nic neztratilo, stejně jako mistru Njalovi nikdo neukradl jeho střih? Jestli si rozumíme.")
                                call heinrichDealMischief2
                            "Kdyby se třeba někdo opil..." if "someone got drunk..." not in victim.asked:
                                hide mcPic
                                $ victim.asked.append("someone got drunk...")
                                if "alcoholic" in eckhard.asked or "alcoholic" in salma.asked or "alcoholic" in lisbeth.asked:
                                    $ victim.say("“Jestli se mě snažíš urazit, tak si mě nepřej!", "angry")
                                    $ mc.say("Vás samozřejmě nemyslím.")
                                    $ victim.say("Tak co tím myslíš?", "angry")
                                else:
                                    $ victim.say("Koho tím myslíš? Doufám, že se nesnažíš nic naznačit.", "angry")
                                jump heinrichDealMischiefOptions
                            "Kdyby třeba někdo z vašich učedníků...":
                                hide mcPic
                                $ victim.asked("accusing apprentices")
                                $ victim.say("Co zase provedli, holomci?", "angry")
                                call heinrichDealMischief1
                            "Kdyby třeba váš syn...":
                                hide mcPic
                                $ victim.asked("accusing son")
                                $ victim.say("Jestli ten budižkničemu něco provedl, tak ať si mě nepřeje!", "angry")
                                call heinrichDealMischief1
                    "Mohl byste například méně pít." if "confession" in boysAsked:
                        hide mcPic
                        $ victim.say("Co má moje pití s čím společného? To se mě snažíš urazit, nebo jak to mám brát?", "angry")
                        $ mc.say("To ne, jenom jsem si všiml[a], že...")
                        "Mistr Heinrich tě nechá mluvit, ale z jeho pohledu se dá jasně vyčíst varování."
                        show mcPic at menuImage
                        menu:
                            "...vám to ve městě dělá špatné jméno.":
                                hide mcPic
                                $ victim.say("Moje jméno je jenom moje věc. A rozhodně nepotřebuju rady od nějakého náhodného strážného.", "angry")
                                if "burned evidence seen" in victim.asked:
                                    $ victim.say("Vrať se radši ke své práci a najdi už konečně moje ztracené boty. Nebo aspoň toho holomka, co mi je zničil.", "angry")
                                else:
                                    $ victim.say("Vrať se radši ke své práci a najdi už konečně moje ztracené boty. Nebo aspoň toho holomka, co mi je ukradl.", "angry")
                            "...si z toho bere příklad váš syn a učedníci.":
                                hide mcPic
                                if "lost bottles solved boys" in victim.asked:
                                    $ victim.say("No dovol?! Já piju jen to, na co si sám vlastníma rukama vydělám!", "angry")
                                    $ mc.say("To by Aachim určitě také rád, přeci jen je to váš syn, ale jak by si ve svém věku mohl pořádně vydělat?")
                                    $ mc.say("Z vlastního si může dát tak nanejvýš nějaký patok pro chudinu.")
                                    $ victim.say("Tak ať nepije vůbec. Nebo ať aspoň nepije tolik, že přestane znát míru.")
                                    show mcPic at menuImage
                                    menu:
                                        "Paní Lisbeth říká, že to se často stává i vám...":
                                            hide mcPic
                                            $ victim.trust -= 3
                                            $ rauvin.trust -=3
                                            $ hayfa.trust -=3
                                            $ solian.trust -= 4
                                            "Mistr Heinrich na tebe jen několik okamžiků upřeně hledí."
                                            $ victim.say("Ven.", "angry")
                                            $ victim.say("Na vyřešení případu máš zhruba tolik času, než dojdu na strážnici si na tebe stěžovat, tak sebou konečně pohni.", "angry")
                                            "Přes veškerou tvou snahu mistr zůstane zcela nesmlouvavý a ty se vzápětí ocitneš na ulici před jeho domem."
                                            $ refusedBy = "victim"
                                            $ leaveOption = "none"
                                        "To by měl, ale nemá vaše zkušenosti. A ty nemůže získat od nikoho lepšího než od vás.":
                                            hide mcPic
                                            $ victim.say("No pít s ním nezačnu, jestli míříš tímhle směrem.")
                                            $ victim.say("Až se vrátí z tovaryšské cesty na zkušenou, tak ano. Do té doby nesmí zapomenout, že je hlavně učedník a já jeho mistr. To by nedělalo dobrotu.")
                                            $ mc.say("Samozřejmě. Mohl by potom být méně ochotný vám naslouchat.")
                                            $ victim.say("Přesně. Ale vysvětlit mu pár věcí můžu. Ať mi nedělá ostudu.")
                                        "Nemá vaše zkušenosti. Možná si myslí, že pil jen tolik, jak často vidí pít vás.":
                                            hide mcPic
                                            $ victim.say("Takže můj vlastní syn krade a můžu za to já?", "angry")
                                            $ mc.say("Jenom se snaží vzít si z vás příklad a...")
                                            $ victim.say("Kdyby radši stejně jako já šil boty.", "angry")
                                            $ victim.say("A kdyby radši všichni dělali, co mají. Třeba hledali moje boty, místo aby strkali nos do záležitostí mojí rodiny.", "angry")
                                else:
                                    $ victim.say("Váš syn chce být jako vy. Ale to, že vy sám s alkoholem nemáte problémy, nezaručí, že na tom on bude stejně.")
                                    $ victim.say("Samozřejmě, že chce být jako já.")
                                    "Heinrich se zamračí, ale zároveň vypadá vlastně téměř potěšeně."
                                    $ victim.say("Ale do toho tobě nic není. Svého syna si srovnám sám.", "angry")
                                    $ mc.say("Na to nikdo nebude vhodnější. Ostatně zřejmě si z vás on a učedníci berou příklad i v tom, že chtějí pít jen ty nejlepší pálenky.")
                                    $ victim.say("No přece se Aachim nespokojí s kdejakou břečkou...")
                                    $ victim.say("Počkej, ty jsi s nimi pil[a], nebo jak to víš? Nemáš pracovat na případu?", "angry")
                                    $ mc.say("Během práce na případu jsem právě zjistil[a], že ty ztracené lahve, o kterých jsme mluvili, vypil Aachim s učedníky. Ale není za tím žádný zlý úmysl, jen kluci také chtěli slavit.")
                                    if "lost bottles solved rumelin" in victim.asked:
                                        $ victim.trust -= 2
                                        $ victim.say("Cože? Neříkal[a] jsi předtím, že mi je ukradl Rumelin?", "surprised")
                                        call stupidExcuse
                                        $ mc.say("Chtěl[a] jsem jenom, abyste je nepotrestal moc přísně")
                                        $ victim.say("S kluky si ještě promluvím, a jestli to opravdu vypili oni, tak je potrestám po zásluze. Ale na tebe si budu stěžovat u tvých nadřízených.", "angry")
                                        $ victim.say("A teď se mi kliď z očí.", "angry")
                                        $ refusedBy = "victim"
                                    else:
                                        $ victim.say("Cože? Chceš říct...", "surprised")
                                        $ mc.say("Že než někoho pozvete k sobě domů na pohárek, raději se podívejte, co mu můžete nabízet, aby to nevypadalo hloupě.")
                                        $ victim.say("Oni vypili moje zásoby?! Já je přetrhnu, víš, kolik to stálo?", "angry")
                                        $ mc.say("Tuším, že výrazně víc, než kdejaká břečka.")
                                        "Mistr Heinrich se na několik okamžiků odmlčí. Působí rozhněvaně, ale ne natolik, aby mu jeho hněv ukázal směr."
                                        $ victim.say("Tohle si budou muset odpracovat. A to při jejich šikovnosti znamená, že jako mí učedníci zešednou.", "angry")
                                        $ status.append("apprentices saved")
                                    if "apprentices in trouble" not in status:
                                        $ status.append("apprentices in trouble")
                    "Promluvím s Njalem, pokud napravíte tu křivdu, kterou jste udělal Zeranovi." if zeranNote.isActive:
                        hide mcPic
                        if "zeran's name cleared" in status:
                            $ victim.say("No zpátky ho brát nebudu. To by nedělalo dobrotu. Ale... no... dobře, asi mu můžu vrátit jeho peníze. Ať to zkusí jinde.")
                            $ status.append("Zeran got his money back")
                            show mcPic at menuImage
                            menu:
                                "To mu určitě pomůže a mělo by mu to stačit.":
                                    hide mcPic
                                    $ victim.say("Doufám, že to bude stačit i mně, abych už měl od toho holomka jednou pro vždy pokoj.", "angry")
                                "To byste měl v každém případě, to není projev dobré vůle.":
                                    hide mcPic
                                    $ victim.say("A co víc by si představoval?", "angry")
                                    show mcPic at menuImage
                                    menu:
                                        "Aspoň mu najít jiného mistra.":
                                            hide mcPic
                                            $ mc.say("Musíte mít v cechu spoustu známých, od vás to vezmou lépe, než od Zerana.")
                                            $ victim.say("Dobře, asi můžu za někým zajít a říct mu, že ten lunt je sice nemehlo jako všichni učedníci, ale vzít si ho pod střechu není nic nebezpečného.")
                                            $ victim.say("Vanya teď myslím někoho hledá, je to elfka a v tomhle městě je z těch lepších. Můžeš Zeranovi říct, ať se za ní staví. A Njalovi, že se o toho holomka postarám.")
                                            $ status.append("Vanya can take Zeran")
                                        "Peníze navíc jako odškodné.":
                                            hide mcPic
                                            $ victim.say("Co je tohle za nesmysl? Peníze se mají vydělávat poctivou prací, ne jen tak dostávat za nic.", "angry")
                                            $ victim.say("Jako učedník bude mít živobytí a bude si moct vydělat malé kapesné. Aspoň bude mít důvod se snažit.", "angry")
                                        "Veřejnou omluvu.":
                                            hide mcPic
                                            $ victim.trust -= 1
                                            $ victim.say("A k čemu mu to bude? Jen bych byl celému městu pro smích a jemu by to nepomohlo.", "angry")
                                            $ victim.say("Navíc já si za svými činy stojím. Že to nebyl on, to jsem tehdy nemohl vědět a rozhodně jsem ho ve svém domě nemohl nechat, když to také on klidně být mohl.", "angry")
                        else:
                            $ victim.trust -= 5
                            "Mistr Heinrich na pár okamžiků není překvapením schopen slova."
                            $ victim.say("Cože?! Vážně?! Toho zmetka, co mi málem zprznil dceru?! Co to po mně chceš?!", "angry")
                            $ mc.say("Ale...")
                            if "burned evidence seen" in victim.asked:
                                $ victim.say("Tohle odmítám poslouchat! Vypadni z mého domu a nevracej se bez mých bot nebo toho holomka, co mi je zničil!", "angry")
                            else:
                                $ victim.say("Tohle odmítám poslouchat! Vypadni z mého domu a nevracej se bez mých bot nebo toho holomka, co mi je ukradl!", "angry")
                            $ refusedBy = "victim"
                    "Aspoň Njalovi za ten střih zaplatit. Můžu mu peníze rovnou donést.":
                        hide mcPic
                        $ victim.say("To by možná mohlo být fér... tedy podle toho, kolik ten trpaslík chce, samozřejmě.")
                        $ victim.say("Zase tak dobrý ten střih není.", "angry")
                        $ mc.say("Co třeba cena jednoho páru bot, které byste podle něj vyrobil?")
                        "Mistr Heinrich se na chvíli zamyslí."
                        $ victim.say("Tohle si ještě budu muset promyslet a propočítat. Pošlu pak kdyžtak Aachima.")
                        $ mc.say("Když to tak zmiňujete, vlastně nevím, jakou cenu přesně mistr Njal myslel... možná bych se ho měl[a] nejdřív zeptat...")
                        $ mc.say("Rozhodně Aachima neposílejte dřív, než dám vědět.")
                        $ victim.say("Chápu. Možná bych se měl s Njalem domluvit napřímo.")
                        $ mc.say("Možná to ještě předtím zkusím nějak urovnat.")
                        $ victim.say("Tak ale pohni, slavnosti se blíží.", "angry")
                    "To si ještě nejsem jist[y], ale na něco přijdu.":
                        hide mcPic
                        "Heinrich se zamračí a pro sebe zavrčí něco o tom, proč s tím pak vůbec začínáš, ale víc nekomentuje."
    return

label stupidExcuse:
    show mcPic at menuImage
    menu:
        "To jsem neříkal[a].":
            hide mcPic
            $ victim.say("To mě máš za pitomce? Nenechám si lhát do očí.", "angry")
        "Musel[a] jsem se splést.":
            hide mcPic
            $ victim.say("Takže mi buď lžeš do očí, nebo jsi ještě hloupější než průměrný strážný.", "angry")
        "Vyšly najevo nové okolnosti.":
            hide mcPic
            $ victim.say("Takže mi buď lžeš do očí, nebo jsi ještě hloupější než průměrný strážný.", "angry")
    return

label heinrichDealMischief1:
    if "confession" in boysAsked and "confession" in son.asked:
        show mcPic at menuImage
        menu:
            "Myslím tu jejich malou pitku." if "lost bottles solved boys" in victim.asked:
                hide mcPic
                $ victim.say("Tu, za kterou je chci vyhodit? To není žádná klukovina, to je krádež pod střechou jejich mistra.", "angry")
                $ mc.say("Co kdyby se z vašich soukromých zásob nic neztratilo, stejně jako mistru Njalovi nikdo neukradl jeho střih? Jestli si rozumíme.")
                call heinrichDealMischief2
            "Kdy jste naposled kontroloval své zásoby vína a jiného alkoholu?" if "lost bottles solved boys" not in victim.asked:
                hide mcPic
                if "apprentices in trouble" not in status:
                    $ status.append("apprentices in trouble")
                if "accusing son" in victim.asked:
                    $ victim.say("Říkáš, že mi Aachim učednická chodí na moje soukromé zásoby?", "angry")
                else:
                    $ victim.say("Říkáš, že mi ta holota učednická chodí na moje soukromé zásoby?", "angry")
                if "lost bottles solved rumelin" in victim.asked:
                    $ victim.trust -= 2
                    $ victim.say("Neříkal[a] jsi předtím, že mi ty lahve ukradl Rumelin?", "angry")
                    call stupidExcuse
                    $ mc.say("Chtěl[a] jsem jen říct, co kdyby se z vašich soukromých zásob nic neztratilo, stejně jako mistru Njalovi nikdo neukradl jeho střih? Jestli si rozumíme.")
                    $ victim.say("Takže ty mi nejdřív lžeš a pak máš tu drzost za mnou chodit s takovouhle špinavostí? To si zkoušej u Rumelina, ale ne u mě.", "angry")
                    $ victim.say("Koukej se okamžitě vrátit k případu a vyřešit ho dřív, než si na tebe stihnu stěžovat u tvých nadřízených.", "angry")
                    $ victim.say("A moji domácnost nech mně. Do té ti nic není.", "angry")
                    $ refusedBy = "victim"
                else:
                    $ mc.say("Říkám, že se z vašich soukromých zásob nic neztratilo, stejně jako mistru Njalovi nikdo neukradl jeho střih. Jestli si rozumíme.")
                    label heinrichDealMischief2:
                    "Heinrich se zamračí."
                    $ victim.say("Rozumím tomu, že si mě asi pleteš s Rumelinem.", "angry")
                    if "accusing son" in victim.asked:
                        $ victim.say("Co je tohle vůbec za dohodu? Proč by Njalovi mělo záležet na na Aachimovi?", "angry")
                    else:
                        $ victim.say("Co je tohle vůbec za dohodu? Proč by Njalovi mělo záležet na mých učednících?", "angry")
                    show mcPic at menuImage
                    menu:
                        "Záleží mu na tom, jak se stavíte ke spravedlnosti.":
                            hide mcPic
                            $ mc.say("Když ukážete, že také dokážete odpouštět, můžu to použít při přesvědčování, že by měl odpustit i on.")
                            "Heinrich se zamyslí a pak pomalu přikývne."
                            $ victim.say("No dobře, kvůli Eckhardovi. Nic z toho se nestalo. A ty teď padej z mého domu a místo věcí, které se nestaly, vyšetři tu jednu, která se stala.")
                            $ status.append("apprentices saved")
                        "To vás nemusí zajímat. Návrh je jasný, přijměte, nebo odmítněte.":
                            hide mcPic
                            $ victim.trust -= 2
                            $ victim.say("V tom případě odmítám. Vydírat se nenechám a Eckhard taky ne.", "angry")
                            $ victim.say("“A ty se koukej vrátit ke své práci, než si dojdu promluvit s tvými nadřízenými.", "angry")
                        "Záleží na nich mně, jestli se jich nikdo jiný nezastane.":
                            hide mcPic
                            $ victim.trust -= 1
                            $ victim.say("A ty se jich chceš zastávat? Vždyť jsi právě řekl[a], že kradli pod mou střechou!", "angry")
                            $ mc.say("Nechci, aby měli zkažený celý život kvůli jedné nerozvážnosti.")
                            $ victim.say("Sahat do mých zásob není nerozvážnost, ale zlodějina. Museli dobře vědět, co dělají.", "angry")
                            $ mc.say("Jsou to mladí kluci, ti občas prostě nepřemýšlí. Já jen prosím, abyste vybral trest, který z nich neudělá věčné nádeníky, kteří ani nedokončili učení.")
                            $ victim.say("Hm. Milosrdnější než Heulwen. A Eckharda do toho taháš proč?", "angry")
                            $ mc.say("Chtěl[a] jsem, abyste kromě velkorysosti měl ještě další důvod, proč nad tím celým přemýšlet.")
                            $ victim.say("Takže mě opravdu máš za Rumelina. No, učedníci tu zůstanou a budou mi moci dokázat, že se polepšili. A jestli proti Eckhardovi uslyším křivé slovo, vyřídím si to ne s nimi, ale s tebou osobně.", "angry")
                            if "burned evidence seen" in victim.asked:
                                $ victim.say("A teď se prosím přestaň zdržovat věcmi, do kterých ti nic není, a najdi konečně toho vandala.", "angry")
                            else:
                                $ victim.say("A teď se prosím přestaň zdržovat věcmi, do kterých ti nic není, a najdi konečně toho zloděje.", "angry")
            "Celé to byla jen nešťastná náhoda...":
                hide mcPic
                $ victim.say("Tak tohle si chci poslechnout. Co byla nešťastná náhoda?", "angry")
                if "accusing son" in victim.asked:
                    $ victim.say("Jestli s mými botami něco provedl Aachim, tak ho chci vidět na pranýři, bez ohledu na to, že to je můj syn. A ještě předtím ho vlastnoručně přetrhnu jak hada.")
                else:
                    $ victim.say("Jestli s mými botami něco provedla ta holota učednická, tak je chci vidět na pranýři, bez ohledu na to, že pak nebudou moci pracovat. A ještě předtím je vlastnoručně přetrhnu jak hada.")
                show mcPic at menuImage
                menu:
                    "Vlastně si nejsem jist[y]...":
                        hide mcPic
                        $ victim.trust -= 1
                        $ victim.say("Tak proč tohle všechno? Nejdřív začneš o dobré vůli, pak chvíli chodíš kolem horké kaše a nakonec řekneš, že vlastně nic? To myslíš, že ani jeden z nás nemá nic lepšího na práci?", "angry")
                        $ victim.say("Koukej se radši vrátit k vyšetřování. A až budeš něco opravdu chtít, řekni to rovnou.", "angry")
                    "O vaše boty nejde.":
                        hide mcPic
                        $ mc.say("Kluci zkazili nějaký materiál a báli se, co tomu řeknete.")
                        $ victim.say("To se jim stává běžně. Co to bylo zač, že jsou z toho tak vyděšení?", "angry")
                        $ mc.say("Já... si vlastně nejsem jist[y]. Pochopte, jak ševcovině nerozumím...")
                        $ victim.say("Chápu. V každém případě si s nimi o tom promluvím. Jestli sahali na něco drahého a ještě to zkazili, ať si mě nepřejí.")
                        $ mc.say("Jenom se snažili pracovat co nejlépe, abyste na ně mohl být hrdý.")
                        $ victim.say("Mají dělat, co se jim řekne. Nejvíc hrdý na ně budu, až konečně ušijí pořádnou pevnou botu.", "angry")
                        $ mc.say("Jistě že to nebylo nejchytřejší, proto klukovina. Ale chtěli vám udělat radost, i když hloupě. To možná stojí za trochu dobré vůle.")
                        $ victim.say("Asi uvidíme podle toho, o co přesně šlo.")
                    "Ano, za ztrátu vašich bot může Aachim." if "accusing son" in victim.asked:
                        hide mcPic
                        $ victim.asked("A proč jsi ho ještě nezatkl[a]?")
                        show mcPic at menuImage
                        menu:
                            "Nebyl[a] jsem si jist[y], jestli byste to chtěl.":
                                hide mcPic
                                $ mc.say("Přeci jen by to mohlo poškodit vaši pověst. Navíc teď, před slavnostmi a volbou nového cechmistra...")
                                $ victim.say("To je vlastně pravda. Možná bude lepší, když si Aachima srovnám sám.")
                                $ victim.say("Nebo tebe, jestli ho obviňuješ neprávem.", "angry")
                                $ mc.say("Jen jsem chtěl[a], abyste na něj nebyl moc tvrdý...")
                                $ victim.say("Kvůli Eckhardovi? Ten by byl první, kdo by mi poradil, ať si to s tím holomkem pořádně vyříkám.", "angry")
                                $ victim.say("A taky by mi poradil, ať se tu s tebou nevybavuju o pochybných dohodách a okamžitě tě vyhodím.", "angry")
                                $ victim.say("S tím musím souhlasit. Dveře najdeš.", "angry")
                                if "apprentices in trouble" not in status:
                                    $ status.append("apprentices in trouble")
                            "Ještě nemám dost důkazů.":
                                hide mcPic
                                $ victim.say("Tak na zatčení nemáš důkazy, ale na obvinění ano?")
                                $ victim.say("Asi bych si měl jít promluvit s tvým velitelem. Protože můj syn je možná budižkničemu, ale rozhodně ne zloděj. A nikdo nebude tvrdit opak a už vůbec ne bez důkazů.", "angry")
                                $ mc.say("Jen jsem chtěl[a], abyste na něj nebyl moc tvrdý...")
                                $ victim.say("Hlavně by někdo měl být tvrdší na tebe, aby ses přestal[a] navážet do mé rodiny.", "angry")
                                $ victim.say("O Aachima se postarám sám. Hned po tom, co si na tebe dojdu stěžovat.", "angry")
                                $ victim.say("A teď se koukej vrátit k vyšetřování.", "angry")
                        $ refusedBy = "victim"
                        $ leaveOption = "none"
                    "Ano, za ztrátu vašich bot můžou učedníci." if "accusing apprentices" in victim.asked:
                        hide mcPic
                        $ victim.asked("A proč jsi je ještě nezatkl[a]?")
                        show mcPic at menuImage
                        menu:
                            "Nebyl[a] jsem si jist[y], jestli byste to chtěl.":
                                hide mcPic
                                $ mc.say("Přeci jen by to mohlo poškodit vaši pověst. Navíc teď, před slavnostmi a volbou nového cechmistra...")
                                $ victim.say("To je vlastně pravda. Možná bude lepší, když si je srovnám sám.")
                                $ victim.say("Nebo tebe, jestli je obviňuješ neprávem.", "angry")
                                $ mc.say("Jen jsem chtěl[a], abyste na ně nebyl moc tvrdý...")
                                $ victim.say("Kvůli Eckhardovi? Ten by byl první, kdo by mi poradil, ať si to s těmi holomky pořádně vyříkám.", "angry")
                                $ victim.say("A taky by mi poradil, ať se tu s tebou nevybavuju o pochybných dohodách a okamžitě tě vyhodím.", "angry")
                                $ victim.say("S tím musím souhlasit. Dveře najdeš.", "angry")
                                if "apprentices in trouble" not in status:
                                    $ status.append("apprentices in trouble")
                            "Ještě nemám dost důkazů.":
                                hide mcPic
                                $ victim.say("Tak na zatčení nemáš důkazy, ale na obvinění ano?")
                                $ victim.say("Asi bych si měl jít promluvit s tvým velitelem. Protože my jsme slušná domácnost a nikdo tady nekrade. A nikdo nebude tvrdit opak a už vůbec ne bez důkazů.", "angry")
                                $ mc.say("Jen jsem chtěl[a], abyste na ně nebyl moc tvrdý...")
                                $ victim.say("Hlavně by někdo měl být tvrdší na tebe, aby ses přestal[a] navážet do mé rodiny.", "angry")
                                $ victim.say("O učedníky se postarám sám. Hned po tom, co si na tebe dojdu stěžovat.", "angry")
                                $ victim.say("A teď se koukej vrátit k vyšetřování.", "angry")
                $ refusedBy = "victim"
                $ leaveOption = "none"
    return

label mcAdmitsBurglary:
    "Heinrich bez dalšího varování udělá rychlý krok směrem k tobě a vystřelí pěstí. Vzápětí ucítíš otřes a bolest na tváři."
    $ victim.say("A takhle si představuješ práci hlídky?", "furious")

    if victim.trust > 3:
        "Než se stihneš rozhodnout, jestli se hájit, bránit, nebo utéct, mistr tě chytí pod krkem a přiřazí tě ke stěně. Drží tě pevně a navzdory očividnému hněvu dobře hlídá tvoje ruce i další způsoby, jak by ses snad mohl[a] pokusit uniknout."
        $ victim.say("Tohle považuju za hodně velkou zradu. Buď rád[a], že doteď ses choval[a] celkem slušně, protože to je ten jediný důvod, proč odtud odejdeš po svých.", "furious")
        "Mistr Heinrich přivolá Aachima a společně tě pevně sevřou a vyvedou ven z domu."
    else:
        "Než se stihneš rozhodnout, jestli se hájit, bránit, nebo utéct, dopadnou na tebe další tvrdé údery, které mistr Heinrich doprovází nadávkami."
        $ mc.imageParameter = "beaten"
        "Brzy je jasné, že ševcovského mistra nezastavíš ani mu nedokážeš vyklouznout."
        if lisbeth.trust > 3:
            "I přes rámus rvačky uslyšíš rychlé kroky."
            $ lisbeth.say("Heinrichu, co to děláš? V našem domě! Co Olwenův zákon pohostinství?", "surprised")
            "Její manžel se zastaví s pěstí zdviženou k úderu, ale neotočí se k ní ani nepovoluje sevření, kterým ti znemožňuje cokoli podniknout."
            $ victim.say("Zákon pohostinství tady porušil[a] on[a]. Zneužil[a] moji důvěru a vloupal[a] se mi do dílny.", "furious")
            $ lisbeth.say("Opravdu? Nemůže to být jen nějaká mýlka?", "surprised")
            $ victim.say("[sam].capitalize() se právě přiznal[a].", "furious")
            "Paní Lisbeth se nadechne, ale poté ti jen věnuje smutný a zklamaný pohled a odejde z místnosti."
        elif ada.trust > 3:
            "I přes rámus rvačky uslyšíš rychlé kroky."
            $ ada.say("Co to zase děláš? To už musíš mlátit lidi i ve vlastním domě?", "surprised")
            "Její otec se zastaví s pěstí zdviženou k úderu, ale neotočí se k ní ani nepovoluje sevření, kterým ti znemožňuje cokoli podniknout."
            $ victim.say("Takhle se se mnou neopovažuj mluvit, nebo budeš další na řadě.", "furious")
            $ ada.say("Proč nám pořád jenom děláš ostudu?", "angry")
            if gender == "M":
                $ victim.say("Tenhle podrazák zneužil[a] moji důvěru a vloupal[a] se mi do dílny.")
            else:
                $ victim.say("Tahle podrazačka zneužil[a] moji důvěru a vloupal[a] se mi do dílny.")
            $ ada.say("Určitě? Nebo to tak jenom trochu vypadalo a to ti stačilo?", "angry")
            $ victim.say("Ukradl[a] odtamtud tvoje milostné dopisy a potom je ukazoval[a] kdo ví komu.", "furious")
            $ ada.say("Cože? Co to je za nesmysl?", "surprised")
            $ victim.say("Právě se k tomu přiznal[a].", "furious")
            "Ada několik okamžiků zůstane nerozhodně stát a poté se prudce otočí na patě a rázným krokem opět odejde."
            "Heinrich si tě chvíli měří a potom přidá ještě několik tvrdých ran."
        elif son.trust > 3:
            "I přes rámus rvačky uslyšíš rychlé kroky a několik tlumených slov a potom do místnosti vejde Heinrichův syn."
            $ son.say("Co se děje? Proč... v čem jste se nepohodli?", "surprised")
            "Jeho otec se zastaví s pěstí zdviženou k úderu, ale neotočí se ani nepovoluje sevření, kterým ti znemožňuje cokoli podniknout."
            if gender == "M":
                $ victim.say("Tenhle podrazák zneužil[a] moji důvěru a vloupal[a] se mi do dílny.")
            else:
                $ victim.say("Tahle podrazačka zneužil[a] moji důvěru a vloupal[a] se mi do dílny.")
            $ son.say("... aha... určitě? Co tam dělal[a]?", "surprised")
            $ victim.say("Nic, o čem má smysl mluvit.", "angry")
            if "Aachim seen during break-in" in status:
                show mcPic at menuImage
                menu:
                    "Aachim v té dílně byl také.":
                        hide mcPic
                        $ victim.say("Nejen že se mi vloupáš do dílny, ale ještě mi chceš namluvit takhle nehorázný nesmysl? Za co mě máš?", "furious")
                        $ son.say("Asi už neví, jak se zachránit, tak se snaží odvést pozornost.", "angry")
                        $ victim.say("Špína.", "furious")
                    "Jen jsem pátral[a] po tom zloději...":
                        hide mcPic
                        $ victim.say("V noci a v mojí dílně bez mého vědomí. O tom už jsme mluvili.", "furious")
                        $ victim.say("Špíno.","furious")
                    "{i}(neříct nic){/i}":
                        hide mcPic
            "Heinrich si tě chvíli měří a potom přidá ještě několik tvrdých ran. Aachim mezitím odejde z místnosti."
        else:
            "Všimneš si, že rámus rvačky přiláká další členy domácnosti, ale nikdo z nich nezasahuje. Po chvíli se tvé modřiny začnou slévat dohromady a mistr Heinrich konečně přestane."
        $ victim.say("Tak a teď se půjdeme zeptat, co si o tom celém myslí tví nadřízení.", "angry")
        "Mistr Heinrich přivolá Aachima a společně tě pevně sevřou, zvednou na nohy a vyvedou ven z domu." 
    scene bg heinrich outside
    "Na ulici tě potom začnou táhnout směrem ke strážnici."
    "Vaše skupinka brzy vzbudí pozornost dalších měšťanů. Ptají se, co se děje, a mistr Heinrich procedí krátkou odpověď o vloupání do dílny. Brzy si tuto zprávu přihlížející začínají předávat sami. Někteří z nich jdou s vámi - zřejmě se nestává často, že by došlo k zatčení člena hlídky."
    scene bg guardhouse
    "Dovnitř na strážnici jsou však vpuštěni jen Heinrich a Aachim - a samozřejmě ty [sam]. I tam vzbudíte značný rozruch a brzy se do hloučku kolem vás sejdou nejspíš všichni, kdo zrovna se na strážnici nachází."
    "Jakmile vás spatří Solian, zpozorní, rychle vstane a kmitne pohledem mezi vámi dvěma."
    $ solian.say("Co se to děje? Snad [mcName] nic neprovedl[a]?", "surprised")
    $ victim.say("Ta vaše nová naděje se ke mně vloupala. Takhle se hlídka chová?", "furious")
    show mcPic at menuImage
    menu:
        "To je lež!":
            hide mcPic
        "Pomozte mi někdo!":
            hide mcPic
        "Nesahej na mě, bídáku!":
            hide mcPic
        "{i}(Mlčet){/i}":
            hide mcPic
    $ solian.say("Runo, hlídej dveře. Nikdo nesmí dovnitř ani ven.", "angry")
    $ solian.say("Mistře Heinrichu, buďte bez obav, to určitě vyšetříme.")
    $ victim.say("Přivedl jsem vám [pronoun4] až sem. Doufám, že odtud neodejde jinak než v řetězech.", "furious")
    $ solian.say("To je dobře možné. Co tedy přesně provedl[a]?")
    $ victim.say("Vloupal[a] se do mojí dílny, ukradl[a] tam dopisy, které moje dcera dostala od toho elfského kašpara, a pak mi to ještě drze přizná do očí!", "furious")
    $ victim.say("Jestli ta špína okamžitě neskončí aspoň na pranýři, postarám se, aby se všichni dozvěděli, co si to naše nová hlídka dovoluje. A schválně, jak se jim to bude líbit.", "furious")
    $ solian.say("To nebude nutné. Můžu vás ujistit, že hlídka se do ničích domů nevloupává, a pokud to nějaký hlídkař kdy udělal, čeká ho náležitý trest.", "angry")
    $ runa.say("[callingMc].capitalize(), co k tomu můžeš říct ty?")
    show mcPic at menuImage
    menu:
        "Je to lež, v dílně jsem nikdy nebyl[a] jinak než pod dozorem!":
            hide mcPic
            $ solian.say("To by mohl říct každý. Důkazy mluví proti tobě.", "angry")
        "Dal mi klíč, co čekal?":
            hide mcPic
            "Mistr Heinrich zrudne a pohne se směrem k tobě. Tušíš, že před další ranou pěstí tě zachránila jen přítomnost dalších členů hlídky."
            $ runa.say("Takže jsi tam vážně byl[a]? Doufala jsem, že ne.", "surprised")
        "Bylo to nutné pro vyšetřování.":
            hide mcPic
            $ runa.say("Takže jsi tam vážně byl[a]? Doufala jsem, že ne.", "surprised")
            $ solian.say("Prozkoumat dílnu jistě bylo na místě, ale pouze se svolením mistra Heinricha. Cokoli jiného je překročení našich pravomocí a navíc neodpustitelná drzost.")
        "Hayfa by na mém místě jednala stejně.":
            hide mcPic
            $ solian.say("To je možné, ale teď mluvíme o tvém případu a odváděním pozornosti na jiné členy hlídky si nijak nepomůžeš.", "angry")
    $ solian.say("[mcName].capitalize() teď umístíme do jedné z našich cel a zasadíme se, aby co nejdříve proběhl soud a náležitě [pronoun4] potrestal.")
    $ solian.say("Mistře Heinrichu, uděláme vše pro to, aby vyšetřování krádeže vašich bot tímto zatčením nijak neutrpělo. Osobně se o to zasadím.")
    "Solian k tobě dojde, uchopí tě za paži a začne tě směrovat směrem ke schodům do sklepa. Neochotně ho následuješ, v místnosti plné lidí by odpor neměl naději na úspěch."
    scene bg cell
    "Brzy tedy spatříš jednu z pověstných cel zevnitř a zaklapne za tebou mříž, kterou Solian pečlivě zamkne."
    play sound audio.prisonDoorClose
    $ solian.say("A takhle to dopadá, když Rauvin až moc poslouchá Hayfu. A kdo to teď bude muset vysvětlovat? Já.", "angry")
    $ solian.say("Doufám, že městská rada nebude zbytečně měkká. V případě obyčejného vloupání by mohlo zůstat u peněžitého trestu a potom vyhnání z města nebo něčeho podobného, ale na člena hlídky by u podobného zločinu měli být mnohem přísnější.", "angry")
    $ solian.say("Protože tohle jde přímo proti tomu, od čeho hlídka v tomhle městě je.", "angry")
    "Solian se otočí a rychlým krokem se vrátí nahoru ke své práci. Ty tak zůstaneš [sam] a můžeš nerušeně přemítat, jaký trest tě nejspíše čeká."
    jump thrownOut

###

label victimOptionsRemainingCheck:
    call zeranInnocentOptionsRemainingCheck
    call zairisGuiltyOptionsRemainingCheck

    $ victimOptionsRemaining = 0
    if "shoes description" not in clues:
        $ victimOptionsRemaining += 1
    if "enemies" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "enemies" in rumelin.asked and "fired apprentices" not in victim.asked and gender == "M":
        $ victimOptionsRemaining += 1
    if "enemies" in rumelin.asked and "fired apprentices" not in victim.asked and gender == "F":
        $ victimOptionsRemaining += 1
    if "fired apprentices" in victim.asked and "fired apprentices offense" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "fired apprentices" in victim.asked and "fired apprentices" not in clues:
        $ victimOptionsRemaining += 1
    if "best sale" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "fired apprentices offense" in victim.asked and "proof against Zeran" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "proof against Zeran" in victim.asked and "Zeran's letters" not in victim.asked:
        $ victimOptionsRemaining += 1
    if lotte.alreadyMet == True and "relationship" not in victim.asked:
        $ victimOptionsRemaining += 1
    if lotte.alreadyMet == True and "lisbeth friends" not in victim.asked:
        $ victimOptionsRemaining += 1
    if lotte.alreadyMet == True and "secret lover" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "confession" in rumelin.asked and "rumelin exposed" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "stolen idea" in clues and "stolen idea" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "burned evidence seen" in victim.asked and "calm Heinrich" in status and "burned evidence not as bad" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "own work" in njal.asked and "plan B" in clues and "join forces" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "join forces victim pending" in status and "join forces survey" in status:
        $ victimOptionsRemaining += 1
    if time.days > 1 and "plan B" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "join forces clueless" in njal.asked and "stolen idea" not in clues and "conflict with Njal" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "join forces victim approves" in status and "join forces" in njal.asked and "join forces go-ahead" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "join forces victim approves" in status and "join forces clueless" in njal.asked and "join forces" not in njal.asked and "join forces go-ahead clueless" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "stolen idea" in victim.asked and "should arrest eckhard" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "confession" in boysAsked and "lost bottles solved rumelin" not in victim.asked and "lost bottles solved boys" not in victim.asked not in victim.asked:
        $ victimOptionsRemaining += 1
    if "journeymen" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "journeymen" in victim.asked and "Eckhard relationship" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "Eckhard relationship" in victim.asked and "flattery" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "zeran innocent" not in victim.asked and "zeran cleared" not in status and zeranInnocentOptionsRemaining > 0:
        $ victimOptionsRemaining += 1
    if "zairis guilty" not in victim.asked and "zeran cleared" not in status and zairisGuiltyOptionsRemaining > 0:
        $ victimOptionsRemaining += 1
    if "Ada closed door" in status and "Ada closed door" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "zeran cleared" in status and "zeran cleared" not in victim.asked:
        $ victimOptionsRemaining += 1
    if "fireshow" in status and "fireshow" not in victim.asked:
        $ victimOptionsRemaining += 1
    return

label zeranInnocentOptionsRemainingCheck:
    $ zeranInnocentOptionsRemaining = 0
    call zairisGuiltyOptionsRemainingCheck
    if "zeran handwriting checked" in status and "zeran innocent handwriting" not in victim.asked:
        $ zeranInnocentOptionsRemaining += 1
    if "letters for Ada seen" in status and "Amadis grave" in zeran.asked and "zeran innocent amadis grave" not in victim.asked:
        $ zeranInnocentOptionsRemaining += 1
    if "letters for Ada seen" in status and "expensive paper" not in victim.asked:
        $ zeranInnocentOptionsRemaining += 1
    if "zairis guilty" not in victim.asked and "zeran cleared" not in status and zairisGuiltyOptionsRemaining > 0:
        $ zeranInnocentOptionsRemaining += 1
    return

label zairisGuiltyOptionsRemainingCheck:
    $ zairisGuiltyOptionsRemaining = 0
    if "Zairis handwriting checked" in status and "zairis guilty handwriting" not in victim.asked:
        $ zairisGuiltyOptionsRemaining += 1
    if "letters for Ada seen" in status and "Amadis grave" in zairis.asked and "zairis guilty amadis grave" not in victim.asked:
        $ zairisGuiltyOptionsRemaining += 1
    if "letters for Ada seen" in status and "poetry" in zairis.asked and "zairis guilty poetry" not in victim.asked:
        $ zairisGuiltyOptionsRemaining += 1
    if "letters for Ada seen" in status and "zairis guilty style" not in victim.asked:
        $ zairisGuiltyOptionsRemaining += 1
    if "Zairis handwriting checked" in status and "zairis guilty paper" not in victim.asked:
        $ zairisGuiltyOptionsRemaining += 1
    return
