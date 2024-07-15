label workshopController:
    # check if visit makes sense
    call workshopOptionsRemainingCheck from _call_workshopOptionsRemainingCheck_1
    if workshopOptionsRemaining == 0:
        "Nenapadá tě, co dalšího v dílně mistra Heinricha ještě prohlížet."
        return
    # walk over
    if currentLocation != "victim house" and currentLocation != "victim street":
        $ time.addMinutes(15)
        $ currentLocation = "workshop"
    $ origAsked = workshop.checked.copy()

    # visit itself
    if "straight to workshop" in status:
        call straightToWorkshop from _call_straightToWorkshop
    elif time.days == 1 and time.hours < 14:
        call workshopNotCleaned from _call_workshopNotCleaned
    elif "workshop visited" not in status:
        call workshopCleanedFirst from _call_workshopCleanedFirst
    else:
        call workshopAgain from _call_workshopAgain
    call workshopOptions from _call_workshopOptions
    call leavingWorkshop from _call_leavingWorkshop

    # adjust time and status
    $ time.addMinutes((len(workshop.checked) - len(origAsked)) * 5)
    if "straight to workshop" in status:
        $ status.remove("straight to workshop")
    if "workshop visited" not in status:
        $ status.append("workshop visited")
    if "victim house visited" not in status:
        $ status.append("victim house visited")
    if "no privacy" in status:
        $ status.remove("no privacy")

    if currentLocation == "victim house":
        call victimHouseInterior
        jump victimHouseholdConversationEnded
    else:
        call neighboursController
    return

label straightToWorkshop:
    scene bg heinrich outside

    if victim.trust < -2:
        "Cestou se Heinrich mračí a pod vousy mumlá nadávky na adresu cechmistra Rumelina, syna s učedníky, městské hlídky a zbytku světa."
    else:
        "Cestou se Heinrich mračí a pod vousy mumlá nadávky na adresu cechmistra Rumelina, syna s učedníky a zbytku světa."
    "Konečně dorazíte k výstavnímu domu, ke kterému přiléhá prostorná dílna. Mistr Heinrich sáhne do kapsy, pak se zmateným výrazem zkusí ještě druhou."
    $ victim.say("Možná má klíč pořád u sebe Eckhard... On včera večer odemykal, možná mi klíč zapomněl vrátit. Teď asi můžeme přes dům, ale sakra práce, budu za ním muset zajít...")
    $ eckhardNote.isActive = True
    if "Eckhard" not in clues:
        $ clues.append("Eckhard")
    if "forgotten key" not in clues:
        $ clues.append("forgotten key")

    $ flag = True
    label frontOfWorkshopReaction:
    show mcPic at menuImage
    menu:
        "Proč jste si neodemkl sám?" if flag is True:
            hide mcPic
            $ flag = False
            $ victim.trust -= 1
            $ victim.say("Asi jsem měl plné ruce. Co je tohle za výslech?", "angry")
            show mcPic at menuImage
            menu:
                "Každý detail může být důležitý.":
                    pass
                "Omlouvám se.":
                    $ victim.trust += 0.5
            hide mcPic
            jump frontOfWorkshopReaction
        "Můžu vám od něj klíč vyzvednout, pokud by to pomohlo?":
            hide mcPic
            if victim.trust < -2:
                $ victim.say("Než to nechávat na hlídce, to si tam radši dojdu. Ty se starej o svou práci a můj ukradený výrobek.", "angry")
            else:
                $ victim.say("To by vlastně šlo. Stačí říct, že tě posílám já.", "happy")
                $ mc.say("Zaběhnu tam hned, jak tady skončíme.")
                "Heinrich kývne a zavede tě do dílny."
                $ victim.trust += 1
                $ solian.trust += 1
                $ status.append("retrieving workshop key")
        "{i}(Vzít za kliku){/i}" if "door tried" not in workshop.checked:
            hide mcPic
            $ flag = False
            $ workshop.checked.append("door tried")
            $ clues.append("workshop unlocked")
            "Když mistr Heinrich od dveří poodstoupí, sáhneš po klice od dveří a zatlačíš. Stačí jen trocha síly a dveře se otevřou."
            $ victim.say("Jak to?", "surprised")
            $ victim.say("Chci říct, ehm… no to je jedno. Ale za tím Eckhardem stejně budu muset zajít.", "angry")
            $ victim.say("Tak pojďme, ať tu nestojíme celý den.")
            jump frontOfWorkshopReaction
        "{i}(Jít dovnitř){/i}":
            hide mcPic
    $ flag = ""

