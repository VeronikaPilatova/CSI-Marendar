label lisbethMain:
    $ lisbeth.say("Mně? Samozřejmě ráda pomůžu, ale já do manželovy dílny nechodím ani uklízet.")
    if lastSpokenWith == "":
        $ lisbeth.say("Pojďte dál.")
        call victimHouseInterior

    $ lastSpokenWith = "lisbeth"
    $ heinrichHouseholdSpokenWith.append("lisbeth")
    $ origAsked = lisbeth.asked.copy()
    call lisbethOptions
    $ time.addMinutes((len(lisbeth.asked) - len(origAsked)) * 3)
    jump victimHouseholdConversationEnded
    return

label lisbethOptions:
    call lisbethOptionsRemainingCheck from _call_lisbethOptionsRemainingCheck_1
    if lisbethOptionsRemaining == 0:
        $ mc.say("Děkuji vám za trpělivost.")
        $ lisbeth.say("Pokud to pomůže najít manželův výrobek…")
        return

    show mcPic at menuImage
    menu:
        "Stalo se vám něco?" if lisbeth.imageParameter == "beaten" and "beaten" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("beaten")
            $ lisbeth.say("Ne, všechno je v pořádku. Hlavní je najít ten ukradený mistrovský výrobek.")
        "Všimla jste si včera v noci něčeho nebo někoho podezřelého?" if "anything suspicious" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("anything suspicious")
            "Lisbeth se nadechne a pak se rozohní víc, než jsi ji měl[a] zatím možnost vidět."
            $ lisbeth.say("Jediné podezřelé individuum, kterého jsem si všimla, byl manžel.", "angry")
            $ lisbeth.say("Že se z hospody vrátí až někdy nad ránem a vzbudí mě hlukem, jako kdyby boural dílnu, to je jedna věc. Ale že mu to nestačí, vypije potom ještě v noci víc než půlku domácího baru, včetně těch opravdu dobrých lahví pro návštěvy, a ještě ty prázdné lahve někam zašantročí, to už je moc.", "angry")
            $ lisbeth.say("A navíc dělá, že si nic nepamatuje, a popírá to, prase jedno.", "angry")
            if "alcoholic" in lisbeth.asked:
                $ lisbeth.say("...to se mu vlastně nepodobá, většinou si věci pamatuje.")
        "Tušíte, kdy šel potom váš manžel spát?" if "anything suspicious" in lisbeth.asked and "coming home" not in eckhard.asked and "coming home" not in lisbeth.asked:
            call victimComingToBed
        "Takže váš manžel nešel hned po příchodu do postele?" if "anything suspicious" in lisbeth.asked and "coming home" not in eckhard.asked and "coming home" not in lisbeth.asked:
            call victimComingToBed
        "Můžu se zeptat, jak vypadaly ty ztracené lahve?" if "anything suspicious" in lisbeth.asked and "bottles description" not in clues:
            hide mcPic
            $ lisbeth.asked.append("lost bottles")
            $ clues.append("bottles description")
            if "bottles description" in salma.asked:
                $ clues.append("lost bottles")
            $ lisbeth.say("Část jich byla s vínem, ty byly hodně úzké, a část kulatá s tvrdším alkoholem. Všechny skleněné, myslím zelené nebo modré sklo? Něco takového.")
            $ lisbeth.say("Proč vás to vlastně zajímá?")
            $ mc.say("Jenom pro jistotu. Nikdy nevíte, co se ukáže být důležité.")
        "Po odchodu vašeho muže v dílně nikdo nebyl?" if "workshop empty" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("workshop empty")
            $ lisbeth.say("Myslím, že ne. Ale jak jsem říkala, já tam nechodím.")
        "Kdo všechno žije ve vaší domácnosti?" if "family" not in victim.asked and "family" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("family")
            $ lisbeth.say("Kromě naší rodiny ještě dva učedníci.")
            $ mc.say("A rodina znamená…?")
            $ lisbeth.say("Manžel, já a naše dvě děti, Aachim a Ada.")
            call unlockFamily
        "Napadá vás někdo, kdo by chtěl vašeho manžela poškodit?" if "enemies" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("enemies")
            "Lisbeth se zamyslí, ale pak pomalu zavrtí hlavou."
            $ lisbeth.say("Bohužel nenapadá.", "sad")
            $ mc.say("Váš manžel nemá s nikým spory?")
            $ lisbeth.say("Heinrich se umí pohádat i o spálenou večeři, ale to nejsou spory, kvůli kterým by mu kdokoli mohl chtít opravdu ublížit.")
        "Můžete mi něco říct o vztazích uvnitř ševcovského cechu?" if "guild relations" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("guild relations")
            "Lisbeth se zatváří omluvně."
            $ lisbeth.say("Bojím se, že v tomhle vám moc nepomůžu. To je manželův svět, já ostatní mistry vlastně moc neznám.", "sad")
            $ mc.say("Nepotkáváte je na cechovních slavnostech?")
            $ lisbeth.say("To ano, ale jen jako člověk zvenku. Zkuste si možná promluvit s Nirevií, ta má o lidech vždy výborný přehled.")
            $ nireviaNote.isActive = True
        "Pamatujete si na ty učedníky, které váš mistr propustil?" if "enemies" in rumelin.asked and "fired apprentices" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("fired apprentices")
            $ lisbeth.say("Samozřejmě, Gerd odešel asi před dvěma týdny. Milý chlapec, jsem ráda, že může v učení pokračovat jinde. Teď je u Njala.")
            $ mc.say("Proč vlastně odešel?")
            "Lisbeth si povzdechne."
            $ lisbeth.say("Myslím, že byl na Heinricha moc živý a neukázněný. A rozhodně měl moc svou vlastní hlavu.")
            $ lisbeth.say("On to všechno myslel dobře, ale když má Heinrich nějakou představu, tak nesnáší jakékoliv odchylky od ní. Zvlášť, když byl teď před slavnostmi ve stresu. Chystá se volba cechmistra a Heinrich o tu pozici už dlouho usiluje.")
            $ mc.say("A co ti zbylí dva učedníci?")
            $ lisbeth.say("Sigi byl šikovný, ale nestačil na Heinrichovy nároky. Jeho otec mu zařídil místo u jiného mistra. V Sehnau, myslím.")
            $ lisbeth.say("A Zeran... Ada říká, že mezi nimi nikdy nic nebylo a pak by chudák kluk skončil v dočasné čtvrti bez důvodu. Ale ať mě Olwen klidně potrestá, radši to, než aby zničil život mé malé holčičce.")
            $ gerdNote.isActive = True
            $ zeranNote.isActive = True
            $ clues.append("Zeran offense")
            $ clues.append("Zeran innocent")
        "Jak by měl Zeran zničit život vaší dceři?" if "fired apprentices" in lisbeth.asked and "ruined life" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("ruined life")
            $ lisbeth.say("Psal jí milostné dopisy a snažil se ji svést.")
            $ lisbeth.say("I kdyby nebyl o dost starší a navíc bez prostředků, jaký život by ji čekal s elfem? Nemohla by s ním nikdy mít rodinu.")
            $ mc.say("Aha, samozřejmě. To s dětmi mě nenapadlo.")
            $ lisbeth.say("Teď je všude plno Amadise Půlelfa, kvůli té divadelní hře. Úžasný rytíř, zachránce říše, a tak vůbec. Ale už se nemluví o tom, jaká on byl výjimka. A že normálně se půlelf prostě nenarodí nebo nepřežije prvních pár dní a jen ohrožuje chudáka matku.")
            $ clues.append("Zeran offense")
        "Ada vztah se Zeranem přiznala?" if "ruined life" in lisbeth.asked and "Ada's boyfriend" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("Ada's boyfriend")
            $ lisbeth.say("Ta to samozřejmě popírala, ale ty dopisy jsme viděli. A kdo jiný je mohl psát?")
            $ mc.say("Byly podepsané jménem?")
            $ lisbeth.say("Jen písmenem Z. Ale jak říkal Heinrich, kolik je asi černovlasých elfů se jménem začínajícím stejně a s přístupem k Adě?")
            show mcPic at menuImage
            menu:
                "To určitě může hlídka zjistit.":
                    hide mcPic
                    $ lisbeth.say("Není potřeba ztrácet čas vašich lidí něčím, co už je vyřešené.")
                    $ mc.say("Takže nikdo jiný nebyl ani v podezření?")
                "To dává smysl. Takže nikdo jiný ani nebyl v podezření?":
                    hide mcPic
            if lisbeth.trust > 2:
                $ lisbeth.asked.append("Zairis mentioned")
                $ clues.append("Zairis suggested as Ada's boyfriend")
                $ lisbeth.say("Ada se to pokoušela hodit na Rovienova syna, ale to až ve chvíli, kdy Heinrich Zerana opravdu vyhodil.")
                $ lisbeth.say("Kdyby to byla pravda a ne jenom snaha najít někoho, koho nebudeme moct potrestat, proč by něco neřekla dřív?")
                $ mc.say("Možná se jen bála, že ten vztah nebudete schvalovat?")
                $ lisbeth.say("No to bychom neschvalovali, s ním ani s žádným jiným elfem. Ale právě proto je dobře, že je Zeran z domu.", "angry")
                $ lisbeth.say("Je mi ho líto, ale na Adě mi záleží mnohem víc. Nemůžu nic riskovat.")
                $ zairisNote.isActive = True
            else:
                $ lisbeth.say("Rozhodně ne dost na to, abychom si mohli dovolit riskovat. Zerana je mi líto, ale na Adě mi záleží mnohem víc.")
        "Takže Rovienova syna jste nijak neřešili?" if "Zairis mentioned" in lisbeth.asked and "Zairis investigated" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("Zairis investigated")
            $ lisbeth.say("Jistě, že ne. Přece nepůjdeme za váženým obchodníkem kvůli něčemu, co Ada vyhrkla jen proto, že na ni něco vyplavalo.")
            $ lisbeth.say("Tohle je záležitost naší rodiny a v ní by měla zůstat.")
        "Jaký je váš manžel, když se napije?" if kaspar.alreadyMet == True and "alcoholic" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("alcoholic")
            if "alcoholic" not in eckhard.asked and "alcoholic" not in salma.asked:
                $ victim.trust -= 1
            $ lisbeth.say("Jak to myslíte?")
            $ mc.say("Bývá pak vzteklý? Pamatuje si pak, co v opilosti dělal?")
            $ lisbeth.say("..spíš bývá veselý. Několikrát mě probudil zpěvem a zpívat Heinrich opravdu neumí. Ale vzteklý… ne, to normálně nebývá.")
            $ lisbeth.say("Nanejvýš pak ráno, když je mu špatně, ale i tehdy je spíš nabručený než vzteklý.")
            $ mc.say("A co ta paměť, mívá často výpadky?")
            $ lisbeth.say("Ne, to nemívá… Proč se vlastně ptáte? Jak souvisí manželovo pití s ukradeným výrobkem?")
            show mcPic at menuImage
            menu:
                "Mistr Kaspar říkal, že se vás mám zeptat.":
                    hide mcPic
                    $ lisbeth.say("Pak nevím, co Kaspar naznačoval, ale vůbec se mi to nelíbí.")
                    $ lisbeth.relationships["kaspar"] -= 1
                    $ lisbeth.asked.append("kaspar's slander")
                "Jen sleduji jednu stopu pátrání.":
                    hide mcPic
        "Jaký vztah vlastně máte s manželem?" if lotte.alreadyMet == True and "relationship" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("relationship")
            $ lisbeth.trust -= 1
            $ lisbeth.say("Co je tohle za otázky? Přísahali jsme si společnou cestu životem, dokud nepřejdeme přes poslední práh. A po té cestě šťastně jdeme už přes patnáct let.")
            $ mc.say("Omlouvám se, nechtěl[a] jsem vás urazit.")
            $ lisbeth.say("Potřebujete ještě něco?")
        "Můžete se u svého muže přimluvit za Aachima a učedníky?" if "confession" in boysAsked and "defend boys" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("defend boys")
            if "boys punished for drinking" in status:
                $ lisbeth.say("Za ten vypitý alkohol? Nejsem si jistá, jestli v tomhle už není pozdě.", "sad")
                $ mc.say("Doufám, že je mistr Heinrich ještě nestihl opravdu vyhodit z domu.")
                $ lisbeth.say("Zatím jen ze služby, v domě naštěstí můžou zůstat do slavností. Prý si na nich mají rovnou najít jiného mistra, já jenom doufám, že je vůbec někdo vezme. Víc jsem manžela bohužel obměkčit nedokázala.", "sad")
                $ mc.say("To se s tím už nedá vůbec nic dělat?")
                $ lisbeth.say("Když se Heinrich pro něco rozhodne, mění názor velmi těžko. Musel by mít opravdu silný důvod.", "sad")
            elif "lost bottles solved boys" in victim.asked:
                $ lisbeth.say("Za ten vypitý alkohol? To už jsem zkoušela.")
                $ lisbeth.say("Vypadal trochu na vážkách, myslím, že hodně pomohlo, jak jste ho hned na začátku zastavil[a] před tím prvním návalem vzteku. Ale jestli to bude stačit, to nevím.")
                $ mc.say("Nedalo by se tomu ještě nějak pomoct? Nemohl by se přimluvit ještě někdo další?")
                $ lisbeth.say("Možná zkuste mistra Eckharda. S Heinrichem jsou přátelé už od učňovských dob a jen bohové vědí, kolik toho už spolu vypili. Jestli v něm někdo dokáže vyvolat pochopení pro pitky, co dopadnou špatně, tak on.")
                $ lisbeth.say("Zašla bych za ním sama, ale nikdy jsme si s ním nerozuměli. Bála bych se, abych to tím jen nezhoršila.", "sad")
                if "defend boys" in eckhard.asked:
                    $ mc.say("Ve skutečnosti jsem už za ním byl[a]. Slíbil, že se za Heinrichem staví.")
                    $ lisbeth.say("To byla skvělá myšlenka, děkuji!", "happy")
                    $ lisbeth.say("V tom případě už asi nemůžeme udělat nic víc.")
                    $ lisbeth.say("Doufám, že se zase neopijí pod obraz… i když tentokrát by to možná vlastně pomohlo věci.")
                    $ lisbeth.trust += 1
                else:
                    $ mc.say("Děkuji za radu, zkusím se za ním co nejdřív zastavit.")
                    $ lisbeth.say("Děkuji. A pak už bude zbývat jen modlit se k bohům, aby Eckhardově snaze požehnali.")
            else:
                $ lisbeth.say("Přimluvit? Kvůli čemu?", "surprised")
                $ mc.say("Ty ztracené lahve z vašich domácích zásob opravdu nevypil váš muž. Vypili to Aachim a učedníci.")
                $ lisbeth.say("Prosím? Všechno? Jste si jist[y]?", "surprised")
                $ mc.say("Přiznali se a do všeho to zapadá.")
                $ lisbeth.say("To je... to je ale dost velká drzost. Není to ve skutečnosti dokonce porušení zákona pohostinství? Nebo úcty k rodičům? Jedno z toho určitě a to jsou oba velmi těžké hříchy.", "surprised")
                $ lisbeth.say("Manžel je za to bude muset přísně potrestat.", "angry")
                $ mc.say("Myslíte, že je opravdu bude chtít vyhodit?")
                $ lisbeth.say("No rozhodně si to kluci zaslouží. Taková...", "angry")
                $ lisbeth.say("Počkejte, vyhodit? To snad... ale Heinrich bude hrozně zuřit. Nejspíš by to opravdu udělal.", "surprised")
                $ mc.say("Proto se ptám, jestli byste se mohla nějak přimluvit.")
                $ lisbeth.say("To zkusím, až se to dozví. Oba ale víme, že udržování pořádku v rodině je na pánovi domu. A přesvědčit o něčem Heinricha pro mě často bývá těžké.")
                $ mc.say("Napadá vás někdo, kdo by to dokázal?")
                $ lisbeth.say("Možná zkuste mistra Eckharda.")
                $ lisbeth.say("S Heinrichem jsou přátelé už od učňovských dob a jen bohové vědí, kolik toho už spolu vypili. Jestli v něm někdo dokáže vyvolat pochopení pro pitky, co dopadnou špatně, tak on.")
                if "defend boys" in eckhard.asked:
                    $ mc.say("Ve skutečnosti jsem už za ním byl[a]. Slíbil, že se za Heinrichem staví.")
                    $ lisbeth.say("V tom případě už mě nenapadá nikdo jiný.")
                    $ lisbeth.say("Doufám, že se zase neopijí pod obraz... i když tentokrát by to možná vlastně pomohlo věci.")
                    $ lisbeth.trust += 1
                else:
                    $ mc.say("Děkuji za radu, zkusím se za ním co nejdřív zastavit.")
        "Jedna ze sousedek vás včera v noci viděla jít do domu s cizím mužem. Kdo to byl?" if lotte.alreadyMet == True and "night meeting" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("night meeting")
            if "Kaspar and Lisbeth" not in clues:
                $ clues.append("Kaspar and Lisbeth")
            "Lisbeth se na moment zatváří poplašeně, pak se ale ovládne."
            $ lisbeth.say("To byl mistr Kaspar. Nesl mi vrátit jednu knihu, kterou si předtím půjčil. Olwenovu cestu.")
            if "lisbeth friends" in ada.asked:
                $ mc.say("Já myslel[a], že pro tu jste si včera poslala Adu. Nebo ji nepřinesla?")
                "Lisbeth nasucho polkne a na chvili uhne očima."
                $ lisbeth.say("Vlastně máte pravdu. Musela jsem se splést. Kaspar měl knih půjčených několik, muselo to být něco jiného.")
                $ lisbeth.cluesAgainst += 1
        "Je něco mezi vámi a mistrem Kasparem?" if "Kaspar and Lisbeth" in clues and "Kaspar and Lisbeth" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("Kaspar and Lisbeth")
            "Lisbeth se rozšíří oči překvapením a možná strachem, pak se ale ovládne."
            $ lisbeth.say("Co by mezi námi mělo být?")
            if "night meeting" not in lisbeth.asked:
                show mcPic at menuImage
                menu:
                    "Doufal[a] jsem, že to mi řeknete vy.":
                        hide mcPic
                    "Jedna sousedka vás včera v noci viděla vítat cizího muže.":
                        hide mcPic
                        $ lisbeth.say("To ale nebylo… jak to mohlo vypadat.", "surprised")
                        $ mc.say("Můžete to v tom případě uvést na pravou míru?")
                        $ lisbeth.say("K ničemu mezi námi nedošlo. Včera večer, ani nikdy jindy.")
            else:
                $ mc.say("Doufal[a] jsem, že to mi řeknete vy.")
            $ lisbeth.say("Mistr Kaspar je velmi milý a pozorný člověk. Dalo by se říct, že jsme přátelé.")
            $ mc.say("Přátelé?")
            $ lisbeth.say("Několikrát jsme spolu mluvili, když Heinrich… nebyl poblíž. Myslím, že je také osamělý.")
            $ lisbeth.say("Je jeden z mála lidí, s kým můžu hovořit o knihách. Je k nim velmi vnímavý. Neodsuzuje je jako zbytečnost ani nemá dojem, že kážou zbytečně upjatou morálku.")
            $ lisbeth.say("Rozhodně by ho ani nenapadlo nic… nevhodného. Stejně jako mě.", "angry")
        "Ví o vašem přátelství s mistrem Kasparem váš manžel?" if "Kaspar and Lisbeth" in lisbeth.asked and "Heinrich knows" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("Heinrich knows")
            $ lisbeth.say("Neví. A byla bych ráda, kdyby to tak mohlo zůstat. Heinrich z nějakého důvodu nemá Kaspara rád, nemusel by to pochopit.")
            show mcPic at menuImage
            menu:
                "Nevidím důvod mu cokoli říkat.":
                    hide mcPic
                    $ lisbeth.trust += 1
                    $ lisbeth.say("To je rozumné. Nechci před svým manželem nic tajit, ale znám ho dobře a vím, že občas má sklony k ukvapeným závěrům.")
                "Myslím, že váš manžel si zaslouží pravdu.":
                    hide mcPic
                    $ lisbeth.trust -= 1
                    $ lisbeth.say("Pravdu o čem? Že jsou témata, o kterých ráda mluvím, ale jeho nezajímají? Že jsou ve městě lidé, se kterými si v některých ohledech rozumím lépe než s ním?")
                    $ lisbeth.say("To všechno on ví a nevidím důvod, proč mu to připomínat. V lepším případě by ho to nezajímalo. V horším by ho to ranilo.")
                "Je možné, že to bude muset vyjít na povrch během vyšetřování.":
                    hide mcPic
                    $ lisbeth.say("Jak to souvisí? Ale kdyby to bylo nutné, tak prosím dejte hned od začátku najevo, co to je a hlavně co to není.")
                    $ lisbeth.say("Heinrich má občas sklony k ukvapeným závěrům.")
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("join forces")
            $ status.append("join forces survey")
            $ lisbeth.say("Já myslím, že by to bylo hezké. Dva mistři se spojí, aby svého boha uctili o to lépe. Bylo by vidět, že myslí hlavně na Einiona, protože žádný z nich by si nemohl uzmout všechnu slávu.", "happy")
            $ lisbeth.say("Ale neděje se to moc často, asi je těžké něco takového vymyslet.")
            $ mc.say("Jednu takovou možnost teď má zrovna váš manžel, mohl by něco vyrobit spolu s mistrem Njalem.")
            $ lisbeth.say("Heinrich o něčem takovém uvažuje? To bych do něj nikdy neřekla!", "surprised")
            $ mc.say("Máte tušení, jak by to město vnímalo zrovna u těch dvou?")
            $ lisbeth.say("Určitě by se jim to líbilo. Jestli se Heinrich s někým spojí, musí jít o něco úžasného.")
            "Lisbeth se zarazí a na chvíli se zamyslí."
            $ lisbeth.say("Chci říct, vlastně si nejsem jistá. Cech má spoustu členů a já se starám hlavně o domácnost.")
            $ lisbeth.say("Možná si zkuste promluvit s paní Nirevií? Ta má vždy o lidech dokonalý přehled, pokud by to někdo dokázal odhadnout, tak ona.")
            show mcPic at menuImage
            menu:
                "Děkuji vám za radu, zajdu za ní.":
                    hide mcPic
                "Za ní bych s tím radši nechodil[a].":
                    call joinForcesAskSalma
        "Nechci zbytečně plašit, ale je možné, že střevíce vašeho manžela nenajdeme neporušené." if time.days > 1 and "plan B" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("plan B")
            $ clues.append("plan B")
            $ lisbeth.trust += 1
            $ mc.say("Víte, jestli má váš manžel pro jistotu připravený nějaký náhradní výrobek na slavnosti?")
            $ lisbeth.say("Nemá, a když jsem mu to zkoušela navrhnout, jenom se rozčílil.", "sad")
            $ mc.say("Proč mu tolik záleží na tom, aby to byly zrovna tyto střevíce?")
            $ lisbeth.say("Záleží mu na tom, aby to bylo něco výjimečného, na čem plně ukáže svoje schopnosti. Takové věci bohužel nemůže vyrábět každý den a zrovna teď mu asi v dílně nic takového neleží.")
            $ lisbeth.say("Nesnese pomyšlení, že by všichni věděli, že by mohl přinést i něco lepšího. A hlavně že by to věděl on sám.")
        "Viděla jste včera to taneční vystoupení s ohněm?" if "fireshow" in status and "fireshow" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("fireshow")
            $ lisbeth.say("Samozřejmě, že ne! To se přece nesluší. A navíc jsem měla práci doma v kuchyni.", "angry")
        "Tušíte, kdo tam tak být mohl?" if "fireshow" in lisbeth.asked and "fireshow 2" not in lisbeth.asked:
            hide mcPic
            $ lisbeth.asked.append("fireshow 2")
            $ lisbeth.say("Kdekdo, obávám se, ale nechtěla bych nikoho pomlouvat.", "sad")
            $ lisbeth.say("Můžu ale potvrdit, že tam nebyl můj manžel. Tedy dokud tam nešel hasit, samozřejmě.")
            $ lisbeth.say("Já vím, že bych neměla soudit lidi, které neznám, ale přijde kdo ví odkud, poblázní všechny v okolí a pak si hraje s ohněm uprostřed města? Já tomu nerozumím.", "sad")
            show mcPic at menuImage
            menu:
                "Kdyby byla rozumná, dělá poctivou práci.":
                    hide mcPic
                    $ lisbeth.trust += 1
                    $ lisbeth.say("Přesně. Vím nejméně o dvou domácnostech, kde by potřebovali spolehlivou výpomoc.")
                "Celé to byla jenom nehoda.":
                    hide mcPic
                    $ lisbeth.trust -= 1
                    $ lisbeth.say("Vychovala jsem dvě děti. Ty když něco rozbily, také to vždy byla jenom nehoda.", "angry")
        "Děkuji vám za trpělivost.":
            hide mcPic
            $ lisbeth.say("Pokud to pomůže najít manželův výrobek…")
            return
    jump lisbethOptions
    return

