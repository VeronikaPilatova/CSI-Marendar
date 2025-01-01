label adaMain:
    $ adaNote.isActive = True
    if lastSpokenWith == "":
        $ lisbeth.say("Nejsem si jistá, jestli bude zrovna ona něco vědět... ale jak chcete. Pojďte dál a já vám ji zavolám.")
        call victimHouseInterior
    else:
        $ lisbeth.say("Nejsem si jistá, jestli bude zrovna ona něco vědět... ale jak chcete. Dojdu pro ni.")

    $ lastSpokenWith = "ada"
    $ heinrichHouseholdSpokenWith.append("ada")
    $ origAsked = ada.asked.copy()
    call adaIntro
    if ada.status != "closed door":
        call adaOptions
    $ time.addMinutes((len(ada.asked) - len(origAsked)) * 3)
    jump victimHouseholdConversationEnded
    return

label adaIntro:
    if ada.status == "closed door":
        call adaIntroAngryAgain
    elif ada.status == "angry":
        call adaIntroAngry
    else:
        "Paní Lisbeth přivede asi čtrnáctiletou dívku se zvědavým výrazem."
        $ ada.say("S čím vám můžu pomoct?")
    return

label adaIntroAngry:
    "Paní Lisbeth přivede zamračenou Adu a nechá vám soukromí."
    "Jakmile je její matka mimo doslech a než se stihneš začít ptát, Ada na tebe vyštěkne vlastní otázku."
    if any("ada confrontation" in str for str in status):
        $ ada.say("Ty máš ještě tu drzost sem chodit? Já ti vážně byla ochotná věřit, že možná nejsi tak špatn[y]!", "angry")
        $ mc.say("A na tom se něco změnilo?")
        $ ada.say("No to si piš, že změnilo!")
    else:
        $ ada.say("Co si o sobě myslíš, jen tak si přijít do našeho domu po tom, co jsi udělal[a]?", "angry")
        label adaIntroAngryMenu:
        show mcPic at menuImage
        menu:
            "...prosím?" if "adaIntroAngryResponse1" not in ada.asked:
                $ ada.asked.append("adaIntroAngryResponse1")
                hide mcPic
                $ ada.say("Sedíš si na uších? Měl[a] bys táhnout a nechat nás všechny na pokoji.", "angry")
                jump adaIntroAngryMenu
            "Jak jinak může hlídka pomáhat?":
                hide mcPic
                if "letters from Ada" in victim.asked and "ada confrontation letters" not in status:
                    $ ada.say("Třeba tak, že nebude šířit lži. Ale to tě asi nenapadlo, co?", "angry")
                else:
                    $ ada.say("Třeba tak, že nebude strkat nos do věcí, do kterých jim nic není. Ale to tě asi nenapadlo, co?", "angry")
            "Co jsem podle tebe udělal[a]?":
                hide mcPic
            "Mluvíš o...":
                hide mcPic
    label adaAngryReasons:
    if "kaspar and lisbeth ratted out" in status and "ada confrontation lisbeth" not in status:
        $ ada.say("Viděl[a] jsi, jak teď vypadá máma?", "angry")
        $ ada.say("Každému kromě tebe a mého otce přece musí být jasné, že by nikdy neudělala nic špatného. Nic proti Olwenovi, proti tomu, co se považuje za slušné, nic proti chlapovi, kterého asi pořád ještě miluje!", "angry")
        $ status.append("ada confrontation lisbeth")
        $ status.append("ada confrontation ongoing")
        show mcPic at menuImage
        menu:
            "Nic takového jsem tvému otci neřekl[a].":
                hide mcPic
                $ ada.say("Nelži. Křičel tady na celý dům, vím velmi dobře, co přesně se dozvěděl a od koho.", "angry")
            "Omlouvám se, nedošlo mi, jak to vezme.":
                hide mcPic
                $ ada.say("A to sis nevšiml[a], jak vždycky vyletí, když se mu něco nelíbí?", "angry")
            "Kaspar byl v jeho dílně, to jsem přece říct musel[a].":
                hide mcPic
                if gender == "M":
                    $ ada.say("A už jsi ho zatknul? Jestli ne, tak to asi tak důležité nebylo.", "angry")
                else:
                    $ ada.say("A už jsi ho zatkla? Jestli ne, tak to asi tak důležité nebylo.", "angry")
            "Má přece právo vědět, s kým se jeho žena baví.":
                hide mcPic
                $ mc.say("Zvlášť, když to jako nevěra opravdu vypadá.")
                $ ada.trust -= 2
                $ ada.say("A ty zase vypadáš jako osel. Půjdeš mu to taky hned říct?", "angry")
    if "boys punished for drinking" in status and "ada confrontation boys drinking" not in status:
        if "ada confrontation ongoing" in status:
            $ ada.say("A co teď budou dělat Ferdi a Rudi?", "angry")
        else:
            $ ada.say("Co teď budou Rudi a Ferdi dělat?", "angry")
        $ status.append("ada confrontation boys drinking")
        if "ada confrontation ongoing" not in status:
            $ status.append("ada confrontation ongoing")
        $ ada.say("Táta je vyhodí, oni budou bez peněz, bez dokončeného vyučení, vždyť dopadnou jako Zeran! To jsi chtěl[a]?")
        show mcPic at menuImage
        menu:
            "To je přiměřené, kradli v domě svého mistra.":
                hide mcPic
                $ ada.say("Je přiměřené zničit jim život kvůli jedné hlouposti? No to mě podrž.", "angry")
                $ ada.say("A jestli myslíš, že jsi tím pomohl[a] tátovi, tak se pleteš. On sice na učedníky pořád nadává, ale zapřáhnout do práce je vždycky uměl. Teď to všechno bude muset dělat sám jen s chudákem Aachimem.", "angry")
            "Opravdu? Nečekal[a] jsem, že to dojde tak daleko...":
                hide mcPic
                $ ada.say("A až kvůli tobě někoho pověsí, také budeš takhle vyjeven[y]?", "angry")
            "Určitě mají někoho, kdo jim pomůže.":
                hide mcPic
                $ ada.say("To je dobře, že tě napadlo nad tím přemýšlet předtím, než jsi otevřel[a] pusu, že jo?")
    if "zairis dealt with" in status and "ada confrontation zairis" not in status:
        if "ada confrontation ongoing" in status:
            $ ada.say("A taky jsi mu řekl[a] o Zairisovi.", "angry")
        else:
            $ ada.say("Řekl[a] jsi tátovi o Zairisovi.", "angry")
            $ ada.say("Táta si to s ním šel hned vyřídit, prý vtrhl do jeho domu jako velká voda, potom se do toho vložil Rovien... to jsou všichni v hlídce tak pitomí? Nebo vám prostě jenom nezáleží, co se komu stane?", "angry")
        $ status.append("ada confrontation zairis")
        if "ada confrontation ongoing" not in status:
            $ status.append("ada confrontation ongoing")
        show mcPic at menuImage
        menu:
            "Omlouvám se, nedošlo mi, co tvůj otec udělá.":
                hide mcPic
                $ ada.say("To jsem si všimla. Zato ti došla soudnost, co?", "angry")
            "Je to tvůj otec, má právo vědět, s kým se stýkáš":
                hide mcPic
                $ ada.trust -= 2
                $ ada.say("Takže celá rodina má být neustále pod dohledem, to je to, co si myslíš?", "angry")
            "Chtěl[a] jsem očistit Zerana, aby mohl dokončit učení.":
                hide mcPic
                $ ada.say("A to nešlo nějak jinak?", "angry")
        $ ada.say("Teď ani jeden z nás nesmí na krok z domu a kdo ví, co s ním jeho rodiče ještě provedou.", "sad")
    $ ada.say("A jestli ti tohle jako důvod, proč jsem naštvaná, nestačí, tak se nemáme, o čem bavit.")
    $ ada.status = "closed door"
    if "ada confrontation ongoing" in status:
        $ status.remove("ada confrontation ongoing")
    show mcPic at menuImage
    menu:
        "Ve skutečnosti mi to opravdu nepřijde jako moc dobrý důvod.":
            hide mcPic
            $ ada.say("Potom už ode mě nečekej žádnou pomoc.", "angry")
            $ ada.status = "closed door"
            if gender == "M":
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotného, dokud se opět neobjeví její matka."
            else:
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotnou, dokud se opět neobjeví její matka."
            return
        "Chápu tě, ale stojím si za tím, co jsem udělal[a].":
            hide mcPic
            $ ada.say("A z toho mám padnout na zadek? Jak jsem říkala, nemáme, o čem se bavit.", "angry")
            if gender == "M":
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotného, dokud se opět neobjeví její matka."
            else:
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotnou, dokud se opět neobjeví její matka."
            return
        "Soustředíš se na podružnosti. Já hlavně vyšetřuji zločiny.":
            hide mcPic
            $ ada.say("Kéž by, to by se nám tu všem žilo lépe. Ale ty místo hledání té tátovy bačkory strkáš nos do našich osobních věcí, které s tím vůbec nesouvisí.", "angry")
            $ ada.say("Jak jsem říkala, nemáme, o čem se bavit.", "angry")
            if gender == "M":
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotného, dokud se opět neobjeví její matka."
            else:
                "S tím se Ada prudce otočí a nechá tě stát v místnosti samotnou, dokud se opět neobjeví její matka."
            return
        "Odsuzuješ mě moc rychle. Snažím se všude pomáhat, jak to jen jde.":
            hide mcPic
            if sum("ada confrontation" in s for s in status) > 1:
                $ ada.say("Tak mi o tom radši nic neříkej, nebo se naštvu ještě víc, při tom, jak to dopadá.", "angry")
                return
            else:
                $ ada.say("Vážně? To jsem zvědavá.")
    
    label adaAngryCounterargumentOptions:
    call adaAngryCounterargumentOptionsRemainingCheck
    if adaAngryCounterargumentOptionsRemaining == 0:
        $ ada.say("Dokud nepřijdeš na něco lepšího, pátrej si někde jinde, ale se mnou nepočítej.", "angry")
        return
    show mcPic at menuImage
    menu:
        "Pomohl[a] jsem přece Zeranovi získat nové učednické místo." if "Zeran continues apprenticeship" in status and "appeasing Ada - helped Zeran" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - helped Zeran")
            $ ada.say("To je pravda, to mu pomohlo hodně. Možná nejsi úplně ztracený případ.")
            $ ada.say("Ale stejně jsem naštvaná.", "angry")
            $ ada.status = ""
        "Zarazil[a] jsem cechmistrovi jeho podvod na Njalovi." if "rumelin exposed" in status and "appeasing Ada - rumelin exposed" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - rumelin exposed")
            $ ada.say("Mě ale cechovní politika vůbec nezajímá.", "angry")
        "Domluvil[a] jsem tvému otci spolupráci s Njalem." if "join forces victim approves" in status and "join forces njal approves" in status and "appeasing Ada - join forces" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - join forces")
            $ ada.say("To je určitě skvělý obchod, ale my nepotřebujeme víc peněz.")
        "Dal[a] jsem nějaké peníze žebračce Erle." if "given money" in erle.asked and "appeasing Ada - money for Erle" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - money for Erle")
            $ ada.trust -= 1
            $ ada.say("A tím mě chceš ohromit? Za pár měďáků darovaných žebračce si mě nekoupíš.", "angry")
        "Jsme dohodnutí s Aachimem, že spolu zajdeme za vaším otcem a zkusíme domluvit, aby nemusel pokračovat v učení, ve kterém je nešťastný." if "help promised" in aachim.asked and "appeasing Ada - aachim help promised" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - aachim help promised")
            $ ada.say("Vážně? To mě upřímně řečeno spíš děsí. Ale jestli mu to pomůže...")
            $ ada.say("Hlavně tohle by mohl říct každý. Jestli něčemu pomůžeš, tak se můžeme bavit. Do té doby tě nechci vidět.", "angry")
        "Pomohl[a] jsem přece Aachimovi domluvit s tvým otcem, aby nemusel pokračovat v učení, ve kterém je nešťastný." if "father son confrontation successful" in status and "appeasing Ada - aachim successful" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - aachim successful")
            $ ada.say("To je pravda... to mu hodně pomohlo.", "happy")
            $ ada.say("Chudák už dávno věděl, že dobrý švec z něj nebude.", "sad")
            $ ada.status = ""
        "Pokusil[a] jsem se pomoct vztahu tvých rodičů." if "think about relationship" in victim.asked and "appeasing Ada - parents relationship" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - parents relationship")
            if "flowers" in status and "kaspar and lisbeth ratted out" in status:
                $ ada.say("A potom jsi to zkazil víc, než Aachim svou první botu.", "angry")
                $ ada.say("Ale je pravda, že chvíli se otec dokonce i snažil a máma byla šťastná.", "sad")
                $ ada.status = ""
            elif "flowers" in status:
                $ ada.say("Je pravda, že se otec začal snažit. Takhle šťastnou jsem mámu už dlouho neviděla.", "happy")
                $ ada.status = ""
            elif "kaspar and lisbeth ratted out" in status:
                $ ada.say("Tak už nikdy nikomu nepomáhej, jestli to děláš takhle.", "angry")
            else:
                $ ada.say("Možná, ale bez úspěchu. To mě vážně neohromí.")
        "Pomáhal[a] jsem hasit požár." if "firefighter" in status and "appeasing Ada - firefighter" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - firefighter")
            $ ada.say("No ještě aby ne! Toho se účastnila celá ulice včetně mě, táty a kluků.", "surprised")
            $ ada.say("Pomáhat s hašením je přirozená a správná věc, ne něco, čím mě můžeš uchlácholit.", "angry")
            $ ada.say("Navíc to nebyl žádný velký oheň na to, kolik lidí tam přiběhlo. To tě ani nemohlo stát žádnou velkou námahu.", "angry")
        "Zařídil[a] jsem svědky ve prospěch té tanečnice s ohněm." if katrin.cluesAgainst > 0 and "appeasing Ada - Katrin" not in ada.asked:
            hide mcPic
            $ ada.asked.append("appeasing Ada - Katrin")
            $ ada.say("Opravdu? A co z toho máš?", "angry")
            $ mc.say("Nic. Ale jí to hodně pomůže.")
            $ ada.say("Jak je vůbec možné, že ji nikdo nevaroval? Zákaz otevřeného ohně na ulici je tady jedním z nejdůležitějších zákonů.", "angry")
            $ ada.say("Neměla by tohle hlídka všem příchozím říct? To tady ta holka má být odsouzená kvůli tomu, že někdo jiný neudělal svoji práci?", "angry")
            $ mc.say("To nevím. Rozhodně to nebyla ta část hlídky, ve které jsem já.")
            $ ada.say("No a ti svědci, co jsi sehnal[a]. Bude to stačit?")
            if katrin.cluesAgainst == 1:
                $ mc.say("Doufám. Zatím mám jednoho.")
                $ ada.say("No nevím, hlasů proti ní asi bude mnohem víc. Když si vzpomenu, co říkali ti lidé na ulici během hašení...", "sad")
                $ ada.say("Ale každá pomoc asi dobrá.")
            elif katrin.cluesAgainst == 2:
                $ mc.say("Doufám. Zatím mám dva.")
                $ ada.say("No… snad. Jestli to jsou osoby s dost silným hlasem, mohlo by ji jejich svědectví aspoň uchránit nejhoršího.")
            else:
                if katrin.cluesAgainst == 3:
                    $ mc.say("Doufám. Zatím mám tři.")
                elif katrin.cluesAgainst == 4:
                    $ mc.say("Doufám. Zatím mám čtyři.")
                elif katrin.cluesAgainst == 5:
                    $ mc.say("Doufám. Zatím mám pět.")
                elif katrin.cluesAgainst == 6:
                    $ mc.say("Doufám. Zatím mám šest.")
                else:
                    $ mc.say("Doufám, ale už jich mám spoustu.")
                $ ada.say("Tolik? A všechno osoby se silným hlasem? Kde jsi jich tolik na[sel]?", "surprised")
                $ ada.say("Bez práce to nebylo. Jsem ve městě krátce, ale celé dny jen mluvím s různými lidmi. To mi pomohlo odhadnout, za kým zajít.")
                $ ada.say("No, dobrá práce. Tak doufejme, že to vyjde.", "happy")
            $ ada.say("Potřebuješ tedy ode mě něco?")
            $ ada.status = ""
        "Proto jsem v hlídce":
            hide mcPic
            $ ada.say("To by mohl říct každý. Tak hledej ty tátovy zatracené boty a nech naši rodinu na pokoji.", "angry")
        "Nic lepšího nemám." if any("appeasing Ada" in str for str in ada.asked):
            hide mcPic
            $ ada.say("To tedy žádná sláva.", "angry")
            $ ada.say("Dokud nepřijdeš na něco lepšího, pátrej si někde jinde, ale se mnou nepočítej.", "angry")
            return
        "To je teď asi jedno.":
            hide mcPic
            $ ada.say("Chápu. Tak jestli ti to je jedno, tak mě prosím nezdržuj.", "angry")
            return
    if ada.status == "closed door":
        jump adaAngryCounterargumentOptions
    else:
        $ ada.say("No dobře, třeba to s tebou není všechno ztracené. Ale než příště něco uděláš, přemýšlej prosím, co by to všechno mohlo způsobit.")
    return

