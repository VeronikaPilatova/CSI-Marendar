label workshopNightController:
    $ currentLocation = "workshop night"
    call workshopNightIntro

    $ actionsTaken = 0
    call workshopNightOptions

    $ currentLocation = ""
    return

label workshopNightIntro:
    scene bg heinrich outside lit window
    "Když dojdeš k domu mistra Heinricha, v jedné z místností se ještě svítí. Čekání, až celý dům ztichne a usne, nejspíš netrvá déle než půl hodiny, ale na prázdné ulici ti to připadá až příliš dlouho."
    scene bg heinrich outside dark
    "Naposled se rozhlédneš po okolních domech a neubráníš se krátké motlitbě, aby se zrovna nikdo nedíval z okna. Pak přejdeš ke dveřím do dílny a otočíš klíčem."
    "Dveře otevřou, tišeji, než ses bál[a], a ty vklouzneš dovnitř."
    scene bg workshop
    "Tvá lampa ozáří police, které sahají až téměř ke stropu. V nich jsou narovnané boty všech druhů a velikostí v různém stavu dokončení a pod nimi dřevěná kopyta různých tvarů."
    "U jedné stěny stojí stolek se dvěma zásuvkami plný všemožných nástrojů, vedle něj je trojnohé sedátko a o kus dál směrem ke dveřím zvláštní stolice s dřevěnými čelistmi na jednom konci."
    "V rohu místnosti je krb a nedaleko dveří velký koš na odřezky kůže a jiný odpad."
    return

