label eckhardController:
    # check if visit makes sense
    call eckhardOptionsRemainingCheck
    if optionsRemaining == 0 and ("retrieving workshop key" not in status or "carrying key" in status or "too late for key" in status):
        "Nenapadá tě, na co dalšího se Eckarda ještě zeptat."
        return
    call preludeController

    # walk over
    if eckhard not in cells:
        if eckhard.alreadyMet == False:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        $ currentLocation = "eckhard house"
    $ origAsked = eckhard.asked.copy()

    # visit itself
    if eckhard in cells:
        call eckhardCellsIntro
    else:
        call eckhardIntro
        if "retrieving workshop key" in status and "carrying key" not in status and "too late for key" not in status:
            if time.days == 1 and time.hours < 17:
                call sentForKey
            else:
                call sentForKeyLate
        elif eckhard.alreadyMet == False:
            call eckhardFirst
        else:
            call eckhardOptions

    # adjust time and status
    $ time.addMinutes((len(eckhard.asked) - len(origAsked)) * 5)
    if eckhard.alreadyMet == False:
        $ eckhard.alreadyMet = True

    call leavingFriend
    return

label eckhardIntro:
    scene bg eckhard
    "Na první zaklepání na dveře nikdo nereaguje."
    "Až když zabušíš ještě jednou a hlasitěji, otevře ti rozcuchaný muž s kruhy pod očima."
    $ eckhard.say("Ne tak nahlas! Kdo to… co chceš?")
    if eckhard.alreadyMet == True:
        $ eckhard.say("Aha, to jsi zase ty. Potřebuje hlídka ještě něco?")
    return

label sentForKey:
    $ mc.say("Posílá mě mistr Heinrich, že byste měl mít klíč od jeho dílny.")
    $ eckhard.say("Já mu ho nevrátil? Byl jsem přesvědčený, že jo. Aby mohl zase zamknout.")
    show mcPic at menuImage
    menu:
        "Vy jste nezamykal?":
            hide mcPic
            $ eckhard.say("Ne, to bych si pamatoval. Vevnitř byla tma, já to tam neznám… to musel Heinrich.")
        "Můžete se prosím podívat?":
            hide mcPic
    "Eckhard si sáhne k pasu, kde asi čeká brašničku, ale nahmátne jen látku své haleny."
    $ eckhard.say("Počkej tady.")
    "Eckhard se vrátí do domu, přes dveře chvíli slyšíš tlumené klení. Pak se ale vrátí s širokým úsměvem a masivním klíče v ruce."
    $ eckhard.say("To jsem blázen… opravdu jsem ho měl u sebe. Ale kdo potom zamknul?", "happy")
    $ eckhard.say("No nic, Heinricha pozdravuj.")
    $ status.append("carrying key")
    if "workshop unlocked" not in clues:
        $ clues.append("workshop unlocked")
    call eckhardOptionsRemainingCheck from _call_eckhardOptionsRemainingCheck_1
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
                $ eckhard.say("Asi jo… jenom ne moc najednou, bolí mě hlava.")
                jump eckhardOptions
    return

label sentForKeyLate:
    $ status.append("too late for key")
    $ status.remove("retrieving workshop key")
    $ status.append("not reliable")
    $ victim.trust -= 3
    $ mc.say("Posílá mě mistr Heinrich, že byste měl mít klíč od jeho dílny.")
    $ eckhard.say("To jsem měl, pořád nechápu, jak se to stalo. A kdo dílnu zase zamknul, když já to nebyl. Ale Heinrich si pro něj už přišel sám.")
    $ eckhard.say("Nadával u toho na zatracenou hlídku, která by nenašla ani vlastní zadek a nechytila ani rýmu. A že těm něco svěřit je…")
    if eckhard.alreadyMet == True:
        $ eckhard.say("Nic proti tobě, samozřejmě.")
    else:
        $ eckhard.say("Promiň, co že jsi to chtěl[a]?")
    call eckhardOptionsRemainingCheck from _call_eckhardOptionsRemainingCheck_2
    if optionsRemaining == 0:
        $ mc.say("Hlavně, že je klíč vrácený.")
        "Eckhard přikývne a rozloučí se."
        return
    else:
        show mcPic at menuImage
        menu:
            "Hlavně, že je klíč vrácený.":
                hide mcPic
                "Eckhard přikývne a rozloučí se."
                return
            "Můžu se vás ještě na pár věcí zeptat?":
                hide mcPic
                $ eckhard.say("Asi jo… jenom ne moc najednou, bolí mě hlava.")
                jump eckhardOptions
    return

