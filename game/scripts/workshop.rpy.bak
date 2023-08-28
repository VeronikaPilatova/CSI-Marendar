label workshopController:
    # check if visit makes sense
    call workshopOptionsRemainingCheck
    if optionsRemaining == 0:
        "" "Nenapadá tě, co dalšího v (mistrově) dílně ještě prohlížet."
        return
    # walk over
    if currentLocation != "victim house":
        $ time.addMinutes(15)
        $ currentLocation = "victim house"
    $ origAsked = workshopChecked.copy()

    # visit itself
    if "straight to workshop" in status:
        call straightToWorkshop
    elif time.days == 1 and time.hours < 14:
        call workshopNotCleaned
    elif "workshop visited" not in status:
        call workshopCleanedFirst
    else:
        call workshopAgain
    call workshopOptions
    call leavingWorkshop

    # adjust time and status
    $ time.addMinutes((len(workshopChecked) - len(origAsked)) * 5)
    if "straight to workshop" in status:
        $ status.remove("straight to workshop")
    if "workshop visited" not in status:
        $ status.append("workshop visited")
    if "victim house visited" not in status:
        $ status.append("victim house visited")
    return

label straightToWorkshop:
    scene bg exterior02

    if victim.trust < -2:
        "" "Cestou se (mistr) mračí a pod vousy mumlá nadávky na adresu (hlavy cechu), syna s učedníkem, městské hlídky a zbytku světa."
    else:
        "" "Cestou se (mistr) mračí a pod vousy mumlá nadávky na adresu (hlavy cechu), syna s učedníkem a zbytku světa."
    "" "Konečně dorazíte k výstavnímu domu, ke kterému přiléhá prostorná dílna. (Mistr) sáhne do kapsy, pak se zmateným výrazem zkusí ještě druhou."
    $ victim.say("Možná má klíč pořád u sebe (přítel)... On včera večer odemykal, možná mi klíč zapomněl vrátit. Teď asi můžeme přes dům, ale sakra práce, budu za ním muset zajít...")
    $ friendNote.isActive = True
    if "forgotten key" not in clues:
        $ clues.append("forgotten key")

    $ flag = True
    label frontOfWorkshopReaction:
    show mcPic at menuImage
    menu:
        "Proč jste si neodemkl sám?" if flag is True:
            hide mcPic
            $ victim.trust -= 1
            $ victim.say("Asi jsem měl plné ruce. Co je tohle za výslech?", "angry")
            $ flag = False
            jump whyNotUnlockHimself
        "Můžu vám od něj klíč vyzvednout, pokud by to pomohlo?":
            hide mcPic
            if victim.trust < -2:
                $ victim.say("Než to nechávat na hlídce, to si tam radši dojdu. Ty se starej o svou práci a můj ukradený výrobek.", "angry")
            else:
                $ victim.say("To by vlastně šlo. Stačí říct, že tě posílám já.", "happy")
                $ victim.trust += 1
                $ status.append("retrieving workshop key")
        "{i}(Jít dovnitř){/i}":
            hide mcPic
    $ flag = ""

label workshopNotCleaned:
    scene bg workshop
    if "straight to workshop" in status:
        "" "Váš příchod překvapí tři asi patnáctileté mladíky, kteří vypadají, jako by toho moc nenaspali. Mistr (jméno) je jedním pohybem ruky vyžene a sám se se založenýma rukama postaví ke stěně, aby na tebe mohl dohlížet."
        $ status.append("boys seen")
        $ sonNote.isActive = True
        $ apprentice1Note.isActive = True
        $ apprentice2Note.isActive = True
    else:
        "" "Mistr (jméno) tě pustí dovnitř a postaví se se založenýma rukama ke stěně, aby na tebe mohl dohlížet."
    "" "Dílna je plná bot všech druhů a velikostí v různém stavu dokončení, od sotva začatých po plně připravené k prodeji. Většina z nich je narovnaná v policích, které sahají až téměř ke stropu, jen menší hromádka v rohu stále čeká na roztřídění. Pod botami jsou připravená dřevěná kopyta různých tvarů a velikostí."
    "" "U jedné stěny stojí stolek se dvěma zásuvkami plný nejrůznějších nástrojů, vedle něj je trojnohé sedátko a o kus dál zvláštní stolice s dřevěnými čelistmi na jednom konci.\nV rohu místnosti je ohniště, které nejspíš někdo zapomněl vymést."
    return