###

label victimComingToBed:
    hide mcPic
    $ lisbeth.asked.append("coming home")
    "Lisbeth se zamyslí."
    $ lisbeth.say("No… vzbudil mě hlukem v dílně. Snažila jsem se ho ignorovat a spát, já musím vstávat se slepicemi. Potom mě vzbudil znova, když se hrabal do postele. Ten jeho povedený kamarád mu u toho ještě něco šeptal, myslím.", "angry")
    $ lisbeth.say("Přišlo mi to jako hned po sobě, ale kolik mezi tím bylo času doopravdy netuším.")
    $ mc.say("Takže jestli ještě pili doma, tím vás nevzbudili?")
    $ lisbeth.say("Asi ne… to je vlastně dost zvláštní. Čekala bych, že tím hluku natropí ještě víc.")
    $ lisbeth.say("Ale co jiného by se s tím pitím stalo?")
    return

label joinForcesAskSalma:
    hide mcPic
    $ mc.say("Váš muž přímo ohrožuje pozici toho jejího, nemůžu si být jist[y], jestli by paní Nirevia poradila správně.")
    $ lisbeth.say("Na tom asi něco bude, to mě nenapadlo...")
    $ lisbeth.say("Tak… možná hostinská Salma? Ta není ani v cechu, ale se všemi jeho členy se dobře zná?")
    $ mc.say("To je zajímavý nápad. Děkuji za radu.")
    return