label eckhardFirst:
    $ mc.say("Jsem %(mcName)s z městské hlídky a vyšetřuji krádež v dílně mistra Heinricha. Včera jste spolu byli v hospodě U Salmy?")
    $ status.append("eckhard introductions")
    $ eckhard.say("Jo, to jsme byli. Slavili jsme a asi jsme to trochu přehnali.")
    $ eckhard.say("Vždycky si říkám, že nebudu pít tolik, ale… ale Heinrich na tom byl ještě hůř.")
    $ mc.say("Můžu vám položit pár otázek?")
    $ eckhard.say("Jo… jenom ne moc najednou, bolí mě hlava.")
    jump eckhardOptions

label eckhardCellsIntro:
    "Eckharda najdeš, jak přechází po cele a čas od času se poškrábe na hlavě."
    $ eckhard.say("Jdete mě pustit?")
    show mcPic at menuImage
    menu:
        "Ano, jdu vás pustit.":
            hide mcPic
            $ eckhard.say("No výborně. Já jsem věděl, že je hlídka rozumná.", "happy")
            "Odemkneš celu a odvedeš Eckharda ven ze strážnice."
            scene bg door01
            $ eckhard.say("Tak se uvidíme na slavnostech?", "happy")
            $ mc.say("Pokud vás nebudeme potřebovat dřív. Neopouštějte prosím Marendar.")
            $ eckhard.say("To se nemusíte bát. Proč bych to dělal?", "surprised")
            $ cells.remove(eckhard)
        "Chci se vás jen na pár věcí zeptat.":
            hide mcPic
            $ eckhard.say("Na to mě ale nemusíte držet tady... rád vám na všechno odpovím i doma.", "surprised")
            $ mc.say("Bohužel nemám jinou možnost.")
            $ eckhard.say("Ale… no dobře, tak se ptejte.", "sad")
            $ eckhard.say("Ale stejně to nechápu.", "sad")
            jump eckhardOptions
    return

