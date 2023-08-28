label rumelinController:
    # check if visit makes sense
    if "rumelin closed door" in status and ("rumelin owes favour" not in status or favourOptionsRemaining == 0):
        "Cechmistr Rumelin s tebou stále odmítá mluvit."
        return
    call rumelinOptionsRemainingCheck
    if optionsRemaining == 0:
        "Nenapadá tě, co dalšího se cechmistra Rumelina ještě ptát."
        return
    call preludeController

    # walk over
    if rumelin not in cells:
        if rumelin.alreadyMet == False:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        if time.hours < 18:
            $ currentLocation = "rumelin study"
        else:
            $ currentLocation = "rumelin home"
    $ origAsked = rumelin.asked.copy()

    # visit itself
    if rumelin in cells:
        call rumelinCellsIntro
    elif "rumelin exposed" in status or "rumelin threatened" in status:
        call rumelinClosedDoor
    elif rumelin.alreadyMet == False:
        call rumelinFirst
    else:
        call rumelinAgain
    call rumelinOptions
    call leavingRumelin

    # adjust time spent and status
    $ time.addMinutes((len(rumelin.asked) - len(origAsked)) * 3)
    if rumelin.alreadyMet == False:
        $ rumelin.alreadyMet = True
    if time.hours > 17 and "rumelin home visited" not in status:
        $ status.append("rumelin home visited")
        $ nireviaNote.isActive = True
        $ nirevia.alreadyMet = True
    return

label rumelinFirst:
    # before 6pm - Rumelin at work
    if time.hours < 18:
        scene bg guildmaster outside
        "Mistr Rumelin je jako představený cechu zaměstnaný člověk, ale když vysvětlíš, o co se jedná, podaří se ti domluvit s ním schůzku. Cech ševců a obuvníků sídlí v krásné budově na náměstí, spolu s cechy brašnářů, sedlářů a kožedělců."
        scene bg guildmaster inside
    # after 6pm - Rumelin at home
    else:
        scene bg rumelin outside
        "V tuto hodinu už mistr Rumelin v budově cechu není, ale zkusíš ho navštívit doma."
        "Najdeš krásný dům v elfí čtvrti a zaklepeš na dveře. Otevře ti starší elfka a tázavě se na tebe podívá."
        $ mc.say("Dobrý den. Jsem %(mcName)s z městské hlídky a vyšetřuji krádež v dílně jednoho z ševcovských mistrů.")
        $ nirevia.say("Pak asi budete chtít mluvit s mým manželem. Touto dobou už ale nepracuje.")
        if gender == "M":
            $ mc.say("Mohl bych s ním mluvit i tak? Případ velice spěchá.")
        else:
            $ mc.say("Mohla bych s ním mluvit i tak? Případ velice spěchá.")
        $ nirevia.say("Co se ztratilo a komu?")
        $ mc.say("Mistru Heinrichovi někdo v noci ukradl jeho čerstvě dokončený mistrovský výrobek.")
        $ nirevia.say("Na Einionovy slavnosti? To by pro mistra Heinricha mohl být vážný problém.")
        if gender == "M":
            $ mc.say("Právě proto bych uvítal vaši pomoc při vyšetřování.")
            "Elfka se na moment zamračí, ale pak kývne a pokyne ti, abys šel dál."
        else:
            $ mc.say("Právě proto bych uvítala vaši pomoc při vyšetřování.")
            "Elfka se na moment zamračí, ale pak kývne a pokyne ti, abys šla dál."
        scene bg rumelin inside
        $ nirevia.say("Dojdu pro manžela.")
        if gender == "M":
            "Paní Nirevia ti pokyne, aby ses zatím posadil. Cechmistr Rumelin dorazí za okamžik s těžko čitelným výrazem."
        else:
            "Paní Nirevia ti pokyne, aby ses zatím posadila. Cechmistr Rumelin dorazí za okamžik s těžko čitelným výrazem."
        $ mc.say("Omlouvám se, že vás ruším takhle pozdě...")
    # common introduction
    $ rumelin.say("Hlídka má samozřejmě mou plnou podporu v pátrání. Pokud se ukradená věc nenajde do slavností, mohlo by to poškodit pověst celého cechu a to ani nemluvím o urážce Einiona samotného…")
    $ mc.say("Děkuji vám za ochotu.")
    return

