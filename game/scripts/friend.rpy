label friendController:
    # check if visit makes sense
    call friendOptionsRemainingCheck
    if optionsRemaining == 0 and ("retrieving workshop key" not in status or "carrying key" in status or "too late for key" in status):
        "" "Nenapadá tě, na co dalšího se (přítele) ještě zeptat."
        return
    # walk over
    $ time.addMinutes(15)
    $ currentLocation = "friend house"
    $ origAsked = friendAsked.copy()

    # visit itself
    call friendIntro
    if "retrieving workshop key" in status and "carrying key" not in status and "too late for key" not in status:
        if time.days == 1 and time.hours < 17:
            call sentForKey
        else:
            call sentForKeyLate
    elif "friend met" not in status:
        call friendFirst
    else:
        call friendOptions

    # adjust time and status
    $ time.addMinutes((len(friendAsked) - len(origAsked)) * 5)
    if "friend met" not in status:
        $ status.append("friend met")

    call leavingFriend
    return

label friendIntro:
    scene bg friend
    "" "Na první zaklepání na dveře nikdo nereaguje."
    "" "Až když zabušíš ještě jednou a hlasitěji, otevře ti rozcuchaný muž s kruhy pod očima."
    $ friend.say("Ne tak nahlas! Kdo to… co chceš?")
    if "friend met" in status:
        $ friend.say("Aha, to jsi zase ty. Potřebuje hlídka ještě něco?")
    return

label sentForKey:
    $ mc.say("Posílá mě (okradený mistr), že byste měl mít klíč od jeho dílny.")
    $ friend.say("Já mu ho nevrátil? Byl jsem přesvědčený, že jo. Aby mohl zase zamknout.")
    show mcPic at menuImage
    menu:
        "Vy jste nezamykal?":
            hide mcPic
            $ friend.say("Ne, to bych si pamatoval. Vevnitř byla tma, já to tam neznám… to musel (okradený mistr).")
        "Můžete se prosím podívat?":
            hide mcPic
    "" "(Přítel) si sáhne k pasu, kde asi čeká brašničku, ale nahmátne jen látku své haleny."
    $ friend.say("Počkej tady.")
    "" "(Přítel) se vrátí do domu, přes dveře chvíli slyšíš tlumené klení. Pak se ale vrátí s širokým úsměvem a masivním klíče v ruce."
    $ friend.say("To jsem blázen… opravdu jsem ho měl u sebe. Ale kdo potom zamknul?", "happy")
    $ friend.say("No nic, (okradeného mistra) pozdravuj.")
    $ status.append("carrying key")
    if "workshop unlocked" not in clues:
        $ clues.append("workshop unlocked")
    call friendOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Vyřídím.")
        return
    else:
        show mcPic at menuImage
        menu:
            "Vyřídím.":
                hide mcPic
                return
            "Můžu se vás ještě na pár věcí zeptat?":
                hide mcPic
                $ friend.say("Asi jo… jenom ne moc najednou, bolí mě hlava.")
                jump friendOptions
    return

label sentForKeyLate:
    $ status.append("too late for key")
    $ status.remove("retrieving workshop key")
    $ victim.trust -= 3
    $ mc.say("Posílá mě (okradený mistr), že byste měl mít klíč od jeho dílny.")
    $ friend.say("To jsem měl, pořád nechápu, jak se to stalo. A kdo dílnu zase zamknul, když já to nebyl. Ale (okradený mistr) si pro něj už přišel sám.")
    $ friend.say("Nadával u toho na zatracenou hlídku, která by nenašla ani vlastní zadek a nechytila ani rýmu. A že těm něco svěřit je…")
    if "friend met" in status:
        $ friend.say("Nic proti tobě, samozřejmě.")
    else:
        if gender == "M":
            $ friend.say("Promiň, co že jsi to chtěl?")
        else:
            $ friend.say("Promiň, co že jsi to chtěla?")
    call friendOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Hlavně, že je klíč vrácený.")
        "" "(Přítel) přikývne a rozloučí se."
        return
    else:
        show mcPic at menuImage
        menu:
            "Hlavně, že je klíč vrácený.":
                hide mcPic
                "" "(Přítel) přikývne a rozloučí se."
                return
            "Můžu se vás ještě na pár věcí zeptat?":
                hide mcPic
                $ friend.say("Asi jo… jenom ne moc najednou, bolí mě hlava.")
                jump friendOptions
    return

label friendFirst:
    $ mc.say("Jsem %(mcName)s z městské hlídky a vyšetřuji krádež v dílně mistra (jméno). Včera jste spolu byli (v hospodě).")
    $ status.append("friend introductions")
    $ friend.say("Jo, to jsme byli. Slavili jsme a asi jsme to trochu přehnali.")
    $ friend.say("Vždycky si říkám, že nebudu pít tolik, ale… ale (okradený mistr) na tom byl ještě hůř.")
    $ mc.say("Můžu vám položit pár otázek?")
    $ friend.say("Jo… jenom ne moc najednou, bolí mě hlava.")
    jump friendOptions

