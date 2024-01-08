label libraryPreparation:
    default literatureTopics = ["wellWrittenTrash", "farawayTravels", "fables", "saucyTales", "seriousHistory"]
    default lawTopics = ["lawIntro"]
    default historyTopics = ["historyIntro"]
    default pastTrialsTopics = ["pastTrialsIntro", "cultistsTrial"]
    return

label libraryController:
    call libraryIntro
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
        "Znovu tě přivítá příjemná vůně knih, a jak procházíš mezi regály, mladý elf, který tu vypomáhá, ti kývne na pozdrav."
    return

label libraryOptions:
    menu:
        "{i}(“Půjčit” si vhodnou báseň pro Zairise){/i}" if "promised poetry" in status and not any("poem" in str for str in status):
            $ chosenTopic = "stealPoetry"
        "{i}(Zkonzultovat styl básní pro Adu){/i}" if "letters for Ada seen" in status and "poetry style" not in assistant.asked:
            $ chosenTopic = "libraryConsultLettersForAda"
        "{i}(Odpočinout si při čtení krásné literatury){/i}" if literatureTopics != []:
            $ chosenTopic = renpy.random.choice(literatureTopics)
            $ library.checked.append("literature " + chosenTopic)
            $ literatureTopics.remove(chosenTopic)
            scene bg books
        "{i}(Nastudovat si právo a místní zákony){/i}" if lawTopics != []:
            if "lawIntro" in lawTopics:
                $ chosenTopic = "lawIntro"
            else:
                $ chosenTopic = renpy.random.choice(lawTopics)
            $ library.checked.append(chosenTopic)
            $ lawTopics.remove(chosenTopic)
            scene bg books
        "{i}(Projít zápisy soudních procesů){/i}" if pastTrialsTopics != []:
            $ chosenTopic = pastTrialsTopics[0]
            $ library.checked.append(chosenTopic)
            $ pastTrialsTopics.remove(chosenTopic)
            scene bg books
        "{i}(Nastudovat si městskou historii){/i}" if historyTopics != []:
            $ chosenTopic = historyTopics[0]
            $ library.checked.append(chosenTopic)
            $ historyTopics.remove(chosenTopic)
            scene bg books
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
    return

label libraryConsultLettersForAda:
    $ assistant.asked.append("poetry style")
    $ status.append("letters for Ada checked in library")
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
    "Milenci si spolu užijí a hned na to jde sluha do zahrady "dát za vyučenou" své nevěrné paní - tedy ve skutečnosti jejímu manželovi v šatech své ženy. Manžel se tak dostatečně přesvědčí o věrnosti své ženy i svého služebníka a ti dva se spolu můžou dál tajně scházet."
    "Když se dostaneš ke třetímu příběhu o mladíkovi, kterému hrozí smrt láskou, pokud se mu nepodaří strávit aspoň jednu noc s vdanou dámou svého srdce, nedá ti to a prolistuješ zbytek knihy."
    "I ostatní vyprávění se nesou v podobném duchu, samí záletníci a paroháči, roztoužené dívky a nevěrné manželky. Až se divíš, že se něco takového dá najít v knihovně vedené mladou šlechtičnou."
    return

label seriousHistory:
    "Od knihy s názvem Vojenské úspěchy Armanda de Teyron sis sliboval[a] napínavé popisy bitev, případně drama dlouhého tažení a konflikt lásky k vlasti a touhy po domově. Místo toho se Romaine de Chatevin věnuje politickým vztahům mezi jednotlivými šlechtici, které popisuje tím nejsušším možným způsobem, a detailnímu rozboru strategie jednotlivých bitev."
    "Po chvíli začneš přeskakovat odstavce a celé stránky, ale ani v popisu vzpoury části armády a jejího potlačení nenacházíš sebemenší stopu jakékoli emoce."
    "Až na konci, u výčtu kronik a jiných dokumentů, ze kterých Romaine při zpracování díla vycházel, ti dojde, že máš zřejmě v ruce historickou práci, kterou někdo uložil do špatné police."
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
label historyIntro:
    "Oficiální marendarská kronika sídlí na radnici, kde ji má ve správě městský písař. To byla ostatně tvá první zastávka během hledání práce. Paní Luisa ale pro svou knihovnu nechala pořídit opis, a tak se můžeš seznámit s historií města bez přísného písařova dohledu."
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