label workshopNightOptions:
    menu:
        "{i}(Projít zásuvky u stolu){/i}" if "table at night" not in workshop.checked:
            $ workshop.checked.append("table at night")
            $ actionsTaken += 1
            if "table" in workshop.checked:
                "Ještě jednou a důkladně si prohlédneš střihy a nákresy ve vylomené zásuvce, ale nevidíš na nich nic zvláštního. Některé vypadají poměrně staré a naprostá většina je pravděpodobně kreslená stejnou rukou."
            else:
                $ workshop.checked.append("table")
                "Jedna zásuvka je zamčená, druhou se ti ale podaří vysunout. Uvnitř jsou nějaké papíry, podle všeho nákresy bot, střihů a způsobů jejich šití. Zajímavější je fakt, že zámek na tomto šuplíku byl násilím vylomený."
                "Střihy si prohlédneš důkladně, ale nevidíš na nich nic zvláštního. Některé vypadají poměrně staré a naprostá většina je pravděpodobně kreslená stejnou rukou."
        "{i}(Vylomit zamčenou zásuvku){/i}" if "table" in workshop.checked and "table forced" not in workshop.checked:
            $ workshop.checked.append("table forced")
            $ actionsTaken += 1
            "Přejedeš pohledem po ševcovských nástrojích vyskládaných na stole, ale pak vytáhneš svůj vlastní nůž, od kterého přesně víš, co čekat."
            "Křupnutí, které se ozve, tě přiměje ztuhnout a chvíli nervózně čekat spuštění poplachu. Dům ale zůstává tichý a klidný."
            "Zásuvka je plná papírů. Část z nich je zřejmě obchodní korespondence, v části po chvíli rozpoznáš zápisky o přesných mírách různých zákazníků. Nečekal[a] bys, kolik lidí má každou nohu jinak velkou nebo potřebuje jiné zvláštní úpravy."
        "{i}(Opsat si míry a zvláštnosti nohou měšťanů){/i}" if "table forced" in workshop.checked and "notes taken" not in workshop.checked:
            $ workshop.checked.append("notes taken")
            $ actionsTaken += 1
            "Napadne tě, že podrobnosti o velikosti a tvaru nohy různých lidí by se mohly hlídce dost hodit a uděláš si z nich tolik poznámek, kolik se jen odvažuješ."
        "{i}(Prohlédnout si zbytky materiálu){/i}" if "rubbish" not in workshop.checked:
            $ workshop.checked.append("rubbish")
            $ actionsTaken += 1
            "V koši se zbytky jsou především odřezky kůže různých druhů a velikostí. Jen velmi malá část jsou pokažené kusy. Téměř na dně ale najdeš rozešitý základ bot, na kterém nevidíš žádnou očividnou chybu."
            if "WIP shoes seen" in status:
                "Prohlédneš si ho blíž a neujde ti výrazná podobnost se střevíci, na kterých pracuje mistr Njal. A tedy pravděpodobně i s těmi ukradenými."
            else:
                "Ani bližší prozkoumání ti nepřinese odpovědi, proč ho někdo vyhodil. Materiál ti přijde kvalitnější než naprostá většina ostatních zbytků a odřezků a střih působí velmi komplikovaně."
            if not achievement.has(achievement_name['burglar'].name):
                $ Achievement.add(achievement_name['burglar'])
        "{i}(Najít staré účty a objednávky materiálu){/i}" if "love letters" not in workshop.checked:
            $ workshop.checked.append("love letters")
            $ actionsTaken += 1
            "Po chvíli hledání se ti podaří najít účetní knihu a začneš v ní listovat. Záznamy nejsou vedené příliš systematicky, ale působí věrohodně a aspoň takhle na první pohled v nich nevidíš žádné nesrovnalosti."
            if "AML" in lotte.asked and "confession" not in rumelin.asked:
                "Nákupy materiálu za poslední měsíc se nijak neliší od těch starších. Pokud mělo skutečně dojít ke společným objednávkám pro cech, mistr Heinrich se jich zřejmě neúčastnil."
            "Chceš knihu odložit a pokračovat v prohledávání dílny, když tě zaujme několik složených listů ozdobného papíru, výrazně jiného a nejspíš mnohem dražšího, než je zbytek knihy."
            "Nedá ti to a prohlédneš si je."
            call loveLetters
            if not achievement.has(achievement_name['burglar'].name):
                $ Achievement.add(achievement_name['burglar'])
            $ status.append("letters for Ada seen")
            label loveLettersBurglaryMenu:
            menu:
                "{i}(Přečíst si dopisy znovu){/i}":
                    call loveLetters
                    jump loveLettersBurglaryMenu
                "{i}(Vzít s sebou jako důkaz všechny){/i}":
                    "Schováš si celý baliček do taštičky na opasku v přesvědčení, že nikomu nebude chybět."
                    $ status.append("all love letters kept")
                "{i}(Vzít s sebou jako důkaz jen jeden z papírů){/i}":
                    "Vybereš jeden z dopisů, schováš ho do taštičky na opasku a zbytek vrátíš na místo. Mistr Heinrich přece nemůže mít spočítané, kolik dopisů celkem bylo."
                    $ status.append("one love letter kept")
                "{i}(Vrátit dopisy zpět do účetní knihy){/i}":
                    "Pečlivě všechno vrátíš zpět na původní místo."
        "{i}(Prohlédnout si Heinrichovy nástroje){/i}" if "tools" in workshop.checked and "tools touched" not in workshop.checked:
            $ workshop.checked.append("tools touched")
            $ actionsTaken += 1
            "Pořád si pamatuješ, jak tě dřív mistr Heinrich okřikl, a když teď vezmeš jeho nástroje nerušeně do ruky, cítíš jisté zadostiučinění."
            "Postupně prozkoumáš celou řadu různých nožů, šídel, měřidel a dalších věcí. Všechny vypadají jako velmi dobře vyrobené, jsou čisté a nenajdeš ani stopu rzi nebo jakéhokoli poškození."
            if not achievement.has(achievement_name['heinrichTools'].name):
                $ Achievement.add(achievement_name['heinrichTools'])
        "{i}(Radši odejít z dílny){/i}":
            "Potichu vyklouzneš z dílny a zamkneš za sebou."
            return

    if actionsTaken == 2:
        play sound audio.footsteps1 fadeout 0.5
        "Někde v domě uslyšíš kroky a instinktivně ztuhneš. Tichou dílnou se zvláštně rozléhají a nedokážeš poznat, kam můžou mířit."
        "Po chvíli ale utichnou."
    elif actionsTaken == 3:
        play sound audio.footstepsApproaching
        "Kroky se ozvou znovu a tentokrát se určitě přibližují. Rychle zhasneš lampu, ale to ti mohlo dát jen krátký okamžik na rozhodnutí."
        jump workshopNightIntruder
    jump workshopNightOptions

