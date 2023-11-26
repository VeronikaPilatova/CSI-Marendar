label zairisController:
    $ origAsked = zairis.asked.copy()
    call zairisOptions

    # adjust time spent
    $ zairis.alreadyMet = True
    $ time.addMinutes((len(zairis.asked) - len(origAsked)) * 3)
    return

label zairisOptions:
    call zairisOptionsRemainingCheck
    if zairisOptionsRemaining == 0:
        $ mc.say("To je všechno, na co jsem se chtěl[a] zeptat.")
        return

    show mcPic at menuImage
    menu:
        "Co se ti stalo?" if zairis.imageParameter == "beaten" and "beaten up" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("beaten up")
            $ zairis.say("Stal se mi Heinrich.", "angry")
            if "Ada confronts Zairis" in status:
                $ zairis.say("Ada mě přesvědčila, abych si s ním šel promluvit, ale ten surovec umí mluvit jen pěstmi. Ani mě nepustil ke slovu.", "angry")
            else:
                $ zairis.say("Jak jsi říkal[a], že si s ním mám promluvit... tak ten surovec umí mluvit jen pěstmi. Ani mě nepustil ke slovu.", "angry")
            show mcPic at menuImage
            menu:
                "Doufal jsem, že to vezme lépe." if "Ada confronts Zairis" not in status and gender == "M":
                    hide mcPic
                    $ zairis.say("To já také. Nechápu, jak může mít takový hrubián takovou dceru, jako je Ada.", "angry")
                "Doufala jsem, že to vezme lépe." if "Ada confronts Zairis" not in status and gender == "F":
                    hide mcPic
                    $ zairis.say("To já také. Nechápu, jak může mít takový hrubián takovou dceru, jako je Ada.", "angry")
                "Dost mu na Adě záleží.":
                    hide mcPic
                    $ zairis.trust -= 1
                    $ zairis.say("To může tvrdit, ale kdyby mu na ní záleželo opravdu, pak by ji nechal jít za svým srdcem. Ona není jeho majetek, aby si ji mohl zamknout někam do truhly.", "angry")
                    $ zairis.say("A ze mě dělá div ne zločince, jen za to, že jí skutečně rozumím a chci jí dát vše, po čem její srdce touží.", "angry")
                "Mám ho zatknout za napadení?":
                    hide mcPic
                    "Zairis rozhodně zavrtí hlavou."
                    $ zairis.say("To by všechno jenom zhoršilo. Můj otec by se nejspíš postavil na Heinrichovu stranu, velká část města také... tahle hloupá doba nemá žádné pochopení pro upřímné city.", "sad")
        "Zajímáš se i o psaní poezie?" if "poetry" not in zairis.asked:
            call poetry
        "Kolik toho víš o obchodech svého otce?" if "less deals details" in njal.asked and "business knowledge" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("business knowledge")
            $ zairis.say("Jsem jeho pravá ruka, jednou mám všechny obchodní kontakty převzít. Co potřebujete vědět?")
        "Víš, proč tvůj otec přestal dodávat materiál mistru Njalovi?" if "business knowledge" in zairis.asked and "njal deals" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("njal deals")
            $ zairis.say("O tom slyším poprvé. Ale nejsem u všech obchodů, asi mi to zrovna uniklo.")
        "Víš něco o hromadných nákupech materiálu pro ševcovský cech?" if "business knowledge" in zairis.asked and ("rumelin reasons" in lotte.asked or "njal deals" in rovien.asked) and "bulk orders" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("bulk orders")
            $ zairis.say("Vím, že se o tom občas uvažovalo, ale je hrozně těžké to udělat tak, aby to fungovalo. Mistrů je příliš mnoho, prodávajících také, každý má trochu jiné zboží a jiné představy...")
            $ zairis.say("Co říkal otec, každý včetně mého strýce od té myšlenky rychle zas upustil.")
            $ mc.say("Takže není pravda, že se o to tvůj strýc teď pokouší?")
            $ zairis.say("To někdo říkal? Kdo?")
            if "bulk orders" in rumelin.asked:
                $ mc.say("Tvůj strýc osobně.")
                $ zairis.say("A jak řeší všechny ty… no dobře, on je tady ten nejzkušenější...", "surprised")
            elif "njal deals" in rovien.asked:
                $ mc.say("Tvůj otec.")
                $ zairis.say("To je zvláštní, čekal bych, že o něčem podobném by mi otec řekl... jste si jist[y], že jste to správně pochopil[a]?")
                $ mc.say("Jsem si jist[y]. Doslova říkal, že cechmistr Rumelin se rozhodl, že některý luxusní materiál bude lepší nakupovat pro celý cech najednou.")
                $ zairis.say("Pak je možné, že jsou ty plány ještě hodně v počátcích a možná se to týká jen jednoho nebo dvou druhů zboží.")
            elif "rumelin reasons" in lotte.asked:
                $ mc.say("Karstenova manželka Lotte.")
                $ zairis.say("To se musela splést, strýc má hodně zkušeností a všechny ty problémy velmi dobře zná.")
        "Znáš se s dcerou mistra Heinricha?" if "Ada's boyfriend" in lisbeth.asked and "Ada" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("Ada")
            $ zairis.say("S Adou? Občas se vídáme, na cechovních setkáních, na různých slavnostech a podobně. Proč?")
        "Ada, dcera mistra Heinricha, prý dostala nějaké básně a potřeboval bych názor, od koho tak mohly být." if "poetry" in zairis.asked and "poetry for Ada" not in zairis.asked:
            call poetryForAda
        "Byl jsi někdy u Amadisova hrobu?" if ("letters for Ada seen" in status or "letters topic" in ada.asked) and "Amadis grave" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("Amadis grave")
            $ zairis.say("Jednou jsem měl to štěstí. Je to úžasné místo.", "smile")
            $ zairis.say("Tedy, byl jsem u hrobu toho Amadise, který se vrátil, aby nás zachránil před krvavou lázní, kterou chtěl rozpoutat Hans z Dlouhopolska a jeho povstalecká chátra.")
            $ zairis.say("Chtěl bych se někdy dostat i ke hrobu prvního Amadise, ale tak daleko zatím můj otec necestoval.")
        "Mohl bys mi něco napsat, jen jako ukázku, jak píšeš?" if "letters for Ada seen" in status and "Zairis writing sample" not in status:
            hide mcPic
            $ zairis.say("Ehm… myslíte báseň na zakázku? To by asi chvíli trvalo.", "surprised")
            $ mc.say("Ne, myslím několik libovolných vět. Jde mi pouze o rukopis.")
            $ zairis.say("A k čemu to bude dobré? Můžu vás ubezpečit, že píšu poměrně úhledně, také mě v tom dost dlouho cepovali.", "surprised")
            $ mc.say("Chci si tvůj rukopis porovnat s jinými dokumenty a ověřit autorství.")
            $ zairis.say("Prosím. Ale ujišťuji vás, že cizí báseň bych si nikdy nepřisvojil.", "angry")
            if "stolen poetry" in zairis.asked:
                $ zairis.say("Na rozdíl od někoho.")
            "Mladý elf zmizí v domě a po chvilce ti přinese lístek s pár napsanými řádky."
            show sh zairis quote at truecenter
            pause
            hide sh zairis quote
            $ status.append("Zairis writing sample")
        "Jak vlastně dopadlo tvoje čekání na Jarní madrigaly?" if "book" in zairis.asked and "Rovien house visited" in status and "book 2" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("book 2")
            $ zairis.trust += 1
            $ zairis.say("Poslíček nakonec dorazil. Prý se u brány jeden kupec před ním snad půl dne dohadoval o výšce cla. Nakonec ho prý zaplatil, ale prohlašoval u toho, že to tak nenechá a bude si stěžovat.")
        "Mohl[a] bych si ještě promluvit s tvým otcem?":
            hide mcPic
            $ zairis.say("Předpokládám, že ano. Dojdu se ho zeptat.")
            "Mladý elf se otočí a na chvíli zmizí do jiné místnosti. Slyšíš tlumený rozhovor a pak Zairise vystřídá jeho otec."
            jump rovienController
        "To je všechno, na co jsem se chtěl[a] zeptat.":
            return
    jump zairisOptions

