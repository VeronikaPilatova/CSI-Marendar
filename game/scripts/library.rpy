label libraryPreparation:
    default literatureTopics = ["wellWrittenTrash", "farawayTravels", "fables", "saucyTales", "seriousHistory", "jakobVonDemSchloss", "elvenDragonLegend"]
    default lawTopics = ["lawIntro"]
    default historyTopics = ["historyIntro", "history1", "history2", "history3", "history4", "history5", "history6", "history7"]
    default pastTrialsTopics = ["pastTrialsIntro", "cultistsTrial"]
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
    if "library visited" not in status:
        if origin == "born here":
            "Marendarskou knihovnu si pamatuješ z dětství. Bývala to elegantní budova s vysokými policemi a studovnou, kde se dalo ztratit na dlouhé hodiny - nebo aspoň na tak dlouho, než tě někdo vyhnal zase ven."
            "Pamatuješ si na všeprostupující vůni papíru a kožených desek, pocit tepla a bezpečí, a především na laskavého knihovníka, který v tobě podporoval sny o lepším životě."
            "Tehdy jsi byl[a] přesvědčen[y], že se tam dá najít snad každá kniha na světě. A přestože stará knihovna nepřežila požár, který před dvěma lety město změnil téměř k nepoznání, určitě tu musela zbýt aspoň část jejího kouzla."
            scene bg library
            "Dnes knihovna dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito a i přes provizorní umístění je očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal[a], ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu zase celý den."
        else:
            "Marendar míval krásnou knihovnu s mnoha svazky, ale ta bohužel padla za oběť ničivému požáru města před dvěma lety. Na její obnovu v plné slávě se stále hledají prostředky a mnohem menší sbírka dnes dočasně sídlí v jednom z bohatších městských domů pod vedením Luisy de Vito."
            scene bg library
            "I přes provizorní umístění je knihovna očividně vedená s láskou. Knih ve vysokých policích je možná méně, než jsi doufal[a], ale neujde ti šíře záběru. Od krásné literatury přes filozofii po vědecké spisy... máš chuť strávit tu celý den."
        $ status.append("library visited")
    else:
        scene bg library
        "Znovu tě přivítá příjemná vůně knih, a jak procházíš mezi regály, mladý elf, který tu vypomáhá, ti kývne na pozdrav."
    return

label libraryOptions:
    menu:
        "{i}(“Půjčit” si vhodnou báseň pro Zairise){/i}" if "promised poetry" in status and not any("poem" in str for str in status):
            $ chosenTopic = "stealPoetry"
        "{i}(Zkonzultovat styl básní pro Adu){/i}" if "letters for Ada seen" in status and "poetry style" not in assistant.asked:
            $ chosenTopic = "libraryConsultLettersForAda"
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

label libraryRepeat:
    scene bg library

    if literatureTopics == [] and lawTopics == [] and pastTrialsTopics == [] and historyTopics == []:
        if not achievement.has(achievement_name['bookworm'].name):
            $ Achievement.add(achievement_name['bookworm'])

    call libraryOptionsRemaining
    if optionsRemaining == 0:
        "Vše přečteno"
        return
    if timeOfDay != time.timeOfDayInt():
        "Rozsvícení magického světla"
        $ timeOfDay = time.timeOfDayInt()
    elif time.hours > 21:
        "Je čas jít spát"
        return

    call libraryOptions
    if chosenTopic == "leave":
        return
    else:
        call expression chosenTopic
        jump libraryRepeat

###

label stealPoetry:
    scene bg books
    "Najdeš regál s poezií a po chvíli procházení vezmeš do ruky útlou knihu básní. Se jménem autora ses ještě nesetkal[a], ale většina básní uvnitř mluví o citech nebo pracuje s přírodními motivy. Opíšeš si náhodnou z nich a doufáš, že na Zairise udělá dostatečně dobrý dojem."
    scene bg library
    show expression ("sh stolen poem [race].png") at truecenter
    pause
    hide expression ("sh stolen poem [race].png") at truecenter
    $ status.append("poem stolen")
    $ time.addMinutes(20)
    return

label libraryConsultLettersForAda:
    $ assistant.asked.append("poetry style")
    $ status.append("letters for Ada checked in library")
    "TBD"
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
    else:
        $ readingTopic = renpy.random.choice(lawTopics)
        $ library.checked.append(readingTopic)
        $ lawTopics.remove(readingTopic)
    scene bg books
    call expression readingTopic
    $ time.addMinutes(40)
    if lawTopics != [] and time.hours <= 21:
        menu:
            "Pokračovat":
                jump readingLaw
            "Přestat se čtením":
                pass
    return

label readingPastTrials:
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

### law
label lawIntro:
    "Stejně jako jinde, i v Marendaru se soudci řídí především zvykem a jako vodítko často používají rozsudky svých předchůdců. Nic jako soupis městských zákonů neexistuje, najdeš ale přepisy několika různých nařízení."
    "Ve městě je přísně zakázáno nošení otevřeného ohně na ulici včetně loučí a pochodní a jakékoli neopatrné zacházení s ohněm. Pod zákazem jsou podepsaní Gerfried a Etrian, podle všeho ale v tomto případě potvrzují nařízení vydané ještě Velinem."
    "Ze stejné doby a se stejným podpisem je i podrobně rozepsaný zákaz jakkoli rozdílného zacházení na základě rasy, bez ohledu na původ kteréhokoli z aktérů."
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
    if "letters for Ada seen" in status and "poetry style" not in assistant.asked:
        $ optionsRemaining += 1
    if literatureTopics != []:
        $ optionsRemaining += 1
    if lawTopics != []:
        $ optionsRemaining += 1
    if pastTrialsTopics != []:
        $ optionsRemaining += 1
    if historyTopics != []:
        $ optionsRemaining += 1
