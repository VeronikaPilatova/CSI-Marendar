label libraryPreparation:
    default literatureTopics = ["wellWrittenTrash", "farawayTravels", "fables", "saucyTales", "seriousHistory", "jakobVonDemSchloss", "elvenDragonLegend", "animalLore"]
    default lawTopics = ["lawIntro", "watch", "marketLaws"]
    default historyTopics = ["historyIntro", "history1", "history2", "history3", "history4", "history5", "history6", "history7"]
    default pastTrialsTopics = ["pastTrialsIntro", "pastTrialsAboutWatch", "cultistsTrial", "onionIncident"]
    return

label libraryController:
    call libraryIntro
    $ timeOfDay = time.timeOfDayInt()
    if chosenTopic != "":
        "Dnes jsi ale při[sel] za konkrétním účelem."
    else:
        call libraryOptions
    if chosenTopic != "leave":
        call expression chosenTopic
        call libraryRepeat

    $ chosenTopic = ""
    return

label libraryIntro:
    scene expression ("bg/bg library outside[time.locationTagExt()].png")
    if "library visited" not in status:
        if origin == "born here":
            "Marendarskou knihovnu si pamatuješ z dětství. Bývala to elegantní budova s vysokými policemi a studovnou, kde se dalo ztratit na dlouhé hodiny - nebo aspoň na tak dlouho, než tě někdo vyhnal zase ven."
            "Pamatuješ si na všeprostupující vůni papíru a kožených desek, pocit tepla a bezpečí, a především na laskavého knihovníka, který v tobě podporoval sny o lepším životě."
            "Tehdy jsi byl[a] přesvědčen[y], že se tam dá najít snad každá kniha na světě. A přestože stará knihovna nepřežila požár, který před dvěma lety město změnil téměř k nepoznání, určitě tu musela zbýt aspoň část jejího kouzla."
            scene expression ("bg/bg library inside[time.locationTagInt()].png")
            "Dnes knihovna dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito a i přes provizorní umístění je očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal[a], ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu zase celý den."
        else:
            "Marendar míval krásnou knihovnu s mnoha svazky, ale ta bohužel padla za oběť ničivému požáru města před dvěma lety. Na její obnovu v plné slávě se stále hledají prostředky a mnohem menší sbírka dnes dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito."
            scene expression ("bg/bg library inside[time.locationTagInt()].png")
            "I přes provizorní umístění je knihovna očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal[a], ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu celý den."
        $ status.append("library visited")
    else:
        scene expression ("bg/bg library inside[time.locationTagInt()].png")
        "Znovu tě přivítá příjemná vůně knih, a jak procházíš mezi regály, mladý elf, který tu vypomáhá, ti kývne na pozdrav."   
    if time.timeOfDayInt() == "night" and "library light seen" not in status:
        if time.timeOfDay() == "dusk":
            "Ačkoli venku už je šero, místnost je zalitá příjemným bílým světlem."
        else:
            "Ačkoli venku už je tma, místnost je zalitá příjemným bílým světlem."
        "Zvědavě se rozhlédneš po jeho zdroji a na jednom ze stolů najdeš malou sošku zpodobňující maják čelící hrozivým vlnám. Světlo zcela určitě vychází z ní, nejspíš přímo z vrcholku jeho věže. Nevidíš ale žádný plamen, ze sošky nestoupá ani drobný pramínek dýmu a světlo je stálé a neměnné, jako kdyby vycházelo z drahé svíce - na čtení mnohem příjemnější než nestálé mihotání loučí, s nímž ses mnohdy musel[a] spokojit."
        $ status.append("library light seen")
    return

label libraryRepeat:
    scene expression ("bg/bg library inside[time.locationTagInt()].png")

    if literatureTopics == [] and lawTopics == [] and pastTrialsTopics == [] and historyTopics == []:
        if not achievement.has(achievement_name['bookworm'].name):
            $ Achievement.add(achievement_name['bookworm'])

    call libraryOptionsRemaining
    if optionsRemaining == 0:
        "Vše přečteno"
        return
    if timeOfDay != time.timeOfDayInt():
        scene expression ("bg/bg library inside[time.locationTagInt()].png")
        if "library light seen" not in status:
            "Zatímco čteš, venku klesá slunce k obzoru a místnost se pomalu šeří. V okamžiku, kdy už se smiřuješ s tím, že budeš muset odejít, se však místnost zalije příjemným bílým světlem. Zvědavě se rozhlédneš po jeho zdroji a na jednom ze stolů najdeš malou sošku zpodobňující maják čelící hrozivým vlnám."
            "Světlo zcela určitě vychází z ní, nejspíš přímo z vrcholku jeho věže. Nevidíš ale žádný plamen, ze sošky nestoupá ani drobný pramínek dýmu a světlo je stálé a neměnné, jako kdyby vycházelo z drahé svíce - na čtení mnohem příjemnější než nestálé mihotání loučí, s nímž ses mnohdy musel[a] spokojit."
        $ timeOfDay = time.timeOfDayInt()
    elif time.hours > 21:
        call libraryClosingTime
        return

    call libraryOptions
    if chosenTopic == "leave":
        return
    else:
        call expression chosenTopic
        jump libraryRepeat

label libraryClosingTime:
    "Když konečně knihu odložíš a protáhneš se, knihovnický pomocník zachytí tvůj pohled a přejde k tobě."
    $ librarian.say("Omlouvám se, ale musím vás požádat, abyste ode[sel]. Připozdilo se a já tu musím uklidit a zamknout.")
    show mcPic at menuImage
    menu:
        "Moc se omlouvám, nevšiml[a] jsem si, jak je pozdě.":
            pass
        "Když to musí být…":
            pass 
        "Nemůžete počkat ještě chvíli?":
            pass 
    hide mcPic
    $ librarian.say("Zítra vás tu samozřejmě opět rád uvidím.")
    "Pomocník uloží poslední knihu zpět do police a vyprovodí tě ke dveřím."
    scene expression ("bg/bg library outside[time.locationTagExt()].png")
    $ librarian.say("Pěkný večer a zase se vraťte!")
    "Čerstvý vzduch je po sezení nad knihou příjemný a je díky němu snazší si rozmyslet další postup."
    return

label libraryOptions:
    call lawConsultationOptionsRemainingCheck
    menu:
        "{i}(“Půjčit” si vhodnou báseň pro Zairise){/i}" if "promised poetry" in status and not any("poem" in str for str in status):
            $ chosenTopic = "stealPoetry"
        "{i}(Zkonzultovat styl básní pro Adu){/i}" if "letters for Ada seen" in status and "poetry style" not in librarian.asked and "letters for Ada checked in library" not in status:
            $ chosenTopic = "libraryConsultLettersForAda"
        "{i}(Zeptat se na sečtělé elfy){/i}" if "lover well read" in ada.asked and "well-read elves" not in librarian.asked:
            $ chosenTopic = "libraryConsultWellReadElves"
        "{i}(Požádat o právní konzultaci){/i}" if "law consultation offered" in status and lawConsultationOptionsRemaining > 0:
            $ chosenTopic = "libraryConsultLaw"
        "{i}(Promluvit si s elfím knihovníkem){/i}" if librarian.alreadyMet:
            $ chosenTopic = "librarianOptions"
        "{i}(Odpočinout si při čtení krásné literatury){/i}" if literatureTopics != []:
            $ chosenTopic = "readingLiterature"
        "{i}(Nastudovat si právo a místní zákony){/i}" if lawTopics != []:
            $ chosenTopic = "readingLaw"
        "{i}(Projít zápisy soudních procesů){/i}" if pastTrialsTopics != []:
            $ chosenTopic = "readingPastTrials"
        "{i}(Nastudovat si městskou historii){/i}" if historyTopics != []:
            $ chosenTopic = "readingHistory"
        "{i}(Vrátit se na strážnici){/i}":
            $ chosenTopic = "leave"
    return

###

