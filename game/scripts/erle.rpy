label erleController:
    # check if visit makes sense
    call erleOptionsRemainingCheck
    if optionsRemaining == 0:
        "Nenapadá tě, co dalšího se Erle ještě ptát."
        return
    call preludeController

    # walk over
    if erle.alreadyMet == False:
        $ time.addMinutes(30)
    else:
        $ time.addMinutes(15)
    $ currentLocation = "old bridge"
    $ origAsked = erle.asked.copy()

    # visit itself
    if erle.alreadyMet == False:
        call erleFirst
    else:
        call erleAgain
    call erleOptions
    call leavingErle

    # adjust time spent and status, create events
    if "add Rauvin finds out about AML" in status:
        $ status.remove("add Rauvin finds out about AML")
        $ newEvent = Event(copy.deepcopy(time), "STATUS", 0, "Rauvin knows about AML")
        $ newEvent.when.addHours(6)
        $ eventsList.append(newEvent)
    if "add investigating less deals erle" in status:
        $ status.remove("add investigating less deals erle")
        $ status.append("investigating less deals erle ongoing")
        $ newEvent = Event(copy.deepcopy(time), "erleAMLresults", 2)
        $ newEvent.when.addHours(4)
        $ newEvent.when.addHMinutes(30)
        $ eventsList.append(newEvent)

    $ time.addMinutes((len(erle.asked) - len(origAsked)) * 3)
    if erle.alreadyMet == False:
        $ erle.alreadyMet = True
    stop music fadeout 0.5
    return

label erleFirst:
    play music audio.erle fadeout 0.5 if_changed
    scene bg bridge
    "Starý most najdeš snadno a u něj na břehu řeky skutečně sedí osamělá trpaslice."
    if time.hours < 18:
        "Na Erle je sice vidět život na ulici, nevypadá ale ani zdaleka tak zuboženě nebo zoufale, jak bys od žebráka čekal[a]. Jak sedí na kusu staré deky, tvář s přivřenýma očima nastavenou příjemnému podzimnímu slunci, působí vlastně téměř spokojeně."
    else:
        "Na Erle je sice vidět život na ulici, nevypadá ale ani zdaleka tak zuboženě nebo zoufale, jak bys od žebráka čekal[a]. Jak sedí na kusu staré deky a pozoruje vycházející hvězdy, působí vlastně téměř spokojeně."
    "Když se přiblížíš, natáhne k tobě ruku, aniž by se na tebe pořádně podívala."
    show mcPic at menuImage
    menu:
        "{i}(Dát jí pár mincí){/i}":
            hide mcPic
            $ erle.asked.append("given money")
            $ erle.trust += 1
            $ erle.say("Děkuju.", "happy")
            "Erle se na tebe usměje, podívá se na mince a pak ti jich asi polovinu vrátí."
            $ erle.say("Nech si něco i pro sebe.", "happy")
            show mcPic at menuImage
            menu:
                "No dobře...":
                    hide mcPic
                    "Trochu zmateně vrácené peníze zase schováš."
                "Já mám peněz dost.":
                    hide mcPic
                    $ erle.say("Já teď už taky. Tak si třeba zajdi na něco dobrého.", "happy")
            $ mc.say("Ty jsi Erle? Jsem z městské hlídky a chci ti položit pár otázek.")
        "Ty jsi Erle? Jsem z městské hlídky a chci ti položit pár otázek.":
            hide mcPic
    $ erle.say("Proč ne, času mám dost. Neposadíš se?", "happy")
    "Erle se trochu posune, aby ti udělala místo na dece."
    return

