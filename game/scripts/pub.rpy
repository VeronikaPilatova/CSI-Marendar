label pubController:
    call preludeController

    # walk over
    if "pub visited" not in status:
        $ time.addMinutes(30)
    else:
        $ time.addMinutes(15)
    $ currentLocation = "pub"
    $ origAsked = salma.asked.copy()
    call salmaOptionsRemainingCheck

    # visit itself
    if "pub visited" not in status:
        scene bg pub outside
        call pubFirst
    scene bg pub inside
    call pubIntro
    if optionsRemaining > 0:
        call salmaOptions
        call leavingPub

    # adjust time spent and status, create events
    $ time.addMinutes((len(salma.asked) - len(origAsked)) * 3)
    if "add waiting for suspect list" in status:
        $ status.remove("add waiting for suspect list")
        $ newEvent = Event(copy.deepcopy(time), "STATUS", 0, "waiting for suspect list", 3, "info")
        $ newEvent.when.addHours(1)
        $ eventsList.append(newEvent)
    if "ordered drink" in status:
        $ time.addMinutes(20)
        $ status.remove("ordered drink")
    elif "ordered dinner" in status:
        $ time.addMinutes(30)
        $ status.remove("ordered dinner")
    if "pub visited" not in status:
        $ status.append("pub visited")
    return

label pubFirst:
    "Hostinec se ve skutečnosti jmenuje U Splašeného koně, ale běžně se mu říká U Salmy, podle hobitky, která to tu už dlouho vede železnou rukou netrpící jakoukoliv nesnášenlivost."
    return

label pubIntro:
    if time.hours < 17:
        "V tuhle hodinu je hospoda téměř prázdná, jen u jednoho stolu debatují dva staříci o těch zvláštních nových pořádcích. Když vstoupíš, hostinská Salma odloží hadr, kterým právě utírala bar, a s úsměvem se na tebe otočí."
        $ salma.say("Dobré odpoledne. Co si dáte?")
    elif time.hours < 18:
        "Jak se blíží večer, hospoda se začíná pomalu plnit. Můžeš zachytit útržky hovoru o Einionových slavnostech a u jednoho stolu se nejspíš řeší uzavření obchodní smlouvy. Když vstoupíš, hostinská Salma podá dva čerstvě natočené korbely s pivem mladší hobitce a s úsměvem se otočí na tebe."
        $ salma.say("Dobrý večer. Co si dáte?")
    else:
        "V tuhle hodinu je U Salmy živo a mladá hobitka téměř nestačí roznášet jídlo a pití mezi stoly. Většina hostů diskutuje o blížících se Einionových slavnostech a výrobcích, které se na nich mají objevit. Když vstoupíš, hostinská Salma se na tebe usměje, ale věnovat se ti začne až po natočení několika korbelů."
        $ salma.say("Dobrý večer. Co si dáte?")
    call pubOrder
    if optionsRemaining == 0:
        "Chvíli příjemně posedíš, ale pak je čas vrátit se zas k vyšetřování."
        return
    if "ordered drink" in status or "ordered dinner" in status:
        $ mc.say("Můžu se vás ještě na pár věcí zeptat?")
        $ salma.say("Rozhodně to můžete zkusit. Co potřebujete?")
    if "pub visited" not in status:
        $ mc.say("Jsem z městské hlídky a vyšetřuji krádež výrobku z dílny mistra Heinricha. Prý se tu včera večer pohádal s mistrem Rumelinem?")
        "Salma se zamračí."
        $ salma.say("To je slabé slovo. V jednu chvíli jsem se dokonce bála, že dojde ke rvačce. Heinricha potom naštěstí odvedl mistr Eckhard.", "angry")
    return