label workshopNightIntruder:
    python:
        lastAction = workshop.checked[-1]

    if lastAction == "rubbish":
        "Dveře ven z dílny máš na dosah, nemělo by tedy být těžké vyklouznout ven. Vzpomínáš si také, že pár kroků od tebe je dřevěná lavice, za kterou by ses snad dokázal[a] schovat."
    else:
        "Ke dveřím je to jen několik kroků, které ale v tmavé dílně plné náčiní nemusí být snadné udělat rychle a tiše. Kousek od sebe potom máš koš vrchovatě plný nejrůznějších kůži, za který by ses snad dokázal[a] schovat."

    menu:
        "{i}(Schovat se){/i}":
            "Napůl po paměti skočíš do úkrytu, zaboříš hlavu do nějakého kusu kůže a doufáš, že to bude stačit."
            "Kůže štiplavě páchne a ty se snažíš moc nedýchat, ale zatím nic nespadlo ani nikdo nespustil poplach. Po chvilce se odvážíš otevřít oči a zjistíš, že příhodnou skulinou vidíš, co se v dílně děje."
            "Ze své skrýše pozoruješ, jak do dílny vejde Aachim a potichu za sebou zavře dveře. Jde ke koši se zbytky, chvíli se v něm přehrabuje a pak vyndá neforemný kus materiálu. Až když ho začne upevňovat do čelistí na dřevěné stolici blízko stolku s nástroji, rozpoznáš, že se jedná o rozdělanou botu."
            if "rubbish" in workshop.checked:
                "Právě tu, která tě před chvílí zaujala."
            elif "WIP shoes seen" in status:
                "Tvar té boty ti připadá povědomý a po chvíli přemýšlení si vzpomeneš, kde jsi takovou viděl[a] naposledy. Ta Aachimova má sice jinou barvu a je mnohem méně precizní, ale tvarem se nápadně podobá tomu, na čem pracuje mistr Njal."
            menu:
                "{i}(Promluvit si s Aachimem){/i}":
                    "Pomalu vylezeš z úkrytu."
                    "Při prvním zvuku z tvé strany sebou Aachim trhne a chvíli se zřejmě rozhoduje mezi útěkem a spuštěním poplachu."
                    jump workshopNightMeetingAachim
                "{i}(Čekat na příležitost zmizet){/i}":
                    "Nějakou dobu pozoruješ Aachima při práci a téměř nedýcháš, aby ses náhodou neprozradil[a]."
                    "Aachim chvíli sešívá, pak zamumlá nadávku a část čerstvých stehů zas vytáhne. Přisune si lampu o něco blíž a pokračuje v práci. To se ještě několikrát opakuje."
                    "Už skoro nedoufáš, že Aachim vůbec někdy odejde, když se konečně zvedne a zamíří ke dveřím do domu. Rozdělanou botu nechá na místě."
                    "Na nic nečekáš, tiše vyklouzneš z dílny a zamkneš za sebou vchodové dveře. Pak zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
                    return
        "{i}(Utéct ven z dílny){/i}":
            if lastAction == "rubbish":
                "Vrhneš se ke dveřím, které máš naštěstí téměř za zády. Nahmatáš kliku, pootevřeš je na tak velkou skulinu, aby ses mohl[a] protáhnout, a vyklouzneš ven."
                scene bg heinrich outside dark
                "Zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
                return
            else:
                "Vrhneš se ke dveřím. Sotva ale uděláš dva kroky a vrazíš do nějakého ostrého kusu dřeva ve výšce svého boku. Kousneš se do rtu, abys zastavil[a] nadávku, ale pak se celá ta dřevěná věc překotí s rachotem, který by tvé klení stejně přehlušil."
                "V zápětí se z domu začnou ozývat nové zvuky: rozespalé klení mistra Heinricha, poplašené hlasy učedníků a šramot ještě z dalších míst. Kroky, před kterými jsi předtím prchal[a], se rychle a ostře ozvou naposled a vzápětí do dílny vrazí Aachim s lampou v ruce."
                jump workshopNightAlarm
        "{i}(Promluvit si s příchozím){/i}":
            "Zůstaneš stát na místě a čekáš ten nekonečně dlouhý okamžik, než se pootevřou dveře vedoucí z domu a do dílny vklouzne Aachim s lampou v ruce."
            "Když si tě všimne, vypadá stejně překvapený a vyděšený, jako ty. Udělá jeden krok zpět ke dveřím a chvíli se zřejmě rozhoduje mezi útěkem a spuštěním poplachu."
            jump workshopNightMeetingAachim
    return