label rumelinAgain:
    if time.hours < 18:
        scene bg guildmaster inside
        "Cechmistr Rumelin se s tebou setká znovu, ale nijak se nesnaží skrývat množství své práce."
    else:
        scene bg rumelin inside
        "Cechmistr Rumelin se s tebou setká znovu, ale nijak se nesnaží skrývat, že měl v tuto hodinu výrazně jiné plány."
    $ rumelin.say("Můžu ještě nějak pomoci rychlému uzavření vašeho případu?")
    return

label rumelinClosedDoor:
    # closed door at work - able to use favour when owed
    if time.hours < 18:
        scene bg  inside
        "Cechmistr Rumelin při pohledu na tebe nijak nezmění výraz, ale za jeho chladnou zdvořilostí můžeš jasně číst nepřátelství."
        if "rumelin exposed" in status:
            $ rumelin.say("Nečekal jsem, že se tu ještě ukážete.")
            "Nikdo nezmíní slova odvaha ani drzost, ale není to potřeba."
        else:
            $ rumelin.say("Myslel jsem, že minule jsme vše vyřešili k vzájemné spokojenosti.")
        call rumelinFavourRemainingCheck
        if "rumelin owes favour" in status and favourOptionsRemaining != 0:
            show mcPic at menuImage
            menu:
                "Jdu si vybrat slíbenou laskavost.":
                    hide mcPic
                    if gender == "M":
                        $ rumelin.say("A co byste si přál?")
                    else:
                        $ rumelin.say("A co byste si přála?")
                    call rumelinFavourOptions
                    $ rumelin.say("Předpokládám, že to je vše? Jistě chápete, že mám ještě mnoho práce.")
                "Mám ještě pár otázek k případu..." if "rumelin closed door" not in status:
                    hide mcPic
                    $ rumelin.say("Pak je budete muset položit někomu jinému. Jistě pochopíte, že jsem velmi zaměstnaný a nemůžu záležitosti svého cechu jen tak odložit.")
                    "Cechmistr Rumelin s nekompromisním výrazem ukáže na dveře."
                "Rozumím a nebudu vás rušit." if "rumelin closed door" in status:
                    hide mcPic
                    $ rumelin.say("To bude nejlepší.")
                    "Cechmistr Rumelin s nekompromisním výrazem ukáže na dveře."
        else:
            $ mc.say("Mám ještě pár otázek k případu...")
            $ rumelin.say("Pak je budete muset položit někomu jinému. Jistě pochopíte, že jsem velmi zaměstnaný a nemůžu záležitosti svého cechu jen tak odložit.")
            "Cechmistr Rumelin s nekompromisním výrazem ukáže na dveře."
        $ status.append("rumelin closed door")
    # closed door at home - no confrontation, no favours
    else:
        call rumelinHouseClosedDoor
    $ leaveOption = "none"
    return

label rumelinCellsIntro:
    "Mistr Rumelin působí, jako by vůbec neviděl mříže své cely. Dívá se přímo před sebe a jeho výraz je naprosto klidný. Tebe ale při příchodu probodne pohledem."
    if gender == "M":
        $ rumelin.say("Přišel jsi stáhnout to směšné obvinění?", "angry")
    else:
        $ rumelin.say("Přišla jsi stáhnout to směšné obvinění?", "angry")
    show mcPic at menuImage
    menu:
        "Ano, došlo mi, že to byla chyba.":
            hide mcPic
            $ rumelin.say("Samozřejmě. Věřím, že tví velitelé ti konečně vysvětlili funkci hlídky tady ve městě.")
            $ rumelin.say("Hlídka je tu od udržování pořádku. Slouží městu a nechává cechy, ať se řídí samy. Velitel Galar tomu rozumí velice dobře.")
            scene bg cells entrance
            "Odemkneš celu a odvedeš Rumelina ke vchodu strážnice. Ten se na tebe celou cestu ani nepodívá."
            $ cells.remove(rumelin)
            jump backToEvidenceWall
        "Ne, jdu se vás jen na několik věcí zeptat.":
            hide mcPic
            $ rumelin.say("To je nemilé. Možná budu ochotný odpovědět ve své pracovně, ale rozhodně ne tady.")
            jump backToEvidenceWall
    return