label pubOrder:
    call salmaOptionsRemainingCheck
    show mcPic at menuImage
    menu:
        "Dám si pivo.":
            hide mcPic
            if "pub visited" not in status:
                $ salma.trust += 1
                $ hayfa.trust += 1
            $ status.append("ordered drink")
            $ salma.say("Samozřejmě, hned to bude.")
            "Salma ti natočí poctivý korbel krásně napěněného piva."
        "Jaké víno máte v nabídce?":
            hide mcPic
            if "pub visited" not in status:
                $ salma.trust += 1
                $ rauvin.trust -= 1
            $ status.append("ordered drink")
            $ salma.say("Nejoblíbenější je červené víno z Chatevinu, ale pokud jste znalec, máme i několik ušlechtilejších odrůd. Můžete si vybrat.")
            "Po chvíli prohlížení různých lahví si vybereš a necháš nalít pohár."
        "Nějakou dobrou pálenku.":
            hide mcPic
            if "pub visited" not in status:
                $ salma.trust += 1
                $ hayfa.trust -= 1
                $ rauvin.trust -= 2
            $ status.append("ordered drink")
            $ salma.say("Samozřejmě, hned to bude.")
            "Hostinská ti nalije."
        "Co nabízíte k večeři?" if time.hours > 17:
            hide mcPic
            if "pub visited" not in status:
                $ salma.trust += 1
            $ status.append("ordered dinner")
            if "second dinner with Salma" in dailyStatus:
                $ salma.say("Panečku, kdy vám naposledy dali najíst? Pečínka ani kaše už nejsou, ale můžeme vám donést ještě placku a nějaké ovoce.", "happy")
                $ salma.say("Ale budu chtít nejdřív vše zaplatit. Nic proti vám, vypadáte důvěryhodně, ale občas návštěvníci zkouší různé kousky.")
                "Dáš hostinské pár mincí, ona spokojeně přikývne a zavolá na jednoho z pomocníků. O chvíli později se k tobě přiblíží jeden z hobitích výrostků s jídlem a zvědavě po tobě pokukuje."
                "Jakmile si ale uvědomí, že o tom víš, odvrátí pohled, rychle před tebe postaví tác a zase zmizí. Ty si tak můžeš v klidu vychutnat svou porci, stejně dobrou jako ty předešlé."
            elif "dinner with Salma" in dailyStatus:
                $ salma.say("Výběr je stejný jako předtím, pečínka, kaše s ovocem, placky, sýr a uzené. Věřím, že dost na to, abychom nasytili i ty nejnáročnější jedlíky.", "happy")
                $ salma.say("Co to tedy bude?")
                "Opět si objednáš a zanedlouho opravdu dostaneš další porci. Obslouží tě jiný hobit než předtím, nicméně i tentokrát to je zřejmě Salmin mladší příbuzný a i tentokrát je chuť jídla vynikající."
                $ dailyStatus.append("second dinner with Salma")
            else:
                $ dailyStatus.append("dinner with Salma")
                $ salma.say("Mám tu uvařenou kaši s ovocem a chlebové placky se sýrem a uzeným masem. Nebo můžete dostat i pečínku, pokud si chcete počkat.")
                "Objednáš si dobrou večeři, kterou ti o něco později donese mladý hobit, podle podobnosti pravděpodobně Salmin přibuzný."
            call dinnerAchievementCheck
        "Můžu vám jenom položit pár otázek?" if len(salma.asked) == len(origAsked) and optionsRemaining > 0:
            hide mcPic
            $ salma.say("Asi podle toho, na co se chcete ptát.")
        "Dnes nic, případ spěchá a nemůžu se zdržet." if len(salma.asked) > len(origAsked) or optionsRemaining == 0:
            hide mcPic
            if salma.trust > 0:
                $ salma.say("No dobře, tak jindy.")
            else:
                $ salma.say("No dobře. Ale jíst je vždycky potřeba, stavte se později aspoň na večeři.")
    return