label workshopCleanedFirst:
    scene bg workshop
    "" "Mistr (jméno) tě pustí dovnitř a postaví se se založenýma rukama ke stěně, aby na tebe mohl dohlížet."
    "" "Dílna je plná bot všech druhů a velikostí v různém stavu dokončení, od sotva začatých po plně připravené k prodeji. Až na jeden pár, nejspíš právě rozdělaný, jsou všechny narovnané v policích, které sahají až téměř ke stropu. Pod botami jsou připravená dřevěná kopyta různých tvarů a velikostí."
    "" "U jedné stěny stojí stolek se dvěma zásuvkami plný nejrůznějších nástrojů, vedle něj je trojnohé sedátko a o kus dál zvláštní stolice s dřevěnými čelistmi na jednom konci.\nV rohu místnosti je čistě vymetené ohniště."
    return

label workshopAgain:
    scene bg workshop
    "" "(Jméno) tě mírně neochotně pustí do dílny."
    "" "Ta vypadá uvnitř stejně, jako když jsi tu byl/a naposled. Spousta bot všech druhů a velikostí v policích a u jedné stěny stolek se zásuvkami plný nástrojů, z nichž tak polovina ti vůbec nic neříká."
    return

label workshopOptions:
    call workshopOptionsRemainingCheck
    if optionsRemaining == 0:
        if gender == "M":
            $ mc.say("Děkuji, to je všechno, co jsem chtěl vidět.")
        else:
            $ mc.say("Děkuji, to je všechno, co jsem chtěla vidět.")
        return

    menu:
        "{i}(Prozkoumat stůl){/i}" if "table" not in workshopChecked:
            $ workshopChecked.append("table")
            "" "Na stole leží nástroje všeho druhu, z nichž o některých nemáš ani tušení, jak se používají. Vedle je několik malých misek s voskem a smolou."
            "" "Jedna zásuvka je zamčená, druhou se ti ale podaří vysunout. Uvnitř jsou nějaké papíry, podle všeho nákresy bot, střihů a způsobů jejich šití. Zajímavější je fakt, že zámek na tomto šuplíku byl násilím vylomený."
            $ clues.append("break-in")
        "Co by mělo být v zásuvkách u toho stolu?" if "table" in workshopChecked and "missing stuff1" not in workshopChecked and "table contents" not in workshopChecked:
            $ workshopChecked.append("table contents")
            $ victim.say("Složitější nákresy a střihy. Moje vlastní, samozřejmě. Střevíce na Einionovu slavnost by tam ale rozhodně být neměly.")
        "Co by v těch zásuvkách vlastně mělo být?" if "missing stuff1" in workshopChecked and "table contents" not in workshopChecked:
            $ workshopChecked.append("table contents")
            $ victim.say("Složitější nákresy a střihy. Moje vlastní, samozřejmě. A všechny tam jsou.")
        "Můžete prosím zkontrolovat, jestli v téhle zásuvce něco chybí?" if "table" in workshopChecked and "missing stuff1" not in workshopChecked:
            $ workshopChecked.append("missing stuff1")
            "" "(Jméno) rychle přejde ke stolu, prohlédne si vylomený zámek a pak začne procházet jednotlivé papíry. Trvá to dlouho a jeho výraz je čím dál tím zamračenější."
            $ victim.say("Ne, nic tu nechybí.")
        "Jste si opravdu jistý, že se ze zásuvky nic neztratilo?" if "missing stuff1" in workshopChecked and "missing stuff2" not in workshopChecked:
            $ workshopChecked.append("missing stuff2")
            $ victim.say("To si sedíš na uších, nebo mě máš za pitomce?", "angry")
            $ mc.say("Násilím otevřená je jenom ta jedna a…")
            $ victim.say("Říkám, že nic nechybí, tak nic nechybí.", "angry")
            $ victim.trust -= 1

        "{i}(Zkontrolovat dveře do místnosti){/i}" if "doors" not in workshopChecked:
            $ workshopChecked.append("doors")
            "" "Jedny dveře z dílny vedou na ulici, druhé do mistrova domu. Ani na jedněch z nich nejsou jakékoli stopy násilného vniknutí."
            if "straight to workshop" in status:
                "" "Ty směrem na ulici se bez problému otevřou. Zřejmě byly celou dobu odemčené. (Jméno) předstírá, že si toho nevšiml."
                $ clues.append("workshop unlocked")
            if "workshop unlocked" not in clues:
                $ clues.append("no forced entry")
        "Mohla být dílna celou noc odemčená?" if "workshop unlocked" in clues and "no forced entry" not in workshopChecked:
            $ workshopChecked.append("no forced entry")
            "" "(Jméno) se zamračí ještě víc."
            $ victim.say("O tom nic nevím, ale jestli to tak bylo, rozhodně si to vyřídím s tím, kdo za to může.", "angry")

        "{i}(Prohlédnout si boty){/i}" if "shoes" not in workshopChecked:
            $ workshopChecked.append("shoes")
            "" "Jsou tu boty lehké a elegantní, bytelné do divočiny nebo s kožešinou uvnitř do prudkých mrazů, všechno aspoň co můžeš posoudit prvotřídní práce. Zdá se, že mistr (jméno) nemá žádný typ, kterému by se věnoval více než jiným."

        "{i}(Zkontrolovat materiál){/i}" if "material" not in workshopChecked:
            $ workshopChecked.append("material")
            "" "Je tu všechno od tvrdé kůže na podrážky po tu nejjemnější, ze které by se daly šít taneční boty na šlechtický ples. Nechybí ani dratev, nitě, vosk a různé druhy cvočků."

        "{i}(Prohlédnout si nástroje a vybavení dílny){/i}" if "tools" not in workshopChecked:
            $ workshopChecked.append("tools")
            "" "Na stole je vyrovnaná řada nejrůznějších kleští, šídel a nožů různých tvarů, stejně jako dalších věcí, jejich použití ti uniká. Než ale stihneš vzít cokoli z toho do ruky, (mistr) tě okřikne."
            $ victim.say("Na moje nástroje nesmí sahat ani můj vlastní syn, natož nějaký náhodný strážný!", "angry")

        "{i}(Prozkoumat popel v krbu){/i}" if time.days == 1 and time.hours < 14 and "fireplace" not in workshopChecked:
            $ workshopChecked.append("fireplace")
            "" "Jen pro jistotu prohrábneš popel v krbu. Po chvíli prosévání mezi prsty najdeš mezi ohořelými zbytky dřeva dva drobné kovové cvočky a v zadním rohu nepatrný útržek stuhy, která snad bývala zlatá."
            "" "(Okradený mistr) na tebe vrhne nechápavý pohled."
            $ clues.append("burned evidence")
        "Můžete mi popsat ztracené střevíce?" if "burned evidence" in clues and "shoes description" not in clues:
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
            $ clues.append("shoes description")
        "Mohl by tenhle kousek stuhy být od vašich střevíců?" if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in workshopChecked:
            $ workshopChecked.append("burned evidence seen")
            "" "(Jméno) si ohořelý útržek prohlédne a zamračí se."
            $ victim.say("To by mohlo… kde to bylo? A proč je to napůl spálené?", "angry")
            if gender == "M":
                $ mc.say("Našel jsem to v krbu…")
            else:
                $ mc.say("Našla jsem to v krbu…")
            $ victim.say("Chceš říct, že moje mistrovské dílo někdo nejen ukradl, ale ještě se pokusil zničit? A navíc v mém vlastním krbu v mé vlastní dílně?", "angry")
            $ victim.say("Až ho dostanu do ruky, tak ho vlastníma rukama přetrhnu jak hada!", "angry")
            $ victim.pressure += 2

        "Děkuji, to je všechno, co jsem chtěl vidět." if gender == "M":
            return
        "Děkuji, to je všechno, co jsem chtěla vidět." if gender == "F":
            return
    jump workshopOptions