label rumelinOptions:
    if leaveOption == "none":
        return
    call rumelinOptionsRemainingCheck
    if optionsRemaining == 0:
        if gender == "M":
            $ mc.say("To je všechno, na co jsem se chtěl zeptat. Děkuji vám za spolupráci.")
        else:
            $ mc.say("To je všechno, na co jsem se chtěla zeptat. Děkuji vám za spolupráci.")
        return

    show mcPic at menuImage
    menu:
        "Je pravda, že jste se s mistrem Heinrichem včera pohádal v hospodě U Salmy?" if "pub fight" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("pub fight")
            $ rumelin.say("To je pravda.")
            $ rumelin.say("Když jsem k Salmě přišel já, Heinrich už byl dávno v náladě a vykřikoval na celou hospodu, že jeho dílo bude ozdoba celých slavností a budeme ho ještě všichni prosit, aby se stal cechmistrem.")
            $ rumelin.say("Snažil jsem se ho ignorovat, ale po pár sklenkách mi to nedalo a ohradil jsem se.")
            $ mc.say("O čem jste se hádali?")
            $ rumelin.say("O povinnostech cechmistra, především. Heinrich si myslí, že cechmistrem by měl být nejlepší řemeslník. Pořád nemůže pochopit, že to je politická role, která zahrnuje vyjednávání s městskou radou a rozhodování sporů uvnitř cechu. Musí se hledat řešení a dělat kompromisy.")
            $ rumelin.say("On je mistr svého oboru a to mu nikdo neupírá, ale nedokáže vyjít ani s vlastními lidmi. Nepracuje pro něj jediný tovaryš, protože Heinrich vyžaduje naprostou poslušnost. Jak by pod někým takovým mohl cech prosperovat?")
            $ clues.append("pub fight topic")
            show mcPic at menuImage
            menu:
                "Možná by aspoň někoho inspiroval svým příkladem?":
                    hide mcPic
                    $ rumelin.trust -= 1
                    $ rumelin.say("Možná. A možná by ještě víc lidí odradil nebo přiměl město opustit. Osobně doufám, že se to nebudeme muset dozvědět.")
                "Divím se, že někdo takový má vůbec o vedení cechu zájem.":
                    hide mcPic
                    $ rumelin.trust -= 1
                    $ rumelin.say("Já také, ale zřejmě vidí jen prestiž té pozice a ne práci s ní spojenou.")
        "Napadá vás někdo, s kým má mistr Heinrich spory?" if "enemies" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("enemies")
            $ rumelin.say("Myslím, že nejhorší vztahy má Heinrich uvnitř své vlastní dílny. Není schopný vyjít s žádným tovaryšem a učedníky vyhodil už tři. Jeden z nich dokonce musel jít až do Sehnau.")
        "Podle mistra Heinricha má největší spory s vámi." if "enemies" in rumelin.asked and "main suspect" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("main suspect")
            $ rumelin.trust -= 1
            $ rumelin.say("Dnes možná, zítra to bude možná někdo jiný. Co se mě týče, uznávám ho jako mistra oboru a rozhodně bych mu neukradl dílo, jakkoli se mi nelíbí jeho přístup k lidem.")
        "Víte, kde bych našel ty zbývající učedníky?" if "enemies" in rumelin.asked and "fired apprentices" not in clues and gender == "M":
            call firedApprentices
        "Víte, kde bych našla ty zbývající učedníky?" if "enemies" in rumelin.asked and "fired apprentices" not in clues and gender == "F":
            call firedApprentices
        "S kým má mistr Heinrich spory mimo svou dílnu?" if "enemies" in rumelin.asked and "enemies2" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("enemies2")
            $ rumelin.say("Mimo jeho dílnu bude snazší najít lidi, se kterými Heinrich spory nemá. Rozhádal se s polovinou cechu a s většinou obchodníků, od kterých bere materiál.")
            $ rumelin.say("Ale dohody dodržuje a nemyslím si, že by mu kdokoli z nich chtěl skutečně ublížit.")
        "Je někdo, s kým má mistr Heinrich spory dlouhodobě, nebo silnější než s někým jiným?" if "enemies2" in rumelin.asked and "enemies3" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("enemies3")
            $ rumelin.say("Nevím o tom. On spory snadno rozdmýchá, ale také zase snadno zapomene.")
        "Kde jste byl včera v noci?" if "alibi" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("alibi")
            $ rumelin.say("Od Salmy jsem šel rovnou domů a spát.")
            call alibiReaction from _call_alibiReaction
        "Změnil jste v poslední době nějak způsob obchodování nebo místo uzavírání smluv na materiál?" if "less deals" in salma.asked and "less deals" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("less deals")
            $ rumelin.trust -= 1
            $ rumelin.cluesAgainst += 1
            if rumelin.trust < -4:
                call rumelinTooManyQuestions
                return
            else:
                $ rumelin.say("Proč bych něco takového dělal?")
                if "less deals checked" in status:
                    $ mc.say("Poslední dva týdny vás nikdo neviděl uzavírat smlouvu na nákup materiálu v žádné hospodě ve městě.")
                    $ rumelin.say("Musel bych se podívat do svého účetnictví, ale je možné, že mi zrovna žádný nechyběl. Nebo si možná hostinští nepamatují každou smlouvu.")
                else:
                    $ mc.say("Hostinská Salma se zmínila, že vás už dlouho neviděla uzavírat vaše obvyklé smlouvy na nákup materiálu.")
                    $ rumelin.say("Musel bych se podívat do svého účetnictví, ale je možné, že mi zrovna žádný nechyběl. Nebo si možná Salma nepamatuje každou smlouvu.")
                $ mc.say("Neměl by si právě svědek smlouvu pamatovat?")
                $ rumelin.say("To bohužel nemám možnost ovlivnit. Je to všechno?")
                if rumelin.cluesAgainst == 4:
                    call rumelinConfession
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("join forces")
            $ status.append("join forces survey")
            $ rumelin.say("Proč by to dělali? Slavnosti jsou přece od toho, aby na nich každý předvedl své schopnosti.")
            $ rumelin.say("Nedokážu si představit, proč by to měli chtít udělat, pokud by to neměla být snaha ušetřit si práci. Za to by těžko někdo sklidil potlesk.")
            $ rumelin.say("Jiné by to bylo, kdyby měli společnou dílnu nebo kdyby její založení chtěli ohlásit. To by ale museli pracovat společně na všem a k tomu se tu, pokud vím, nikdo nechystá.")
        "Je pravda, že mistr Njal má v poslední době problémy s nákupem materiálu?" if "less deals" in salma.asked and "njal problems" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("njal problems")
            $ rumelin.say("Nejsem si jistý, je možné, že se s někým nepohodl. Za mnou kvůli tomu nepřišel. Myslel jsem, že se zabýváte Heinrichovým ztracený výrobkem, ne náhodnými spory.")
        "Mluvil jsem s Karstenovou ženou ohledně obchodů s mistrem Njalem." if "AML" in lotte.asked and "Lotte info" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("Lotte info")
            $ rumelin.trust -= 1
            $ rumelin.cluesAgainst += 1
            if rumelin.trust < -4:
                call rumelinTooManyQuestions
                return
            else:
                $ mc.say("Podle ní Karsten jednal podle vašich instrukcí.")
                $ rumelin.say("A jaké instrukce tom podle ní měly být?")
                $ mc.say("Neprodávat konkrétní materiál mistru Njalovi, bez rozumného důvodu. Tak se pochopitelně zajímám, co jste tím sledoval.")
                $ rumelin.say("Mě by zase zajímalo, co podobným očerňováním sleduje paní Lotte. Může se snažit rozeštvat náš cech, ale přineslo by jí to něco?")
        "Takže když se zeptám dalších obchodníků, řeknou mi něco jiného než paní Lotte?" if "Lotte info" in rumelin.asked and "confession" not in rumelin.asked and "other merchants" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("other merchants")
            $ rumelin.trust -= 1
            if rumelin.trust < -4:
                call rumelinTooManyQuestions
                return
            else:
                $ rumelin.say("Netroufám si odhadovat, co kdo z nich odpoví, ale doufám, že nebudou cítit důvod k pomluvám. Nejsem si jistý, jestli by to nebylo plýtvání vaším časem, který je jistě drahý.")
        "Jak přesně měly fungovat vaše společné nákupy pro cech? Je možné, že by tím Karsten přišel o část zisku?" if "Lotte info" in rumelin.asked and "bulk orders" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("bulk orders")
            $ rumelin.say("Samozřejmě, to byla hlavní myšlenka za společnými nákupy. Ušetřit jednotlivým mistrům peníze.")
            $ rumelin.say("Předpokládám, že tím se to celé vysvětluje?")
            show mcPic at menuImage
            menu:
                "To dává smysl, děkuji.":
                    hide mcPic
                "Můžu si jen ujasnit pár detailů?":
                    hide mcPic
                    $ mc.say("Jak se pak měl materiál dostat k mistru Njalovi?")
                    $ rumelin.trust -= 1
                    $ rumelin.cluesAgainst += 1
                    if rumelin.trust < -4:
                        call rumelinTooManyQuestions
                        return
                    else:
                        $ rumelin.say("Měl zajít za mnou. Pokud mu to Karsten zapomněl vyřídit, není to přece má vina.")
                        if rumelin.cluesAgainst == 4:
                            call rumelinConfession
        "Za tohle by vás mohli zatknout." if "confession" in rumelin.asked and "threaten" not in rumelin.asked:
            hide mcPic
            $ rumelin.asked.append("threaten")
            call rumelinThreatened
            return

        "To je všechno, na co jsem se chtěl zeptat. Děkuji vám za spolupráci." if gender == "M":
            hide mcPic
            return
        "To je všechno, na co jsem se chtěla zeptat. Děkuji vám za spolupráci." if gender == "F":
            hide mcPic
            return

        "Zatýkám vás za podvod a snahu poškodit jiného mistra vašeho cechu." (badge="handcuffs") if "confession" in rumelin.asked and rumelin not in arrested:
            hide mcPic
            $ rumelin.say("To je nesmysl, neudělal jsem nic, za co nezákonného. Jděte si raději ještě promluvit se svými nadřízenými.", "angry")
            if "endgame" in status:
                $ mc.say("Mí nadřízení nejsou k dispozici, ale mám jejich plnou důvěru.")
            else:
                show mcPic at menuImage
                menu:
                    "Dobře, ale počítejte s tím, že se vrátím.":
                        hide mcPic
                        $ leaveOption = "angry"
                        return
                    "To není potřeba, půjdete se mnou.":
                        hide mcPic
            "Mistr Rumelin se velmi neochotně nechá odvést na strážnici."
            $ rumelin.arrestReason.append("AML")
            $ arrested.append(rumelin)
            $ status.append("arrest in progress")
            $ leaveOption = "none"
            return

    jump rumelinOptions