label workshopNightAlarm:
    $ son.say("ZLODĚJ! POMOC!", "surprised")
    menu:
        "{i}(Obrátit se na útěk){/i}":
            "Rozběhneš se ke dveřím ven. Ve tmě se nabodneš bokem na roh stolu a narazíš si holeň o ševcovské kopyto, bolest ale sotva vnímáš a teď už nezáleží na tom, kolik hluku naděláš."
            "Aachim udělá několik nerozhodných kroků tvým směrem, nezdá se ale skutečně odhodlaný ti zkřížit cestu. Snadno ho předstihneš."
            scene bg heinrich outside dark
            "Teprve když už běžíš po ulici, uslyšíš, jak se do dílny hrnou další lidé. Několik tváří spatříš i v oknech jiných domů. Máš ale dostatečný náskok."
            "Zahneš za nejbližší roh a brzy se ztratíš komukoli, kdo by tě mohl chtít pronásledovat. Znovu už se do dílny touž noc vracet nechceš, a tak se vydáš spát."
            $ status.append("seen during break in")
            return
        "{i}(Napadnout Aachima){/i}":
            "Vrhneš se na Aachima a ten se sotva stihne připravit k obraně."
            if skill == "combat":
                "Brzy zjistíš, že na rozdíl od tebe se tvůj soupeř moc neumí prát. Snadno ho strhneš pod sebe, uštědříš mu několik tvrdých ran a zaklekneš ho tak, aby nemohl uniknout."
                "Než ale stihneš udělat cokoli dalšího, vběhne do dílny mistr Heinrich a okamžitě se vrhne synovi na pomoc. Oproti Aachimovi je větší a nerozpakuje se ti ublížit a ty brzy zjistíš, že ti je vyrovnaným soupeřem. Když potom do dílny dorazí i zbylí dva učedníci, společnými silami tě přemůžou a ty krátce poté skončíš pevně svázan[y]."
            else:
                "Nepovažuješ se zrovna za rváče, brzy ale zjistíš, že tvůj soupeř se moc neumí prát. Podaří se ti ho dostat na zem a zakleknout ho tak, aby pro něj bylo těžké uniknout."
                "Než ale stihneš udělat cokoli dalšího, vběhne do dílny mistr Heinrich a okamžitě se vrhne synovi na pomoc. Oproti Aachimovi je větší a nerozpakuje se ti ublížit a ty brzy zjistíš, že zápas s ním je nad tvé síly. Když potom do dílny dorazí i zbylí dva učedníci, snadno tě společnými silami udrží na zemi a ty brzy skončíš pevně svázan[y]."
            $ mc.imageParameter = "beaten"
            if not achievement.has(achievement_name['fistfight'].name):
                $ Achievement.add(achievement_name['fistfight'])
            "Až poté mistr Heinrich zvedne Aachimovu lampu a pořádně se na tebe podívá."
            $ victim.say("Ty! Říkal[a] jsi, že jsi z hlídky!", "furious")
            $ mc.say("Já...")
            "Tvou odpověď přeruší tvrdý dopad mistrovy pěsti do tvé tváře."
            $ victim.say("Tohle si s nimi vyřídím. Hlídejte [pronoun4]!", "furious")
            jump workshopNightArrest
        "{i}(Zůstat stát){/i}":
            "Sebevědomě zůstaneš stát na místě, přesvědčen[y], že až ostatní členové domácnosti dorazí, dokážeš vše vysvětlit."
            "Netrvá dlouho a do dílny skutečně vrazí mistr Heinrich."
            $ victim.say("Ty! Co ty tady děláš?", "furious")
            $ mc.say("Pátrám po dalších stopách.")
            $ victim.say("Takhle v noci? Tomu tak věřím. Aachime, pomož mi s [pronoun7]!", "furious")
            "Mistr Heinrich se několika rychlými kroky přesune k tobě, pevně tě chytí za nadloktí a škubne tebou, aby tě vyvedl z rovnováhy. Zpočátku se dokážeš bránit, do zápasu se ale vloží i Aachim a brzy jim přijdou na pomoc i zbylí dva učedníci a ty brzy skončíš pevně svázan[y] na podlaze dílny."
            "Když znovu pohlédneš do mistrovy tváře, zjistíš, že jeho vztek nijak neustoupil. "
            $ victim.say("A oni tvrdili, že mi pomůžeš. Že prý vše skvěle vyšetříš a nemám se ničeho obávat. To si s nimi vyřídím.", "furious")
            $ victim.say("Hlídejte [pronoun4]!", "furious")
            jump workshopNightArrest
    return

