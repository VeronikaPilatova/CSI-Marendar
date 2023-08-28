label guildmasterController:
    # check if visit makes sense
    call guildmasterOptionsRemainingCheck
    if optionsRemaining == 0:
        "" "Nenapadá tě, co dalšího se (cechmistra) ještě ptát."
        return
    # walk over
    $ time.addMinutes(15)
    $ currentLocation = "guildmaster study"
    $ origAsked = guildmasterAsked.copy()

    # visit itself
    scene bg guildmaster
    if "guildmaster met" not in status:
        call guildmasterFirst
    else:
        call guildmasterAgain
    call guildmasterOptions
    call leavingGuildmaster

    # adjust time spent and status
    $ time.addMinutes((len(guildmasterAsked) - len(origAsked)) * 3)
    if "guildmaster met" not in status:
        $ status.append("guildmaster met")
    return

label guildmasterFirst:
    "" "(Jméno) je jako představený cechu zaměstnaný člověk, ale když vysvětlíš, o co se jedná, podaří se ti domluvit s ním schůzku."
    $ guildmaster.say("Hlídka má samozřejmě mou plnou podporu v pátrání. Pokud se ukradená věc nenajde do slavností, mohlo by to poškodit pověst celého cechu a to ani nemluvím o urážce Einiona samotného…")
    $ mc.say("Děkuji vám za ochotu.")
    return

label guildmasterAgain:
    "" "DEBUG: Mluvíš s cechmistrem znovu."
    return

label guildmasterOptions:
    call guildmasterOptionsRemainingCheck
    if optionsRemaining == 0:
        if gender == "M":
            $ mc.say("To je všechno, na co jsem se chtěl zeptat. Děkuji vám za spolupráci.")
        else:
            $ mc.say("To je všechno, na co jsem se chtěla zeptat. Děkuji vám za spolupráci.")
        return

    show mcPic at menuImage
    menu:
        "Je pravda, že jste se s (okradený mistr) včera pohádal v hospodě (jméno)?" if "pub fight" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("pub fight")
            $ guildmaster.say("To je pravda.")
            $ guildmaster.say("Když jsem (do hospody) přišel já, (okradený mistr) už byl dávno v náladě a vykřikoval na celou hospodu, že jeho dílo bude ozdoba celých slavností a budeme ho ještě všichni prosit, aby se stal cechmistrem.")
            $ guildmaster.say("Snažil jsem se ho ignorovat, ale po pár sklenkách mi to nedalo a ohradil jsem se.")
            $ mc.say("O čem jste se hádali?")
            $ guildmaster.say("O povinnostech cechmistra, především. (Okradený mistr) si myslí, že cechmistrem by měl být nejlepší řemeslník. Pořád nemůže pochopit, že to je politická role, která zahrnuje vyjednávání s městskou radou a rozhodování sporů uvnitř cechu. Musí se hledat řešení a dělat kompromisy.")
            $ guildmaster.say("On je mistr svého oboru a to mu nikdo neupírá, ale nedokáže vyjít ani s vlastními lidmi. Nepracuje pro něj jediný tovaryš, protože (mistr) vyžaduje naprostou poslušnost. Jak by pod někým takovým mohl cech prosperovat?")
            $ clues.append("pub fight topic")

        "Napadá vás někdo, s kým má (okradený mistr) spory?" if "enemies" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("enemies")
            $ guildmaster.say("Myslím, že nejhorší vztahy má (okradený mistr) uvnitř své vlastní dílny. Není schopný vyjít s žádným tovaryšem a učedníky vyhodil už tři. Jeden z nich dokonce musel jít až do Sehnau.")
        "Podle (okradeného mistra) má největší spory s vámi." if "enemies" in guildmasterAsked and "main suspect" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("main suspect")
            $ guildmaster.trust -= 1
            $ guildmaster.say("Dnes možná, zítra to bude možná někdo jiný. Co se mě týče, uznávám ho jako mistra oboru a rozhodně bych mu neukradl dílo, jakkoli se mi nelíbí jeho přístup k lidem.")
        "Víte, kde bych našel ty zbývající učedníky?" if "enemies" in guildmasterAsked and "fired apprentices" not in clues and gender == "M":
            call firedApprentices
        "Víte, kde bych našla ty zbývající učedníky?" if "enemies" in guildmasterAsked and "fired apprentices" not in clues and gender == "F":
            call firedApprentices
        "S kým má (okradený mistr) spory mimo svou dílnu?" if "enemies" in guildmasterAsked and "enemies2" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("enemies2")
            $ guildmaster.say("Mimo jeho dílnu bude snazší najít lidi, se kterými (okradený mistr) spory nemá. Rozhádal se s polovinou cechu a s většinou obchodníků, od kterých bere materiál.")
            $ guildmaster.say("Ale dohody dodržuje a nemyslím si, že by mu kdokoli z nich chtěl skutečně ublížit.")
        "Je někdo, s kým má (okradený mistr) spory dlouhodobě, nebo silnější než s někým jiným?" if "enemies2" in guildmasterAsked and "enemies3" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("enemies3")
            $ guildmaster.say("Nevím o tom. On spory snadno rozdmýchá, ale také zase snadno zapomene.")

        "Kde jste byl včera v noci?" if "alibi" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("alibi")
            $ guildmaster.say("(Z hospody) jsem šel rovnou domů a spát.")
            call alibiReaction

        "To je všechno, na co jsem se chtěl zeptat. Děkuji vám za spolupráci." if gender == "M":
            hide mcPic
            return
        "To je všechno, na co jsem se chtěla zeptat. Děkuji vám za spolupráci." if gender == "F":
            hide mcPic
            return
    jump guildmasterOptions