label erleAgain:
    if "investigating less deals erle ongoing" in status:
        $ random = renpy.random.randint(3, 4)
        scene expression ("bg/bg street0[random].png")
        "Erle u řeky nenajdeš, ale krátce poté ji zahlédneš v jedné z bočních uliček města."
        $ erle.say("Obcházím pro tebe ty hospody. Ještě kus mi chybí.")
        $ erle.say("Možná by sis do té doby měl[a] trochu odpočinout, vždyť celý den někde běháš.", "happy")
    else:
        play music audio.erle fadeout 0.5 if_changed
        scene bg bridge
        "Erle znovu najdeš na jejím obvyklém místě u řeky."
        if time.hours < 18:
            $ erle.say("Jdeš si užívat slunce a klid?", "happy")
        else:
            $ erle.say("Jdeš si odpočinout po těžkém dni?", "happy")
    $ mc.say("Mám na tebe ještě pár otázek ke svému případu.")
    $ erle.say("Tak se ptej. Ale myslím, že chvíle odpočinku by ti jen prospěla.", "happy")
    show mcPic at menuImage
    menu:
        "Možná později.":
            hide mcPic
            "Erle pokrčí rameny."
            $ erle.say("Později často znamená nikdy. Tak se ptej, já mám času dost.")
        "Na podobné věci nemám čas.":
            hide mcPic
            "Erle pokrčí rameny."
            $ erle.say("Všichni se pořád jenom za něčím ženou a pak jim to ani k ničemu není.")
            $ erle.say("Nebo o to přijdou.", "sad")
            $ erle.say("Ale posluž si, já mám času dost.")
        "Chvíle odpočinku je přesně to, co teď potřebuju.":
            hide mcPic
            "Erle ti udělá místo vedle sebe na dece a chvíli spolu jen tak sedíte a pozorujete odlesky na hladině řeky. Klid je opravdu velice příjemný a možnost natáhnout si nohy rozbolavělé dlouhým běháním po městě ti přijde ještě víc vhod, než jsi čekal[a]."
            "Erle tě čas od času upozorní na hezky zbarvený list plující po hladině nebo na drobnou rybku okusující vodní rostliny. Strávíte takto velmi příjemnou chvíli, než se k tobě otočí."
            $ erle.say("Znám lidi, jako jsi ty. Teď odpočíváš, ale stejně někam spěcháš a potřebuješ něco dostat z hlavy. Co tedy potřebuješ vědět?")
            $ time.addMinutes(15)
    return