label leavingRumelin:
    if leaveOption == "normal":
        $ rumelin.say("Pokud zloděje nedopadnete a nevrátíte výrobek do slavností, může to poškodit pověst celého cechu. A to samozřejmě nechci dopustit.")
        if "can return" not in rumelin.asked:
            show mcPic at menuImage
            menu:
                "Můžu se vrátit, pokud budu mít další otázky?" if "can return" not in rumelin.asked:
                    hide mcPic
                    $ rumelin.asked.append("can return")
                    $ rumelin.say("Pokud to bude nutné pro vyšetřování, tak jistě. Ale velmi doufám, že celá věc bude uzavřená co nejrychleji.")
                    $ mc.say("Udělám, co bude v mých silách.")
                "Udělám, co bude v mých silách.":
                    hide mcPic
        else:
            $ mc.say("Udělám, co bude v mých silách.")
    elif leaveOption == "angry":
        if "case solved" not in status:
            $ rumelin.say("A teď prosím zkuste chvíli vyšetřovat to, co je tady opravdu důležité. Slavnosti se blíží a zloděje pořád neznáme.")
        else:
            $ rumelin.say("To je vše, že ano? Hlídka má určitě spoustu práce s udržováním pořádku i na jiných místech.")
        "Mistr Rumelin s nekompromisním výrazem ukáže na dveře a nereaguje na žádné další argumenty."
    $ leaveOption = "normal"
    return

