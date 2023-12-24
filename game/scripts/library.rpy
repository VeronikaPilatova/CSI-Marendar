label libraryPreparation:
    default literatureTopics = ["wellWrittenTrash", "farawayTravels"]
    default lawTopics = ["lawIntro"]
    default historyTopics = []
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
        "TBD: knihovna znovu"
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
            $ library.checked.append("law " + chosenTopic)
            $ lawTopics.remove(chosenTopic)
            scene bg books
        "{i}(Nastudovat si městskou historii){/i}" if historyTopics != []:
            $ chosenTopic = renpy.random.choice(historyTopics)
            $ library.checked.append("history " + chosenTopic)
            $ historyTopics.remove(chosenTopic)
            scene bg books
        "{i}(Vrátit se na strážnici){/i}":
            $ chosenTopic = "leave"

    return

label libraryRepeat:
    scene bg library
    if time.hours > 21:
        "Je čas jít spát"
        return
    call libraryOptionsRemaining
    if optionsRemaining == 0:
        "Vše přečteno"
        return
    call libraryOptions
    if chosenTopic = "leave":
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

label lawIntro:
    "Stejně jako jinde, i v Marendaru se soudci řídí především zvykem a jako vodítko často používají rozsudky svých předchůdců. Nic jako soupis městských zákonů neexistuje, najdeš ale přepisy několika různých nařízení."
    "Ve městě je přísně zakázáno nošení otevřeného ohně na ulici včetně loučí a pochodní a jakékoli neopatrné zacházení s ohněm. Pod zákazem jsou podepsaní Gerfried a Etrian, podle všeho ale v tomto případě potvrzují nařízení vydané ještě Velinem."
    "Ze stejné doby a se stejným podpisem je i podrobně rozepsaný zákaz jakkoli rozdílného zacházení na základě rasy, bez ohledu na původ kteréhokoli z aktérů."

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
    if historyTopics != []:
        $ optionsRemaining += 1