label poetry:
    hide mcPic
    $ zairis.asked.append("poetry")
    $ zairis.say("No, snažím se, ale nejsem ještě žádný Amadis. Jak to ale souvisí s vyšetřováním?")
    show mcPic at menuImage
    menu:
        "Nijak, ale zajímá mě to.":
            hide mcPic
            $ zairis.trust += 1
            $ zairis.say("Poezie je má největší vášeň. Moje vlastní díla ale zatím nejsou srovnatelná se skutečnými známými básníky. Bohužel je těžké najít svůj osobní styl bez dostatečného množství studia a až příliš mnoho vzácných děl nepřežilo požár knihovny.")
            $ zairis.say("Měli jsme i několik skutečně starých elfích básní, možná dokonce až z doby založení města… Paní Luisa dělá co může, ale město jí nejspíš nedává tolik prostředků, kolik potřebuje.", "sad")
            $ zairis.say("Ale snažím se číst vše, k čemu se jen mám možnost dostat. Teď nedávno jsem například narazil na sonety tvořené dialogem. Dva hlasy, které dohromady tvoří dokonalou harmonii, a básníkova práce s rytmem byla...")
            "Zairis se zarazí."
            $ zairis.say("Ale takové podrobnosti vás jistě nebudou zajímat a budete se chtít vrátit k vašemu vyšetřování.")
            show mcPic at menuImage
            menu:
                "Máš pravdu, to bychom měli.":
                    hide mcPic
                "Zajímá mě to velmi.":
                    hide mcPic
                    $ zairis.trust += 3
                    if race == "dwarf":
                        $ mc.say("Dostal ses někdy i k našim ságám?")
                        $ zairis.say("Sepsaným ne, ale jednou jsem měl tu čest být u přednesu jedné z nich, v hospodě v Altenbüren.")
                        $ zairis.say("Sága samotná byla o skupině trpaslíků, kteří žili kousek odtud v Chatevinu a rozhodli se bránit svůj domov před povstaleckou armádou, a jejímu autorovi se nějak podařilo i z obyčejných životních situací udělat téměř hrdinské činy hodné obdivu. A celková atmosféra přednesu a obecenstva působila skoro jako na bohoslužbě.")
                        $ mc.say("To vlastně nejsi tak daleko od pravdy...")
                        $ zairis.say("Asi nejvíc mě fascinovala práce s rytmem...")
                        "Debatou o trpasličích ságách a jejich vztahem k jiným druhům poezie strávíte mnohem víc času, než jsi původně plánoval[a]. Pak vás ale přeruší Rovien, který Zairise pošle vrátit se ke skutečné práci."
                    else:
                        "Debatou o různých druzích poezie a oblíbených autorech strávíte mnohem víc času, než jsi původně plánoval[a]. Pak vás ale přeruší Rovien, který Zairise pošle vrátit se ke skutečné práci."
                    $ time.addHours(2)
                    return
        "Taky se snažím psát...":
            hide mcPic
            $ zairis.trust += 2
            $ zairis.say("Opravdu! To je úžasné! Ne každý v tom vidí smysl, přitom umění je to, co dává našim životům hloubku.", "surprised")
            $ zairis.say("A že je básník v hlídce, to je ještě lepší.", "happy")
            $ zairis.say("Můžu si od vás něco přečíst?")
            show mcPic at menuImage
            menu:
                "Zatím píšu hodně špatně, styděl[a] bych se to komukoli ukázat...":
                    call mcBadPoet
                "Jistě, ale nemám teď nic u sebe.":
                    hide mcPic
                    $ zairis.say("Jistě, to je v pořádku. Přineste něco prosím, jakmile budete moct.", "happy")
                    $ zairis.say("Marendarskou knihovnu se po požáru ještě bohužel nepodařilo vybavit tak, jak by si zasloužila. Bude skvělé dostat se k básním, které jsem ještě nečetl.", "happy")
            $ status.append("promised poetry")
        "Ada, dcera mistra Heinricha, prý dostala nějaké básně a potřeboval bych názor, od koho tak mohly být.":
            label poetryForAda:
                hide mcPic
                $ mc.say("Styl, kvalita a tak.")
                $ zairis.say("Ehm... vy máte její básně? Jak...", "surprised")
                $ zairis.say("Chci říct, jestli tady někdo další píše básně, tak mě to zajímá, moc spřízněných duší ve městě neznám, ale proč na tom záleží hlídce?")
                show mcPic at menuImage
                menu:
                    "Autor těch dopisů by mohl být podezřelý z krádeže v Heinrichově dílně.":
                        hide mcPic
                        $ zairis.trust -= 1
                        $ zairis.say("...jako že někdo psal Adě dopisy, dal si s ní dostaveníčko v domě jejích rodičů a pak toho využil, aby se dostal do dílny?")
                        $ zairis.say("Nebo že ji přesvědčil, aby mu odemkla?")
                        $ zairis.say("To je falešná stopa, to by neudělala.")
                        $ mc.say("I tak by mě ale zajímalo, kdo jí ty básně psal.")
                        $ zairis.say("Upřímně řečeno, příliš se mi nechce zkoumat něčí intimní korespondenci jen proto, že vás to zajímá.")
                    "Mistr Heinrich za to vyhodil svého učedníka, tak mě zajímá, jestli právem.":
                        hide mcPic
                        "Zairis odvrátí pohled a na chvíli se odmlčí."
                        $ zairis.say("To byla nešťastná událost. Už to, že Zeran skončil u mistra jako Heinrich, který nikdy nepochopí citlivou elfí duši.", "sad")
                        $ zairis.say("Bylo by mnohem lepší, kdyby ho k sobě tehdy vzal strýc, ale ten prý neměl v dílně místo...", "sad")
                        $ mc.say("Minulost už nezměníme, ale pokud je šance ho očistit, chtěl[a] bych to udělat. A ty dopisy jsou jediná věc, kterou máme v rukou.")
                        $ mc.say("A kvůli které se na něj Heinrich rozzuřil.")
                        $ zairis.say("Já ale Zerana neznám nijak dobře. Nemyslím si, že bych dokázal poznat jeho styl.")
                $ zairis.asked.append("poetry for Ada")
                return
    return