label adaIntroAngryAgain:
    "Paní Lisbeth přivede zamračenou Adu a nechá vám soukromí."
    $ ada.say("Říkala jsem přece jasně, že se s tebou nebudu bavit.", "angry")
    
    $ ada.asked.append("closed door")

    call adaAngryCounterargumentOptionsRemainingCheck
    show mcPic at menuImage
    menu:
        "Myslím, že mi křivdíš. Snažím se všem pomáhat, jak to jen jde." if adaAngryCounterargumentOptionsRemaining != 0:
            hide mcPic
            $ ada.say("No to jsem zvědavá.", "angry")
            call adaAngryCounterargumentOptions
        "Jestli nezačneš spolupracovat, zajdu za tvým otcem." if "Ada closed door" not in victim.asked and "call father" not in ada.asked:
            hide mcPic
            $ ada.asked.append("call father")
            $ ada.trust -= 1
            $ ada.say("Klidně. Třeba tě taky zmlátí, když nic jiného neumí.", "angry")
        "{i}(Požádat mistra Heinricha, aby dceři domluvil){/i}" if "Ada closed door" not in victim.asked:
            hide mcPic
            $ ada.trust -= 2
            $ victim.trust -= 2
            "Netrvá dlouho a stojíš v jedné místnosti s Adou i jejím otcem. Mistr Heinrich si tě zamračeně měří."
            $ victim.say("Tak o co jde, že se to beze mě neobejde?", "angry")
            $ mc.say("Potřebuji se Ady zeptat na pár otázek a ona se mnou odmítá mluvit.")
            $ ada.say("O botách nic nevím a to jsem dávno řekla. Odmítám odpovídat na otázky o naší rodině.", "angry")
            $ victim.say("Proč se vyptáváš na moji rodinu? Nemáš snad pátrat po mém mistrovském výrobku? Co má tohle znamenat?", "angry")
            $ mc.say("Mohlo by to osvětlit některé okolnosti té krádeže.")
            $ victim.say("Tak aby bylo jasno, my jsme slušná domácnost a nikdo tady nekrade, a jestli ten bídák Zeran, Kaspar nebo někdo podobný něco spáchal, nikdo z nás o tom nic neví.", "angry")
            "S tím se mistr Heinrich otočí, pokyne Adě a spolu oba odejdou z místnosti."
        "Tak to se nemusíme navzájem zdržovat.":
            $ ada.say("To tě taky mohlo napadnout, než jsi pro mě mámu poslal[a].", "angry")
    return