label eckhardOptions:
    call eckhardOptionsRemainingCheck from _call_eckhardOptionsRemainingCheck_3
    if optionsRemaining == 0:
        $ mc.say("Děkuji, to jsou všechny otázky.")
        return

    show mcPic at menuImage
    menu:
        "Víte, jaký vám za krádež střihu hrozí trest?" if eckhard in cells and "crime and punishment" not in eckhard.asked:
            hide mcPic
            $ eckhard.say("Nedokážu si představit, že by libovolný soudce podobnou drobnost řešil. Možná jedině nějakou pokutou, kterou ochotně zaplatím.")
        "Kdy jste včera s mistrem Heinrichem odešli z hospody?" if "when did they leave" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("when did they leave")
            $ eckhard.say("Někdy po půlnoci? Nevím přesně. Venku byla tma.")
        "Kde jste se s mistrem Heinrichem rozloučili?" if "coming home" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("coming home")
            $ eckhard.say("Až úplně doma.")
            if "carrying key" in status or time.days > 1 or time.hours > 16:
                $ eckhard.say("Až úplně doma. Já Heinricha dovedl k domu a on trval na tom, že dovnitř musíme přes dílnu, aby se nevzbudila ta jeho semetrika. Chvíli se pral s klíčem, pak jsem nějak odemkl já a on potom…")
                $ eckhard.say("...a potom jsem ten klíč asi zapomněl vrátit.")
                if "carrying key" in status:
                    $ eckhard.say("A teď ho máte vy.")
                elif "key delivered" in status:
                    $ eckhard.say("A pak jsem ho předal vám.")
                else:
                    $ eckhard.say("Heinrich si ho u mě potom vyzvedl. Dost jsem se divil, ale asi jsme byli fakt hodně v náladě.")
                if "forgotten key" not in clues:
                    $ clues.append("forgotten key")
            else:
                $ eckhard.say("Já Heinricha dovedl k domu a on trval na tom, že dovnitř musíme přes dílnu, aby se nevzbudila ta jeho semetrika. Chvíli se pral s klíčem, pak jsem nějak odemkl já a on potom vevnitř zamknul.")
                $ eckhard.say("Nějak jsme se dohrabali až do postele, tam jsem ho nechal a šel jsem rovnou domů.")
                $ mc.say("A jak jste se dostal ven, když bylo zamčeno?")
                $ eckhard.say("Normálně dveřma… no jo vlastně…")
                if "forgotten key" not in clues:
                    $ clues.append("forgotten key")
                if "workshop unlocked" not in clues:
                    $ clues.append("workshop unlocked")
        "Mohla být dílna celou noc odemčená?" if ("workshop unlocked" in clues or "forgotten key" in clues) and "no forced entry" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("no forced entry")
            $ eckhard.say("To bysme museli být fakt hodně namol.")
            $ eckhard.say("Ale abych byl fér… my jsme asi hodně namol byli. Takže možná?")
            if "carrying key" not in status and "key delivered" not in status and time.days == 1 and time.hours < 17:
                call forgottenKeyScene from _call_forgottenKeyScene
        "Všiml jste si včera u dílny mistra Heinricha něčeho podezřelého?" if "anything suspicious" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("anything suspicious")
            $ eckhard.say("Ani ne… byla tam tma a hromada věcí, ale to tam je asi vždycky?")
            $ eckhard.say("Snažili jsme se hlavně být jako myšky a nijak jsme se nerozhlíželi kolem.")
        "Má mistr Heinrich problémy s alkoholem?" if kaspar.alreadyMet == True and "alcoholic" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("alcoholic")
            if "alcoholic" not in lisbeth.asked and "alcoholic" not in salma.asked:
                $ victim.trust -= 1
            "Eckhard zavrtí hlavou a pak toho očividně lituje."
            $ eckhard.say("Ne… rozhodně ne větší, než kdokoli jiný. Ani mu pak ráno nebývá moc špatně, zatímco já chci vždycky umřít. Ale to má spíš alkohol problém se mnou.")
        "Můžete se u mistra Heinricha přimluvit za jeho syna a učedníky?" if "confession" in boysAsked and "defend boys" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("defend boys")
            $ eckhard.say("Přimluvit? Já? Není Heinrichova domácnost jeho věc?", "surprised")
            $ mc.say("To samozřejmě je, ale rád[a] bych, aby neudělal ukvapené rozhodnutí jen proto, že bude zrovna naštvaný.")
            $ eckhard.say("Jo, zuřit on umí. Co zase kluci provedli?")
            $ mc.say("Vypili mu část jeho zásob vína.")
            $ eckhard.say("Cože? Snad ne i chatevinské šedé, na které mě chtěl Heinrich pozvat! To by byla hrozná škoda.", "surprised")
            $ mc.say("Je v lahvi z modrého skla s úzkým hrdlem?")
            $ eckhard.say("Přesně. Snad ne...?", "sad")
            $ mc.say("Bohužel.")
            $ eckhard.say("To je nejhorší zpráva dnešního dne.", "sad")
            $ eckhard.say("No, aspoň je vidět, že kluci mají vkus a jablko nepadlo daleko od stromu.")
            $ mc.say("Můžete zkusit s mistrem Heinrichem promluvit, aby je za to nevyhodil? Třeba mu připomenout, že byl také jednou mladý učedník?")
            $ eckhard.say("To mu nemusím připomínat, na to spolu rádi vzpomínáme.")
            $ eckhard.say("Upřímně, být učedník bylo na nic, neměli jsme ani vindru, pili jsme tu nejhorší břečku a mistr nás každou chvíli řezal. Ale nikdo od nás neočekával, že budeme mít rozum. To mi občas chybí.", "happy")
            if victim.trust > 3:
                $ eckhard.say("A my rozum vážně neměli. Sice jsme mistrovi nevypili jeho zásoby, ale zase jsme se jednou zřídili nějakým levným patokem a potom vyprávěli důležitému zákazníkovi oplzlé vtipy, zatímco čekal na mistra.")
                $ eckhard.say("Mám dojem, že se smál, ale možná jsme to zvládli i za něj. Mistra to rozhodně moc nepobavilo.")
            $ eckhard.say("Pozvu Heinricha k Salmě, když z toho chatevinského nic nebude, a připomenu mu, že my jsme toho za učednických let taky něco vypili.", "happy")
        "Máte tušení, jak se mistr Heinrich mohl dostat ke střihu, který vytvořil mistr Njal?" if "stolen idea" in clues and "stolen idea" not in eckhard.asked and "stolen idea 2" not in eckhard.asked:
            hide mcPic
            "Eckhard zamrká překvapením."
            $ eckhard.say("Ke střihu mistra Njala? Jak víte… to souvisí s krádeží jeho střevíců?")
            call stolenIdea
        "Mistr Heinrich říkal, že od vás dostal střih ukradený mistru Njalovi." if "stolen idea" in victim.asked and "stolen idea" not in eckhard.asked and "stolen idea 2" not in eckhard.asked:
            hide mcPic
            "Eckhard zamrká překvapením."
            $ eckhard.say("Cože? Jak víte… to souvisí s krádeží jeho střevíců?")
            call stolenIdea
        "A tak jste se rozhodl ten střih ukrást?" if "stolen idea" in eckhard.asked and "stolen idea 2" not in eckhard.asked:
            call stolenIdeaConfession
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("join forces")
            $ status.append("join forces survey")
            "Eckhard svraští čelo."
            $ eckhard.say("Proč by to kdo dělal? Spousta zbytečné práce navíc, kterou stejně nikdo pořádně neocení. Myslím, že by to všem bylo celkem jedno.", "angry")
            $ eckhard.say("Teda jestli by to nebylo nějaké hodně divné spojení, že jo, třeba kdyby švec s kolářem spolu udělali… něco. O tom by se určitě mluvilo.")
            $ mc.say("A co kdyby se spojili mistr Heinrich a mistr Njal?")
            $ eckhard.say("Tak by to Njal Heinrichovi zkazil. Rumelin by asi měl radost a ostatní by se divili, jestli se chudák Heinrich pomátl.")
            $ mc.say("Šlo by o to, že by mistr Heinrich vyrobil boty podle střihu mistra Njala a při představení toho výrobku by všem řekli, kdo z nich udělal co.")
            $ eckhard.say("No tak to je něco jiného! To by bylo skvělé dílo, které by si všichni měli prohlédnout!")
            $ eckhard.say("Ono to totiž skvělé dílo už jednou bylo. Vážně doufám, že ten mizera, který ty boty ukradl nebo co se s nimi stalo, dostane pořádně za vyučenou.")
            if "stolen idea" not in eckhard.asked:
                $ mc.say("Oni už mistr Njal a Heinrich spolupracovali?")
                $ eckhard.say("Ne, to ne. Chci říct, Heinrich už jednou vyráběl boty podle Njalova střihu.")
                $ mc.say("A ty boty pak někdo ukradl?")
                $ eckhard.say("No, jo, přesně. A byly dokonalé.", "happy")
                $ eckhard.asked.append("stolen idea slip")
            $ eckhard.say("A kdyby to lidi ve městě viděli, museli by už konečně všichni uznat, že Heinrich je zdaleka nejlepší mistr v Marendaru a pěkných pár městech okolo, a přestat mu konečně upírat místo cechmistra.", "happy")
            $ eckhard.say("Nevím tedy, co by z toho měl Njal. Ten by vypadal, že se chce jenom přiživit na Heinrichově slávě. Ale je to trpaslík, třeba ho prostě Einion nezajímá a chce si to nějak odbýt, aby se neřeklo.")
            $ eckhard.say("Znamená to, že ty boty se zlatou stužkou nakonec Heinrich na slavnosti přinese? To je výborná zpráva!", "happy")
            $ mc.say("Nemůžu zatím nic slíbit. Mistři se zatím na spojení nedohodli.")
            $ eckhard.say("Heinricha přesvědčím, teď jen aby opravdu souhlasil i ten Njal.")
        "Povězte mi víc o těch botách, které mistr Heinrich vyráběl podle střihu mistra Njala." if "stolen idea slip" in eckhard.asked and "stolen idea slip 2" not in eckhard.asked and "stolen idea" not in eckhard.asked:
            hide mcPic
            $ eckhard.asked.append("stolen idea slip 2")
            $ eckhard.say("... to snad není tak důležité, ne?")
            $ mc.say("Jestli už byl mistr Heinrich okraden víckrát, je to pro případ zásadní. Co když to byl stejný pachatel? Potřebuji znát všechny podrobnosti.")
            $ eckhard.say("Víte, no...")
            $ mc.say("Samozřejmě chápu, jestli si to nepamatujete dokonale. Počítám s tím, že se pak vyptám i samotného mistra Heinricha.")
            $ eckhard.say("To nebude nutné.", "surprised")
            $ eckhard.say("Ony podle Njalova nákresu byly šité ty boty, které byly ukradené teď.")
            $ eckhard.say("Jen o tom mistr Njal asi ještě neví.")
        "Jak to může nevědět? To jste mu ten střih ukradli?" if "stolen idea slip 2" in eckhard.asked and "stolen idea 2" not in eckhard.asked:
            call stolenIdeaConfession

        "Děkuji, to jsou všechny otázky.":
            hide mcPic
            $ eckhard.say("Snad to pomohlo…")
            return
        "Zatýkám vás za krádež střihu mistra Njala." (badge="handcuffs") if "stolen idea 2" in eckhard.asked and eckhard not in arrested:
            hide mcPic
            $ eckhard.say("Cože? To můžete? Vždyť to je jenom střih.", "surprised")
            $ eckhard.say("Jestli to je opravdu zločin, tak mi můžete vyměřit nějakou pokutu, ale rozhodně není potřeba mě zatýkat.")
            $ eckhard.say("Já nikam nepůjdu, mám tu dílnu a na slavnosti se těším.")
            $ eckhard.say("A hlavně jsem si dost jistý, že jsem městu pomohl.")
            show mcPic at menuImage
            menu:
                "Dobře, neopouštějte ale Marendar.":
                    hide mcPic
                    $ eckhard.trust += 2
                    $ victim.trust += 2
                "Přiznal jste se ke zločinu, tak vás musím zatknout.":
                    hide mcPic
                    $ eckhard.trust -= 2
                    $ victim.trust -= 2
                    $ eckhard.arrestReason.append("stolen idea")
                    $ arrested.append(eckhard)
                    jump arrest

    if "eckhard introductions" not in status:
        $ eckhard.say("...proč se vlastně ptáš? Děje se něco?")
        $ mc.say("Mistru Heinrichovi se z dílny ztratil jeho mistrovský výrobek. Jsem z městské hlídky.")
        $ eckhard.say("Ty střevíce, které včera došil? Ty musíte najít! Rád pomůžu, jak jenom budu moct.")
        $ status.append("eckhard introductions")
    jump eckhardOptions


