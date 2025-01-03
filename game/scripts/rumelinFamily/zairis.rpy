label zairisController:
    $ origAsked = zairis.asked.copy()
    call zairisOptions

    # adjust time spent
    $ zairis.alreadyMet = True
    $ time.addMinutes((len(zairis.asked) - len(origAsked)) * 3)
    return

label zairisOptions:
    call zairisOptionsRemainingCheck
    call rovienOptionsRemainingCheck
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
                "Doufal[a] jsem, že to vezme lépe." if "Ada confronts Zairis" not in status:
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
        "Zajímáš se i o psaní poezie?" if "letters for Ada seen" in status and "poetry" not in zairis.asked:
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
        "Znáš Zerana?" if "Zeran offense" in clues and "zeran" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("zeran")
            $ zairis.say("Trochu, ale vlastně jsme se nikdy moc nebavili. Proč?")
            show mcPic at menuImage
            menu:
                "Čekal[a] bych to. Jste oba elfové podobného věku, pohybovali jste se ve stejných kruzích...":
                    hide mcPic
                    $ zairis.say("No, ano, dřív jsme se občas potkali, třeba jsme chodívali ke stejnému učiteli...")
                    $ zairis.ay("Ale to už je dávno. Posledních pár let se mnou Zeran nemluví a já se ho doprošovat nebudu.", "angry")
                    $ mc.say("A proč jste se takto rozkmotřili?")
                    $ zairis.say("To se ptejte jeho. Mě ten zoufalec nezajímá.", "angry")
                    $ mc.say("Proč zoufalec?")
                    $ zairis.say("Tak já nevím, asi špatné slovo. Prostě mě nezajímá. Dlouho jsme se neviděli a nechci na tom nic měnit, na to má moc průšvihů.", "angry")
                    $ zairis.say("Nejradši bych na něj úplně zapomněl.")
                "Myslím si, že byl vyhozený neprávem, a chtěl[a] bych ho očistit.":
                    hide mcPic
                    $ zairis.say("Neprávem? Proč? Mistr Heinrich si tím přece byl hodně jistý. A nikdo jiný to také nezpochybňoval.")
                    if "Ada's boyfriend" in lisbeth.asked or "Zeran" in ada.asked or "Ada" in zeran.asked:
                        show mcPic at menuImage
                        menu:
                            "Ada říkala, že to bylo jinak." if "Ada's boyfriend" in lisbeth.asked or "Zeran" in ada.asked:
                                hide mcPic
                                $ zairis.say("Ada je v tom nevinně a měla by na to co nejdřív zapomenout. Jen ji to zbytečně trápí a to si nezaslouží.")
                                $ zairis.say("Asi mu chtěla pomoct, protože je prostě hodná. I když ty dopisy psal on. Nic víc v tom není.")
                                $ zairis.say("Být vámi se tím už nezabývám. Hlídka má určitě důležitější starosti než rozrušovat mladé dívky. Zvlášť když to je úplně zbytečné.")
                                $ zairis.asked.append("Zairis mentioned letters")
                            "Zpochybňoval to Zeran." if "Ada" in zeran.asked:
                                hide mcPic
                                $ zairis.say("No samozřejmě, že ten to popíral. Šlo mu o vyhazov, tak to zkusil. Tomu se přece nedá věřit.", "angry")
                                $ mc.say("Jsou lidi, co by se přiznali, třeba protože by svou lásku nechtěli zapírat.")
                                $ zairis.say("To... samozřejmě. Asi by to bylo správně, když už... když už. Ale rýpat do toho vyhazovu jen kvůli tomu, že Zeran mezi tyhle lidi možná patří, no já nevím.")
                            "Některé okolnosti mi na tom nesedí.":
                                hide mcPic
                                label zairisZeranInnocentTestingWaters:
                                $ zairis.say("Proč nesedí? Vždyť je to úplně jasné. Prostě si vyhodit zasloužil. Všechno to udělal a nikoho si neváží. Na tom není, co zkoumat.", "angry")
                                $ zairis.say("Samozřejmě nechci radit, čím se má hlídka zabývat. Ale tady není nic ke zjišťování. Vůbec.", "angry")
                    else:
                        $ mc.say("Některé okolnosti mi na tom nesedí.")
                        jump zairisZeranInnocentTestingWaters
        "Odkud víš, že Ada ty básně dostala v dopisech?" if "Zairis mentioned letters" in zairis.asked and "letters for Ada" not in zairis.asked and "what letters" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("what letters")
            $ zairis.say("Nevím! Nikdy jsem je neviděl!", "surprised")
            $ zairis.say("Asi jsem to někde zaslechl? Mluvilo se o tom tehdy hodně.")
            $ mc.say("Nevypadáš jako někdo, kdo rád poslouchá drby.")
            $ zairis.say("To nejsem! Nebo jsem to možná neslyšel, ale přišlo mi to přirozené, psát to v dopisu, a zrovna jsem to uhodl.")
            $ zairis.say("Když jsou ty klepy všude, co mám dělat? Nedá se jim vyhnout.")
        "Znáš se s dcerou mistra Heinricha?" if ("Ada's boyfriend" in lisbeth.asked or "zeran" in zairis.asked) and "Ada" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("Ada")
            $ zairis.say("S Adou? Občas se vídáme, na cechovních setkáních, na různých slavnostech a podobně. Proč?")
            $ mc.say("No, o tom, proč mistr Heinrich vyhodil Zerana, jsi předpokládám slyšel?")
            $ zairis.say("Samozřejmě. O tom tehdy v ševcovském cechu klevetili všichni.")
            show mcPic at menuImage
            menu:
                "Ada prý říkala, že ji nesváděl Zeran, ale ty." if "Zairis mentioned" in lisbeth.asked:
                    hide mcPic
                    $ zairis.say("Já že jsem někoho sváděl? Za koho mě máte? Myslíte snad, že bych jen tak z rozmaru ohrozil čest mladé dívky? To si vyprošuji!", "angry")
                "Ada prý říkala, že ty básně dostala od tebe, a ne od Zerana." if "Zairis mentioned" in lisbeth.asked:
                    hide mcPic
                    $ zairis.asked.append("letters for Ada")
                    $ zairis.say("...")
                "Chtěl[a] bych Zerana očistit. Napadá tě, kdo jiný by mohl Adu milovat?":
                    hide mcPic
                    $ mc.say("A hlavně kdo by ji mohl okouzlit?")
                    $ zairis.say("No, milovat ji jistě bude spousta mužů, je to dívka s jasnýma očima a citlivou duší, pro kterou je toto město malé.")
                    $ zairis.say("Tedy, co tak mohu soudit z toho, jak ji znám. Nesetkáváme se bohužel moc často. Ne tolik, jak... no to je jedno.")
                    $ zairis.say("Ale okouzlit ji? To už je něco jiného. To by myslím dokázal jen někdo dostatečně vnímavý k její touze po romantice a dobrodružství.")
                    $ zairis.say("To většina zdejších balíků není.")
                    show mcPic at menuImage
                    menu:
                        "Zeran by to dokázal?":
                            hide mcPic
                            $ zairis.say("No to nevím. Vždy mi přišel hodně přízemní.")
                            $ zairis.say("Ale kde je řečeno, že ji opravdu okouzlil? Už jestli se o to jen neúspěšně pokoušel, je to víc, než na co měl právo.", "angry")
                            $ zairis.say("Možná tím hůř, muselo pro ni být únavné ho pořád odmítat. Dostal, co si zasloužil.", "angry")
                        "Takže někdo jako ty?":
                            hide mcPic
                            $ zairis.say("No, nevím, jestli je vhodné, abych na to odpovídal. Nechtěl bych být nařčen ani z pýchy, ani z falešné skromnosti.")
                            $ zairis.say("Ale jestli je to potřeba k vyšetřování, no, ano, myslím, že bych to mohl dokázat.", "happy")
                            $ zairis.say("Kdyby k tomu byla příležitost a kdybych něco podobného měl v úmyslu, samozřejmě.")
                        "Znáš někoho takového?":
                            hide mcPic
                            $ zairis.say("Upřímně, nechtěl bych nikoho tímto způsobem hodnotit. Co kdybych mu křivdil. To by nebylo správné.")
                            $ zairis.say("Ale nenapadá mě nikdo, o kom bych si byl jistý, že to dokáže.")
        "Ada, dcera mistra Heinricha, dostala nějaké básně a já bych potřeboval[a] bych názor, od koho tak mohly být." if "poetry" in zairis.asked and "poetry for Ada" not in zairis.asked:
            call poetryForAda
        "Byl jsi někdy u Amadisova hrobu?" if ("letters for Ada seen" in status or "letters topic" in ada.asked) and "Amadis grave" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("Amadis grave")
            $ zairis.say("Jednou jsem měl to štěstí. Je to úžasné místo.", "smile")
            $ zairis.say("Tedy, byl jsem u hrobu toho Amadise, který se vrátil, aby nás zachránil před krvavou lázní, kterou chtěl rozpoutat Hans z Dlouhopolska a jeho povstalecká chátra.")
            $ zairis.say("Chtěl bych se někdy dostat i ke hrobu prvního Amadise, ale tak daleko zatím můj otec necestoval.")

        "Všiml[a] jsem si, že tvé písmo je přesně stejné, jako písmo Adina tajného ctitele." if "letters for Ada seen" in status and "Zairis writing sample" in status and "handwriting proof" not in zairis.asked and "expensive paper proof" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("handwriting proof")
            if "letters for Ada" not in zairis.asked:
                $ zairis.say("Písmo jejího tajného ctitele? Asi nevím, co máte na mysli.")
                call zairisLettersForAdaFirstMention
                $ mc.say("Jak ale vysvětlíš to shodující se písmo?")
                call zairisHandwritingProof
        "Navíc je tvoje písmo stejné jako to na dopisech." if "letters for Ada seen" in status and "Zairis writing sample" in status and "handwriting proof" not in zairis.asked and "expensive paper proof" in zairis.asked:
            hide mcPic
            $ zairis.asked.append("handwriting proof")
            call zairisHandwritingProof
        "Všiml[a] jsem si, že používáš stejný papír, jako Adin tajný ctitel." if "letters for Ada seen" in status and "Zairis writing sample" in status and "handwriting proof" not in zairis.asked and "expensive paper proof" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("expensive paper proof")
            $ zairis.say("Jakého tajného ctitele a jaký papír myslíte?")
            call zairisLettersForAdaFirstMention
            $ mc.say("Jak ale vysvětlíš to, že používáš přesně stejný papír?")
            call zairisExpensivePaperProof
        "Navíc používáš stejný papír jako ten, na kterém jsou dopisy pro Adu psané." if "letters for Ada seen" in status and "Zairis writing sample" in status and "handwriting proof" in zairis.asked and "expensive paper proof" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("expensive paper proof")
            call zairisExpensivePaperProof

        "Mohl bys mi něco napsat, jen jako ukázku, jak píšeš?" if "letters for Ada seen" in status and "Zairis writing sample" not in status:
            hide mcPic
            $ zairis.say("Ehm... myslíte báseň na zakázku? To by asi chvíli trvalo.", "surprised")
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

        "Mohl[a] bych si ještě promluvit s tvým otcem?" if rovienOptionsRemaining > 0:
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
        "Ada, dcera mistra Heinricha, dostala nějaké básně a potřeboval[a] bych názor, od koho tak mohly být.":
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
                $ zairis.asked.append("letters for Ada")
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
        $ zairis.trust -= 4
        "Skoro okamžitě se ale jeho výraz změní."
        $ zairis.say("To je Théodore de Banville.", "angry")
        $ zairis.say("To tě přece muselo napadnout, že básně tady z knihovny nejspíš budu znát. Tolik jich tam bohužel ještě není.", "angry")
        $ zairis.say("Ale hlavně… proč? To se mi tak moc pokoušíš zalíbit? Co doufáš, že ti řeknu nebo pro tebe udělám?", "surprised")
        $ zairis.say("A má vůbec smysl ti vysvětlovat, že tohle je také krádež, stejně jako sebrat někomu mistrovský výrobek? Jak mám důvěřovat strážným, když ani nepoznají zlodějinu a sami se jí dopouští?", "angry")
        $ zairis.say("Já tě asi nechápu. Co tedy doopravdy potřebuješ?", "angry")
        return
    elif "poem watch" in status:
        $ zairis.say("Myslím, že jsem se ještě nesetkal s tím, že by v básni někdo tímhle způsobem k někomu promlouval. V milostné lyrice se hovoří k dámě, ale pochopitelně výrazně jiným způsobem.")
        $ zairis.say("Říkám si, nechceš zkusit napsat divadlo? Tam by se to výborně hodilo.")
        $ zairis.say("Nebo jenom scénku, divadelní hra je přece jenom dlouhá.")
    elif "poem hope" in status:
        $ zairis.say("Hm, tolik víry v budoucnost se v poezii jen tak nenajde. Možná to je škoda, dává to hodně příjemný pocit a přiměje to jednoho uvědomit si, že na světě není tak špatně.", "happy")
        $ zairis.say("Přijde mi to jako pěkná volba. Možná bych něco takového také měl někdy zkusit.", "happy")
    elif "poem poverty" in status:
        $ zairis.say("Vážně je to tak špatné? Měl jsem za to, že je tu snaha věci zlepšit.", "surprised")
        $ zairis.say("Přinejmenším už v zemi není tolik banditů jako ještě před pár lety. Nebo to má být poetická nadsázka?")
        show mcPic at menuImage
        menu:
            "Pro někoho se možná věci lepší, ale rozhodně ne pro všechny.":
                hide mcPic
            "Nemá poezie hlavně vyvolávat emoce?":
                hide mcPic
            "To nic neznamená, prostě jsem zrovna měl[a] hlad.":
                hide mcPic
        $ zairis.say("Nemůžu tomu upřít působivost, byť to asi není druh poezie, kterým by někdo chtěl trávit každý večer.")
    $ zairis.say("Rozhodně oceňuji rytmus a rýmy. Ne každý je udrží celou báseň takhle dobré.", "happy")
    $ zairis.say("Co by mě ale zajímalo, nejsem zvyklý na to, že bývají myšlenky řečené takhle zpříma. Většinou bývají víc zabalené do metafor. Je to úmysl, aby to působilo úderněji?")
    "Zairis má podobných dotazů více a rychle z nich vyklíčí živý rozhovor, v němž hledáte nejvýstižnější možná slova, zvažujete použití nejrůznějších básnických obratů a občas se vracíte k celkovému toku myšlenek a pocitů v celé básni."
    "Ačkoli si uvědomuješ, že ti v literární tvorbě chybí zkušenost, netrvá dlouho a cítíš se skoro jako básník."
    "Potom doba pokročí, téma se na určitou chvíli vyčerpá a ty se rozhlédneš kolem sebe."
    $ time.addHours(1)
    $ mc.say("Jakkoli bych s tebou takhle mluvil[a] klidně ještě dlouho, bojím se, že toho ještě dnes musím docela dost oběhnout.")
    $ zairis.say("Pravda je, že mě otec asi také brzy začne podezřívat, jestli se nevyhýbám práci...", "sad")
    $ zairis.say("Potřebuješ ještě něco ke svému případu?")
    return