label workshopNotCleaned:
    scene bg workshop
    if "straight to workshop" in status:
        "Váš příchod překvapí tři asi patnáctileté mladíky, kteří vypadají, jako by toho moc nenaspali. Mistr Heinrich je jedním pohybem ruky vyžene a sám se se založenýma rukama postaví ke stěně, aby na tebe mohl dohlížet."
        $ status.append("boys seen")
        $ sonNote.isActive = True
        $ apprentice1Note.isActive = True
        $ apprentice2Note.isActive = True
    else:
        "Mistr Heinrich tě pustí dovnitř a postaví se se založenýma rukama ke stěně, aby na tebe mohl dohlížet."
    "Dílna je plná bot všech druhů a velikostí v různém stavu dokončení, od sotva začatých po plně připravené k prodeji. Většina z nich je narovnaná v policích, které sahají až téměř ke stropu, jen menší hromádka v rohu stále čeká na roztřídění. Pod botami jsou připravená dřevěná kopyta různých tvarů a velikostí."
    "U jedné stěny stojí stolek se dvěma zásuvkami plný nejrůznějších nástrojů, vedle něj je trojnohé sedátko a o kus dál zvláštní stolice s dřevěnými čelistmi na jednom konci.\nV rohu místnosti je ohniště, které nejspíš někdo zapomněl vymést."
    return

label workshopCleanedFirst:
    scene bg workshop
    "Mistr Heinrich tě pustí dovnitř a postaví se se založenýma rukama ke stěně, aby na tebe mohl dohlížet."
    "Dílna je plná bot všech druhů v různém stavu dokončení, od sotva začatých po plně připravené k prodeji. Až na jeden pár, nejspíš právě rozdělaný, jsou všechny narovnané v policích, které sahají až téměř ke stropu. Pod botami jsou připravená dřevěná kopyta různých tvarů a velikostí."
    "U jedné stěny stojí stolek se dvěma zásuvkami plný nejrůznějších nástrojů, vedle něj je trojnohé sedátko a o kus dál zvláštní stolice s dřevěnými čelistmi na jednom konci.\nV rohu místnosti je čistě vymetené ohniště."
    return

label workshopAgain:
    scene bg workshop
    "Mistr Heinrich tě mírně neochotně pustí do dílny."
    "Ta vypadá uvnitř stejně, jako když jsi tu byl[a] naposled. Spousta bot všech druhů a velikostí v policích a u jedné stěny stolek se zásuvkami plný nástrojů, z nichž tak polovina ti vůbec nic neříká."
    return