label salmaOptions:
    call salmaOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Děkuji, velmi jste mi pomohla.")
        return
    show mcPic at menuImage
    menu:
        "Můžete mi popsat tu hádku?" if "pub fight" not in salma.asked:
            hide mcPic
            $ salma.asked.append("pub fight")
            $ salma.say("Mistr Heinrich přišel první. Byl ve výborné náladě, všem se chlubil dokončením výrobku na Einionovy slavnosti, dokonce zaplatil rundu pro celou hospodu. Potom ale přišel mistr Rumelin, Heinrich se zaměřil na něj a Rumelin si až moc potrpí na své pověsti, než aby si to nechal líbit.")
            if "pub fight" in rumelin.asked:
                $ mc.say("Mistr Rumelin říkal, že se pohádali o povinnostech cechmistra?")
                $ salma.say("Ano, a o tom, kdo by jím ideálně měl být.")
            else:
                $ mc.say("O co se hádali?")
                $ salma.say("O vedení cechu.")
            $ salma.say("Heinrich tvrdil, že cech by měl vést ten nejschopnější a že nejlépe to ukážou Einionovy slavnosti, Rumelin zase, že hlava cechu musí především umět mluvit s lidmi. Oba trvali na tom, že nejlepší kandidát jsou oni sami.")
            $ salma.say("Rumelin potom prohlásil, že se osobně postará o to, aby se Heinrich do čela cechu nikdy nedostal a na to se mu Heinrich pokusil dát pěstí.")
            $ salma.say("Naštěstí promáchl. Rumelin chtěl potom chvíli volat hlídku, já ho začala uklidňovat a Heinricha radši odvedl Eckhard.")
        "Kdy potom mistr Rumelin odešel?" if "rumelin alibi" not in salma.asked:
            hide mcPic
            $ salma.asked.append("rumelin alibi")
            $ salma.say("Těsně před zavírací dobou. Rovien pro něj sice přišel dřív, ale potom tady ještě dlouho seděli společně. Ani toho už moc nevypili. Rumelin říkal, že se chce přes usnutím uklidnit.")
            $ rovienNote.isActive = True
        "Je někdo další, s kým se mistr Heinrich pohádal?" if "other fights" not in salma.asked:
            hide mcPic
            $ salma.asked.append("other fights")
            $ merchantNote.isActive = True
            $ salma.say("Většinou prostě pije a baví se se svými přáteli. Asi jediná další hádka, která mě napadá, byla s Karstenem.")
            if kaspar.alreadyMet == True:
                $ mc.say("To mistr Heinrich také pil?")
                "Salma zavrtí hlavou."
                $ salma.say("Ne, sotva stihl přijít. Už někde ve dveřích si všiml, že tu Karsten sedí, a vyjel na něj.")
            $ salma.say("Heinrich mu vyčítal, že mu prodal zmetek, ze kterého se nedá šít, on se bránil, že veškerý materiál osobně kontroluje. Pak si měli tu slušnost vzít si to ven, takže o moc víc jsem neslyšela.")
            $ salma.say("Ale krátce před tou hádkou si na prodej materiálu opravdu připili, bylo to myslím něco zvláštního na zvláštní boty. Já těmhle věcem moc nerozumím.")
        "Kdo další tady včera večer byl?" if "other people" not in salma.asked:
            hide mcPic
            $ salma.asked.append("other people")
            $ salma.say("Z ševcovského cechu co si vzpomínám nikdo další. Jinak jsme měli dost plno, byla tu spousta obchodníků a řemeslníků. Pokud potřebujete jejich jména, můžu se pokusit dát dohromady seznam, ale nějakou dobu mi to zabere.")
            show mcPic at menuImage
            menu:
                "Budu vám vděčn[y].":
                    hide mcPic
                    $ status.append("add waiting for suspect list")
                    $ salma.say("Pošlu pak ten seznam na strážnici hlídky.")
                "To nebude nutné, ale děkuji.":
                    hide mcPic
        "Má mistr Heinrich problémy s pitím nebo sebeovládáním?" if kaspar.alreadyMet == True and "alcoholic" not in salma.asked:
            hide mcPic
            $ salma.asked.append("alcoholic")
            if "alcoholic" not in lisbeth.asked and "alcoholic" not in eckhard.asked:
                $ victim.trust -= 1
            $ salma.say("Tady problémy nedělá, včerejší hádka byla spíš výjimka. Je to cenný zákazník, který mi přináší velmi dobré tržby. A už proto by nebylo slušné říkat cokoli dalšího.", "angry")
            $ mc.say("Chápu. Rozhodně jsem nechtěl[a] drby.")
        "Měl mistr Heinrich svůj výrobek s sebou?" if kaspar.alreadyMet == True and "lost shoes in pub" not in salma.asked:
            hide mcPic
            $ salma.asked.append("lost shoes in pub")
            "Salma pomalu zavrtí hlavou."
            $ salma.say("Neviděla jsem ho nic ukazovat. A s tím, jak dlouho o svých dokonalých střevících Heinrich mluvil, jsem si jistá, že bych si všimla.")
        "Víte něco o vztazích uvnitř ševcovského cechu?" if "guild relations" not in salma.asked:
            hide mcPic
            $ salma.asked.append("guild relations")
            $ salma.say("Dovnitř cechu nevidím a upřímně jsem za to ráda. Vím hlavně o obchodech a smlouvách, které jednotliví mistři uzavřou přímo v mé hospodě a když se nad tím teď zamyslím… těch vlastně možná o něco ubylo.")
        "Kterých obchodů ubylo? Mezi mistry, nebo nějakých jiných?" if "guild relations" in salma.asked and "less deals" not in salma.asked:
            hide mcPic
            $ salma.asked.append("less deals")
            $ salma.say("Mezi ševcovskými mistry a dodavateli materiálu. Hlavně mistr Njal se bavil s různými obchodníky, často jsem už připravovala poháry na formální přiťuknutí a potom k žádnému obchodu nedošlo.")
            $ salma.say("A Rumelin tady objednávky potvrzoval pravidelně, vlastně dost s těmi stejnými lidmi, a taky už delší dobu neuzavřel žádnou na opravdu kvalitní, luxusní zboží. Ale nemusí to vůbec nic znamenat, to jenom když se přímo ptáte.")
            $ mc.say("Smlouvy na prodej se změnily také?")
            $ salma.say("Ty mi přijdou pořád stejné.")
            $ njalNote.isActive = True
        "Napadá vás něco jiného podezřelého včera v noci nebo dnes ráno?" if "anything suspicious" not in salma.asked:
            hide mcPic
            $ salma.asked.append("anything suspicious")
            $ salma.say("Kromě té hádky? Jediná další jenom trochu neobvyklá věc byla, když dnes ráno donesla žebračka Erle opravdu pěkné skleněné lahve a chtěla za ně polévku.")
            $ salma.say("Bylo jich asi šest, od dost dobrého pití a navíc skoro úplně čisté, za ty tady bude mít Erle polévku celý týden. Ale nevidím, jak by tohle mohlo souviset s ukradenými střevíci.")
        "Můžu se zeptat, jak ty lahve vypadaly?" if "anything suspicious" in salma.asked and "anything suspicious" in lisbeth.asked and "bottles description" not in salma.asked:
            hide mcPic
            $ salma.asked.append("bottles description")
            if "lost bottles" in lisbeth.asked:
                $ clues.append("lost bottles")
            $ salma.say("Modrozelené jakoby mramorované sklo, některé vysoké a spíš úzké a několik kulatých s úzkým hrdlem. Vlastně vám je můžu i ukázat, pořád tady jsou.")
        "Kde bych mohl tu žebračku najít?" if "lost bottles" in clues and "erle" not in salma.asked and  gender == "M":
            hide mcPic
            $ salma.asked.append("erle")
            $ salma.say("Přespává obvykle pod starým mostem, myslím, že ji najdete někde kolem řeky.")
            $ erleNote.isActive = True
        "Kde bych mohla tu žebračku najít?" if "lost bottles" in clues and "erle" not in salma.asked and gender == "F":
            hide mcPic
            $ salma.asked.append("erle")
            $ salma.say("Přespává obvykle pod starým mostem, myslím, že ji najdete někde kolem řeky.")
            $ erleNote.isActive = True
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in salma.asked:
            hide mcPic
            $ salma.asked.append("join forces")
            $ status.append("join forces survey")
            $ salma.say("Myslím, že by to především záleželo na tom, kdo by to byl a jaké by k tomu měli důvody. Mohlo by to být považované za skvělý nápad, nebo také za pohodlnost.")
            $ mc.say("Co kdyby se například spojili mistr Heinrich a mistr Njal?")
            $ salma.say("Ti dva? To by rozhodně všechny překvapilo.")
            $ salma.say("Přinejmenším by ani jednoho z nich nikdo nepodezříval z lenosti, to, že to oba jsou velcí pracanti, jim neberou ani jejich nepřátelé. Ale není mi jasné, proč by to dělali, boty jsou přece poměrně malá věc.")
            $ mc.say("Jde o to, že mistr Njal vymyslel nový střih, který by mistr Heinrich zhotovil. Kdyby každý z nich přinesl vlastní dílo, oběma by něco chybělo - Heinrichovi ten nový nápad a Njalovi Heinrichova přesnost. Společně vytvoří něco skoro dokonalého.")
            $ salma.say("Hm… ano, s tímto vysvětlením to dává smysl. Myslím, že by to lidé přijali.")
            $ salma.say("Také myslím, že by to jim oběma mohlo pomoct. Oba mají pověst samorostů, se kterými je těžké vyjít. Teď by ukázali, že se dokážou dohodnout i ve věci, ve které mohou lidé snadno podlehnout osobní ctižádosti.")
            $ salma.say("Chystá se snad něco takového?")
            $ mc.say("To se uvidí na slavnostech, do té doby nemohu nic říct.")
            $ salma.say("V tom případě se budu těšit o to víc.", "happy")
        "Hledám mladého kluka, který by tu prý měl přespávat, ještě se sestrou." if "finding brother" in katrin.asked and "searching for Kilian" not in salma.asked:
            hide mcPic
            $ salma.asked.append("searching for Kilian")
            if "Killian encounter" in status:
                $ mc.say("Asi dvanáct let, hnědé vlasy. Jmenuje se Kilian.")
            if time.days == 2:
                $ salma.say("Vím, koho myslíte. Ani jeden z nich tu od včerejška nebyl. Je to s Katrin tak špatné, jak se povídá?")
            elif time.days == 3:
                $ salma.say("Vím, koho myslíte. Ani jeden z nich tu nebyl už dva dny. Je to s Katrin tak špatné, jak se povídá?")
            else:
                $ salma.say("Vím, koho myslíte. Ani jeden z nich tu nebyl už tři dny. Je to s Katrin tak špatné, jak se povídá?")
            $ mc.say("Vy asi víte lépe než já, co hrozí někomu, kdo v tomhle městě něco málem zapálí.")
            $ salma.say("Trochu doufám, že se z toho nějak dostane. Působili oba jako milí lidé.", "sad")
            if "helping Katrin" in status:
                $ mc.say("Snažím se jí pomoct, ale zatím není nic jisté.")
        "Pokud se tu Kilian ukáže, můžete dát hlídce vědět?" if "searching for Kilian" in salma.asked and "Kilian - let us know" not in salma.asked:
            hide mcPic
            $ salma.asked.append("Kilian - let us know")
            $ salma.say("Co mu vlastně chcete? On s žádným ohněm nemanipuloval.")
            show mcPic at menuImage
            menu:
                "Možná by jeho svědectví mohlo Katrin pomoct.":
                    hide mcPic
                    $ salma.say("Určitě? Je to chudý malý kluk zdaleka a jeho sestra půjde před soud za žhářství. Kolik lidí ho bude poslouchat?")
                    $ mc.say("Já určitě. Třeba si vzpomene na něco, na čem půjde stavět, aniž by to musel opakovat před soudem.")
                    $ salma.say("No, třeba...")
                "I tak to je její komplic.":
                    hide mcPic
                    $ salma.trust -= 1
                    $ hayfa.trust += 1
                    $ salma.say("“Chápu. Buďte bez obav, jakmile se tu nějaký zločinec objeví, hlídka se to hned dozví.", "angry")
                "Katrin by ho mohla chtít vidět.":
                    hide mcPic
                    $ salma.say("Jen pokud ho tím neuvede do nebezpečí, obávám se. A on to nebezpečí může velmi snadno cítit.")
                    $ salma.say("Ale jestli se tu ukáže, promluvím s ním a uvidím, co se dá dělat.")
        "Pokud Kiliana uvidíte, můžete mu aspoň něco vyřídit?" if "searching for Kilian" in salma.asked and "message for Kilian" not in salma.asked:
            hide mcPic
            $ salma.asked.append("message for Kilian")
            $ salma.say("To asi můžu, ale nemůžu vůbec slíbit, že se sem vrátí. Přeci jen ho tady vidělo dost lidí.")
            $ mc.say("I malá šance je lepší než nic.")
            $ salma.say("To máte samozřejmě pravdu.")
            $ salma.say("Co mu chcete vyřídit?")
            label messageForKilianOptions:
            show mcPic at menuImage
            menu:
                "Rád[a] bych s ním mluvil[a] a slibuji, že se mu nic nestane." if "message for Kilian - asking for meeting" not in status and "message for Kilian - meet me or else" not in status and "message for Kilian - get lost" not in status:
                    hide mcPic
                    $ status.append("message for Kilian - asking for meeting")
                    jump messageForKilianContinue
                "Pokud se přihlásí dobrovolně a nebudeme ho muset nahánět po celém městě, bude to polehčující okolnost." if "message for Kilian - meet me or else" not in status and "message for Kilian - asking for meeting" not in status and "message for Kilian - meet me or else" not in status:
                    hide mcPic
                    $ status.append("message for Kilian - meet me or else")
                    jump messageForKilianContinue
                "Snažím se Katrin pomoct." if "message for Kilian - helping Katrin" not in status:
                    hide mcPic
                    $ status.append("message for Kilian - helping Katrin")
                    jump messageForKilianContinue
                "Katrin ho chce vidět." if "message for Kilian - Katrin asking to meet" not in status:
                    hide mcPic
                    $ status.append("message for Kilian - Katrin asking to meet")
                    jump messageForKilianContinue
                "Takové, jako on, v Marendaru nechceme. Jestli nechce dopadnout jako jeho sestra, měl by se klidit." if "message for Kilian - get lost" not in status and "message for Kilian - asking for meeting" not in status and "message for Kilian - meet me or else" not in status:
                    hide mcPic
                    $ status.append("message for Kilian - get lost")
                    jump messageForKilianContinue
                "Ne, to už je všechno." if any("message for Kilian -" in str for str in status):
                    hide mcPic
                    $ salma.say("Dobře. Jestli se objeví, tak mu to předám.")
        "Všimla jste si na Katrin a jejím bratrovi něčeho zvláštního?" if "searching for Kilian" in salma.asked and "about Katrin and Kilian" not in salma.asked:
            hide mcPic
            $ salma.asked.append("about Katrin and Kilian")
            $ salma.say("Moc ne. Jsou poměrně mladí na to, že cestují sami, ale to pořád není tak neobvyklé.")
            $ salma.say("Na komedianty jsou hodně tiší, většinu času se drželi stranou. Takových jako oni většinou bývá plná místnost. Ale každý jsme nějaký a možná to je jenom nezkušenost.")
            $ salma.say("Rozhodně jsem si na nich nevšimla ničeho špatného.")
        "Byla byste ochotná svědčit ve prospěch Katrin u soudu?" if "about Katrin and Kilian" in salma.asked and "testify for dancer" not in salma.asked:
            hide mcPic
            $ salma.asked.append("testify for dancer")
            $ salma.say("Já u té události přece nebyla. K čemu to bude dobré?", "surprised")
            $ salma.say("Můžu říct, že mi nepřipadala ničím podezřelá, ale nemyslím, že to samo o sobě soud obměkčí.")
            $ salma.say("Na to potřebujete najít někoho, kdo sám viděl, jestli se něčeho dopustila.")
            $ mc.say("A napadá vás někdo takový?")
            $ salma.say("Bohužel. Samozřejmě se tu o tom požáru už mluvilo, ale samé zveličené historky ze třetí ruky a opilecké tlachy. Nic, co by vám pomohlo.")
        "Můžete u soudu s Katrin aspoň poukázat na to, že o její odsouzení nejvíc usiluje Hayfa." if "testify for dancer" in salma.asked and "testify for dancer 2" not in salma.asked:
            hide mcPic
            $ salma.asked.append("testify for dancer 2")
            $ salma.say("Myslíte, že to pomůže?")
            show mcPic at menuImage
            menu:
                "Hayfa je pochybná sektářka, možná tím sleduje vlastní zájmy." if "hayfa's past" in globalClues:
                    hide mcPic
                    $ salma.say("Myslíte? Co ji znám, dělá pro město první poslední a dost mu tím pomáhá. To je pro mě to hlavní.")
                    $ mc.say("To je možné. Ale není to zvláštní, takový výrazný obrat?")
                    $ mc.say("Původně měla s městem úplně jiné plány a změnila je, až když ji chytili a poslali před soud.")
                    $ mc.say("Sekta jako taková sice padla, ale Hayfa pořád může usilovat o co největší moc pro sebe.")
                    $ salma.say("To ano. Je pravda, že už jsem nad jejím chováním přemýšlela i dřív.")
                    $ salma.say("Městu pomáhá a to je dobře, ale co ji k tomu vede, těžko říct.")
                    $ mc.say("Právě. Nechme ji tedy pomáhat, ale nemyslím si, že by měla rozhodovat o něčím životě. Ani že by někdo měl být odsouzený jen na základě obžaloby od ní.")
                    $ salma.say("To by raději neměl, ano. Zkusím soudu připomenout, ať na to myslí.")
                    $ salma.asked.appen("testimony promised")
                    $ katrin.cluesAgainst += 1
                "Všiml[a] jsem si, že Hayfa oheň prožívá nezvykle silně.":
                    hide mcPic
                    if "Hayfa experienced fire" in sabri.asked:
                        $ mc.say("To by se dalo chápat u někoho, kdo místní požár zažil, Hayfa ale přišla do města až asi rok po něm.")
                        $ salma.say("To je vlastně pravda... myslíte, že město mohla i v tomhle tak rychle vzít za vlastní?")
                        $ mc.say("Možná. Nebo ho za vlastní nevzala a jen se snaží zalíbit.")
                        $ salma.say("Co nejsilněji vystoupit proti Katrin je rozhodně způsob, jak se zalíbit. A určitě by chudák holka neměla být potrestaná jen kvůli tomu.")
                        $ salma.say("Zkusím soudu připomenout, že by se neměl nechat unést.")
                        $ salma.asked.appen("testimony promised")
                        $ katrin.cluesAgainst += 1
                    else:
                        $ salma.say("To v tomhle městě není nic zvláštního.")
                        $ salma.say("Hayfa má velmi pochybnou minulost a ne každý věří její proklamované lásce k Marendaru, ale zrovna přístup k ohni jí tu nikdo vyčítat nebude.")
                "Vlastně asi ne, jen mne to napadlo.":
                    hide mcPic
                    $ salma.say("Máte trochu zvláštní nápady, ale dobře, nechme to být.")

        "Děkuji, velmi jste mi pomohla.":
            hide mcPic
            return
    jump salmaOptions