label leavingWorkshop:
    $ victim.say("Tak kdy toho zloděje přivedeš před spravedlnost?")
    menu:
        "Jsem mu na stopě a co nevidět bude dopaden, spolehněte se.":
            $ victim.trust += 1
            return
        "Můžu se vrátit, pokud budu mít další otázky?" if "can return" not in workshopChecked:
            $ workshopChecked.append("can return")
            $ victim.say("Já doufám, že se vrátíš i s mými střevíci.")
            $ mc.say("Pokud by to bylo nutné pro vyšetřování…")
            $ victim.say("Pokud to bude nutné, tak to hlavně zkrať. Nemám na hlídku celý den.")
            return
        "Můžu si ještě promluvit s vašimi učedníky?" if apprentice1Note.isActive == True or apprentice2Note.isActive == True:
            $ victim.say("Když to musí být. Ale nezdržuj je dlouho od práce.")

            if "boys met" in status:
                "" "(Jméno) ti znovu přivede svého syna a učedníky."
            if "boys seen" in status:
                "" "(Jméno) přivede zpět chlapce, kteří v dílně před tvým příchodem uklízeli. Zblízka vypadají ještě unaveněji a jsou očividně nervózní."
            else:
                "" "(Jméno) přivede tři asi patnáctileté mladíky. Všichni vypadají, jako by toho moc nenaspali, a jsou očividně nervózní."

            menu:
                "Nebude to trvat dlouho.":
                    pass
                "Necháte nás prosím o samotě?":
                    $ status.append("privacy")
                    "" "Mistr se zamračí, ale pak beze slova odejde z dílny."
            call boys
    return