label librarianOptions:
    show mcPic at menuImage
    menu:
        "Máte přehled i v tom, kdo ve městě píše?" if chosenTopic == "anythingElse" and "letters for Ada seen" in status and "poetry style" not in librarian.asked and "letters for Ada checked in library" not in status:
            $ librarian.asked.append("poetry style")
            call libraryConsultLettersForAda1Response
        "Spíš se chci poradit, mám tady báseň a hledám jejího autora." if chosenTopic == "anythingElse" and ("poem for Ada copied" in status or "all love letters kept" in status or "one love letter kept" in status) and "poetry style" not in librarian.asked and "letters for Ada checked in library" not in status:
            $ librarian.asked.append("poetry style")
            call libraryConsultLettersForAda2Response
        "Jak dobře znáte návštěvníky knihovny?" if chosenTopic == "anythingElse" and "lover well read" in ada.asked and "well-read elves" not in librarian.asked:
            call libraryConsultWellReadElvesResponse
        
        # law consult
        "Jaké má vlastně hlídka pravomoce? Koho můžu zatknout nebo naopak pustit z cely?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "watch powers" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("watch powers")
            $ librarian.say("V první řadě by se hlídka neměla pouštět do vlastních podniků. Pokud přijde stížnost od někoho z města, je potřeba se jí samozřejmě věnovat, ale co si měšťané dokážou vyřešit sami mezi sebou, do toho hlídka nemá vstupovat.")
            $ librarian.say("I pokud máte o nějakém zločinu nezvratné důkazy, je lepší se nejdříve dohodnout s obětí, jestli o zapojení hlídky stojí. Někdy lidé nechtějí, aby se věc veřejně propírala.")
            $ librarian.say("Většina obětí, svědků i pachatelů žije v tomto městě a nikam neuteče, často tedy ničemu neublíží pár dní počkat a nejdříve si zjistit všechno potřebné.")
            $ librarian.say("Co se týče zatýkání, hlídka má právo zatknout kohokoli a ani myslím není stanovená nejvyšší možná délka zadržení. Nicméně každé zatčení budete muset zdůvodnit městské radě a ta může v případě potřeby vězně zase propustit. Nedostatečně podložené zatčení by pak podlomilo důvěru města v hlídku.")
            $ librarian.say("S propouštěním je to podobné. Hlídka může kdykoli propustit kteréhokoli svého vězně, ale mělo by být jasné, co se od chvíle zatčení změnilo, jinak měšťané v její činnost ztratí důvěru.")
            $ librarian.say("Stejně tak pravděpodobně vyvolá otázky, pokud k propuštění dojde těsně před soudním přelíčením. Ale nevybavuji si zákon, který by to přímo zakazoval.")
        "Chtěl[a] bych si udělat představu o trestech, které by mohly padnout u soudu." if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishments")
            $ librarian.say("To samozřejmě záleží na tom, kdo by byl souzen a co spáchal.")
        "Co kdyby boty mistra Heinricha ukradl nebo zničil jiný mistr?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "punishment for theft - master craftsman" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for theft - master craftsman")
            $ librarian.say("To by nejspíš hodně pošpinilo jeho pověst a to by byl ten nejhorší trest. Kdo by si pak u něj nechal šít?")
            $ librarian.say("Myslím, že by se soud snažil, aby z toho pachatel vyšel se ctí, aby nezpůsobil dlouhodobou zlou krev. Mohl by mu třeba uložit zaplatit mistru Heinrichovi odškodné a dát hodnotný dar Einionově chrámu.")
            $ librarian.say("A hlavně by mu domluvili, aby se nic podobného neopakovalo, a kdyby přitom přišli na nějakou hlubší příčinu, snažili by se ji nějak odstranit. Třeba udobřit mistry, pokud se nenávidí. Město na svých mistrech stojí a rozbroje mezi nimi nikomu nepomohou.")
            $ librarian.say("Samozřejmě by se nejspíš ozývaly hlasy, že teď přece máme to nové právo, které měří všem stejně, a že by trest měl být tvrdší. Co si o tom myslíte, nechám na vás, moc soudů takto po novu zatím neproběhlo. Já sám pochybuji, že se něco výrazně změní.")
        "Co kdyby boty mistra Heinricha ukradl nebo zničil někdo chudý?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "punishment for theft - poor person" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for theft - poor person")
            $ librarian.say("To bych si nepřál být na jeho místě a vy také ne.")
            $ librarian.say("Ono se teď samozřejmě všude říká, jak máme to nové právo, které měří všem stejně. Kdo chce, ať tomu věří. Já si myslím, že by mistr Heinrich zdůrazňoval, jak cenný a neobyčejný ten výrobek byl a jak odporné je krást dar pro Einiona, aby se patřičně pomstil.")
            $ librarian.say("Tomu všemu by soud nejspíš uvěřil. Mistr Heinrich má pověst velmi schopného řemeslníka.")
            $ librarian.say("Očekával bych nějakou dlouhou službu, aby si zloděj ten přečin odpracoval, nebo naopak vyhnání z města. Podle toho, jestli by tu po něm zůstala rodina a podobně.")
            $ librarian.say("A k tomu nejspíš pranýř a rány holí. Prostě trest, který může očekávat chuďas, který rozhněval někoho důležitého.")
        "Co kdyby boty mistra Heinricha ukradl nebo zničil někdo z jeho učedníků?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "shoes' fate" in clues and "punishment for theft - apprentice" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for theft - apprentice")
            $ librarian.say("Tak hloupí přece být nemohou?", "surprised")
            $ librarian.say("V první řadě bych čekal, že mistr Heinrich toho učedníka okamžitě vyžene z domu a z učení. Vzhledem k tomu, že za učení se platí předem a peníze by asi nevrátil, mohlo by být pro učedníka obtížné se vyučit někde jinde.")
            $ librarian.say("Zvlášť s pověstí někoho, kdo kradl v domě svého mistra.")
            $ librarian.say("Nezapomínejte také na to, že dokud je někdo v učení, podléhá mistrovi a ten ho může trestat jako vlastní rodinu. Heinrich by tedy ani nemusel chodit za hlídkou. Ve skutečnosti by tím naopak mohl být za slabocha, co si neumí ve vlastním domě zjednat pořádek.")
            $ librarian.say("Ale co vím o mistru Heinrichovi, ten se rozdávat rány nebojí.")
        "Co může hrozit za krádež ševcovského střihu?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "stolen idea" in clues and "punishment for theft of shoe pattern" not in librarian.asked:
            hide mcPicx 
            $ librarian.asked.append("punishment for theft of shoe pattern")
            $ librarian.say("Vždy je nutné vrátit kradenou věc nebo zaplatit odpovídající obnos a většinou ještě nějaké penále navíc jako odškodné. K tomu soud většinou udělí dodatečnou pokutu ve prospěch města nebo nějaký čas v pranýři, aby byl trest horší než zisk z případné úspěšné krádeže.")
            $ librarian.say("Pokud byl čin obzvlášť závažný, je možné trestat cejchem, nebo dokonce utnutím ruky, ale nepamatuji si, kdy se něco podobného stalo. K podobným trestům i Velin přistupoval zřídka.")
            $ librarian.say("Vy jste ale zmiňoval[a] krádež střihu na boty? Co já vím, ty nemají skoro žádnou cenu, ševci je znají a neševcům nejsou k ničemu dobré. Myslím, že to by zůstalo bez trestu, stejně jako by vás nikdo nepotrestal, kdybyste někomu vypil vodu ze džbánu kousek od plné studny.")
        "Jaký trest by byl třeba za vloupání?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "duplicate key" in status and "punishment for burglary" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for burglary")
            $ librarian.say("To záleží, jestli během vloupání došlo i k napadení někoho z obyvatel, kolik toho bylo ukradeno a jestli byl čin plánovaný, nebo jen výsledkem náhlého popudu.")
            $ librarian.say("V nejlehčím případě, kdy někdo uvidí otevřené dveře a sebere někomu ze stolu drahý svícen a pak si to viditelně vyčítá, by nejspíš stačila domluva, možná spojená s peněžitým trestem.")
            $ librarian.say("Naopak připravený zlovolný čin spojený s napadením může být potrestán až popravou nebo alespoň tělesným trestem a vyhnáním.")
            $ librarian.say("Také je potřeba vzít v úvahu, že vyhnání je těžkým trestem pro usedlíky, ale nic neznamená pro cizince. Ti by místo toho byli potrestaní jinak. Buď naopak zákazem odejít, dokud nezaplatí vysokou pokutu, nebo na těle či na hrdle.")
        "Co kdyby se někomu úplně obyčejnému přišlo na vydírání?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and "AML" in lotte.asked and "punishment for blackmail" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for blackmail")
            $ librarian.say("Na to nejsou tresty pevně ustanovené. K vydírání nedochází často, nebo aspoň ne k takovému, které se potom dostane k soudu.")
            $ librarian.say("Myslím, že by hodně záleželo na tom, k čemu to vydírání mělo směřovat.")
            $ librarian.say("Jestli byl viditelně ohrožen něčí život nebo zdraví, dokážu si představit i těžký tělesný trest nebo popravu, pokud by se samozřejmě soudu nepodařilo nějak dosáhnout usmíření všech zúčastněných. Pak by pachatel nejspíš jen zaplatil nějakou pokutu.")
            $ librarian.say("V méně vážných případech by nejspíš zůstalo u pranýřování. Ostuda a ztráta tváře by byla největším trestem sama o sobě.")
        "Co hrozí té tanečnici s ohněm?" if (chosenTopic == "libraryConsultLaw" or (chosenTopic == "anythingElse" and "law consultation offered" in status)) and "punishments" in librarian.asked and time.days > 1 and "punishment for Katrin" not in librarian.asked:
            hide mcPic
            $ librarian.asked.append("punishment for Katrin")
            $ librarian.say("Zrovna té hrozí skoro všechno, co jen dokáže někdo vymyslet.")
            $ librarian.say("Důležité bude, jestli soud její čin bude považovat za neopatrnost, nebo za úmyslné žhářství. Už neopatrné zacházení s ohněm se podle marendarských zákonů považuje za ohrožení celého města, které se může velmi snadno trestat oběšením.")
            $ librarian.say("Tam je ještě naděje na zmírnění rozsudku. Soud by mohl přihlédnout k tomu, že je mladá a že jako cizinka neznala dobře naše zákony. Nicméně když jde o oheň, neočekával bych větší zmínění trestu než na ten nejtěžší, který ještě neznamená popravu.")
            $ librarian.say("A jestli její čin soud vyhodnotí jako žhářství… myslím, že bude chtít vynést rozsudek, který bude mít výrazně odstrašující povahu.")
            $ librarian.say("Samozřejmě pokud soud naopak sezná, že její jednání město nijak neohrožovalo, potom ta dívka vyvázne bez úhony. Na to bych ale nesázel, pokud se nenajde někdo, kdo bude mluvit v její prospěch.")

        # talk with

        "Děkuji, moc jste mi pomohl, víc vás nebudu zdržovat.":
            hide mcPic
            $ librarian.say("To je v pořádku, od toho tu jsem.")
            return
    
    jump librarianOptions