label leavingPub:
    if "ordered drink" not in status and "ordered dinner" not in status:
        $ salma.say("Pořád si nic nedáte?")
        call pubOrder
    elif "ordered drink" in status:
        $ salma.say("Kdybyste chtěl[a] dolít, stačí říct.")
        $ mc.say("Děkuji, ale měl[a] bych se vrátit k případu.")
        $ salma.say("Na shledanou a stavte se někdy na večeři.")
        $ status.remove("ordered drink")
    elif "ordered dinner" in status:
        "V klidu dojíš a pak se vrátíš k vyšetřování svého případu."
        $ status.remove("ordered dinner")
    return

label messageForKilianContinue:
    $ salma.say("Rozumím. Ještě něco dalšího?")
    jump messageForKilianOptions

###

label salmaOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "pub fight" not in salma.asked:
        $ optionsRemaining += 1
    if "rumelin alibi" not in salma.asked:
        $ optionsRemaining += 1
    if "other fights" not in salma.asked:
        $ optionsRemaining += 1
    if "other people" not in salma.asked:
        $ optionsRemaining += 1
    if kaspar.alreadyMet == True and "alcoholic" not in salma.asked:
        $ optionsRemaining += 1
    if kaspar.alreadyMet == True and "lost shoes in pub" not in salma.asked:
        $ optionsRemaining += 1
    if "guild relations" not in salma.asked:
        $ optionsRemaining += 1
    if "guild relations" in salma.asked and "less deals" not in salma.asked:
        $ optionsRemaining += 1
    if "anything suspicious" not in salma.asked:
        $ optionsRemaining += 1
    if "anything suspicious" in salma.asked and "anything suspicious" in lisbeth.asked and "bottles description" not in salma.asked:
        $ optionsRemaining += 1
    if "lost bottles" in clues and "erle" not in salma.asked:
        $ optionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in salma.asked:
        $ optionsRemaining += 1
    if "finding brother" in katrin.asked and "searching for Kilian" not in salma.asked:
        $ optionsRemaining += 1
    if "searching for Kilian" in salma.asked and "Kilian - let us know" not in salma.asked:
        $ optionsRemaining += 1
    if "searching for Kilian" in salma.asked and "message for Kilian" not in salma.asked:
        $ optionsRemaining += 1
    if "searching for Kilian" in salma.asked and "about Katrin and Kilian" not in salma.asked:
        $ optionsRemaining += 1
    if "about Katrin and Kilian" in salma.asked and "testify for dancer" not in salma.asked:
        $ optionsRemaining += 1
    if "testify for dancer" in salma.asked and "testify for dancer 2" not in salma.asked:
        $ optionsRemaining += 1
    return