label workshopOptions:
    call workshopOptionsRemainingCheck
    if workshopOptionsRemaining == 0:
        $ mc.say("Děkuji, to je všechno, co jsem chtěl[a] vidět.")
        return
    call boysOptionsRemainingCheck

    menu:
        "{i}(Prozkoumat stůl){/i}" if "table" not in workshop.checked:
            $ workshop.checked.append("table")
            "Na stole leží nástroje všeho druhu, z nichž o některých nemáš ani tušení, jak se používají. Vedle je několik malých misek s voskem a smolou."
            "Jedna zásuvka je zamčená, druhou se ti ale podaří vysunout. Uvnitř jsou nějaké papíry, podle všeho nákresy bot, střihů a způsobů jejich šití. Zajímavější je fakt, že zámek na tomto šuplíku byl násilím vylomený."
            $ clues.append("break-in")
        "Co by mělo být v zásuvkách u toho stolu?" if "table" in workshop.checked and "missing stuff1" not in workshop.checked and "table contents" not in workshop.checked:
            $ workshop.checked.append("table contents")
            $ victim.say("Složitější nákresy a střihy. Moje vlastní, samozřejmě. Střevíce na Einionovu slavnost by tam ale rozhodně být neměly.")
        "Co by v těch zásuvkách vlastně mělo být?" if "missing stuff1" in workshop.checked and "table contents" not in workshop.checked:
            $ workshop.checked.append("table contents")
            $ victim.say("Složitější nákresy a střihy. Moje vlastní, samozřejmě. A všechny tam jsou.")
        "Můžete prosím zkontrolovat, jestli v téhle zásuvce něco chybí?" if "table" in workshop.checked and "missing stuff1" not in workshop.checked:
            $ workshop.checked.append("missing stuff1")
            "Mistr Heinrich rychle přejde ke stolu, prohlédne si vylomený zámek a pak začne procházet jednotlivé papíry. Trvá to dlouho a jeho výraz je čím dál tím zamračenější."
            $ victim.say("Ne, nic tu nechybí.")
        "Jste si opravdu jistý, že se ze zásuvky nic neztratilo?" if "missing stuff1" in workshop.checked and "missing stuff2" not in workshop.checked:
            $ workshop.checked.append("missing stuff2")
            $ victim.say("To si sedíš na uších, nebo mě máš za pitomce?", "angry")
            $ mc.say("Násilím otevřená je jenom ta jedna a...")
            $ victim.say("Říkám, že nic nechybí, tak nic nechybí.", "angry")
            $ victim.trust -= 1

        "{i}(Zkontrolovat dveře do místnosti){/i}" if "doors" not in workshop.checked:
            $ workshop.checked.append("doors")
            "Jedny dveře z dílny vedou na ulici, druhé do mistrova domu. Oboje jsou v dobrém stavu a ani na jedněch z nich nejsou jakékoli stopy násilného vniknutí. Dveře vedoucí do domu jsou čerstvě promazané."
            if "straight to workshop" in status and "door tried" not in workshop.checked:
                "Ty směrem na ulici se bez problému otevřou. Zřejmě byly celou dobu odemčené. Mistr Heinrich předstírá, že si toho nevšiml."
            $ clues.append("no forced entry")
            if "workshop unlocked" not in clues:
                $ clues.append("workshop unlocked")
        "Mohla být dílna celou noc odemčená?" if "workshop unlocked" in clues and "no forced entry" not in workshop.checked:
            $ workshop.checked.append("no forced entry")
            "Mistr Heinrich se zamračí ještě víc."
            $ victim.say("O tom nic nevím, ale jestli to tak bylo, rozhodně si to vyřídím s tím, kdo za to může.", "angry")

        "{i}(Prohlédnout si okna){/i}" if "windows" not in workshop.checked:
            $ workshop.checked.append("windows")
            "Okna jsou teď otevřená, je ale možné je zajistit bytelnou petlicí. Zloděj s drobnější postavou by se kterýmkoli z nich prosmýknout dokázal, nenajdeš ale žádné stopy, že by se je někdo pokoušel násilím otevřít zvenčí."
            "Pod jedním z oken je stůl, pod druhým jedno z ševcovských kopyt s připravenými nástroji. Nebylo by snadné oknem prolézt a o nic z toho přitom nezavadit."

        "{i}(Prohlédnout si boty){/i}" if "shoes" not in workshop.checked:
            $ workshop.checked.append("shoes")
            "Jsou tu boty lehké a elegantní, bytelné do divočiny nebo s kožešinou uvnitř do prudkých mrazů, všechno, aspoň co můžeš posoudit, prvotřídní práce. Zdá se, že mistr Heinrich nemá žádný typ, kterému by se věnoval více než jiným."
            "Boty jsou poměrně dobře srovnané a nenajdeš žádné poničení. Nevypadá to, že by se jimi v noci někdo přehraboval, a pokud ano, dobře po sobě uklidil."

        "{i}(Zkontrolovat materiál){/i}" if "material" not in workshop.checked:
            $ workshop.checked.append("material")
            "Je tu všechno od tvrdé kůže na podrážky po tu nejjemnější, ze které by se daly šít taneční boty na šlechtický ples. Nechybí ani dratev, nitě, vosk a různé druhy cvočků."

        "{i}(Prohlédnout si nástroje a vybavení dílny){/i}" if "tools" not in workshop.checked:
            $ workshop.checked.append("tools")
            "Na stole je vyrovnaná řada ševcovských kopyt a dále nejrůznějších kleští, šídel a nožů různých tvarů, stejně jako dalších věcí, jejichž použití ti uniká. Než ale stihneš vzít cokoli z toho do ruky, mistr Heinrich tě okřikne."
            $ victim.say("Na moje nástroje nesmí sahat ani můj vlastní syn, natož nějaký náhodný strážný!", "angry")

        "{i}(Prozkoumat popel v krbu){/i}" if time.days == 1 and time.hours < 14 and "fireplace" not in workshop.checked:
            $ workshop.checked.append("fireplace")
            "Jen pro jistotu prohrábneš popel v krbu. Po chvíli prosévání mezi prsty najdeš mezi ohořelými zbytky dřeva v zadním rohu nepatrný útržek stuhy, která snad bývala zlatá"
            "Mistr Heinrich na tebe vrhne nechápavý pohled."
            $ clues.append("burned evidence")
        "Můžete mi popsat ztracené střevíce?" if "burned evidence" in clues and "shoes description" not in clues:
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
            $ clues.append("shoes description")
        "Mohl by tenhle kousek stuhy být od vašich střevíců?" if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in victim.asked:
            "Mistr Heinrich si ohořelý útržek prohlédne a zamračí se."
            if "boys promised secrecy" in status:
                $ son.trust -= 3
                $ optimist.trust -= 3
                $ yesman.trust -= 3
                $ ada.trust -= 1
                $ status.remove("boys promised secrecy")
                $ status.append("secrecy broken")
            call burnedEvidenceSeenVictim
        "Můžu si ještě promluvit s vašimi učedníky?" if (apprentice1Note.isActive == True or apprentice2Note.isActive == True) and boysOptionsRemaining != 0:
            $ victim.say("Když to musí být. Ale nezdržuj je dlouho od práce.")
            if "boys met" in status:
                "Mistr Heinrich ti znovu přivede svého syna a učedníky."
            elif "boys seen" in status:
                "Mistr Heinrich přivede zpět chlapce, kteří v dílně před tvým příchodem uklízeli. Zblízka vypadají ještě unaveněji a jsou očividně nervózní."
            else:
                "Mistr Heinrich přivede tři asi patnáctileté mladíky. Všichni vypadají, jako by toho moc nenaspali, a jsou očividně nervózní."
            show mcPic at menuImage
            menu:
                "Nebude to trvat dlouho.":
                    hide mcPic
                    "Heinrich přikývne a založí si ruce, očividně připravený poslouchat každé vaše slovo."
                    $ status.append("no privacy")
                "Necháte nás prosím o samotě?":
                    hide mcPic
                    "Mistr se zamračí, ale pak beze slova odejde z dílny."
            call boysMain
        "Děkuji, to je všechno, co jsem chtěl[a] vidět.":
            return
    jump workshopOptions