###

label stealPoetry:
    scene bg books
    "Najdeš regál s poezií a po chvíli procházení vezmeš do ruky útlou knihu básní. Se jménem autora ses ještě nesetkal[a], ale většina básní uvnitř mluví o citech nebo pracuje s přírodními motivy. Opíšeš si náhodnou z nich a doufáš, že na Zairise udělá dostatečně dobrý dojem."
    scene expression ("bg/bg library inside[time.locationTagInt()].png")
    show expression ("sh stolen poem [race].png") at truecenter
    pause
    hide expression ("sh stolen poem [race].png") at truecenter
    $ status.append("poem stolen")
    $ time.addMinutes(20)
    return

label libraryConsultLettersForAda:
    $ librarian.asked.append("poetry style")
    "Luisa de Vito tu dnes není, snadno ale najdeš mladého elfa, který jí v knihovně vypomáhá."
    $ librarian.say("Co pro vás můžu udělat? Hledáte nějaký svazek?")
    show mcPic at menuImage
    menu:
        "Máte přehled i v tom, kdo ve městě píše?":
            label libraryConsultLettersForAda1Response:
            hide mcPic
            $ librarian.say("Myslíte knihy k vytištění? Skoro nikdo. Přeci jen, nechat natisknout knihu není levná záležitost.")
            $ librarian.say("Zhruba před rokem se tady v Marendaru tiskla sága o jednom trpasličím runovém kováři, ale ani ta nebyla původně napsaná přímo tady ve městě. My sami jsme sepsali jen několik smolných knih a výtisků nových zákonů, aspoň co si pamatuji.")
            $ librarian.say("Tedy, myslím, že Valeran z hlídky - té části, která hlídá brány, asi se s ním nebudete moc potkávat - sepisuje něco o historii, ale jestli z toho někdy bude kniha, těžko říct.")
            $ librarian.say("Ostatní knihy, které tu máme, jsme většinou dovezli z jiných měst.")
            show mcPic at menuImage
            menu:
                "Děkuji, to byl vyčerpávající přehled.":
                    hide mcPic
                    $ librarian.say("Rádo se stalo. Potřebujete ještě něco?")
                    $ chosenTopic = "anythingElse"
                    jump librarianOptions
                "Je možné, že ten, koho hledám, píše básně jen pro sebe a pro přátele.":
                    hide mcPic
                    $ librarian.say("To se potom bohužel nemám, jak dozvědět. Za mnou se svými básněmi nikdo nechodí.")
                    $ mc.say("Nemáte alespoň odhad, kdo by něco takového mohl psát?")
                    $ librarian.say("Upřímně, to může být skoro kdokoli. I někdo, do koho by to jeden neřekl, může občas složit třeba nějakou milostnou báseň, neslušnou říkanku nebo výsměšnou rýmovačku. A když už je vymyslí, jistě že si je zapíše, byla by škoda je zapomenout.")
        "Spíš se chci poradit, mám tady báseň a hledám jejího autora." if "poem for Ada copied" in status or "all love letters kept" in status or "one love letter kept" in status:
            label libraryConsultLettersForAda2Response:
            hide mcPic
            $ librarian.asked.append("poem for Ada shown")
            $ librarian.say("Můžu se pokusit. Samozřejmě neznám zpaměti všechny knihy, které tu máme, ale přečetl jsem toho dost.")
            "Elf si od tebe vezme papír s básní a po chvilce zavrtí hlavou."
            $ librarian.say("Bohužel. Tuhle báseň neznám. Jsem si skoro jistý, že není z žádné knihy, kterou tady máme.")
            $ librarian.say("Odkud ji máte? Třeba by mi to napovědělo.")
            show mcPic at menuImage
            menu:
                "Dostala ji dcera mistra Heinricha od svého tajného ctitele.":
                    hide mcPic
                    $ librarian.say("A vy s mojí pomocí chcete onoho ctitele vypátrat? To musím odmítnout.")
                    $ librarian.say("Nemám takový přehled o tvorbě všech ve městě, abych si byl odpovědí zcela jistý, a nechtěl bych někoho neprávem uvést do potíží.")
                    $ librarian.say("Mohlo by to uvrhnout špatné světlo na knihovnu a to by paní Luisa nesnesla.")
                    show mcPic at menuImage
                    menu:
                        "To chápu, nebudu naléhat.":
                            hide mcPic
                            $ librarian.say("V pořádku. Mohu vám pomoci nějak jinak?")
                            $ chosenTopic = "anythingElse"
                            jump librarianOptions
                        "Ten ctitel je pokrytec, který si potíže zaslouží.":
                            hide mcPic
                            $ mc.say("Nechal za sebe potrestat někoho nevinného.")
                            $ librarian.say("I pokud to tak je, tak to, pokud vím, není zločin. Pořád nerozumím, proč se o to hlídka zajímá.")
                            $ librarian.say("Mohu vám pomoci nějak jinak?")
                            $ chosenTopic = "anythingElse"
                            jump librarianOptions
                        "Naopak, je to způsob, jak někomu hodně pomoct.":
                            hide mcPic
                            $ mc.say("Heinrich za autora považuje svého bývalého učedníka, kterého kvůli tomu vyhnal. Já se snažím očistit jeho jméno.")
                            $ librarian.say("Ach tak. Souhlasím, že být připraven o budoucnost jen kvůli klamnému dojmu si nikdo nezaslouží.", "angry")
                            "Elf si znovu přečte báseň a na chvíli se zamyslí."
                            $ librarian.say("Nejsem si dokonale jistý, ale podobné sonety myslím píše Zairis. Aspoň těch pár, co mi ukazoval, tomu vlastně dost odpovídaly.")
                            $ mc.say("Děkuji, moc jste mi pomohl.")
                            $ status.append("letters for Ada checked in library")
                "Někdo mi ji nechal za oknem.":
                    hide mcPic
                    $ librarian.say("A nebude potom vhodnější dát za to okno odpověď? Myslím, že by ani nemusela být veršovaná.", "surprised")
                    $ mc.say("Jak mám ale vědět, co za odpověď psát, když neznám autora?")
                    $ mc.say("Nechci hned takhle na začátek udělat chybu…")
                    $ librarian.say("...", "surprised")
                    $ librarian.say("No, ostatně mi do toho nic není a tohle je aspoň zajímavá otázka.", "happy")
                    "Elf si znovu přečte báseň a na chvíli se zamyslí."
                    $ librarian.say("Nejsem si dokonale jistý, ale podobné sonety myslím píše Zairis. Aspoň těch pár, co mi ukazoval, tomu vlastně dost odpovídaly.")
                    $ mc.say("Děkuji, moc jste mi pomohl.")
                    $ status.append("letters for Ada checked in library")
                    if gender =! "F" or race =! "elf":
                        $ librarian.say("Ale jestli by zrovna vám dával na okno báseň… jste si jist[y], že to bylo pro vás?", "surprised")
                        $ librarian.say("Ale to mi nepřísluší soudit.")
                    "Knihovník se krátce zamyslí." 
                    $ librarian.say("Počkejte… ne, to nebude on. Sice zřejmě zamilovaný je a cíl svého citu tají, ale už to trvá nějakou dobu a prý se snad několikrát setkali. Jestli chápu správně, to na vás nesedí.")
                "To bohužel nemůžu říct. Je to součástí případu, který v městské hlídce vyšetřujeme.":
                    hide mcPic
                    $ librarian.say("Skutečně? A proč se prosím hlídka zajímá o milostný život obyvatel města?", "surprised")
                    $ mc.say("Potřeboval[a] bych s autorem té básně mluvit, to je celé.")
                    $ librarian.say("Ale z jakého důvodu, to už říct nemůžete.")
                    $ librarian.say("Pak já zase nemůžu říct nic, čím bych si byl dokonale jistý. Nemám takový přehled o tvorbě všech ve městě a nechtěl bych někoho neprávem uvést do potíží.", "angry")
                    $ librarian.say("Mohlo by to uvrhnout špatné světlo na knihovnu a to by paní Luisa nesnesla.")
                    $ librarian.say("Čím si ale jistý jsem, je, že psát milostnou poezii není zločin, bez ohledu na její kvalitu.")
                    $ librarian.say("Ne, že by zrovna tato báseň nebyla pěkná.")
                    $ librarian.say("Mohu vám pomoci nějak jinak?")
                    $ chosenTopic = "anythingElse"
                    jump librarianOptions
    return