label workshopNightArrest:
    "Heinrich několika ráznými kroky přejde ke dveřím. Ačkoli mu svítí jen mihotavé světlo, pohybuje se po dílně s naprostou jistotou."
    $ son.say("A nebudou teď všichni spát?", "surprised")
    $ victim.say("Ne na dlouho.", "furious")
    "Mistr odejde a ty osamíš s jeho učedníky. Vypadají celou událostí zaskočení, ale hlídají tě pozorně a nenechají se vtáhnout do rozhovoru. Prohodí pouze pár slov s Lisbeth, Adou a několika sousedy, když se přijdou ujistit, že je vše v pořádku."
    if "ada confrontation zairis" in status:
        "Jediný z nich, v kom vzbudíš větší zájem, je Ada, která k tobě přejde a chvíli si tě měří nepřátelským pohledem. Zdá se, že váhá, jestli se do tebe pustit slovy, nebo jestli tě rovnou nakopnout."
        "Nakonec ti pouze věnuje opovržlivý pohled a beze slova opět odejde."
    if son.imageParameter == "beaten":
        "Aachim se později nakrátko vzdálí, aby si ošetřil rány, které jsi mu během zápasu uštědřil[a], a opět se vrátí."
    "Jinak okamžiky ubíhají v tichu a klidu. Učedníci zhasnou svítilnu a dílna zůstane ponořená do téměř úplné tmy, se kterou zápasí jen slabé světlo hvězd a pouličních lamp pronikající oknem, které předtím otevřeli."
    "Potom se zvenčí ozve dvojice odhodlaných kroků a dveře se rozrazí."
    $ victim.say("Tak tady [pronoun4] máte. A já doufám, že už [pronoun4] uvidím jenom dvakrát, jednou u soudu a podruhé na popravišti.", "angry")
    $ rauvin.say("Nejdřív všechno musíme prošetřit.")
    $ victim.say("Co prosím vás chcete prošetřovat? Chytili jsme zloděje přímo v mé dílně? Nechcete snad říct, že hlídka se teď vloupává slušným lidem do domů?", "furious")
    $ rauvin.say("Ne, to rozhodně ne. [mcName] tady je bez mého vědomí a být tady nemá.")
    $ rauvin.say("Pomožte mi s [pronoun7], ať to máme za sebou a můžeme jít spát.", "sad")
    $ victim.say("S radostí. Stejně neusnu, dokud [pronoun4] neuvidím bezpečně pod zámkem.", "angry")
    "Oba muži tě chytí každý z jedné strany, společně tě vytáhnou na nohy a začnou tě vést směrem ke dveřím. Rauvin ti připadá bledší než obvykle, ale možná to je jen světlem nebo tím, že musel vstát uprostřed noci."
    scene bg street05 dark
    "Během cesty sotva padne pár slov. Mistr Heinrich je celou dobu o půl kroku napřed a netrpělivě tě táhne kupředu. Rauvin tě drží o poznání méně pevně - skoro ti připadá, že kdyby tě vedl sám, byla by naděje na útěk."
    scene guardhouse dark
    "Ševcovský mistr vás nicméně nemíní nechat samotné a ty brzy opět vstoupíš do strážnice, kde tě jen před pár dny do marendarské městské hlídky přijali."
    scene bg cells entrance
    "Teď ovšem můžeš na svou stěnu s poznámkami vrhnout jen krátký pohled a Rauvin s mistrem Heinrichem tě dovlečou hlouběji, do cel, které byly kdysi tak obávané."
    scene bg cell
    play sound audio.prisonDoorClose
    "Brzy za tebou zaklapne zámek a oba muži opět odejdou."
    $ status.append("arrested during break in")
    jump mcArrested