label adaOptions:
    call adaOptionsRemainingCheck
    if adaOptionsRemaining == 0:
        $ mc.say("To je všechno, můžeš zase jít.")
        "Dívka pokrčí rameny a odejde."
        return

    show mcPic at menuImage
    menu:
        "Všimla sis včera večer něčeho nebo někoho podezřelého?" if "anything suspicious" not in ada.asked:
            hide mcPic
            $ ada.asked.append("anything suspicious")
            "Dívka zavrtí hlavou."
            $ ada.say("Ne, tady se nikdy nic neděje.")
            $ mc.say("Zkus se zamyslet, každý detail může být důležitý.")
            "Dívka se kousne do rtu, ale pak opět jen zavrtí hlavou."
        "Byl někdo po odchodu mistra Heinricha v jeho dílně?" if "workshop empty" not in ada.asked:
            hide mcPic
            $ ada.asked.append("workshop empty")
            "Dívka na moment zaváhá a pak zavrtí hlavou."
            $ ada.say("Ne. Totiž… nedívala jsem se tam, ale myslím, že ne.")
            if liese.alreadyMet == True:
                $ mc.say("Ale prý se tam potom ještě dlouho svítilo.")
                $ ada.say("Možná… tam kluci ještě uklízeli?")
                $ ada.say("Táta je náročný, tak jim to občas trvá.")
        "Pije tvůj otec často ještě po příchodu domů?" if "anything suspicious" in lisbeth.asked and "drunkard" not in ada.asked:
            hide mcPic
            $ ada.asked.append("drunkard")
            $ ada.say("Občas, většinou i s přáteli, když je z hospody vyhodí a oni ještě nemají dost. Většinou po nich potom musím ráno uklízet.")
            $ mc.say("Včera také? Tvá matka říkala něco o ztracených lahvích.")
            $ ada.say("Dnes ráno jsem si žádných lahví nevšimla. A táta po sobě neuklízí nikdy.")
            $ ada.say("Prý to je ženská práce.", "angry")
        "Tušíš, jaký vztah mají tví rodiče?" if lotte.alreadyMet == True and "parents relationship" not in ada.asked:
            hide mcPic
            $ ada.asked.append("parents relationship")
            $ ada.say("Táta si myslí, že když občas mámě koupí drahý šperk, spraví se tím to všechno ostatní.")
            $ ada.say("Vůbec nechápe, že žena občas potřebuje třeba báseň, nebo něco jiného od srdce.", "blushing")
        "To je ze zkušenosti?" if "parents relationship" in ada.asked and "experience" not in ada.asked:
            hide mcPic
            $ ada.asked.append("experience")
            "Dívka zaváhá a rozhlédne se kolem sebe, jestli jste opravdu sami."
            $ ada.say("Možná trochu…", "blushing")
        "A kdo je ten šťastlivec?" if "experience" in ada.asked and "boyfriend" not in ada.asked:
            hide mcPic
            $ ada.asked.append("boyfriend")
            $ ada.say("To vám tak budu říkat. Řeknete to tátovi a budou z toho problémy.")
        "Je možné, že by tvoje matka měla milence?" if lotte.alreadyMet == True and "secret lover" not in ada.asked:
            hide mcPic
            $ ada.asked.append("secret lover")
            "Dívka zavrtí hlavou."
            $ ada.say("Máma? To fakt ne. Ta je na podobné věci moc nudná. A až moc miluje pořádek.")
        "Je někdo, s kým si tvoje matka rozumí?" if lotte.alreadyMet == True and "lisbeth friends" not in ada.asked:
            hide mcPic
            $ ada.asked.append("lisbeth friends")
            if "Kaspar and Lisbeth" not in clues:
                $ clues.append("Kaspar and Lisbeth")
            $ ada.say("S většinou ženských z ulice a manželek lidí z cechu. Vyměňují si recepty a tak.")
            $ mc.say("A je někdo, s kým si je blíž než s ostatními? A třeba spolu mluví i o osobních věcech?")
            "Dívka se zamyslí."
            $ ada.say("Možná mistr Kaspar? Baví se spolu dost a půjčují si knížky. Zrovna včera jsem šla pro jednu, kterou máma chtěla vrátit.")
            $ ada.say("Olwenova cesta - sbírka mravoučných příběhů. Nuda na nudu, ale co čekat od mámy.")
            if "night meeting" in lisbeth.asked:
                $ mc.say("Já myslel[a], že tu vrátil mistr Kaspar sám, někdy včera pozdě večer.")
                "Ada zavrtí hlavou."
                $ ada.say("Ne, já ji mámě přinesla. Zkusila jsem i nakouknout dovnitř, ale bylo to opravdu tak hrozné, jak to zní.")
                $ ada.say("Kdo to říkal?")
                $ mc.say("Tvoje matka, prý se tady s ní mistr Kaspar stavil.")
                $ ada.say("Aha. Tak… se možná spletla? A on přinesl něco jiného?")
                $ ada.say("Názvy těhle věcí zní všechny stejně...")
                $ ada.say("Nebo jsem se spletla já? Už vlastně nevím.")
                $ lisbeth.cluesAgainst += 1
        "Jak dobře ses znala se Zeranem?" if "Zeran offense" in clues and "Zeran" not in ada.asked:
            hide mcPic
            $ ada.asked.append("Zeran")
            $ ada.say("Tak... normálně. Přes dva roky jsme spolu bydleli, jasně, že jsme se občas bavili. Vyprávěl mi elfí legendy a tak.")
            $ ada.say("Ale nic mezi námi nebylo.")
            $ clues.append("Zeran innocent")
            show mcPic at menuImage
            menu:
                "Prý vás spolu viděli a někdo ti posílal dopisy...":
                    hide mcPic
                    $ ada.trust -= 1
                    $ ada.say("Ale to nebyl...", "surprised")
                    "Dívka se zamračí a pokrčí rameny."
                    $ ada.say("Stejně mi tady nikdo nevěří.", "angry")
                "Já ti věřím.":
                    hide mcPic
                    $ ada.trust += 1
                    $ ada.say("Vážně? Tak to jste první.")
        "Takže ti ty dopisy posílal někdo jiný?" if "Zeran" in ada.asked and "love letters" not in ada.asked:
            hide mcPic
            $ ada.asked.append("love letters")
            "Dívka se zarazí těsně před tím, než stihne odpovědět."
            $ ada.say("Proč bych vám vlastně měla něco říkat? Stejně mi tady nikdo nevěří.", "angry")
            show mcPic at menuImage
            menu:
                "Protože by to mohlo pomoct Zeranovi.":
                    hide mcPic
                    $ ada.say("To jsem zkoušela. A nijak to nepomohlo, ať jsem říkala cokoliv. Táta si radši myslel, že to chci hodit na někoho jiného, než aby změnil názor.", "angry")
                "Protože na pravdě záleží.":
                    hide mcPic
                    "Ada pokrčí rameny s výrazem, který nevypadá ani trochu přesvědčeně."
                    $ ada.say("Možná vám, ale v tomhle domě nikomu. Když jsem zkusila říct pravdu tátovi, tak to všechno jenom zhoršilo.", "sad")
            $ mc.say("Jestli mi řekneš, kdo...")
            $ ada.say("Tak to řeknete tátovi a on jenom zase vypění. Znova to vážně zkoušet nebudu.", "angry")
        "Můžeš mi aspoň říct, o čem jste si psali?" if "love letters" in ada.asked and "letters topic" not in ada.asked:
            hide mcPic
            $ ada.asked.append("letters topic")
            "Ada se na chvíli zamyslí, ale pak pokrčí rameny."
            $ ada.say("To asi můžu, to táta stejně ví. Ale k ničemu vám to nebude.")
            $ ada.say("Psal mi básně, opravdu krásné. A vyprávěl o zajímavých místech, která navštívil. Jednou dokonce viděl Amadisův hrob, to jsem trochu záviděla.", "blushing")
            $ ada.say("Doma se o historii nikdo nezajímá a rytířským ideálům by se jenom vysmáli. I máma čte jenom nudné mravoučné hlouposti, pro tátu je hrdina jenom ten, kdo vyrobí lepší botu, a kluci nic neberou vážně.", "angry")
            $ ada.say("Nikdo z nich Amadisův život nemůže pochopit.")
        "Tvůj ctitel musí být hodně sečtělý" if "letters topic" in ada.asked and "lover well read" not in ada.asked:
            hide mcPic
            $ ada.asked.append("lover well read")
            $ libraryNote.isActive = True
            $ ada.say("To je, většinu básní v místní knihovně prý už zná nazpaměť a doufá, že paní Luisa pořídí nějaké nové. A doporučil mi spisy od Ignáce z Mardenu, prý dokud mě na podobnou cestu nevezme sám.", "blushing")
        "A proč se tvůj tajný ctitel nepřihlásil sám, když tolik obdivuje Amadise?" if "letters topic" in ada.asked and "lover conscience" not in ada.asked:
            hide mcPic
            $ ada.asked.append("lover conscience")
            $ ada.say("Říkal, že i Amadis musel čekat, než Gisellin otec konečně souhlasil s jejich svatbou. A přijít moc brzo by tátu opravdu jenom rozzuřilo.")
            $ mc.say("Ale Amadis by určitě nenechal za svoje rozhodnutí platit někoho jiného.")
            if ada.trust > 0 and "flowers achievement" in status:
                "Ada se zamračí."
                $ ada.say("To je pravda. A jemu by možná i táta věřil víc než mně...", "angry")
                $ ada.say("Asi se ho na to dojdu zeptat.", "angry")
                $ status.append("Ada confronts Zairis")
                $ zairis.imageParameter = beaten
            else:
                $ ada.say("Jediný, kdo tady o něčem rozhodoval, byl táta. A neposlouchal vůbec nikoho.", "angry")
        "Myslíš, že by Zeran ukradl střevíce tvého otce?" if "Zeran offense" in clues and "Zeran thief" not in ada.asked:
            hide mcPic
            $ ada.asked.append("Zeran thief")
            $ ada.say("To si nemyslím. Komu by to pomohlo?")
            $ mc.say("Mohl by se chtít pomstít tvému otci, za vyhazov a zkaženou pověst.")
            "Dívka se zamyslí."
            $ ada.say("Nevím. Možná, ale musel by se za ten měsíc hodně změnit.")
        "Prý si byl Zairis promluvit s tvým otcem." if "zairis confessed" in status:
            hide mcPic
            show mcPic at menuImage
            menu:
                "Doufám, že to Zeranovi umožní pokračovat v učení.":
                    hide mcPic
                    $ ada.say("To by si zasloužil. Když už mě teď táta drží v domácím vězení a nevypadá, že by chtěl rychle vychladnout jako vždycky, tak ať to aspoň Zeranovi pomůže. Ale podle mě ho táta zpátky nevezme.", "sad")
                    $ mc.say("Proč? Má teď přece důkaz, že v tom byl nevinně.")
                    $ ada.say("To by se potom musel každý den dívat na připomínku toho, že udělal chybu, a to on nesnese. On musí mít vždycky pravdu, bez ohledu na zbytek světa.", "angry")
                    $ ada.say("A i kdyby ho někdo přinutil, odnesl by to nejvíc zase Zeran.", "sad")
                    $ ada.say("Asi by mu ale mohl vrátit peníze za učení. Pak by Zeran mohl dokončit učení u nějakého jiného mistra. To by mu pomohlo dost.")
                    $ ada.say("“A pak odejde na tovaryšské putování a na jeho konci se nejspíš usadí někde daleko odtud.", "sad")
                "Doufám, že se mu nic nestalo.":
                    hide mcPic
                    $ ada.trust += 1
                    $ ada.say("Táta je hulvát a surovec a pokusil se ho zmlátit. Na ulici před domem, před všemi sousedy. Naštěstí ho zastavili dřív, než Zairisovi stihl opravdu ublížit, ale stejně.", "angry")
        "To je všechno, můžeš zase jít.":
            hide mcPic
            "Dívka pokrčí rameny a odejde."
            return
    jump adaOptions