label leavingWorkshop:
    $ victim.say("Tak kdy toho zloděje přivedeš před spravedlnost?")
    if "can return" not in workshop.checked:
        show mcPic at menuImage
        menu:
            "Jsem mu na stopě a co nevidět bude dopaden, spolehněte se.":
                hide mcPic
            "Můžu se vrátit, pokud budu mít další otázky?":
                hide mcPic
                $ workshop.checked.append("can return")
                $ victim.say("Já doufám, že se vrátíš i s mými střevíci.")
                $ mc.say("Pokud by to bylo nutné pro vyšetřování…")
                $ victim.say("Pokud to bude nutné, tak to hlavně zkrať. Nemám na hlídku celý den.")
    else:
        $ mc.say("Jsem mu na stopě a co nevidět bude dopaden, spolehněte se.")
    return

###

label burnedEvidenceSeenVictim:
    $ victim.asked.append("burned evidence seen")
    $ victim.say("To by mohlo… kde to bylo? A proč je to napůl spálené?", "angry")
    $ mc.say("Na[sel] jsem to v krbu...")
    $ victim.say("V jakém krbu? Kde?", "angry")
    if currentLocation == "workshop":
        $ mc.say("Tady v dílně.")
    else:
        $ mc.say("Ve vaší dílně.")
    $ victim.say("Chceš říct, že moje mistrovské dílo někdo nejen ukradl, ale ještě se pokusil zničit? A navíc v mém vlastním krbu v mé vlastní dílně?", "angry")
    $ victim.say("Až ho dostanu do ruky, tak ho vlastníma rukama přetrhnu jak hada!", "angry")
    $ victim.pressure += 2
    $ lisbeth.pressure += 1
    $ ada.pressure += 1
    $ son.pressure += 1
    $ optimist.pressure += 1
    $ yesman.pressure += 1
    return

###

label workshopOptionsRemainingCheck:
    $ workshopOptionsRemaining = 0
    if "table" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "table" in workshop.checked and "table contents" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "table" in workshop.checked and "missing stuff1" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "missing stuff1" in workshop.checked and "missing stuff2" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "doors" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "workshop unlocked" in clues and "no forced entry" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "shoes" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "material" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if "tools" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    if time.days == 1 and time.hours < 14  and "fireplace" not in workshop.checked:
        if time.minutes < 45 or currentLocation == "victim house":
            $ workshopOptionsRemaining += 1
    if "burned evidence" in clues and "shoes description" not in clues:
        $ workshopOptionsRemaining += 1
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence seen" not in victim.asked:
        $ workshopOptionsRemaining += 1
    if "windows" not in workshop.checked:
        $ workshopOptionsRemaining += 1
    return