label workshopNightMeetingAachim:
    # trust too low - Aachim sets the alarm
    if son.trust < 0:
        "Pak si tě lépe prohlédne a s nevírou na tebe zazírá."
        $ son.say("Co tady děláte?", "angry")
        show mcPic at menuImage
        menu:
            "Jenom se snažím pátrat po tom zloději.":
                hide mcPic
                $ son.say("To přece...", "angry")
                "Potom se Aachim konečně rozhodne a prudce se nadechne."
            "{i}(Zamířit ke dveřím ven){/i}":
                hide mcPic
                "Aachim tě okamžik nehnutě sleduje, potom se konečně rozhodne a prudce se nadechne."
            "{i}(Zamířit k němu){/i}":
                "Aachim ustoupí o krok, do něčeho narazí a prudce se nadechne."
        jump workshopNightAlarm
    # trust high enough for conversation
    else:
        "Pak si tě lépe prohlédne a trochu se uklidní."
        $ son.say("Co tady... jak jste se sem vůbec dostal[a]?")
        $ status.append("workshop night conversation start")
        label workshopNightAachimMeetingMenu:
        show mcPic at menuImage
        menu:
            "Bylo odemčeno." if "workshop night conversation start" in status and "own key" not in son.asked and "worshop unlocked" not in son.asked:
                hide mcPic
                $ son.asked.append("workshop unlocked")
                $ son.trust -= 1
                $ son.say("To určitě nebylo, po včerejší krádeži táta dveře dvakrát zkontroloval.", "angry")
                $ son.say("Takže proč se sem zatraceně vloupáváte jako nějaký vyvrhel?", "angry")
            "Na tom asi tak moc nezáleží." if "doesn't matter" not in son.asked:
                hide mcPic
                $ son.asked.append("doesn't matter")
                $ son.trust -= 1
                $ son.say("Já si myslím, že na tom záleží.", "angry")
            "Jednoduše, odemkl jsem si." if "workshop night conversation start" in status and "own key" not in son.asked and gender == "M":
                hide mcPic
                $ son.asked.append("own key")
                $ mc.say("Vyzvedával jsem včera klíč od dílny u mistra Eckharda, tak jsem si nechal zhotovit duplikát.")
                $ son.say("...cože? A... to se smí?", "surprised")
                $ mc.say("Když to je kvůli vyšetřování, tak ano.")
                $ son.say("A... co tady tedy vyšetřujete?", "surprised")
                jump workshopNightAachimMeetingMenu
            "Jednoduše, odemkla jsem si." if "workshop night conversation start" in status and "own key" not in son.asked and gender == "F":
                hide mcPic
                $ son.asked.append("own key")
                $ mc.say("Vyzvedávala jsem včera klíč od dílny u mistra Eckharda, tak jsem si nechala zhotovit duplikát.")
                $ son.say("...cože? A... to se smí?", "surprised")
                $ mc.say("Když to je kvůli vyšetřování, tak ano.")
                $ son.say("A... co tady tedy vyšetřujete?", "surprised")
                jump workshopNightAachimMeetingMenu
            "Jenom se snažím pátrat po tom zloději." if "investigating" not in son.asked:
                hide mcPic
                $ son.asked.append("investigating")
                $ mc.say("Kdyby tady ještě byly nějaké stopy, které jsme dřív přehlédli. Nebo kdyby se ten zloděj zkusil vrátit.")
                $ son.say("A proč je to nutné dělat v noci? Vždyť to vypadá jako vloupání!", "surprised")
            "Zkouším zjistit, jestli tu nezůstalo něco, co by pomohlo Zeranovi." if "helping Zeran" not in son.asked and "Zeran innocent" in clues:
                hide mcPic
                $ son.asked.append("helping Zeran")
                $ son.say("Vážně doufám, že nezůstalo. Proč mu chcete vůbec pomáhat?")
                show mcPic at menuImage
                menu:
                    "Myslím si, že je nevinný.":
                        hide mcPic
                        $ son.trust -= 1
                        $ son.say("A co vás k tomu vede? Že má krásné nevinné oči a tváří se hrozně ublíženě?", "angry")
                        $ son.say("Tomu nevěřte, ten se umí přetvařovat jako nikdo. Byl tady dva roky a nikdo nic netušil. Had jeden zatracený.", "angry")
                        jump workshopNightAachimNotConvinced
                    "Nikdo jiný se ho nezastane.":
                        hide mcPic
                        $ son.trust -= 1
                        $ son.say("A zkoušel[a] jste se zamyslet nad tím, proč? Protože pak by vám bylo jasné, že ten had si žádné zastání nezaslouží.", "angry")
                        $ son.say("O vlastní rodinu přišel, a tak se pokusil procpat do té naší. A zneužil k tomu naivní holku.", "angry")
                        jump workshopNightAachimNotConvinced
                    "Šlo to tehdy nějak moc rychle.":
                        hide mcPic
                        $ mc.say("Bojím se, že kdyby Zeran náhodou mluvil pravdu, stejně by neměl naději tvého otce přesvědčit, protože ten když se rozzlobí, tak už nikoho neposlouchá. Tak se chci radši ujistit.")
                        $ son.say("Poslouchání není jeho silná stránka, to je pravda.", "angry")
                        $ son.say("Myslím, že mrháte časem, ale jestli chcete radši pomáhat Zeranovi než hledat tátovy střevíce... já vám v tom bránit nebudu.")
                        $ son.say("Ale stejně se mi nelíbí představa, že by vás tu někdo viděl.", "angry")
                        jump workshopNightAachimConversation
            "Myslím si, že tvůj otec něco tají." if "Heinrich keeping secrets" not in son.asked:
                hide mcPic
                $ son.asked.append("Heinrich keeping secrets")
                $ son.say("A co, prosím vás? Ten když si něco myslí, hned to všem řekne na plnou hubu a ještě k tomu většinou přidá ránu.")
                $ son.say("To možná brzy poznáte na vlastní kůži, jestli nás tu najde.")
                show mcPic at menuImage
                menu:
                    "Myslím, že provádí nějaké čachry v obchodech.":
                        hide mcPic
                        $ son.say("Prosím? Jaké čachry? To je naprostý nesmysl.", "surprised")
                        $ son.say("Táta je rád, že dokáže obchodovat úplně běžně, aniž by si znepřátelil celé město. Na tohle nemá ani chuť, ani myšlenky.")
                        $ son.say("A hlavně táta je leccos, ale není podvodník a nevráží kudly do zad. Ten na sebe vždycky upozorní, než se do někoho pustí.")
                        jump workshopNightAachimNotConvinced
                    "Zajímalo by mě, jestli má nějaké nepřátele, o kterých se nezmínil.":
                        hide mcPic
                        $ mc.say("Nebo které si sám neuvědomuje.")
                        $ son.say("Takoví možná nějací jsou, ale jak to chcete zjistit tady? To se radši zeptejte Salmy nebo Nirevie.")
                        $ mc.say("Cechmistrovi s ním mají spory, nemuseli by být upřímní, když jde o něj. A Salma nemůže vědět všechno.")
                        $ mc.say("Chtěl[a] jsem jen krátce probrat účetní knihy, obchodní dopisy a jiné papíry, jestli nenarazím na něco podezřelého.")
                        $ son.say("No dobře, to možná dává smysl... ale stejně se mi nelíbí představa, že by vás tu někdo viděl.")
                        jump workshopNightAachimConversation
                    "Napadlo mě, jestli si sem náhodou nevodí společnost.":
                        hide mcPic
                        $ son.trust -= 2
                        $ son.say("Tak to jste vedle, sem si vodí nanejvýš Eckharda a k tomu se hrdě přiznává.")
                        $ son.say("Jestli něco takového dělá, tak někde, kam mu nemůže náhodou vběhnout nějaký učedník a kde nemá manželku jednu stěnu od sebe.")
                        $ son.say("Vážně, co mi to tu vykládáte? Že táta sukničkaří, dělá to na tom nejhloupějším možném místě a ještě se u toho nejspíš nechal okrást?", "angry")
                        $ son.say("To si jděte vyprávět kamarádům do hospody, ale mě s tím neotravuj.", "angry")
                        jump workshopNightAachimNotConvinced
            "Myslím si, že někdo v domě něco tají." if "someone keeping secrets" not in son.asked:
                hide mcPic
                $ son.asked.append("someone keeping secrets")
                $ son.say("Cože? Já ale… chci říct, kdo by… to je přece nesmysl!", "surprised")
                $ son.say("Co to je za hloupé důvody? To máte přece zjistit z rozhovorů, ne z vloupaček!", "angry")
                jump workshopNightAachimNotConvinced

        if "workshop night conversation start" in status:
            $ status.remove("workshop night conversation start")
            jump workshopNightAachimMeetingMenu
        else:
            label workshopNightAachimNotConvinced:
            $ son.say("A vůbec, proč se tady s vámi bavím. Měl[a] byste vypadnout.", "angry")
            "Aachim se významně podívá na dveře a pak zpět na tebe."
            label workshopNightAachimNotConvincedMenu:
            show mcPic at menuImage
            menu:
                "Ale neřekneš nikomu, že jsem tu byl[a]?" if "don't tell" not in son.asked:
                    hide mcPic
                    $ son.asked.append("don't tell")
                    $ son.say("Když zmizíš rychle, tak ne.", "angry")
                "Potřebuju už jenom chvíli." if "just a moment" not in son.asked:
                    hide mcPic
                    $ son.asked.append("just a moment")
                    $ son.say("Chvíli už jste měl[a], to vám musí stačit.", "angry")
                "Máš pravdu, půjdu.":
                    hide mcPic
                    "Aachim přikývne a zvedne lampu tak, aby ti dobře posvítil na cestu ke dveřím."
                    scene bg heinrich outside dark
                    "Zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
                    return
                "Odejdu, až budu já chtít.":
                    hide mcPic
                    $ son.say("Ale...", "surprised")
                    "Aachim na moment zaváhá a potom se prudce nadechne."
                    jump workshopNightAlarm
            jump workshopNightAachimNotConvincedMenu