label leavingFriend:
    if "carrying key" in status:
        menu:
            "{i}(Donést klíč mistru Heinrichovi){/i}":
                jump victimHouseholdController
            "{i}(Vzít klíč k zámečníkovi){/i}" if "duplicate key" not in status:
                jump locksmith
            "{i}(Vrátit se na strážnici){/i}":
                return
    else:
        return

###

label forgottenKeyScene:
    "Eckhard se zamračí, sáhne si k pasu, kde asi čeká brašničku, ale nahmátne jen látku své haleny."
    $ eckhard.say("Počkej tady.")
    "Eckhard se vrátí do domu a po chvíli zase vyjde se zmateným výrazem a masivním klíče v ruce."
    $ eckhard.say("To jsem blázen… budu ho muset Heinrichovi vrátit.")
    show mcPic at menuImage:
    menu:
        "To byste asi měl.":
            hide mcPic
        "Můžu mu ho donést, pokud chcete.":
            hide mcPic
            $ eckhard.say("To mi pomůže, díky. Já bych tam došel, ale je mi dneska špatně…")
            $ status.append("carrying key")
    $ clues.append("forgotten key")
    $ time.addMinutes(10)
    return

label stolenIdea:
    $ eckhard.asked.append("stolen idea")
    $ mc.say("Velmi, vzhledem k tomu, že ty střevíce byly šité podle cizího nápadu.")
    $ eckhard.say("To je ale normální. Někdo něco zdokonalí, zbytek cechu to potom převezme a třeba ještě vylepší...")
    $ mc.say("Pokud se tvůrce nápadu nerozhodne nechat si ho jen pro sebe. Mistr Njal byl na ten svůj hrdý a nevím o tom, že by se o něj chtěl dělit.")
    $ eckhard.say("A to je právě ten problém! Heinrich je mnohem lepší švec než Njal. Ten nejlepší ve městě. Když se objeví náročné vylepšení, Heinrich by měl být ten, kdo tu věc opravdu ušije.")
    $ eckhard.say("Njal to taky nechápal...")
    return