###

label firedApprentices:
    hide mcPic
    $ rumelin.asked.append("fired apprentices")
    $ rumelin.say("Jednoho z nich si myslím vzal k sobě mistr Njal. Ten druhý se mám dojem chytil špatné společnosti, možná by se dal najít v někde dočasné čtvrti.")
    $ clues.append("fired apprentices")
    $ gerdNote.isActive = True
    $ zeranNote.isActive = True
    return

label alibiReaction:
    show mcPic at menuImage
    menu:
        "Může vám to někdo potvrdit?":
            hide mcPic
            $ rumelin.say("Doma byla má žena, můžete se jí zeptat. Z hospody mne doprovodil můj bratr Rovien.")
            $ rumelin.say("Chápu, proč se na to ptáte, ale co by mi osobně taková krádež přinesla? Většina cechu sdílí mé názory, jsem přesvědčený, že Heinricha stejně do vedení nezvolí. Jediné, k čemu celá tahle nešťastná záležitost může vést, je zhoršení postavení nás všech.")
            $ nireviaNote.isActive = True
            $ rovienNote.isActive = True
            $ rumelin.asked.append("alibi details")
        "Samozřejmě vás nikdo nepodezírá.":
            hide mcPic
            $ rumelin.trust += 1
            $ rumelin.say("Hlídka jen dělá svou práci. A já v této věci skutečně nemám co skrývat.")
    return