label erleOptions:
    call erleOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("To je všechno, na co jsem se chtěl[a] zeptat.")
        return

    show mcPic at menuImage
    menu:
        "Prý jsi dnes ráno donesla Salmě nějaké lahve?" if "bottles" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles")
            $ erle.say("To je pravda. Ty byly krásné, moc hezká práce. Taky z nich měla Salma radost.", "happy")
        "Jak ses k těm lahvím dostala?" if "bottles" in erle.asked and "bottles 2" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles 2")
            $ erle.say("Našla jsem je pohozené v blátě. Nejspíš někdo bohatý, kdo neví, že sklo má cenu.")
        "Kde přesně byly?" if "bottles 2" in erle.asked and "bottles location" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles location")
            $ erle.say("Kousek odtud po proudu řeky, zachycené těsně u břehu. Někdo je asi chtěl hodit do vody.")
            $ mc.say("Na tomhle břehu?")
            $ erle.say("Myslím… asi ano. Proč?")
            show mcPic at menuImage
            menu:
                "Ty lahve byly nejspíš kradené.":
                    hide mcPic
                    $ erle.say("Tak to je musíme co nejrychleji vrátit! Snad je má Salma ještě u sebe...", "surprised")
                    $ erle.say("Ale proč by někdo kradl lahve a pak je házel do řeky?")
                    $ erle.say("Myslím, že je ukradl včetně toho pití vevnitř.")
                    $ erle.say("Ale to už vrátit nedokážeme...", "sad")
                "Souvisí to s mým vyšetřováním.":
                    hide mcPic
                    $ erle.say("Ale na vyhazování lahví přece není nic špatného?", "surprised")
                    $ erle.say("Třeba se jich někdo jen chtěl zbavit, aby se o ně nemusel bát?")
                    show mcPic at menuImage
                    menu:
                        "Cože?":
                            hide mcPic
                            $ mc.say("Pokud by se o ně bál, tak by se jich přece nezbavil.")
                            $ erle.say("Bát se můžeš jenom o něco, co máš. Když to už není, není ani strach.")
                            $ erle.say("Nebo ty snad umíš přijít o něco dvakrát?")
                            $ mc.say("Mně přijde nejlepší o to nepřijít ani jednou.")
                            $ erle.say("To většině lidí. Snaží se držet vše pevně v hrsti, kupují koše a staví domy, aby to tam ukryli.")
                            $ erle.say("A pak přijde válka nebo povodeň a všechno to zmizí jako nic.", "sad")
                            $ erle.say("Proč plýtvat úsilím na něco, co stejně nevydrží?", "sad")
                            $ erle.say("Lepší je být šťastný teď, dokud to jde.")
                            $ clues.append("Erle's philosophy")
                        "Možná...":
                            hide mcpic
                            $ erle.say("Jestli neměl, jak je využít, tak bych se mu vlastně nedivila. Jenom by musel dávat pozor, aby je třeba nerozbil.")
                            $ erle.say("Mohl je donést Salmě sám, ale jestli nevěděl, že by mohly někoho potěšit...")
                            "Erle pokrčí rameny."
                "Zajímá mě, kam tu lidé vyhazují odpadky.":
                    hide mcPic
                    $ erle.say("Správně by je měli nosit za hradby, ale většinou je pohodí jen tak na ulici. V lepších čtvrtích s nimi aspoň posílají sloužící na smetiště.")
                    $ erle.say("Na takovém smetišti se dá najít spousta hezkých věcí. Potěší tě a pak je můžeš někomu dát za trochu jídla.", "happy")
                    $ erle.say("Nejbližší je kousek odtud, směrem k bráně. Můžu tě tam zavést.", "happy")
                    $ mc.say("To asi nebude potřeba, ale díky.")
                    $ erle.say("Opravdu? Můžu i pomoct s hledáním...")
                    $ mc.say("Možná někdy jindy.")
                    $ erle.say("Dobře.", "happy")
        "Neviděla jsi toho, kdo ty lahve vyhodil?" if "bottles 2" in erle.asked and "see who threw bottles away" not in erle.asked:
            hide mcPic
            $ erle.asked.append("see who threw bottles away")
            $ erle.say("Jistěže ne! To bych mu řekla, ať tak hezké lahve radši někomu daruje, když už je sám nechce.", "surprised")
            $ mc.say("Ani jsi ho neviděla projít kolem? Nebo ji?")
            $ erle.say("I kdybych viděla, nevěděla bych, že to je on.")
        "Mohl ty lahve a boty vyhodit mistr Kaspar?" if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it kaspar" not in erle.asked:
            hide mcPic
            $ erle.asked.append("war is kaspar")
            $ erle.say("Asi mohl, ale moc se mi to nezdá. Tomu myslím chodí uklízet a vynášet odpadky dcera jednoho tovaryše.")
            $ erle.say("Ale nepořádek od něj by to nejspíš být mohl. Myslím, že ten si potrpí na drahé pití v krásných lahvích.")
        "Mohli ty lahve a boty vyhodit učedníci mistra Heinricha nebo jeho syn?" if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it apprentices" not in erle.asked:
            hide mcPic
            $ erle.asked.append("war it apprentices")
            $ erle.say("Nevím, možná? Heinrich docela pije a myslím, že občas i z docela pěkných lahví.")
            $ erle.say("Ale nepovedené boty myslím většinou vyhazují jinam")
        "Mohl ty lahve a boty vyhodit Gerd?" if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it gerd" not in erle.asked:
            hide mcPic
            $ erle.asked.append("war it gerd")
            $ erle.say("Gerd, ten teď pracuje u Njala, že jo? Asi mohl, ale spíš myslím, že by ty boty rozebrali a něco na nich ještě vyzkoušeli.")
            $ erle.say("A kde by přišli k tolika lahvím? Co já vím, ani jeden z nich moc nepije.")
        "Mohl ty lahve a boty vyhodit mistr Rumelin?" if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it rumelin" not in erle.asked:
            hide mcPic
            $ erle.asked.append("was it rumelin")
        "Znáš nějak blíž mistra Njala?" if njalNote.isActive and "njal" not in erle.asked:
            hide mcPic
            $ erle.asked.append("njal")
            $ erle.say("Trochu. Když sem přišel, docela se o mě zajímal. Myslel si, že potřebuju pomoct. Teď už ho to naštěstí přešlo.")
            $ erle.say("Pořád mi občas donese kousek masa a placku k jídlu nebo mě požádá, abych mu za pár měďáků něco uklidila. To je od něj milé. A potřebuje to, není to zrovna pořádný mužský a jeho učedníci nejsou o nic lepší.", "happy")
        "Co si o mistru Njalovi myslíš?" if "njal" in erle.asked and "njal 2" not in erle.asked:
            hide mcPic
            $ erle.asked.append("njal 2")
            $ erle.say("Já si většinou o nikom nic nemyslím. Šetří mi to spoustu překvapení. Občas i zklamání. Působí ale jako slušný člověk.")
            $ erle.say("Myslím, že si o sobě myslí, že je docela chytrý. A v lecčem asi opravdu je. Nic si nedělá z tradic a klidně odešel do města, kde moc trpaslíků není, a při výrobě zkouší i takové věci, které by jeho mistři a otcové nemohli snést.")
            $ erle.say("Ale zároveň je pořád hloupý. Myslím, že mu hodně záleží na těch lidských slavnostec. Ne proto, že by tak uctíval Einiona, ale protože se potřebuje předvést a bude zklamaný, jestli jeho výrobek nezíská dostatečné uznání.")
            $ erle.say("Jak může být chytrý někdo, kdo si nechá ublížit jen tím, že ho několik zkostnatělých lidí odsoudí?")
        "Bylo mezi těmi odpadky ještě něco dalšího?" if "bottles 2" in erle.asked and "anything else" not in erle.asked:
            hide mcPic
            $ erle.asked.append("anything else")
            $ erle.say("Nějaké odstřižky a kusy kůže a jedny poničené boty. Ty byly taky hezké, ale moc tenké na rozumné nošení, i kdyby nebyly popálené a celé promočené. Ale proč vyhodili ty lahve, to nechápu.")
            $ erle.say("No, jejich škoda. Stěžovat si nebudu.", "happy")
        "Máš ty boty ještě? Můžu je vidět?" if "anything else" in erle.asked and "shoes" not in erle.asked:
            hide mcPic
            $ erle.asked.append("shoes")
            $ erle.say("Nechala jsem je tam. K čemu by mi byly?")
        "Přesně stejné lahve se ztratily z domu mistra Heinricha." if "bottles" in erle.asked and "bottles stolen" not in erle.asked:
            hide mcPic
            $ erle.asked.append("bottles stolen")
            $ erle.say("Pak má Heinrich dobrý vkus.", "happy")
            $ erle.say("A asi je bohatý a neví, že sklo má cenu.")
            "Erle pokrčí rameny."
        "Můžu ti nějak pomoct?" if "help" not in erle.asked:
            hide mcPic
            $ erle.asked.append("help")
            $ erle.say("Já nepotřebuju pomoct. Mám přesně to, co potřebuju.", "happy")
            $ erle.say("Ale jestli ti na tom záleží, můžeš mi čas od času přinést něco malého k jídlu nebo mi zaplatit pár drobáků za to, že něco uklidím nebo někam donesu.")
        "Proč nežebráš na nějakém lepším místě? Třeba před nějakých chrámem?" if "chosen place" not in erle.asked:
            hide mcPic
            $ erle.asked.append("chosen place")
            $ mc.say("Mohla bys mít víc peněz.")
            $ erle.say("Stačí mi, když se mám další den za co najíst. Tady se mi líbí a nemusím tu poslouchat žádné poučky o správné cestě. Navíc pod most se můžu schovat před deštěm nebo kroupami.", "happy")
        "Kdybys potřebovala střechu nad hlavou, vím o jedné ubytovně." if sabri.alreadyMet == True and "Sabri" not in erle.asked:
            hide mcPic
            $ erle.asked.append("Sabri")
            $ erle.say("Tu, co ji vede ten divný kněz, jak se to... Sabri?")
            $ mc.say("Ano...")
            $ erle.say("Tak to nejsi první, kdo mě tam posílá.")
            $ mc.say("A Sabri tě nepřijal?")
            $ erle.say("Nelíbil se mi. Pořád do každého něco hučí o tom, že je lepší než ostatní, má na víc a měl by za tím jít.", "angry")
            show mcPic at menuImage
            menu:
                "A co je na tom špatně?":
                    hide mcPic
                "Taky se mi nelíbil, ale není to lepší, než spát na ulici?":
                    hide mcPic
                    $ erle.say("Radši budu na ulici s čistou hlavou, než pod jednou střechou s někým takovým. Nemohla jsem se zbavit pocitu, že by se mnou měl nějaké vlastní plány.")
            $ erle.say("A co je špatně na tom, být spokojená s tím, co mám?")
        "Jak můžeš být spokojená s tímhle životem?" if "Sabri" in erle.asked and "satisfied" not in erle.asked:
            hide mcPic
            $ erle.asked.append("satisfied")
            $ erle.say("Je hezký den a já měla k snídani moc dobrou teplou polívku. Nic mi nechybí a nic mi nepřebývá.", "happy")
            $ mc.say("Co střecha nad hlavou, ta ti opravdu nechybí?")
            $ erle.say("Aspoň se nemusím bát, že o ni zase přijdu. K čemu je pachtit se za věcmi, které ti potom stejně nezůstanou?")
        "Mohla bys mě naučit, jak být spokojen[y] v bídě?" if "teach me" not in erle.asked:
            call erleTeachMe
        "Myslíš, že takhle na tebe můžou být tví předkové hrdí?" if race == "dwarf" and "ancestors" not in erle.asked:
            hide mcPic
            $ erle.asked.append("ancestors")
            $ erle.say("Podle předků jsem se snažila žít většinu života. Štěstí mi to nepřineslo a jestli na mě předkové hrdí byli, pak mi to nedali nijak najevo. Tak teď ať si svůj názor nechají pro sebe.", "angry")
            $ erle.say("Oni to mají jednoduché, ti už o nic přijít nemůžou.")
            show mcPic at menuImage
            menu:
                "To není pravda.":
                    hide mcPic
                    $ mc.say("Pokud na naše předky zapomeneme, přestaneme o nich vyprávět a vážit si jich, nic po nich nezůstane. To ti nepřijde jako ztráta?")
                    $ erle.say("Pak budeme mít konečně klid a oni taky.")
                    "Erle pokrčí rameny, ale její sevřené rty a pohled stranou působí méně lhostejně, než by asi chtěla."
                "Na tom vlastně něco bude.":
                    hide mcPic
                    "Erle mlčky přikývne a dál už se k tématu nevrací."
        "Máš někoho, kdo bude po tvé smrti vyprávět tvůj příběh?" if race == "dwarf" and "who will tell your story" not in erle.asked:
            hide mcPic
            $ erle.asked.append("who will tell your story")
            $ erle.say("Můj příběh nikdo vyprávět nebude a je to tak lepší.")
            $ mc.say("To po tobě po smrti ale nic nezůstane!")
            $ erle.say("Přesně. Není to krásné?", "happy")
            show mcPic at menuImage
            menu:
                "V některých ohledech možná…?":
                    hide mcPic
                    $ erle.say("Není úžasné, kolika starostí to jednoho zbaví?", "happy")
                "To není zrovna obvyklý názor.":
                    hide mcPic
                    $ erle.say("Také neznám nikoho dalšího, kdo by si něco podobného myslel.")
                    jump erleViewOnDwarfLifeStories
                "Mně to krásné nepřipadá.":
                    hide mcPic
                    $ erle.say("To skoro nikomu.")
                    label erleViewOnDwarfLifeStories:
                    $ erle.say("Většina trpaslíků místo toho nutí ty, co je přežijí, aby se o nich učili nazpaměť spoustu zbytečností. Kde žili, co vyráběli, s kým bojovali…")
                    $ erle.say("Přitom jejich výrobky už se většinou rozpadly, v jejich domovech žije někdo jiný a na dávných bitvách už nezáleží a ty příběhy jsou stejně z půlky lež a z druhé samá bolest.")
                    show mcPic at menuImage
                    menu:
                        "Na tom něco bude…":
                            hide mcPic
                            $ erle.say("Zase nenech starou Erle, aby se ti dostala moc hluboko do hlavy.", "happy")
                        "Pořád se mi to nezdá.":
                            hide mcPic
                            $ erle.say("Nečekám, že tě přesvědčím, a ani se o to nechci snažit.")
                    $ erle.say("Pozorovat řeku je mnohem příjemnější. Vidíš tu rybu, jak se snaží něco sezobnout z hladiny?")
        "Potřebuju se vyptat místních hostinských na obchody mistra Rumelina. Obejdeš je pro mě?" if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status and "help" in erle.asked:
            hide mcPic
            $ erle.asked.append("asked to investigate less deals")
            $ mc.say("Můžeš si tím vydělat jídlo na dalších pár dní.")
            $ erle.say("Obejít pár hospod určitě můžu, ale budu rozumět tomu, co mi řeknou?", "surprised")
            $ mc.say("Je to poměrně jednoduché. Rumelin vždy uzavíral obchody hlavně U Splašeného koně, ale Salma říkala, že v poslední době už tam nechodí. Potřebuju zjistit, jestli teď chodí někam jinam.")
            $ mc.say("Možná si jen oblíbil jinou hospodu, to se může stát. Ale jestli najednou obchody neuzavírá, bude mě zajímat, co za tím vězí.")
            $ mc.say("Jedná se o nákup ševcovského materiálu, ne o prodej bot.")
            $ erle.say("To zvládnu. Hned na to půjdu!", "happy")
            $ erle.say("... mám jim říkat, že to je pro hlídku? Jinak mi to možná nebudou chtít říct.", "surprised")
            show mcPic at menuImage
            menu:
                "Ano, řekni, že se ptám já a jen mi šetříš čas.":
                    hide mcPic
                    $ erle.say("Dobře, to by je mělo přesvědčit snadno.", "happy")
                    $ status.append("add Rauvin finds out about AML")
                    $ erle.asked.append("working for the watch")
                "Neříkej, vymysli si jiný důvod.":
                    hide mcPic
                    $ mc.say("Třeba že jsem tohle náhodou zmínil[a], když jsem s tebou mluvil o botách mistra Heinricha, a ty máš o mistra Rumelina starost.")
                    $ erle.say("Já ti nevím, v tomhle nejsem moc dobrá… ale uvidím, co se dá dělat.", "sad")
                    $ erle.asked.append("investigating excuse")
                "Neříkej a nic nevysvětluj. Když tě odbydou, nedá se nic dělat.":
                    hide mcPic
                    $ erle.say("Dobře, snad budou ochotní.")
                    $ erle.asked.append("investigating without explanation")
            $ erle.say("Hned se do toho pustím a pak tě někde najdu.")
            $ status.append("add investigating less deals erle")
            "Erle vstane, protáhne si záda a vyrazí do města."
            return
        "Zatýkám tě za krádež mistrovského výrobku mistra Heinricha." (badge="handcuffs") if erle not in allArrested:
            hide mcPic
            $ erle.say("Za krádež čeho?", "surprised")
            $ mc.say("Těch bot, které jsi pak zahodila.")
            $ erle.say("Myslíš těch, co byly ve vodě u skleněných lahví? Jak bych mohla ukrást něco, co jsem nechala na místě?", "surprised")
            $ mc.say("Žádné výmluvy, prostě půjdeš se mnou.")
            "Erle mírně zmateně zavrtí hlavou a nechá se odvést na strážnici."
            $ erle.arrestReason.append("stolen shoes")
            $ newlyArrested.append(erle)
            $ status.append("arrest in progress")
            return
        "To jsou všechny moje otázky.":
            hide mcPic
            return
    jump erleOptions