label stolenIdeaConfession:
    hide mcPic
    $ eckhard.asked.append("stolen idea 2")
    $ eckhard.say("Já ho chtěl koupit. Nabídl jsem Njalovi poctivou cenu, ale on se nechtěl nechat přemluvit.")
    $ eckhard.say("A potom jsem jednou šel kolem jeho dílny, dveře byly otevřené jako obvykle a nikdo kolem nebyl… dokonalá příležitost, jasné pozvání od Einiona. Ten přece pomáhá těm, kdo si pomůžou sami.")
    $ eckhard.say("To jsem to měl ignorovat?")
    show mcPic at menuImage
    menu:
        "To by bylo podle zákona, ano.":
            hide mcPic
            $ rauvin.trust += 1
            $ eckhard.say("Zákon ale nepočítá s tím, že by si někdo střihy hamounil pro sebe. K čemu to pak je? Věci jsou od toho, aby se vyráběly.")
        "Chápu to pokušení, ale...":
            hide mcPic
            $ eckhard.say("Ale co? Hamounit střih pro sebe k ničemu není. Věci jsou od toho, aby se vyráběly.")
    $ eckhard.say("Kdybych prostě počkal, až to Njal vyrobí, a sehnal a přinesl Heinrichovi hotové boty, nikdo by ani neceknul. A přitom to je totéž. Rozdíl je jenom v tom, že by tím nemohl uctít Einiona na slavnostech.")
    $ eckhard.say("Pro Njala by měla být čest, že jeho nápad zpracuje někdo tak schopný, jako je Heinrich.")
    $ eckhard.say("Podívejte, vždyť to je jenom nákres. Njalovi tím přece nevznikla žádná škoda, ne? Mohl si to vždycky rozkreslit znovu.")
    $ eckhard.say("To je rozhodně mnohem méně práce než muset znovu vyrábět celé boty. Hlavní je chytit toho zloděje.")
    $ mc.say("Hlídka zkoumá všechny zločiny, které s těmi botami souvisí. Krádež je jen jeden z nich.")
    return