###

label adaOptionsRemainingCheck:
    $ adaOptionsRemaining = 0
    if "anything suspicious" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "workshop empty" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "anything suspicious" in lisbeth.asked and "drunkard" not in ada.asked:
        $ adaOptionsRemaining += 1
    if lotte.alreadyMet == True and "parents relationship" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "parents relationship" in ada.asked and "experience" not in ada.asked:
        $ adaOptionsRemaining += 1
    if lotte.alreadyMet == True and "secret lover" not in ada.asked:
        $ adaOptionsRemaining += 1
    if lotte.alreadyMet == True and "lisbeth friends" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "Zeran offense" in clues and "Zeran" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "Zeran" in ada.asked and "love letters" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "Zeran offense" in clues and "Zeran thief" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "love letters" in ada.asked and "letters topic" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "letters topic" in ada.asked and "lover conscience" not in ada.asked:
        $ adaOptionsRemaining += 1
    if "zairis confessed" in status:
        $ adaOptionsRemaining += 1
    if "letters topic" in ada.asked and "lover well read" not in ada.asked:
        $ adaOptionsRemaining += 1
    return

label adaAngryCounterargumentOptionsRemainingCheck:
    $ adaAngryCounterargumentOptionsRemaining = 0
    if "Zeran continues apprenticeship" in status and "helped Zeran" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "rumelin exposed" in status and "rumelin exposed" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "join forces victim approves" in status and "join forces njal approves" in status and "join forces" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "help promised" in aachim.asked and "aachim help promised" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "father son confrontation successful" in status and "aachim successful" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "think about relationship" in victim.asked and "parents relationship" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    if "given money" in erle.asked and "money for Erle" not in ada.asked:
        $ adaAngryCounterargumentOptionsRemaining += 1
    return

label adaAngryCheck:
    if "zairis dealt with" in status and "ada confrontation zairis" not in status:
        $ ada.status = "angry"
    if "kaspar and lisbeth ratted out" in status and "ada confrontation lisbeth" not in status:
        $ ada.status = "angry"
    return