label lisbethOptionsRemainingCheck:
    $ lisbethOptionsRemaining = 0
    if "anything suspicious" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "workshop empty" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "family" not in victim.asked and "family" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "enemies" in rumelin.asked and "fired apprentices" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "anything suspicious" in lisbeth.asked and "anything suspicious" in salma.asked and "lost bottles" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if kaspar.alreadyMet == True and "alcoholic" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "enemies" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "guild relations" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "fired apprentices" in lisbeth.asked and "ruined life" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if lotte.alreadyMet == True and "relationship" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "ruined life" in lisbeth.asked and "Ada's boyfriend" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if time.days > 1 and "plan B" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "anything suspicious" in lisbeth.asked and "coming home" not in eckhard.asked and "coming home" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if lotte.alreadyMet == True and "night meeting" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "confession" in boysAsked and "defend boys" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "fireshow" in status and "fireshow" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "fireshow" in lisbeth.asked and "fireshow 2" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "Zairis mentioned" in lisbeth.asked and "Zairis investigated" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "Kaspar and Lisbeth" in clues and "Kaspar and Lisbeth" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if "Kaspar and Lisbeth" in lisbeth.asked and "Heinrich knows" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    if lisbeth.imageParameter == "beaten" and "beaten" not in lisbeth.asked:
        $ lisbethOptionsRemaining += 1
    return