label friendOptions:
    call friendOptionsRemainingCheck
    if optionsRemaining == 0:
        if gender == "M":
            $ mc.say("Děkuji, to jsou všechny otázky.")
        else:
            $ mc.say("Děkuji, to jsou všechny otázky.")
        return

    show mcPic at menuImage
    menu:
        "Kdy jste včera s (okradeným) odešli z hospody?" if "when did they leave" not in friendAsked:
            hide mcPic
            $ friendAsked.append("when did they leave")
            $ friend.say("Někdy po půlnoci? Nevím přesně. Venku byla tma.")
        "Kde jste se s (okradeným) rozloučili?" if "coming home" not in friendAsked:
            hide mcPic
            $ friendAsked.append("coming home")
            $ friend.say("Až úplně doma.")
            if "carrying key" in status or time.days > 1 or time.hours > 16:
                $ friend.say("Až úplně doma. Já (mistra) dovedl k domu a on trval na tom, že dovnitř musíme přes dílnu, aby se nevzbudila ta jeho semetrika. Chvíli se pral s klíčem, pak jsem nějak odemkl já a on potom…")
                $ friend.say("...a potom jsem ten klíč asi zapomněl vrátit.")
                if "carrying key" in status:
                    $ friend.say("A teď ho máte vy.")
                elif "key delivered" in status:
                    $ friend.say("A pak jsem ho předal vám.")
                else:
                    $ friend.say("“(Okradený) si ho u mě potom vyzvedl. Dost jsem se divil, ale asi jsme byli fakt hodně v náladě.")
                if "forgotten key" not in clues:
                    $ clues.append("forgotten key")
            else:
                $ friend.say("Já (mistra) dovedl k domu a on trval na tom, že dovnitř musíme přes dílnu, aby se nevzbudila ta jeho semetrika. Chvíli se pral s klíčem, pak jsem nějak odemkl já a on potom vevnitř zamknul.")
                $ friend.say("Nějak jsme se dohrabali až do postele, tam jsem ho nechal a šel jsem rovnou domů.")
                $ mc.say("A jak jste se dostal ven, když bylo zamčeno?")
                $ friend.say("Normálně dveřma… no jo vlastně…")
                if "forgotten key" not in clues:
                    $ clues.append("forgotten key")
                if "workshop unlocked" not in clues:
                    $ clues.append("workshop unlocked")
        "Mohla být dílna celou noc odemčená?" if ("workshop unlocked" in clues or "forgotten key" in clues) and "no forced entry" not in friendAsked:
            hide mcPic
            $ friendAsked.append("no forced entry")
            $ friend.say("To bysme museli být fakt hodně namol.")
            $ friend.say("Ale abych byl fér… my jsme asi hodně namol byli. Takže možná?")
            if "carrying key" not in status and "key delivered" not in status and time.days == 1 and time.hours < 17:
                call forgottenKeyScene
        "Všiml jste si včera u (mistrovy) dílny něčeho podezřelého?" if "anything suspicious" not in friendAsked:
            hide mcPic
            $ friendAsked.append("anything suspicious")
            $ friend.say("Ani ne… byla tam tma a hromada věcí, ale to tam je asi vždycky?")
            $ friend.say("Snažili jsme se hlavně být jako myšky a nijak jsme se nerozhlíželi kolem.")
        "Děkuji, to jsou všechny otázky.":
            hide mcPic
            $ friend.say("Snad to pomohlo…")
            return
    if "friend introductions" not in status:
        $ friend.say("...proč se vlastně ptáš? Děje se něco?")
        $ mc.say("(Okradenému mistrovi) se z dílny ztratil jeho mistrovský výrobek. Jsem z městské hlídky.")
        $ friend.say("Ty střevíce, které včera došil? Ty musíte najít! Rád pomůžu, jak jenom budu moct.")
        $ status.append("friend introductions")
    jump friendOptions


label leavingFriend:
    if "carrying key" in status:
        menu:
            "Donést klíč (okradenému mistrovi)":
                jump victimHouseholdController
            "Vzít klíč k zámečníkovi" if "duplicate key" not in status:
                jump locksmith
            "Vrátit se na strážnici":
                return
    else:
        return

label locksmith:
    scene bg locksmith
    "" "Po chvíli hledání se ti podaří najít malý krámek se znakem dvou klíčů nade dveřmi a vejdeš dovnitř."
    "" "Hobit za pultem se na tebe zářivě usměje."
    $ locksmith.say("Co pro vás můžu udělat?")
    show mcPic at menuImage
    menu:
        "Potřeboval/a bych duplikát tohoto klíče. Ideálně tak, abych tady nemusel/a ten klíč dlouho nechat…":
            hide mcPic
            "" "Zámečník si od tebe vezme klíč od dílny (okradeného mistra) a prohlédne si ho."
            $ locksmith.say("Samozřejmě, to nebude problém. Dejte mi chvilku na formu a do večera budete mít druhý klíč.")
            $ mc.say("Děkuji, večer se pro něj stavím.")
            $ status.append("duplicate key")
            $ time.addMinutes(15)
        "Vlastně nic, jenom se tu rozhlížím.":
            hide mcPic
            $ locksmith.say("Kdyby vám něco padlo do oka, stačí říct.")
    jump leavingFriend

###

label forgottenKeyScene:
    "" "(Přítel) se zamračí, sáhne si k pasu, kde asi čeká brašničku, ale nahmátne jen látku své haleny."
    $ friend.say("Počkej tady.")
    "" "(Přítel) se vrátí do domu a po chvíli zase vyjde se zmateným výrazem a masivním klíče v ruce."
    $ friend.say("To jsem blázen… budu ho muset (okradenému) vrátit.")
    show mcPic at menuImage
    menu:
        "To byste asi měl.":
            hide mcPic
        "Můžu mu ho donést, pokud chcete.":
            hide mcPic
            $ friend.say("To mi pomůže, díky. Já bych tam došel, ale je mi dneska špatně…")
            $ status.append("carrying key")
    $ clues.append("forgotten key")
    $ time.addMinutes(10)
    return

label friendOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "when did they leave" not in friendAsked:
        $ optionsRemaining += 1
    if "coming home" not in friendAsked:
        $ optionsRemaining += 1
    if ("workshop unlocked" in clues or "forgotten key" in clues) and "no forced entry" not in friendAsked:
        $ optionsRemaining += 1
    if "anything suspicious" not in friendAsked:
        $ optionsRemaining += 1