label rumelinTooManyQuestions:
    $ rumelin.say("Začínám mít pocit, že se vzdalujete od svých úkolů a navíc překračujete hranice dané svým postavením. Máte vyšetřovat zločiny, ne zpochybňovat obchodní rozhodnutí vážených měšťanů.", "angry")
    show mcPic at menuImage
    menu:
        "Omlouvám se.":
            hide mcPic
        "Mám povinnost vyšetřit jakékoliv podezření na možný zločin.":
            hide mcPic
            $ rumelin.say("A také je vaší povinností krotit svůj zápal a neplýtvat časem počestných lidí ani časem hlídky, kterou platíme ze svých daní.", "angry")
    if gender == "M":
        $ rumelin.say("Myslím, že je čas, abyste se vrátil ke svému skutečnému případu.", "angry")
    else:
        $ rumelin.say("Myslím, že je čas, abyste se vrátila ke svému skutečnému případu.", "angry")
    "Mistr Rumelin s nekompromisním výrazem ukáže na dveře a nereaguje na žádné další argumenty."
    $ leaveOption = "none"
    return

label rumelinConfession:
    $ mc.say("Takže si to shrňme.")
    $ mc.say("Salma si všimla, že jste přestal uzavírat obchody tak, jak jste byl zvyklý, aniž by k tomu byl známý důvod. Tvrdíte, že šlo o společné nákupy materiálu, ale k Njalovi se žádný materiál nedostal a ostatní mistři pořád nakupují sami za sebe.")
    $ mc.say("Karsten dostal přímo od vás instrukce, že s Njalem nemá obchodovat, ale nesměl říct žádné vysvětlení.")
    if "bulk orders" in zairis.asked:
        $ mc.say("Navíc váš synovec Zairis říká, že myšlenku společných nákupů jste sám už dávno zavrhl jako neuskutečnitelnou.")
    $ mc.say("Určitě pochopíte, že mě zajímá, co za tím stojí, a že pokud se to nedozvím od vás, budu se muset vyptávat mnohem více lidí. Je naše povinnost vyšetřit jakékoli podezření na snahu někoho poškodit.")
    $ rumelin.say("Snaha někoho poškodit? Njal chtěl poškodit celý cech. Ten tvrdohlavý trpaslík mi nenechal žádnou jinou možnost, jak zachovat tvář všem.", "angry")
    $ mc.say("Poslouchám.")
    $ rumelin.say("Njal chtěl… přijít na Einionovy slavnosti se stejným výrobkem, jako jiný mistr. Jen proto, aby toho druhého zesměšnil.")
    if "police business" in njal.asked:
        $ mc.say("Nepožadoval ještě předtím vrácení svého střihu, podle kterého mistr Heinrich své dílo vytvořil?")
        $ rumelin.say("To ale na celém problému nic nemění. Co jsem mohl dělat, když s Heinrichem se nedá rozumně mluvit?", "angry")
    else:
        $ mc.say("Proč by mistr Njal něco podobného dělal?")
        $ rumelin.say("Měl s Heinrichem nějaký spor o autorství střihu na střevíce, které Heinrich šil na slavnosti. Chtěl, abych to vyřešil, ale jak, když s Heinrichem se nedá rozumně mluvit?")
        $ rumelin.say("A místo toho, aby si to nechal vysvětlit, si Njal musel postavit hlavu také.", "angry")
    $ rumelin.say("Zpomalit Njala bylo nejmenší zlo.")
    $ rumelin.say("Už měl i rozpracovaný jiný výrobek, doufal jsem, že se prostě vrátí ke svému původnímu nápadu. Opravdu nechápu, proč to neudělal, pak by tu žádný problém nebyl.")
    $ rumelin.asked.append("confession")
    return