label leavingErle:
    menu:
        "{i}(Zkontrolovat místo nálezu){/i}":
            "Vydáš se po proudu řeky, rozhlížíš se po břehu a doufáš, že tu boty pořád ještě budou."
            scene bg riverbank
            "Slunce stále příjemně svítí, ale tady u vody je o něco chladněji než uprostřed města a proud unáší spadané listy. Doufáš, že se ti podaří u hlídky uchytit a nebudeš muset trávit zimu někde na profukujícím seníku."
            "Nakonec Heinrichovy boty v blátě málem přehlédneš a musíš se několik kroků vrátit. Promočený, špinavý a deformovaný kus fialové kůže mistrovské dílo příliš nepřipomíná a až na bližší pohled začneš rozpoznávat kovové ozdoby a elegantní tvarování."
            "Pokusíš se je v řece co nejvíc očistit, ale nemusíš být švec, aby ti bylo jasné, že je už nelze zachránit."
            $ status.append("stolen shoes found")
        "{i}(Vrátit se na strážnici){/i}":
            pass
    return

###

label erleTeachMe:
    hide mcPic
    $ erle.asked.append("teach me")
    if time.hours > 17:
        $ erle.say("Vidíš, jak krásně svítí hvězdy? Stačí si prostě říct, že víc k dobrému životu nepotřebuješ.")
    else:
        $ erle.say("Vidíš, jak krásně svítí slunce? Stačí si prostě říct, že víc k dobrému životu nepotřebuješ.")
    show mcPic at menuImage
    menu:
        "Mít hezký dům a spoustu dobrého jídla by mi přišlo mnohem lepší.":
            hide mcPic
            $ erle.say("Dokud bys o to nepři[sel]. Pak by to bylo mnohem horší, než nemít nic od začátku.", "sad")
        "Na tom možná něco bude.":
            hide mcPic
            "Erle jen přikývne a víc se k tématu nevrací."
        "Co bys dělala, kdyby pršelo?":
            hide mcPic
            $ erle.say("Schovala se pod most, poslouchala zvuk deště a užívala si, že kolem nikdo není a já mám klid.")
    return