label libraryConsultWellReadElves:
    "Luisa de Vito tu dnes není, snadno ale najdeš mladého elfa, který jí v knihovně vypomáhá."
    $ librarian.say("Co pro vás můžu udělat? Hledáte něco konkrétního?")
    $ mc.say("Spíš bych potřeboval[a] radu. Jak dobře znáte návštěvníky knihovny?")
    label libraryConsultWellReadElvesResponse:
    $ librarian.asked.append("well-read elves")
    $ librarian.say("Určitě neznám všechny, ale pravidelné čtenáře celkem dobře. Mnoho z nich i pomáhalo s obnovou knihovny.")
    $ librarian.say("Proč se ptáte?")
    show mcPic at menuImage
    menu:
        "Mohlo by to souviset s mým případem.":
            hide mcPic
            $ librarian.say("No dobrá, co tedy potřebujete vědět?")
            $ mc.say("Potřebuji určit totožnost jednoho elfa. Vím, že je mladý a velmi rád chodí číst do knihovny. Nejčastěji zřejmě poezii a spisy o historii.")
            $ librarian.say("Úplně nejčastěji tady bývá Kaderyn. Je chudák vážně nemocný a čtení je jedna z mála věcí, na kterou má sílu.")
            $ mc.say("Ten můj elf byl jednou u Amadisova hrobu, to by Kaderyn zvládl?")
            $ librarian.say("Rozhodně ne. V tom případě váš muž bude Zairis. Syn obchodníka Roviena. Občas s otcem cestuje, takže ten se k hrobu velmi snadno mohl dostat. A přečetl tu už také skoro všechno.")
            $ mc.say("Jste si jistý, že by tomu popisu nemohl odpovídat ještě někdo další?")
            $ librarian.say("Pokud má jít opravdu o velkého čtenáře, pak ano. Chodí sem samozřejmě větší množství čtenářů, ale ostatní se zajímají o jiné žánry, nejsou to elfí mladíci nebo nejsou zdaleka tak zapálení.")
            $ clues.append("zairis")
        "Rád[a] bych se seznámil[a] s někým s podobnými zájmy.":
            hide mcPic
            $ librarian.say("Potom asi záleží, jaký druh literatury vás zajímá. Někdo sem chodí studovat zákony, někdo kroniky, někdo se zajímá o náboženské spisy…")
            show mcPic at menuImage
            menu:
                "Zajímají mě hlavně zákony.":
                    hide mcPic
                    $ librarian.say("Myslím, že o těch si úplně nejlépe pohovoříte s panem de Vito. Nebo můžete někdy večer zajít k výčepu, jak se teď leccos mění, bývá to tam obvyklé téma hovoru.")
                    $ librarian.say("Tady v knihovně po nich taková poptávka nebývá.")
                    $ librarian.say("Nebo jsem tady ještě já, pokud nevyžadujete někoho, kdo má postavení nebo uznání.")
                    $ librarian.say("Já jsem touhle dobou mohl být právník, kdyby…", "angry")
                    if "law consultation offered" not in status:
                        call librarianLawConsultationOffered2
                "Chtěl bych studovat historii.":
                    hide mcPic
                    $ librarian.say("Potom zajděte za Valeranem, který pracuje v hlídce jako jeden ze strážných u brány. O historii toho ví hodně a co vím, rád o ní bude mluvit s kýmkoli.")
                "Chci se víc ponořit do otázek víry a bohů.":
                    hide mcPic
                    $ librarian.say("Ve skutečnosti tu máme hlavně různé mravoučné příběhy a bajky, učené teologie jen pomálu.")
                    $ librarian.say("Jestli to je to, co vás zajímá, zkuste ševcovou Lisbeth. Není jediná, kdo podobné příběhy čte, ale je přátelská a věřím, že s vámi ráda bude mluvit. Na další čtenáře vás pak třeba odkáže ona nebo se mě zeptáte znovu.")
                "Chci vědět co nejvíc o cizích krajích.":
                    hide mcPic
                    $ librarian.say("To tady hltá kdekdo. Takovou Adu od ševců už sem její rodiče ani nechtějí pouštět, protože se bojí, že jí nějaký cestopis ještě víc zamotá hlavu.")
                    $ librarian.say("Za mě lepší číst cestopisy než nečíst vůbec jako pan otec, ale kdo jsem, abych se do toho vměšoval.", "angry")
                    $ librarian.say("Další nadšenec je Zairis, ten už všechny cestopisy přečetl nejméně třikrát.")
                    $ librarian.say("Ale ten tedy čte skoro cokoli. Dokonce i ty olwenitské mravoučné příběhy všechny přečetl, ačkoli lidské bohy neuctívá a pokaždé si pak stěžoval, že když byl olwenitským rytířem Amadis, určitě měl na čtení něco mnohem kvalitnějšího.")
                    $ clues.append("zairis")
                "Nejvíc mě baví něco hrdinského a dobrodružného.":
                    hide mcPic
                    $ librarian.say("To bývá velmi oblíbené. Největší odborník na ně je nejspíš Zairis. Zvlášť jestli vás zajímá Amadis, moc rád o něm s vámi bude básnit, ale raději si na to vyhraďte dost času.")
                    $ clues.append("zairis")
                "Zajímám se o poezii.":
                    hide mcPic
                    $ librarian.say("Největší nadšenec do poezie je jednoznačně Zairis. Četl už všechno, co tu máme, a neustále se ptá, kdy seženeme něco dalšího.")
                    $ librarian.say("Dokonce i sám píše, a co mohu soudit, dost slušně, ačkoli se s tím veřejně moc nechlubí. Určitě bude rád, jestli s ním budete ochotn[y] o poezii diskutovat.")
                    $ clues.append("zairis")
                    if ("poem for Ada copied" in status or "all love letters kept" in status or "one love letter kept" in status) and "poem for Ada shown" not in librarian.asked:
                        show mcPic at menuImage
                        menu:
                            "Myslíte, že by tahle báseň mohla být jeho?":
                                hide mcPic
                                $ librarian.say("Nevím. Rozhodně ji neznám. Kde jste k ní při[sel]?")
                                $ mc.say("To je dlouhá historie, obávám se.")
                                $ librarian.say("Chápu, známe umělce…")
                                "Knihovník chvíli báseň zamyšleně studuje."
                                $ librarian.say("Vlastně ano, myslím, že by to mohlo být od něj. Nemůžu to samozřejmě vědět s jistotou, ale jeho styl mi připomíná nejvíc.")
                                $ librarian.say("Rozhodně to není z žádného svazku, co bychom měli tady v knihovně.")
                                $ librarian.say("Takže jestli vám někdo tvrdil, že to je nesmírně cenný rukopis od někoho slavného… nejspíš tomu tak nebude.")
                                $ status.append("letters for Ada checked in library")
                            "Děkuji, moc jste mi pomohl.":
                                hide mcPic
                                $ librarian.say("Rádo se stalo. Potřebujete ještě něco?")
                                $ chosenTopic = "anythingElse"
                                jump librarianOptions
    $ mc.say("Děkuji, moc jste mi pomohl.")
    $ librarian.say("Rádo se stalo. Potřebujete ještě něco?")
    $ chosenTopic = "anythingElse"
    jump librarianOptions