###

label locksmith:
    scene bg locksmith outside
    "Po chvíli hledání se ti podaří najít malý krámek se znakem dvou klíčů nade dveřmi a vejdeš dovnitř."
    scene bg locksmith inside
    "Hobit za pultem se na tebe zářivě usměje."
    $ locksmith.say("Co pro vás můžu udělat?")
    show mcPic at menuImage
    menu:
        "Potřeboval[a] bych duplikát tohoto klíče. Ideálně tak, abych tady nemusel[a] ten klíč dlouho nechat...":
            hide mcPic
            call duplicatingKey
        "Vlastně nic, jenom se tu rozhlížím.":
            hide mcPic
            $ locksmith.say("Kdyby vám něco padlo do oka, stačí říct.")
    scene bg locksmith outside
    jump leavingFriend

label duplicatingKey:
    "Zámečník pozvedne obočí, ale rychle zas nasadí svůj původní úsměv."
    $ locksmith.say("Samozřejmě, to nebude problém. Snad jen… můžu se zeptat, o co se jedná? Proč to tak spěchá?")
    $ mc.say("Jedná se o záležitost městské hlídky.")
    $ locksmith.say("Jistě. Jen… jistě máte od hlídky nějaké potvrzení, že? Pochopte, určitě také nechcete, aby se mohl za člena městské hlídky prohlásit kdokoli.")
    if "provisional watchman" in status:
        $ mc.say("Samozřejmě. Tady je moje pověření.")
        $ locksmith.say("To vypadá v pořádku… výborně, moc vám děkuji.")
    else:
        $ mc.say("Ve skutečnosti... jsem si ho zapomněl[a] vzít s sebou. A opravdu potřebuji pokračovat ve vyšetřování případu. Můžu vám své pověření ukázat až při převzetí toho duplikátu?")
        $ locksmith.say("To by asi mohlo být… dobře, tedy při převzetí. Ale budu vám velmi zavázán, když si na něj vzpomenete.")
    "Zámečník si od tebe vezme klíč od dílny mistra Heinricha a prohlédne si ho."
    $ locksmith.say("Výborně. Dejte mi chvilku na formu a do večera budete mít druhý klíč.")
    $ mc.say("Děkuji, večer se pro něj stavím.")
    $ status.append("duplicate key")
    $ time.addMinutes(15)
    return