###

label whyNotUnlockHimself:
    show mcPic at menuImage
    menu:
        "Každý detail může být důležitý.":
            pass
        "Omlouvám se.":
            $ victim.trust += 0.5
    hide mcPic
    jump frontOfWorkshopReaction

label workshopOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "table" not in workshopChecked:
        $ optionsRemaining += 1
    if "table" in workshopChecked and "table contents" not in workshopChecked:
        $ optionsRemaining += 1
    if "table" in workshopChecked and "missing stuff1" not in workshopChecked:
        $ optionsRemaining += 1
    if "missing stuff1" in workshopChecked and "missing stuff2" not in workshopChecked:
        $ optionsRemaining += 1
    if "doors" not in workshopChecked:
        $ optionsRemaining += 1
    if "workshop unlocked" in clues and "no forced entry" not in workshopChecked:
        $ optionsRemaining += 1
    if "shoes" not in workshopChecked:
        $ optionsRemaining += 1
    if "material" not in workshopChecked:
        $ optionsRemaining += 1
    if "tools" not in workshopChecked:
        $ optionsRemaining += 1
    if time.days == 1 and time.hours < 14  and "fireplace" not in workshopChecked:
        if time.minutes < 45 or currentLocation == "victim house":
            $ optionsRemaining += 1
    if "burned evidence" in clues and "shoes description" not in clues:
        $ optionsRemaining += 1
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in workshopChecked:
        $ optionsRemaining += 1
    return