label libraryConsultLaw:
    jump librarianOptions

label librarianLawConsultationOffered:
    "Když zvedneš hlavu, všimneš si mladého knihovníka, který tě se zaujetím pozoruje."
    $ librarian.say("Zajímáte se o právo?")
    show mcPic at menuImage
    menu:
        "Nedávno jsem nastoupil[a] do městské hlídky, tak se snažím zorientovat v zákonech.":
            hide mcPic
            $ librarian.say("Samozřejmě, hlídka by měla vědět, kde je její místo. A co má za úkol.")
        "Ano, fascinuje mě, jak se vyvíjí.":
            hide mcPic
            $ librarian.say("Tak velké změny to zase nejsou.", "angry")
    label librarianLawConsultationOffered2:
    $ librarian.say("Já jsem touhle dobou mohl být právník, kdyby…", "angry")
    "Knihovník pokrčí rameny, ale lhostejně to nepůsobí ani trochu."
    show mcPic at menuImage
    menu:
        "Ale nejsi?":
            hide mcPic
            $ librarian.say("Byl bych, kdyby byl svět spravedlivý. Ale znalosti a schopnosti bez známostí očividně neznamenají nic.", "angry")
        "Můžu nějak pomoct?":
            hide mcPic
            $ librarian.say("Vy asi těžko, pokud nemáte známé na dost vysokých místech.", "sad")
            $ librarian.say("I když… se soudcem určitě do styku přijdete…")
        "{i}(neříct nic){/i}":
            hide mcPic
    "Mladý elf se na tebe zkoumavě podívá."
    $ librarian.say("Možná bychom si mohli pomoct vzájemně. Pokud by se vám někdy v oblasti zákonů hodila konzultace, rád vám budu k dispozici. A vy se pak můžete o mé pomoci zmínit vašim nadřízeným nebo rovnou u soudu.")
    show mcPic at menuImage
    menu:
        "Děkuji, určitě na to budu myslet.":
            hide mcPic¨
            "Knihovník se na tebe usměje a pak se vrátí ke své práci."
        "To by nemělo být nutné.":
            hide mcPic
            $ librarian.say("Uvidíte. V každém případě víte, kde mne najít.")
    $ status.append("law consultation offered")
    return

### reading
label readingLiterature:
    $ readingTopic = renpy.random.choice(literatureTopics)
    $ library.checked.append("literature " + readingTopic)
    $ literatureTopics.remove(readingTopic)
    scene bg books
    call expression readingTopic
    $ time.addMinutes(40)
    if literatureTopics != [] and time.hours <= 21:
        menu:
            "Pokračovat":
                jump readingLiterature
            "Přestat se čtením":
                pass
    return

label readingLaw:
    if "lawIntro" in lawTopics:
        $ readingTopic = "lawIntro"
        if "law consultation offered" not in status:
            call librarianLawConsultationOffered
    else:
        $ readingTopic = renpy.random.choice(lawTopics)
    $ library.checked.append(readingTopic)
    $ lawTopics.remove(readingTopic)
    scene bg books
    call expression readingTopic
    $ time.addMinutes(40)
    if lawTopics != [] and time.hours <= 21:
        menu:
            "Najít si k pravomocem hlídky ještě soudní zápisy" if readingTopic == "watch" and "pastTrialsAboutWatch" not in library.checked:
                $ readingTopic = "pastTrialsAboutWatch"
                jump readingPastTrials
            "Pokračovat":
                jump readingLaw
            "Přestat se čtením":
                pass
    return

label readingPastTrials:
    if readingTopic not in pastTrialsTopics:
        $ readingTopic = pastTrialsTopics[0]
    $ library.checked.append(readingTopic)
    $ pastTrialsTopics.remove(readingTopic)
    scene bg books
    call expression readingTopic
    $ time.addMinutes(40)
    if pastTrialsTopics != [] and time.hours <= 21:
        menu:
            "Pokračovat":
                jump readingPastTrials
            "Přestat se čtením":
                pass
    return

label readingHistory:
    if "historyIntro" in historyTopics:
        "Oficiální marendarská kronika sídlí na radnici, kde ji má ve správě městský písař. To byla ostatně tvá první zastávka během hledání práce. Paní Luisa ale pro svou knihovnu nechala pořídit opis, a tak se můžeš seznámit s historií města bez přísného písařova dohledu."
        $ historyTopics.remove("historyIntro")
    $ readingTopic = historyTopics[0]
    $ library.checked.append(readingTopic)
    $ historyTopics.remove(readingTopic)
    scene bg books
    call expression readingTopic
    $ time.addMinutes(40)
    if historyTopics != [] and time.hours <= 21:
        menu:
            "Pokračovat":
                jump readingHistory
            "Přestat se čtením":
                pass
    return    

### random books and lore
### literature
label wellWrittenTrash:
    "Ze své volby se cítíš trochu rozpačitě. Mohlo tě asi napadnout, že “příběhy k poučení” budou klást důraz hlavně na kázání o morálce před zajímavostí zápletky. Tuto knihu ale napsal kněz Einiona, boha všech řemeslníků a umělců - a autor, nutno přiznat, byl v řemesle skládání vět dobře zběhlý."
    "Než si uvědomíš, jak hloupý děj většiny příběhů je, máš už za sebou notný kus knihy a až zpětně si uvědomíš, že tě ze sezení ve strnulé poloze bolí záda."
    return