label rumelinThreatened:
    $ rumelin.say("To je směšné. Žádný soudce by mne neodsoudil kvůli něčemu takovému.")
    $ mc.say("Možná, ale chcete to riskovat? Už jen mluvit o tom vám může snadno zničit pověst, přinejmenším by se velmi rychle našel někdo jiný na pozici cechmistra.")
    $ rumelin.say("Co se snažíte naznačit?", "angry")
    show mcPic at menuImage
    menu:
        "Jakou hodnotu by pro vás mělo mé mlčení?":
            hide mcPic
            $ rumelin.trust -= 5
            $ status.append("rumelin threatened")
            $ rumelin.say("Vydírání. Mohlo mě napadnout, že se hlídka tak snadno nezmění.")
            $ rumelin.say("Chcete peníze?")
            show mcPic at menuImage
            menu:
                "Co jiného?":
                    hide mcPic
                    "Cechmistr Rumelin s kamenným výrazem popojde pár kroků ke stolu, vytáhne z jedné ze zásuvek menší váček a podá ti ho."
                    "Potěžkáš ho, prohrábneš se zlatými mincemi uvnitř a spokojeně kývneš."
                    $ rumelin.say("Věřím, že tohle bude bohatě stačit.")
                    $ status.append("Rumelin's money")
                "Radši si nechám dlužit laskavost.":
                    hide mcPic
                    "Cechmistr Rumelin povytáhne obočí, jinak ale nezmění výraz."
                    $ rumelin.say("Dobrá. Budu si vás pamatovat. Jen prosím mějte na paměti, že nemohu udělat nic, co by poškodilo cech.")
                    $ status.append("rumelin owes a favour")
            $ leaveOption = "angry"
        "Abyste si začal chystat obhajobu, protože to musím nahlásit svým nadřízeným.":
            hide mcPic
            if gender == "M":
                $ rumelin.say("Vřele děkuji za varování. Ve skutečnosti, já obhajobu potřebovat nebudu, ale vy byste si měl lépe načíst marendarské zákony.")
            else:
                $ rumelin.say("Vřele děkuji za varování. Ve skutečnosti, já obhajobu potřebovat nebudu, ale vy byste si měla lépe načíst marendarské zákony.")
            $ leaveOption = "angry"
        "Že chci být vaším přítelem, a tak se o tom ode mě nikdo nedozví.":
            hide mcPic
            $ rumelin.trust += 5
            $ mc.say("Vím, že jste muž na svém místě, a vy teď doufám věříte, že se na mě můžete spolehnout.")
            "Cechmistr Rumelin povytáhne obočí, jinak ale nezmění výraz."
            $ rumelin.say("Už je to nějakou dobu, co jsem měl naposledy přítele v hlídce, ale stále si pamatuji, že to může být velmi užitečné. Věřím, že si dokážeme vzájemně pomoci.")
            if "case solved" not in status:
                if gender == "M":
                    $ rumelin.say("Děkuji vám. Teď byste ale asi měl vrátit k vašemu původnímu případu. Je to dobrý způsob, jak nabrat zásluhy.")
                else:
                    $ rumelin.say("Děkuji vám. Teď byste ale asi měla vrátit k vašemu původnímu případu. Je to dobrý způsob, jak nabrat zásluhy.")
            else:
                if gender == "M":
                    $ rumelin.say("Děkuji vám. Teď byste se ale asi měl vrátit ke své další práci, abychom nevzbudili žádná podezření.")
                else:
                    $ rumelin.say("Děkuji vám. Teď byste se ale asi měla vrátit ke své další práci, abychom nevzbudili žádná podezření.")
            $ leaveOption = "none"
    return