###

label eckhardOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "when did they leave" not in eckhard.asked:
        $ optionsRemaining += 1
    if "coming home" not in eckhard.asked:
        $ optionsRemaining += 1
    if ("workshop unlocked" in clues or "forgotten key" in clues) and "no forced entry" not in eckhard.asked:
        $ optionsRemaining += 1
    if "anything suspicious" not in eckhard.asked:
        $ optionsRemaining += 1
    if kaspar.alreadyMet == True in status and "alcoholic" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea" in clues and "stolen idea" not in eckhard.asked and "stolen idea 2" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea" in victim.asked and "stolen idea" not in eckhard.asked and "stolen idea 2" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea" in eckhard.asked and "stolen idea 2" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea 2" in eckhard.asked and eckhard not in arrested:
        $ optionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea slip" in eckhard.asked and "stolen idea slip 2" not in eckhard.asked and "stolen idea" not in eckhard.asked:
        $ optionsRemaining += 1
    if "stolen idea slip 2" in eckhard.asked and "stolen idea 2" not in eckhard.asked:
        $ optionsRemaining += 1
    if "confession" in boysAsked and "defend the boys" not in eckhard.asked:
        $ optionsRemaining += 1
    if eckhard in cells and "crime and punishment" not in eckhard.asked:
        $ optionsRemaining += 1
    return