label farawayTravels:
    "O mnoha kněžích Olwena se říká, že jen sedí ve svých chrámech a pobírají desátky a že tak by uctívání boha cesty vypadat nemělo. Ignáce z Mardenu z něčeho podobného ovšem rozhodně nelze obviňovat."
    "Jestli lze jeho cestopisu věřit, viděl snad víc moří a přešel víc pohoří, než kolik běžný člověk dokáže vyjmenovat měst - a že jich každý tovaryš pozná pěknou řádku, když chodí na zkušenou."
    "Ignácovo vyprávění je plné poutavých popisů cizích krajů. Lidé s čepicemi ze stočené látky, které vypadají trochu jako ulity některých korýšů, obrovská jízdní zvířata s pěti nohama, hrbatí koně, pálenka z koňského mléka, neuvěřitelně dlouhý seznam překvapení, která se všechna dají najít na jednom jediném světě."
    "Jako písaře tě navíc zaujme, jakou váhu má v některých zemích kaligrafické umění. Kdyby tomu tak bylo i zde, mohl tvůj život možná vypadat jinak. Takto musíš knihu brzy opět zavřít a vrátit se do Marendaru."
    return
label fables:
    "Zalistuješ útlou knihou bajek a neubráníš se úsměvu. Je to spíš levný výtisk na nepříliš drahém papíře, ale jsou tu všechny příběhy, které znáš velmi dobře z dětství. Jak liška lstí připravila havrana o kořist, jak se liška s čápem navzájem pozvali na večeři, jak se pes chtěl servat se svým odrazem v řece a přišel o kořist, o vychytralém oslu, kterému se nechtělo nosit náklad..."
    "Než tě kratičká jednoduchá vyprávění omrzí, jsi skoro na konci knihy."
    return
label saucyTales:
    "Pro odreagování sis vybral[a] knihu zábavných příběhů a začetl[a] se do vyprávění o manželovi, který pro neustálé modlení zapomínal na své manželské povinnosti, a jak ho chytrý kněz dostal z domu a užil si s manželkou sám."
    "V druhém příběhu se sluha zamiluje do ženy svého pána a domluví si s ní tajné dostaveníčko. Paní ale tuší, že její žárlivý manžel by mohl mít podezření. Radši mu proto poví, k čemu se ji jeho služebník snažil přesvědčit, a aby ho mohl potrestat, pošle manžela čekat na něj v jejím oděvu."
    "Milenci si spolu užijí a hned na to jde sluha do zahrady 'dát za vyučenou' své nevěrné paní - tedy ve skutečnosti jejímu manželovi v šatech své ženy. Manžel se tak dostatečně přesvědčí o věrnosti své ženy i svého služebníka a ti dva se spolu můžou dál tajně scházet."
    "Když se dostaneš ke třetímu příběhu o mladíkovi, kterému hrozí smrt láskou, pokud se mu nepodaří strávit aspoň jednu noc s vdanou dámou svého srdce, nedá ti to a prolistuješ zbytek knihy."
    "I ostatní vyprávění se nesou v podobném duchu, samí záletníci a paroháči, roztoužené dívky a nevěrné manželky. Až se divíš, že se něco takového dá najít v knihovně vedené mladou šlechtičnou."
    return
label seriousHistory:
    "Od knihy s názvem Vojenské úspěchy Armanda de Teyron sis sliboval[a] napínavé popisy bitev, případně drama dlouhého tažení a konflikt lásky k vlasti a touhy po domově. Místo toho se Romaine de Chatevin věnuje politickým vztahům mezi jednotlivými šlechtici, které popisuje tím nejsušším možným způsobem, a detailnímu rozboru strategie jednotlivých bitev."
    "Po chvíli začneš přeskakovat odstavce a celé stránky, ale ani v popisu vzpoury části armády a jejího potlačení nenacházíš sebemenší stopu jakékoli emoce."
    "Až na konci, u výčtu kronik a jiných dokumentů, ze kterých Romaine při zpracování díla vycházel, ti dojde, že máš zřejmě v ruce historickou práci, kterou někdo uložil do špatné police."
    return
label jakobVonDemSchloss:
    "Podle toho, jak je ohmataná, patří kniha příběhů o Jakobovi von dem Schloss zřejmě mezi oblíbené tituly. Slavného zbojníka ukazuje jako lidového hrdinu, který bere jen bohatým, chudým dává, vysmívá se aroganci pánů a především zas a znovu utíká ze všech pastí, které na něj líčí zákon."
    "V jednom z příběhů se třeba Jakoba rozhodl přivést před spravedlnost jeden boháč a dokonce se mu podařilo najít dům jeho matky. Aby se zbytečně nezahazoval s chydými lidmi, zeptal se boháč pobudy, co odpočíval před domem, jestli Jakob von dem Schloss v domě bydlí. Ten přisvědčil a dokonce nabídl, že boháči pohlídá koně a bič, zatímco on půjde dovnitř."
    "Jakmile se za boháčem zavřely dveře, pobuda, samozřejmě Jakob sám, skočil na koně a rozjel se přímo k boháčovu domu. Tam jeho manželce ještě zadýchaný vylíčil potíže, do kterých se její muž dostal, a požádal ji o peníze, které by mu mohl doručit. Na důkaz toho, že ho skutečně poslal její manžel, ukázal jeho koně a bič. Boháčově ženě to stačilo, peníze vydala s mnoha slovy díků, a Jakob s nově nabytým bohatstvím zmizel."
    "Knihu zavřeš s úsměvem. Kéž by byl boj s nespravedlností tak snadný i ve skutečném životě."
    return
label elvenDragonLegend:
    "Vezmeš do ruky knihu starých elfích legend s nádherně vyvedeným drakem na deskách. Příběhy o prvním elfím králi a jeho čtyřech knížatech jsou veršované a obsahují překvapivě mnoho lyrických pasáží a komplikované symboliky, ze které se ti podaří pochopit jen část. Dýchá z nich ale romantika starých časů a především hluboké souznění se zemí a zájem o poddané, jejichž problémy hrdinové osobně řeší."
    "Centrální příběh pak popisuje putování za příčinou nepřirozené zkázy, požárů a zemětřesení, které začaly elfí říši náhle zachvacovat. Po mnoha útrapách našli hrdinové zdroj - na holé skále, uprostřed krajiny spálené na uhel, se svíjel drak a chrlil oheň všude kolem sebe."
    "Král přistoupil blíž, přes varování a prosby svých knížat, a uviděl, že z drakova břicha trčí zlomené kopí a způsobuje mu strašlivou bolest. Drak se na krále upřeně zadíval, ale nezaútočil. To mladému elfovi dodalo odvahu překonat i zbývající vzdálenost a dotknout se kopí."
    "Ve chvíli, kdy král kopí vytáhl z rány, se drak uklidnil, pokývl na znamení díků a pak se stočil na skále a usnul. Králi zůstalo v ruce zlomené kopí a kolem něj zotavující se země a modrá obloha nad hlavou."
    return
label animalLore:
    "Očekáváš učebnici pro začínající sokolníky a psovody, kniha ale podrobně rozebírá nejen lov a chov domácích tvorů, ale zejména chování zvířat ve volné přírodě – a nezřídka jim připisuje lidské vlastnosti."
    "Autor například popisuje, že vraní rodiny se starají o své staré a nemocné a truchlí nad mrtvými, že divocí koně pořádají bojové hry, aby posílili pouto ve stádě, a že lišky v zimě tančí na sněhu, aby vábily měsíc. Některé pasáže působí jako vědecké pojednání, jiné jako sbírka loveckých anekdot, a v jednom zvlášť podivném odstavci autor tvrdí, že některé kočky umí číst lidské myšlenky."
    if race == "elf":
        "Kniha je poutavá a lehce se čte a obsahuje některé zajímavé postřehy, část domněnek ti však připadá značně odvážná. Bylo by užitečné, kdyby autor zahrnul i některé zkušenosti hraničářů, zřejmě se však jednalo o jednoho z lidských učenců, kteří se o elfí tradice nezajímají."
    else:
        "Ačkoliv mnohé příběhy berou víc z fantazie než z pozorování, kniha je poutavá a lehce se čte. Nakonec ji odložíš s pobaveným úsměvem a s novou chutí podívat se na svět kolem sebe trochu jinýma očima."
    return