label rumelinFavourOptions:
    show mcPic at menuImage
    menu:
        "Zařídit, aby mistr Heinrich vzal zpátky svého bývalého učedníka Zerana." if "why not finish apprenticeship" in zeran.asked:
            hide mcPic
            $ mc.say("Nebo mu aspoň vrátil peníze, které za učení zaplatil, aby ho mohl dokončit u jiného mistra.")
            "Cechmistr Rumelin překvapeně pozvedne obočí."
            $ rumelin.say("Zajímavá žádost. Můžu se pokusit, ale nebudu schopen nic slíbit. Můžu mistrům ve svém cechu dávat doporučení, ale ne někoho z něčemu donutit.")
            show mcPic at menuImage
            menu:
                "Stačí mi, když uděláte vše, co bude ve vašich silách.":
                    hide mcPic
                    $ rumelin.say("To vám slíbit můžu.")
                    $ status.remove("rumelin owes a favour")
                    $ status.append("rumelin spoke to Heinrich about Zeran")
                "Pokud to není jisté, pak si svou službičku raději nechám na později.":
                    hide mcPic
                    $ rumelin.say("Jak si přejete.")
        "Zařídit, aby někdo z vašeho cechu nechal Zerana dokončit učení." if "why not finish apprenticeship" in zeran.asked:
            hide mcPic
            $ rumelin.say("A Zeran je…?")
            $ mc.say("Bývalý učedník mistra Heinricha, vyhozený bez důkazů a neprávem. Heinrich mu ani nevrátil peníze, které Zeran za učení zaplatil.")
            "Cechmistr Rumelin překvapeně pozvedne obočí."
            $ rumelin.say("Pokud vám na něm tolik záleží… zjistím, co můžu udělat.")
            show mcPic at menuImage
            menu:
                "Zaslouží si, aby se za něj někdo postavil, a nikdo jiný to neudělá.":
                    hide mcPic
                "Nechat ho v dočasné čtvrti je škoda jeho schopností.":
                    hide mcPic
            $ rumelin.say("Dobrá. Nemůžu samozřejmě mistry ve svém cechu k ničemu nutit, jen jim dávat doporučení, ale věřím že zařídit to bude v mých silách.")
            $ status.remove("rumelin owes a favour")
            $ status.append("rumelin helping Zeran")
        "Vlastně si to ještě nechám projít hlavou.":
            hide mcPic
            "Rumelin bez zjevného zájmu pokrčí rameny."
            $ rumelin.say("Jak si přejete.")
    return

###

label rumelinFavourRemainingCheck:
    $ favourOptionsRemaining = 0
    if "why not finish apprenticeship" in zeran.asked:
        $ favourOptionsRemaining += 1
    return

label rumelinOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "pub fight" not in rumelin.asked:
        $ optionsRemaining += 1
    if "enemies" not in rumelin.asked:
        $ optionsRemaining += 1
    if "enemies" in rumelin.asked and "fired apprentices" not in clues:
        $ optionsRemaining += 1
    if "enemies" in rumelin.asked and "enemies2" not in rumelin.asked:
        $ optionsRemaining += 1
    if "enemies2" in rumelin.asked and "enemies3" not in rumelin.asked:
        $ optionsRemaining += 1
    if "enemies" in rumelin.asked and "main suspect" not in rumelin.asked:
        $ optionsRemaining += 1
    if "alibi" not in rumelin.asked:
        $ optionsRemaining += 1
    if "less deals" in salma.asked and "less deals" not in rumelin.asked:
        $ optionsRemaining += 1
    if "less deals" in salma.asked and "njal problems" not in rumelin.asked:
        $ optionsRemaining += 1
    if "AML" in lotte.asked and "Lotte info" not in rumelin.asked:
        $ optionsRemaining += 1
    if "Lotte info" in rumelin.asked and "bulk orders" not in rumelin.asked:
        $ optionsRemaining += 1
    if "Lotte info" in rumelin.asked and "confession" not in rumelin.asked and "other merchants" not in rumelin.asked:
        $ optionsRemaining += 1
    if "confession" in rumelin.asked and "threatened" not in rumelin.asked:
        $ optionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in rumelin.asked:
        $ optionsRemaining += 1
    if "confession" in rumelin.asked and rumelin not in arrested:
        $ optionsRemaining += 1
    return