###

label erleOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "bottles" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles" in erle.asked and "bottles 2" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles 2" in erle.asked and "bottles location" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles 2" in erle.asked and "anything else" not in erle.asked:
        $ optionsRemaining += 1
    if "anything else" in erle.asked and "shoes" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles" in erle.asked and "bottles stolen" not in erle.asked:
        $ optionsRemaining += 1
    if "chosen place" not in erle.asked:
        $ optionsRemaining += 1
    if sabri.alreadyMet == True and "Sabri" not in erle.asked:
        $ optionsRemaining += 1
    if "Sabri" in erle.asked and "satisfied" not in erle.asked:
        $ optionsRemaining += 1
    if race == "dwarf" and "ancestors" not in erle.asked:
        $ optionsRemaining += 1
    if "teach me" not in erle.asked:
        $ optionsRemaining += 1
    if "bottles 2" in erle.asked and "see who threw bottles away" not in erle.asked:
        $ optionsRemaining += 1
    if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it kaspar" not in erle.asked:
        $ optionsRemaining += 1
    if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it apprentices" not in erle.asked:
        $ optionsRemaining += 1
    if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it gerd" not in erle.asked:
        $ optionsRemaining += 1
    if "who threw bottles away" in erle.asked and "anything else" in erle.asked and "was it rumelin" not in erle.asked:
        $ optionsRemaining += 1
    if njalNote.isActive and "njal" not in erle.asked:
        $ optionsRemaining += 1
    if "njal" in erle.asked and "njal 2" not in erle.asked:
        $ optionsRemaining += 1
    if "help" not in erle.asked:
        $ optionsRemaining += 1
    if race == "dwarf" and "who will tell your story" not in erle.asked:
        $ optionsRemaining += 1
    if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status and "help" in erle.asked:
        $ optionsRemaining += 1
    if erle not in allArrested:
        $ optionsRemaining += 1
    return