label leavingGuildmaster:
    $ guildmaster.say("Pokud zloděje nedopadnete a nevrátíte výrobek do slavností, může to poškodit pověst celého cechu. A to samozřejmě nechci dopustit.")
    show mcPic at menuImage
    menu:
        "Můžu se vrátit, pokud budu mít další otázky?" if "can return" not in guildmasterAsked:
            hide mcPic
            $ guildmasterAsked.append("can return")
            $ guildmaster.say("Pokud to bude nutné pro vyšetřování, tak jistě. Ale velmi doufám, že celá věc bude uzavřená co nejrychleji.")
            $ mc.say("Udělám, co bude v mých silách.")
        "Udělám, co bude v mých silách.":
            hide mcPic
    return

###

label firedApprentices:
    hide mcPic
    $ guildmasterAsked.append("fired apprentices")
    $ guildmaster.say("Jednoho z nich si myslím vzal k sobě (vynálezce). Ten druhý se mám dojem chytil špatné společnosti, možná by se dal najít v někde dočasné čtvrti.")
    $ clues.append("fired apprentices")
    $ firedApprentice1Note.isActive = True
    $ firedApprentice2Note.isActive = True
    return

label alibiReaction:
    show mcPic at menuImage
    menu:
        "Může vám to někdo potvrdit?":
            hide mcPic
            $ guildmaster.say("Doma byla manželka, můžete se jí zeptat. Z hospody mne doprovodil můj bratr.")
            $ guildmaster.say("Chápu, proč se na to ptáte, ale co by mi osobně taková krádež přinesla? Většina cechu sdílí mé názory, jsem přesvědčený, že (okradeného mistra) stejně do vedení nezvolí. Jediné, k čemu celá tahle nešťastná záležitost může vést, je zhoršení postavení nás všech.")
            $ guildmasterWifeNote.isActive = True
        "Samozřejmě vás nikdo nepodezírá.":
            hide mcPic
            $ guildmaster.trust += 1
            $ guildmaster.say("Hlídka jen dělá svou práci. A já v této věci skutečně nemám co skrývat.")
    return

label guildmasterOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "pub fight" not in guildmasterAsked:
        $ optionsRemaining += 1
    if "enemies" not in guildmasterAsked:
        $ optionsRemaining += 1
    if "enemies" in guildmasterAsked and "fired apprentices" not in clues:
        $ optionsRemaining += 1
    if "enemies" in guildmasterAsked and "enemies2" not in guildmasterAsked:
        $ optionsRemaining += 1
    if "enemies2" in guildmasterAsked and "enemies3" not in guildmasterAsked:
        $ optionsRemaining += 1
    if "enemies" in guildmasterAsked and "main suspect" not in guildmasterAsked:
        $ optionsRemaining += 1
    if "alibi" not in guildmasterAsked:
        $ optionsRemaining += 1
    return