### law
label lawIntro:
    "Stejně jako jinde, i v Marendaru se soudci řídí především zvykem a jako vodítko často používají rozsudky svých předchůdců. Nic jako soupis městských zákonů neexistuje, najdeš ale přepisy několika různých nařízení."
    "Ve městě je přísně zakázáno nošení otevřeného ohně na ulici včetně loučí a pochodní a jakékoli neopatrné zacházení s ohněm. Pod zákazem jsou podepsaní Gerfried a Etrian, podle všeho ale v tomto případě potvrzují nařízení vydané ještě Velinem."
    "Ze stejné doby a se stejným podpisem je i podrobně rozepsaný zákaz jakkoli rozdílného zacházení na základě rasy, bez ohledu na původ kteréhokoli z aktérů."
    return
label watch:
    "O pravomocech hlídky najdeš několik dokumentů z různých období a každý z nich dává naprosto odlišný obraz."
    "Za Velinovy vlády hlídka nepodléhala žádnému dohledu a případné přečiny strážných si řešila sama. Mohla jen na základě podezření vstupovat do obydlí měšťanů nebo zabavovat majetek a bylo jen málo způsobů, jak se jejím zásahům bránit - zvlášť pokud si chtěl stěžovat někdo, kdo nebyl elf."
    "Když se moci chopili Gerfried a Etrian, důsledně odstranili veškeré upřednostňování elfů a zavedli, že jakékoli rozhodnutí hlídky musí potvrdit městský soud. K soudu se naopak může obrátit někdo, kdo věří, že mu hlídka ublížila; pokud mu soud dá za pravdu, potrestá nejen provinilého člena hlídky, ale i hlídku jako celek například peněžitou pokutou."
    "S příchodem Listiny práv a povinností se tento princip ještě zvýraznil: hlídka má mnoho možností a pravomocí, ale zároveň se z jejich použití musí přísně zodpovídat."
label marketLaws:
    "Mnoho zákonů a nařízení se týká místních jarmarků. Všimneš si přitom, že určité přečiny spáchané během trhu jsou trestané přísněji, například rvačky nebo drobná zlodějina. Velmi přísně se též město staví k jakémukoli druhu šizení zboží. Naopak k rušení klidu nadměrným halasem se soudy zdají přistupovat spíše shovívavě."
    "Některá nařízení dokonce zacházejí do takových podrobností, jako že není povoleno svévolně přesouvat stánky jiných trhovců. Město se též snaží bojovat proti falešným kostkám a během každého z několika posledních jarmarků kvůli nim někdo skončil v pranýři."
    "Trochu neobvyklé je pak pravidlo, že kdokoli, kdo v Marendaru dlouhodobě nebydlí, v něm má přísně zakázáno vařit nebo vykonávat jakákoli řemesla nebo jiné činnosti využívající oheň."
    return

### past trials
label pastTrialsIntro:
    "Snadno najdeš několik tlustých svazků s opisy soudních protokolů, velmi rychle ale získáš pocit, že by se snadno daly zkrátit na méně než desetinu. Naprostá většina soudů za poslední rok se týká náhodných rvaček v hospodě nebo drobných krádeží."
    "Tresty si bývají podobné, nejčastěji zůstává jen u vyplacení odškodného a podle zápisů snad vždy došlo k usmíření obou stran."
    return
label cultistsTrial:
    "Poslední zajímavý soudní proces se odehrál asi před rokem, kdy byl za spiknutí proti městu a pokus otrávit purkmistra Oswalda souzen člen městské rady Ridian spolu se svými spolupachateli Sabrim a Hayfou."
    "Ridian se ani nepokoušel zapírat, naopak se podle záznamu hrdě přihlásil k vedení celé skupiny, vystupoval po celou dobu líčení povýšeně a přál městu, aby znovu vyhořelo. To vzbudilo velké pobouření všech přítomných a Ridian byl oběšen “jako obyčejný sprostý zločinec”."
    "Hayfa a Sabri byli nejprve odsouzeni k vyhnanství, nicméně Hayfa prosila, aby mohla zůstat a odčinit svou vinu prací pro město, a Sabri vyjádřil přání zůstat s ní."
    "Městská rada se nechala obměkčit, trest tedy byl změněn: oba mají svou vinu odčinit prací pro město a do té doby ho naopak opustit nesmí. Sabri bude trest vykonávat po dobu dvou let. Hayfě, protože projevila upřímnou lítost, byl trest snížen na jeden rok."
    "Rychle spočítáš, že toto období uplynulo jen před několika týdny. Dohledem a zadáváním práce byl pověřen městský úředník Janis."
    return
label pastTrialsAboutWatch:
    "Napadlo tě dohledat si ještě soudní spisy z poslední doby, které by mohly něco napovědět o pravomocech hlídky."
    "Najdeš jediný případ, kdy hlídkař někoho vážně zranil, a to bylo ve rvačce, ve které na něj opilý potulný tovaryš vytasil nůž. Soud považoval tento druh obrany za přiměřený a naopak tovaryše vyhnal z města, ačkoli ještě nosil obvazy a sotva chodil."
    "V jiných případech, kdy hlídka musí zakročit proti různým výtržníkům nebo drobným zlodějům, rvačky končí nanejvýš podlitinami a na tom soud také nikdy neshledal nic špatného. V mnoha případech také výtržníka přemohli obyvatelé města a hlídka dorazila až poté."
    "Zatčení nebývá zcela obvyklé. Pokud je k němu dobrý důvod, soud ho posvětí, nicméně hlídka tyto důvody musí vysvětlit v samostatném procesu a o tomto zdůvodnění se vyhotoví důkladný zápis."
    "Hlídka také může v případě menších provinění uložit na místě peněžitý trest. Takovou pokutu je ale nezbytně nutné zapsat; pokud člen hlídky nedokáže potvrzení o pokutě vydat, není provinilec povinen pokutu zaplatit."
    "Nenajdeš žádný záznam, podle kterého by někdo z hlídky od Velinova pádu vstoupil do měšťanského domu z jiného důvodu, než aby zatkl zločince. V jednom případě byla z podobného slídění nařčená Hayfa, soud ale obvinění neuznal pro nedostatek důkazů."
    return
label onionIncident:
    "Před několika měsíci došlo k úsměvnému incidentu mezi městským úředníkem Janisem a trhovkyní Martou. Janis si během kontroly zeleninového trhu všiml, že Marta prodává cibule za nižší cenu, než jakou místní obchodnický cech stanovil."
    "Upozornil ji tedy a došlo nejdříve ke slovní potyčce, ve které ho Marta nazvala navoněným škrábalem, bezzubým škrabopisem a skrčkem. Když Janis trval na tom, že Marta musí ceny upravit, hodila po něm trhovkyně cibuli a poté utekla."
    "Marta během několika dní stanula před soudem. Za nedodržení stanovené ceny byla potrestána pokutou vůči městu a obchodnímu cechu ve výši ceny jednoho koše cibulí a dostala zákaz prodeje na tři dny. Jako omluvu Janisovi za nactiutrhání a napadení jí pak bylo uloženo se veřejně omluvit a přinést mu čtyři následující neděle vždy pět výstavních cibulí."
    return

### history
label history1:
    "O nejranější historii kroniky mnoho neříkají. Marendar podle nich byl nicméně založen dlouho před tím, než lidé přišli na kontinent, a po celou svou historii byl v kontaktu s nejvýznamnějšími elfími centry obchodu, kultury a vzdělanosti."
    return