label mcBadPoet:
    hide mcPic
    $ zairis.say("To je ale jediný způsob, jak se to naučit. Buďte bez obav, jsme ve stejné situaci, přece se nebudeme navzájem shazovat.", "happy")
    $ zairis.say("Navíc marendarskou knihovnu se po požáru ještě bohužel nepodařilo vybavit tak, jak by si zasloužila. Bude skvělé dostat se k básním, které jsem ještě nečetl.", "happy")
    $ mc.say("Zamyslím se nad tím, ale nic neslibuji.")
    return

label mcPoemReaction:
    "Podáš Zairisovi list papíru a ten se dychtivě pustí do čtení."
    if "poem stolen" in status:
        "Skoro okamžitě se ale jeho výraz změní."
        $ zairis.say("To je Théodore de Banville. Jeho básně znám velmi dobře.", "angry")
    return

###

label zairisOptionsRemainingCheck:
    $ zairisOptionsRemaining = 0
    if "poetry" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "less deals details" in njal.asked and "business knowledge" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "business knowledge" in zairis.asked and "njal deals" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "business knowledge" in zairis.asked and ("rumelin reasons" in lotte.asked or "njal deals" in rovien.asked) and "bulk orders" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "Ada's boyfriend" in lisbeth.asked and "Ada" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "poetry" in zairis.asked and "poetry for Ada" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "letters for Ada seen" in status and "Amadis grave" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if zairis.imageParameter == "beaten" and "beaten up" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "letters for Ada seen" in status and "Zairis writing sample" not in status:
        $ zairisOptionsRemaining += 1
    if "book" in zairis.asked and "Rovien house visited" in status and "book 2" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    return