label workshopNightAachimConversation:
    "Aachim se nervózně rozhlédne po dílně, ale pak se pohledem vrátí zpátky k tobě."
    $ son.say("Co se domluvit, že tady dnes v noci nebyl ani jeden z nás?")
    $ mc.say("To mi přijde pro nás oba nejlepší.")
    "Na chvíli zavládne ticho. Aachim uhne pohledem a pak se na tebe opět nejistě podívá."
    $ mc.say("Co tady děláš ty?")
    $ son.say("Vyrábím. Nebo se o to aspoň snažím.")
    $ mc.say("A to musíš pracovat po celém dni ještě tajně v noci? Čekal[a] bych, že touhle dobou budeš chtít dělat cokoli jiného.")
    $ son.say("Přes den můžu dělat jenom to, co táta nařídí. Chtěl jsem… přinést na slavnosti vlastní výrobek.")
    $ son.say("To učedníci normálně nedělají, ale chtěl jsem to zkusit stejně. Možná jsem doufal, že to na tátu udělá dojem, nebo že mi potom dá aspoň na chvíli pokoj, nebo tak něco… zatracená práce.", "sad")
    if not achievement.has(achievement_name['burglar'].name):
        $ Achievement.add(achievement_name['burglar'])

    call aachimAloneOptions

    label workshopNightConversationEnd:
        queue sound [ audio.woodCreak, audio.doorSlam ]
        "Odněkud z domu se ozve zavrzání a pak bouchnutí dveří. Oba sebou s Aachimem trhnete."
        if actionsTaken == 4:
            $ son.say("Tím se to rozhoduje, vážně byste měl[a] jít. Jestli nás tady někdo chytí, tak to oba šíleně schytáme.")
        else:
            $ son.say("Měl[a] byste jít. Jestli nás tady někdo chytí, tak to oba šíleně schytáme.")
        label workshopNightConversationEndMenu:
        show mcPic at menuImage
        menu:
            "Máš pravdu.":
                hide mcPic
                "Aachim ti posvítí na cestu ke dveřím ven na ulici a zavře za tebou, spíš z nervozity než kvůli tomu, že bys to opravdu potřeboval[a]."
                scene bg heinrich outside dark
                "Zmizíš z místa tak rychlým krokem, jak se jen odvažuješ."
                return
            "A co ty?" if "what about you" not in son.asked:
                hide mcPic
                $ son.asked.append("what about you")
                $ son.say("Já se zkusím vyplížit taky, ale já tady aspoň bydlím.")
                $ son.say("Ale jestli mě tady táta chytí s někým cizím, tak dost možná taky nebudu.")
            "Ještě jsem nenašel, co hledám." if "not found enough" not in son.asked and gender == "M":
                hide mcPic
                $ son.asked.append("not found enough")
                $ son.say("Tady už žádné stopy být nemůžou. Ne po tom, co jsme to tady s klukama prohledali asi desetkrát. A asi pětkrát uklidili, než nám dal táta konečně pokoj.")
            "Ještě jsem nenašla, co hledám." if "not found enough" not in son.asked and gender == "F":
                hide mcPic
                $ son.asked.append("not found enough")
                $ son.say("Tady už žádné stopy být nemůžou. Ne po tom, co jsme to tady s klukama prohledali asi desetkrát. A asi pětkrát uklidili, než nám dal táta konečně pokoj.")
            "Ještě s tebou musím mluvit, můžu zítra přijít?" if "need to talk more" not in son.asked:
                hide mcPic
                $ son.asked.append("need to talk more")
                $ son.say("Třeba. Když to musí být. Ale teď hlavně běžte.")
            "Odejdu, až budu já chtít." if "not found enough" in son.asked or "what about you" in son.asked:
                hide mcPic
                $ son.say("Ale...", "surprised")
                "Aachim na moment zaváhá a potom se prudce nadechne."
                jump workshopNightAlarm
        jump workshopNightConversationEndMenu

label loveLetters:
    if currentLocation == "workshop night":
        scene bg workshop
    elif currentLocation == "victim house":
        call victimHouseInterior
    show sh love letter1
    pause
    hide sh love letter1
    show sh love letter2
    pause
    hide sh love letter2
    show sh love letter3
    pause
    hide sh love letter3
    show sh love letter4
    pause
    hide sh love letter4
    return