label zairisLettersForAdaFirstMention:
    $ mc.say("Dostaly se mi do rukou dopisy, které Ada dostala, a snažím se najít jejich autora.")
    $ zairis.say("Aha... A co mu chcete?")
    $ zairis.say("Chci říct, mně je to v zásadě jedno, ale není to její věc, s kým si dopisuje?")
    show mcPic at menuImage
    menu:
        "Autor těch dopisů by mohl být podezřelý z krádeže v Heinrichově dílně.":
            hide mcPic
            $ zairis.trust -= 1
            $ zairis.say("... jako že někdo psal Adě dopisy, dal si s ní dostaveníčko v domě jejích rodičů a pak toho využil, aby se dostal do dílny?", "surprised")
            $ zairis.say("Nebo že ji přesvědčil, aby mu odemkla?", "surprised")
            $ zairis.say("To je falešná stopa, to by neudělala.", "angry")
            $ mc.say("I tak by mě ale zajímalo, kdo jí ty básně psal.")
            $ zairis.say("Jestli vás to ale jenom zajímá a nepomáhá to pátrání, nevidím důvod, proč se tím zabývat. Pořád to považuji za soukromou záležitost a vy máte určitě důležitější věci na práci.", "angry")
        "Mistr Heinrich za to vyhodil svého učedníka, tak mě zajímá, jestli právem.":
            hide mcPic
    return

label zairisHandwritingProof:
    "TBD"
    return

label zairisExpensivePaperProof:
    $ zairis.say("Ale prosím, podobný papír se dá běžně koupit a používá ho kde kdo. To přece nemůžete považovat za důkaz.")
    $ mc.say("Celou řadu možných odesilatelů to ale naopak vylučuje. Například Zerana.")
    $ zairis.say("No, možná. On se tváří jako chudáček, ale třeba si ty peníze někde sehnal?")
    $ mc.say("Třeba. Ale není to pravděpodobné.")
    return

###

label zairisOptionsRemainingCheck:
    $ zairisOptionsRemaining = 0
    if if "letters for Ada seen" in status and "poetry" not in zairis.asked:
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
    if "Zeran offense" in clues and "zeran" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "Zairis mentioned letters" in zairis.asked and "letters for Ada" not in zairis.asked and "what letters" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "letters for Ada seen" in status and "Zairis writing sample" in status and "handwriting proof" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    if "letters for Ada seen" in status and "Zairis writing sample" in status and "expensive paper proof" not in zairis.asked:
        $ zairisOptionsRemaining += 1
    return