label history2:
    "Součástí vévodství Gernlinden se Marendar stal už v raných fázích formování lidské říše a již tehdy ho spolu s celým baronstvím získal v léno rod de Méprepen. Nejvážnější spory mezi baronem a městem nastaly za vlády Arlema de Méprepen, který se pokusil vynutit zvláštní platby za privilegia a další svobody důležité zejména pro elfy, hobity a částečně trpaslíky (například výrazné daně na veškeré knihy, zvláštní daně pro bezdětné osoby, povinnost řemeslníkům účastnit se Einionových slavností nebo se z účasti vyplatit); od většiny z nich musel baron nakonec upustit."
    "Naopak velkého uznání si ve městě získal baron Jocelin, který se vyznamenal ve válce proti sousednímu hrabství Eichenau a kterému se podařilo dohodnout výhodné obchodní vazby s městem Königswiesen, které bylo v důsledku války k hrabství připojeno."
    return
label history3:
    "Když v Gernlindem došlo ke sporům o regentství nad mladým vévodou, které postupně přerostly v občanskou válku, rozhodl se baron Séraphin de Méprepen - otec současného barona - do bojů naplno vrhnout. Nedařilo se mu však a brzy potřeboval nové prostředky, aby ve válčení mohl pokračovat. Stále proto zvyšoval daně a Marendar jako své jediné město jimi zatěžoval nejvíc. V závěru vlády navíc zavedl zvláštní daně pro marendarskou elfí, hobití a trpasličí komunitu, z titulu toho, že se jejich členy příliš nedařilo verbovat do armády. To vyvolalo silnou nevraživost příslušníků těchto ras vůči baronovi a přeneseně i proti ostatním lidem ve městě."
    "Když pak Séraphin padl v jedné z mnoha bitev, na jeho místo nastoupil jeho velmi mladý syn Séverin. Jeden z jeho podřízených zemanů, Constance z Anatolu, se proti novému baronovi vzbouřil a místo obnovení lenních slibů a složení přísahy věrnosti vpadl na baronovo území. Tehdy Marendar vycítil příležitost zbavit se nenáviděné vlády. Velitel městské hlídky Velin se postavil do čela povstání, které mělo skoncovat s rasovou diskriminací, a město vyhlásilo nezávislost. Séverin byl plně zaměstnán bojem s Constancem a nedokázal se proti tomu nijak postavit."
    return
label history4:
    "Nějakou dobu po Velinově povstání byla jeho vláda zřejmě skutečně otevřená všem a ke všem spravedlivá, postupně se ale na vysoké posty dostala výrazná elfí většina, která začala prosazovat především zájmy své vlastní komunity. Na protesty ze strany lidí, zvyklých na výsadní postavení, reagoval Velin nejprve poukázáním na to, že lidé mohou odejít kamkoli jinam, protože všude kromě Marendaru jsou ve většině, a později zaváděním skutečně nerovnoprávných nařízení a represí."
    "Městská hlídka byla po celou dobu Velinovy vlády hlavní opora jeho moci a Velin se nijak neštítil používat ji proti všem, kdo by si dovolili byť jen stěžovat. Nechal dokonce rozšířit sklepení pod strážnicí a vybudovat velké množství nových cel."
    return
label history5:
    "K největšímu povstání lidské komunity proti Velimově vládě došlo přibližně před dvěma lety. Podle kronikáře ho vyvolali dva cizinci, kteří hned po jeho krvavém potlačení prchli z města, to ale může být především snaha přesunout vinu bezpečně mimo samotný Marendar. Povstání bylo potlačeno během jediné noci, i tak si ale vyžádalo mnoho životů a následné popravy jich měly stát ještě více."
    "Den po povstání, ještě než k popravám stačilo dojít, ale vypukl strašlivý požár. Asi polovina města včetně části nejvýstavnější čtvrti lehla popelem, zemřelo mnoho lidí, elfů i příslušníků jiných ras a mnohem více jich přišlo o domov a veškeré živobytí. Velinovi v požáru zemřel jediný syn a on se s tou ztrátou nikdy nevyrovnal, nijak původ požáru nevyšetřoval a rovnou přísahal strašlivou pomstu lidským povstalcům i lidským obyvatelům města obecně."
    "Vyšetřování ovšem provedl zeman Corneille z Anatolu, který na svém území - tedy několik dní cesty od Marendaru - zadržel elfího ohnivého mága Promethise, odsoudil ho a nechal upálit. Kronika pečlivě vysvětluje, že Promethisova vina byla nesporná, protože byla dokázána na základě svědectví svědků přímo z Marendaru, potvrzena místními runovými kováři, a dokonce ověřena i pomocí božího soudu, kde sám zeman z Anatolu proti Promethisovi nastoupil v souboji."
    "Velin se naštěstí svým běsněním rychle připravil o podporu i nejbližších stoupenců. Kapitán Etrian z městské hlídky nakonec radši uzavřel spojedectví s Gerfriedem, jedním z lidských povstaleckých vůdců, a Velina uvěznili."
    return
label history6:
    "Etrian a Gerfried vydrželi v čele města necelý rok. Oba byli vnímaní jako nutné zlo, pokud ne přímo zrádci vlastního lidu, uzurpátoři a tyrani. Podepsali několik poměrně přísných zákonů, především proti manipulaci s ohněm ve městě a jakýmkoli projevům rasové nenávisti, zdá se ale, že se jim podařilo město v rámci možností stabilizovat. Nástup nové městské rady kronika prezentuje jako vítězství práva nad tyranií, kdy Gerfried a Etrian kapitulovali před vůlí lidu a bylo jim umožněno svobodně dožít mimo veřejné funkce."
    return
label history7:
    "Zajímavým zápisem z poslední doby je pak zmínka o tom, že jeden z členů nové městské rady - Ridian, bohatý elf a jeden z mluvčích za uprchlíky před požárem - se pokusil ovládnout město s pomocí jakési sekty. Spiknutí bylo odhaleno, Ridian byl popraven a potrestáni byli i jeho pomocníci. Kronikář se o Ridianovi vyjadřuje s velkou nenávistí, neboť bývalý radní prý během soudu místo obhajoby popřál městu, ať konečně celé shoří."
    "Nyní je však rada opět úplná a město opět přijalo Séverina de Méprepen jako svého barona. Baron je oslavován jako milovaný vládce, který výrazně pomohl ukončit bezpráví v celém Gernlinden a navrátit pravého vévodu na trůn a který navíc podstatně přispěl k nastolení nových, spravedlivějších zákonů."
    "Nová městská rada je ve funkci jen krátce, nicméně kronika obsahuje několik zápisů o přestavbě města, návratu uprchlíků a v neposlední řadě též o obnově městské hlídky. Kronikář se o ní vyjadřuje s uznáním a nadějí do budoucna."
    return

###

label libraryOptionsRemaining:
    $ optionsRemaining = 0
    if "promised poetry" in status and not any("poem" in str for str in status):
        $ optionsRemaining += 1
    if "letters for Ada seen" in status and "poetry style" not in librarian.asked:
        $ optionsRemaining += 1
    if "lover well read" in ada.asked and "well-read elves" not in librarian.asked:
        $ optionsRemaining += 1
    if literatureTopics != []:
        $ optionsRemaining += 1
    if lawTopics != []:
        $ optionsRemaining += 1
    if pastTrialsTopics != []:
        $ optionsRemaining += 1
    if historyTopics != []:
        $ optionsRemaining += 1

label lawConsultationOptionsRemainingCheck:
    $ lawConsultationOptionsRemaining = 0
    if "watch powers" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "punishment for theft - master craftsman" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "punishment for theft - poor person" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "shoes' fate" in clues and "punishment for theft - apprentice" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "stolen idea" in clues and "punishment for theft of shoe pattern" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "duplicate key" in status and "punishment for burglary" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and "AML" in lotte.asked and "punishment for blackmail" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    if "punishments" in librarian.asked and time.days > 1 and "punishment for Katrin" not in librarian.asked:
        $ lawConsultationOptionsRemaining += 1
    return
