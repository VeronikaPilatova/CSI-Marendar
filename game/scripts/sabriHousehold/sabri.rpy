label sabriController:
    $ origAsked = sabri.asked.copy()
    if sabri.alreadyMet == False:
        call sabriFirst
    else:
        call sabriAgain
    call sabriOptions
    if sabri.alreadyMet == False:
        $ sabri.alreadyMet = True
        $ sabriNote.isActive = True

    # adjust time spent
    $ lastSpokenWith = "sabri"
    $ time.addMinutes((len(sabri.asked) - len(origAsked)) * 3)
    return

label sabriFirst:
    scene bg sabri outside
    $ sabri.say("Vítej. Jsem Sabri a tahle ubytovna je moje dílo. Jestli potřebuješ útočiště před křivdou nebo tlakem okolí, dokážu pomoct.")
    scene bg sabri inside
    return

label sabriAgain:
    scene bg sabri outside
    $ sabri.say("Vítej. Co tě tíží tentokrát?")
    scene bg sabri inside
    return

label sabriOptions:
    call sabriOptionsRemainingCheck
    call zeranOptionsRemainingCheck
    if sabriOptionsRemaining == 0 and zeranOptionsRemaining == 0:
        return

    show mcPic at menuImage
    menu:
        "Co je tohle za místo?" if "place" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("place")
            $ sabri.say("Marendar? Město, které málem zadusilo samo sebe a teď teprve hledá, jak pokračovat dál.")
            $ sabri.say("Dočasná čtvrť? Budoucí chudinská čtvrť. Část města pro ty, kdo si nemohou dovolit víc. Nádeníci, někteří tovaryši, nemocní. Pár domů se tu ještě opraví a část obyvatel se přesune jinam. Většina zdejších bude živořit podobným způsobem jako teď do konce života.")
            $ sabri.say("A tenhle dům? Sem přichází ti, kdo svoje postavení chtějí změnit. Kdo cítí, že si zaslouží víc.")
        "To zní jako nebezpečná sebranka." if "place" in sabri.asked and "dangerous people" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("dangerous people")
            $ sabri.say("Nebezpečná zaběhnutým pořádkům nebo něčímu pocitu nadřazenosti možná ano. Nebezpečná zdraví nebo majetku ne. Nepouštím sem lidi, kteří touží po pomstě, jen ty, kteří si chtějí vybudovat nový život.")
        "Co to je za lidi?" if "place" in sabri.asked and "people" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("people")
            $ sabri.say("Ti, kteří se nějak narodili a jinak chtějí žít. Hlavně lidé a elfové, ale už tu byl i jeden trpaslík. Mají vůli, mají schopnosti, nemají prostředky.")
            $ mc.say("A ty prostředky máš?")
            $ sabri.say("Nějaké ano. Svoje životy ale mění sami, s mojí podporou.")
        "Co tady ti lidé dělají?" if "place" in sabri.asked and "what people do here" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("what people do here")
            $ sabri.say("Hledají si svou cestu. Posilují svou sebejistotu a utvrzují se v tom, co opravdu chtějí. Část jich pak odejde do jiného města, část si najde uplatnění tady. Část jich cestu nedokončí, protože selže jejich vůle.")
        "Proč jim takto pomáháš?" if "place" in sabri.asked and "why help" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("why help")
            $ sabri.say("Jsem kněz Purushotamy. Můj bůh stojí za všemi, kdo se cítí zrazení, opuštění nebo nedocenění a mají odhodlání to změnit. Podporuje všechny, kdo chtějí žít v jiném řádu než v tom, do kterého se narodili. Sloužím bohu a lidem a tím i celému městu, protože ti lidé pak dokážou mnohem víc.")
            $ mc.say("A co z toho máš ty? Jak ty měníš svůj život?")
            $ sabri.say("Já už svůj život dávno změnil. Získal jsem naplnění. Co bych měl žádat víc?")
        "Znáš Hayfu?" if "hayfa" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("hayfa")
            $ sabri.say("Jistě. Takových jako ona by město potřebovalo co nejvíc.")
        "Proč zrovna jako ona?" if "hayfa" in sabri.asked and "what makes hayfa special" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("what makes hayfa special")
            $ sabri.say("Protože bude chránit město do roztrhání těla a protože je neobyčejně schopná. Ale to bys přece měl[a] vědět lépe než já. Já nesloužím v hlídce, ty ano.")
        "Jak jste se poznali?" if "hayfa" in sabri.asked and "meeting hayfa" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("meeting hayfa")
            call sabriAboutHayfaPast
        "Kde se to všechno naučila?" if "hayfa" in sabri.asked and "hayfa skills" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("hayfa skills")
            call sabriAboutHayfaPast
        "Jak to v dočasné čtvrti chodí?" if "temporary quarter" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("temporary quarter")
            $ sabri.say("Jako v každé chudé čtvrti. Lidé se protloukají, jak jen mohou.")
            $ sabri.say("Elfové a lidé se stále ještě úplně neusmířili a moc se nestýkají. A jsou tu i takoví, kdo nejsou přijímaní ani mezi komunitou vlastní rasy v dočasné čtvrti. Ti stojí opravdu na kraji společnosti.")
            $ mc.say("A ti pak končí u tebe, předpokládám?")
            $ sabri.say("Často se o to pokouší. Ne všichni jsou vhodní.")
        "Bydlí tady Zeran?" if zeranNote.isActive == True and "zeran" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran")
            $ sabri.say("Ano.")
        "Můžu se Zeranem mluvit?" if "zeran" in sabri.asked and zeranOptionsRemaining > 0:
            hide mcPic
            $ sabri.say("Pokud bude chtít. Počkej tady.")
            "Sabri se otočí a vejde hlouběji do domu. Tlumeně zaslechneš klepání na dveře a krátký nezřetelný rozhovor. Potom se před tebou objeví mladý elf s nepřátelským pohledem."
            jump zeranController
        "Tušíte, co má Zeran v plánu?" if "zeran" in sabri.asked and "zeran plans" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran plans")
            $ sabri.say("Pokud vím, získat nějaké peníze a odejít jinam. Nebo odejít i bez peněz, jestli to bude trvat moc dlouho. Tohle město ho zklamalo.")
        "Dalo by se Zeranovi nějak pomoci?" if "zeran" in sabri.asked and "zeran help" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran help")
            $ sabri.say("Peníze asi neodmítne, ale myslím, že hlavně potřebuje pocit, že ho někdo bere vážně.")
        "Opravdu měl Zeran vztah s Heinrichovou dcerou?" if "zeran" in sabri.asked and "zeran and ada" not in sabri.asked and "Zeran offense" in clues:
            hide mcPic
            $ sabri.asked.append("zeran and ada")
            $ sabri.say("Neměl.")
            $ mc.say("Proč si to myslíte?")
            $ sabri.say("Jsem kněz a nějakou dobu už u mně žije.")
            $ sabri.say("Správná otázka podle mě zní, jak ho z toho někdo mohl podezřívat. Kdyby spolu něco měli, nejspíš by jí nepsal básničky a určitě by ji nezapíral i poté, co ho vyhnali.")
            $ clues.append("Zeran innocent")
        "Je možné, že Zeran ukradl výrobek mistra Heinricha určený pro Einionovy slavnosti?" if "zeran" in sabri.asked and "zeran thief" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran thief")
            $ sabri.say("To si nemyslím. Kdyby se chtěl mstít, nezůstal by jen u jedněch bot a okamžitě by po činu utekl z města.")
        "Byl včera v noci Zeran opravdu nedaleko západní brány? Tvrdí, že tam pracoval." if "alibi" in zeran.asked and "zeran alibi" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran alibi")
            $ sabri.say("Vím, že si domluvil práci, většinu noci byl pryč a ráno se vrátil s penězi. Také jsem potom nepotkal nikoho, kdo by si stěžoval, že ta práce nebyla odvedená. Věřím, že toho by si všimli.")
            $ sabri.say("Ale jestli byl u západní brány, nebo u východní, na to jsem se neptal.")
        "Mám důkazy, že Zeran je nevinný." if "letters for Ada seen" in status and "zeran cleared" not in status and "zeran innocent" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("zeran innocent")
            $ sabri.say("Výborně. A jak s nimi naložíš?")
            show mcPic at menuImage
            menu:
                "Půjdu s nimi za hlídkou.":
                    hide mcPic
                    $ sabri.say("V tom případě bych ti doporučil, abys je předal[a] Hayfě.")
                    $ sabri.say("Co vím, o osud chudých lidí se tam zajímá nejvíc.")
                "Půjdu s nimi za mistrem Heinrichem.":
                    hide mcPic
                    $ sabri.say("Pak doufám, že ty důkazy jsou opravdu přesvědčivé. Pokud vím, mistr Heinrich nerad mění názor.")
                "Předám vám je a bude na vás, jak s nimi naložíte. Můj případ to není.":
                    hide mcPic
                    $ sabri.say("Krádež bot je podstatnější než zničený život mladého elfa?")
                    $ sabri.say("Dobrá, není na mně, abych to posuzoval.")
                    $ sabri.say("Poslouchám.")
                    label sabriToldProofZeranInnocent:
                    call zeranInnocentProofSummary
                    $ mc.say(zeranInnocentProofSummary)
                    if "confession" in zairis.asked:
                        $ mc.say("Navíc se ke vztahu s Adou přiznal někdo jiný.")
                        $ sabri.say("Kdo?")
                        show mcPic at menuImage
                        menu:
                            "Zairis, syn obchodníka Roviena.":
                                hide mcPic
                                $ sabri.trust += 1
                                call zairisGuiltyProofSummary
                                if zairisGuiltyProofSummary != "":
                                    $ mc.say(zairisGuiltyProofSummary)
                            "To je soukromá věc těch dvou.":
                                hide mcPic
                                $ sabri.say("Je to také věc Zerana a teď už i má, jak velmi dobře víš, a do soukromých věcí těch dvou už jsi podle všeho zasáhl.")
                                $ sabri.say("Pokud mi to ale nechceš říct a důvod schováváš za ohleduplnost, dobrá.")
                    $ sabri.say("Děkuji ti za důkazy, které jsi přednesl[a]. Využiji je, jak nejlépe to bude možné.")
                "To záleží na tom, co mi za ně můžete nabídnout.":
                    hide mcPic
                    $ sabri.say("Jakou platbu se představuješ? Peníze dávám na chod ubytovny a vlivu ve městě mám pramálo.")
                    show mcPic at menuImage
                    menu:
                        "Buď něco vymyslete, nebo vám ty důkazy nedám.":
                            hide mcPic
                            $ sabri.say("Tuto hru hrát nebudu. Potřebujete mluvit o něčem důležitém?")
                            jump sabriOptions
                        "Přesvědčte Hayfu, aby mi hlídka udělala službičku.":
                            hide mcPic
                            $ sabri.say("O něčem takovém ji nikdo nepřesvědčí a nemá smysl se o to pokoušet.")
                            $ sabri.say("Potřebujete mluvit o něčem důležitém, nebo tento rozhovor ukončíme?")
                            jump sabriOptions
                        "Zařiďte mi nějaké lepší bydlení.":
                            hide mcPic
                            $ sabri.say("Dokážu zařídit samostatný slušný kamrlík tady v dočasné čtvrti. Za cenu, kterou z hlídkařského platu bez potíží zaplatíš.")
                        "Budu u vás mít službičku.":
                            hide mcPic
                            $ sabri.say("S tím se dá souhlasit. Jestli budete potřebovat něco rozumného, někdo odtud najde chvíli, aby s tím pomohl.")
                    $ sabri.say("Teď chci slyšet ty důkazy.")
                    jump sabriToldProofZeranInnocent
        "Byla Hayfa v Marendaru během požáru?" if "Hayfa experienced fire" in globalClues or "Killian encounter" in status and "Hayfa experienced fire" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("Hayfa experienced fire")
            $ globalClues.append("Hayfa's arrival to Marendar")
            $ sabri.say("Ne, přišli jsme asi o rok po něm. Proč?")
            if "Hayfa experienced fire" in globalClues:
                $ mc.say("Hayfa říkala, že požár města zažila.")
                $ sabri.say("A mluvila pravdu. Zažila ho později a jiným způsobem než všichni ostatní, ale o nic méně skutečně.")
            else:
                $ mc.say("Působí, že pro ni ta událost je hodně osobní.")
                $ sabri.say("A přesně tak to je. Zažila požár později a jiným způsobem než všichni ostatní, ale o nic méně skutečně.")
            $ mc.say("Tomu nerozumím, jakým způsobem?")
            $ sabri.say("To si nechám pro sebe.")
        "Slyšel[a] jsem, že jste se s Hayfou pokusili ovládnout celé město." if "hayfa's past" in globalClues and "past crimes" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("past crimes")
            $ sabri.say("A co dalšího jsi slyšel[a]?")
            show mcPic at menuImage
            menu:
                "Že to už je dlouho a od té doby městu oba pomáháte.":
                    hide mcPic
                "Že váš vůdce chtěl celý Marendar podpálit.":
                    hide mcPic
                "Že jste málem zabili purkmistra.":
                    hide mcPic
                "Že jste obalamutili spoustu slušných lidí.":
                    hide mcPic
                "Ne dost, proto se ptám vás.":
                    hide mcPic
                    $ sabri.say("Co myslíš, že uslyšíš, aby to změnilo tvůj názor?")
            $ sabri.say("Říká se toho hodně a většina je pravda.")
            $ sabri.say("Naši tehdejší vůdcové vytyčili cestu a my ji pomáhali projít. Oni jsou teď mrtví, naše původní společenství se rozpadlo, Hayfa si Marendar zamilovala nade vše a i já se tu rozhodl zůstat.")
            $ sabri.say("O moc víc nemá smysl dodávat. Názor na to celé si tvoříš [sam] a já nemám v úmyslu se tě v tom pokoušet ovlivňovat.")
        "Jak je možné, že vás město nepotrestalo?" if "past crimes" in sabri.asked and "not punished" not in sabri.asked:
            hide mcPic
            $ sabri.asked.append("not punished")
            $ sabri.say("Potrestalo. Ridiana oběsili, to byl ten, kdo nás tehdy vedl, a já a Hayfa jsme strávili hodně času prací pro město.")
            $ sabri.say("A už nám to zůstalo.")
            $ mc.say("To se nikdo nebál, že prostě utečete?")
            $ sabri.say("Původní trest mělo být vyhnanství, Hayfa hodně prosila, aby tu mohla zůstat.")

        "Už vás dál nebudu zdržovat. Děkuji vám za pomoc.":
            hide mcPic
            return

    if len(sabri.asked) - len(origAsked) > 3 and "mc faith" not in sabri.asked:
        $ sabri.say("Teď se zeptám pro změnu já. Jaký bůh je ti nejbližší?")
        $ sabri.asked.append("mc faith")

        show mcPic at menuImage
        menu:
            "Následuji trpasličí tradice, stejně jako mí předkové." if race == "dwarf":
                hide mcPic
                $ personality.append("faith - dwarf traditions")
                $ sabri.say("A je to pro tebe zdroj jistoty, nebo jen neustálého tlaku? Je to připomínka velikosti tvého lidu, nebo velikosti jeho ztráty?")
                show mcPic at menuImage
                menu:
                    "O tom s tebou nemíním mluvit. Nejsi trpaslík, nemůžeš to pochopit.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("To je v pořádku. O některých věcech je lepší přemýšlet o samotě.")
                    "Jsou to pevné základy, díky kterým mnou nic nemůže otřást.":
                        hide mcPic
                        $ sabri.say("Potom máš velké štěstí. Alespoň dokud to nezačne znamenat ustrnutí na místě, kde už nic nečeká.")
                    "Upřímně, je to hlavně zvyk.":
                        hide mcPic
                        "Sabri jen krátce přikývne a nijak už nenavazuje."
            "Držím se tradic svého lidu." if race == "hobbit" or race == "elf":
                hide mcPic
                if race == hobbit:
                    $ personality.append("faith - hobbit traditions")
                    $ sabri.say("To u hobita není nic překvapivého. Pevná oddanost starým učením, bez ohledu na to, kolik předsudků a temných podezření vyvolávají.")
                    $ mc.say("Na té víře není nic temného. Na bohy lidí nebo elfů jsme moc malí, tak se modlíme po svém, to je všechno.")
                    $ sabri.say("O víře hobitů se skoro nic neví. Neznámo vždy vyvolává nejistotu.")
                    $ mc.say("Nebudu přece opouštět víru svých otců jen proto, že lidé za vším vidí to nejhorší.")
                    $ sabri.say("Ta volba je jen tvá.")
                elif race == elf:
                    $ personality.append("faith - elf traditions")
                    $ sabri.say("A cítíš se být v harmonii se světem, ke které by ta víra měla vést?")
                    show mcPic at menuImage
                    menu:
                        "Jak mám cítit harmonii, když třu bídu s nouzí?":
                            hide mcPic
                            $ cultistMaterial += 1
                            $ sabri.say("Teď aspoň máš dlouhodobou práci.")
                            $ mc.say("V hlídce jsem velmi krátce, ještě nevím, jestli v ní vidět svou budoucnost.")
                            $ sabri.say("Budoucnost je taková, jakou si ji vytvoříš, v hlídce, nebo mimo ni.")
                        "Jistě! Ostatně svět se teď zase mění k lepšímu. To je důkaz, že nerovnováha není přirozená a sama vždy skončí.":
                            hide mcPic
                            $ sabri.say("Sama, nebo přičiněním několika nebo možná mnoha lidí a jejich vůle?")
                            show mcPic at menuImage
                            menu:
                                "Samozřejmě, že každá změna se děje prostřednictvím lidí. To, že se takoví lidé vždy objeví, je přece součástí toho přirozeného návratu světa k rovnováze.":
                                    hide mcPic
                                    $ sabri.say("Pak ti tedy přeji, aby se takoví našli vždy, když tě stihne neštěstí. A aby se našli včas.")
                                "Pokud to má být otázka, jestli mám odhodlání se o to také zasloužit, tak samozřejmě!":
                                    hide mcPic
                                    $ cultistMaterial += 1
                                    $ sabri.say("Na to může být hlídka velmi vhodné místo.")
                                    $ mc.say("Přesně tak.")
            "Einion. Moje práce je pro mne důležitá a jsem na ní stejně hrd[y], jako bývají řemeslníci a umělci.":
                hide mcPic
                $ personality.append("faith - Einion")
                $ sabri.say("Tím myslíš hlídku? Nejsi v ní jen krátce?")
                show mcPic at menuImage
                menu:
                    "Tím myslím své písařské umění.":
                        hide mcPic
                        $ sabri.say("Kterému se ale nevěnuješ. Místo toho nosíš glejt se znakem hlídky a hledáš cizí boty.")
                    "Ano, tím myslím hlídku. Vždy jsem doufal[a] v práci, která bude něco znamenat, a teď jsem ji konečně na[sel].":
                        call einionFollowerWatch
                    "Jsem hrdý na každou práci, kterou dělám, a vždy ji dělám, jako by mělo vzniknout to nejdražší dílo.":
                        hide mcPic
                        $ sabri.say("A jde ti tedy jen její o precizní provedení, nebo o její smysl?")
                        $ mc.say("Nebudu přece dělat nic, co smysl nemá.")
                        $ sabri.say("Hodně řemeslníků a umělců se stejně jako Heinrich honí jenom za precizní technikou. Pro jiné je jediný smysl jejich práce to, že za ni dostanou pár mincí, a veškerý další účel jim uniká.")
                        $ sabri.say("Myslím, že stojí za to se ptát, k jakému cíli která činnost vede.")
            "Chci hlavně chránit ostatní a Saral mi k tomu pomáhá najít sílu a neústupnost.":
                hide mcPic
                $ personality.append("faith - Saral")
                $ sabri.say("A kdo přesně to je, ti ostatní, které chceš chránit?")
                show mcPic at menuImage
                menu:
                    "Všichni, kdo to potřebují.":
                        hide mcPic
                        $ cultistMaterial -= 1
                        $ sabri.say("A počítáš mezi ty všechny i sebe sama?")
                    "Všichni mé rasy.":
                        hide mcPic
                        $ cultistMaterial -= 1
                        $ sabri.say("S tímto přístupem můžeš zrovna v Marendaru hodně ošklivě narazit. V minulosti vedl k mnoha mrtvým.")
                        $ sabri.say("Co je důležitější, leckdo tvé rasy má oproti tobě úplně rozdílnou povahu, přesvědčení, bohatství nebo možnosti, někteří dokonce uctívají jiné bohy. Z čeho tedy tvá sounáležitost pramení?")
                    "Všichni, kdo si to zaslouží.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("A kdo to je? Ti, do dodržují zákony, které jsi nepsal[a]? Ti, kdo jednají podle tvé vlastní morálky, aniž byste o tom spolu mluvili?")
                    "Moje rodina a přátelé.":
                        hide mcPic
                        $ sabri.say("Působíš, že ve městě nejsi dlouho. Kolik opravdu blízkých lidí tady máš?")
                $ sabri.say("Ne každý věřící přemýšlí o tom, co jejich odpověď znamená. Doufám, že ty ano.")
            "Carys, protože bez lásky nic dalšího nemá význam":
                hide mcPic
                $ personality.append("faith - Carys (love)")
                $ sabri.say("Carys ti může dát šťastnou lásku, ale nebude se zajímat, o co přijdeš výměnou. Nebojíš se, že pro lásku ztratíš svoje další touhy?")
                show mcPic at menuImage
                menu:
                    "I kdyby k tomu došlo, bude to podružné.":
                        hide mcPic
                        $ cultistMaterial -= 1
                        $ sabri.say("Stavět život jen na lásce je nebezpečné. Jestli ji z jakéhokoli důvodu ztratíš, nemáš pak vůbec nic.")
                    "Nic obětovat nemám v úmyslu. Lásce poručit nemůžu, ale vše ostatní si dokážu získat vlastní silou.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("Carys ani její kněží nejsou známí tím, že by pomáhali získat například uznání druhých nebo dostatečné živobytí. Dokážeš všechny své touhy naplnit [sam] jen prací v hlídce?")
                        show mcPic at menuImage
                        menu:
                            "Jsem o tom přesvědčen[y].":
                                hide mcPic
                                $ sabri.say("Potom máš zřejmě velmi vysoké sebevědomí, nebo velmi skromné touhy. Když si nedáš pozor, obojí ti může ublížit.")
                            "Nic lepšího nemám.":
                                hide mcPic
                                $ sabri.say("Když se budeš dobře dívat, možná něco lepšího najdeš.")
            "Carys, protože je to i bohyně štěstí a to nakonec stejně rozhoduje.":
                hide mcPic
                $ personality.append("faith - Carys (luck)")
                $ sabri.say("Rozhoduje štěstí, které si [sam] připravíš, nebo štěstí, které tě potká bez tvého přičinění?")
                show mcPic at menuImage
                menu:
                    "Jen ti nejlépe připravení dokážou štěstí patřičně využít.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("Jiný bůh by ti dokázal dát nejen příležitost, ale právě i sílu se jí chopit. Jestli od Carys chceš pouze štěstí, věříš, že vše ostatní získáš [sam]?")
                    "Příprava nemá ve výsledku význam, stejně bude vše nakonec jinak.":
                        hide mcPic
                        $ cultistMaterial -= 2
                        $ sabri.say("Náhoda může všechno změnit, ale přesto se teď staví široké ulice a nehořlavé domy.")
                        $ sabri.say("Stejně tak život by neměl být jen shluk chatrných stavení se slaměnou střechou.")
            "Olwen. Kdo jiný než bůh cesty mi pomůže projít životem?":
                hide mcPic
                $ personality.append("faith - Olwen")
                $ sabri.say("Není ale cesta, kterou nabízí, předem vytyčená? To největší bohatství se často nachází mimo cesty, tam, kam běžně nikdo nezavítá.")
                $ mc.say("Olwen dává podporu na každé cestě, ne jen na těch, které už někdo vydláždil.")
                $ sabri.say("Olwen sám možná. U jeho kněží to může být něco jiného.")
                $ sabri.say("Olwena následuje spousta lidí a vést je všechny stejným směrem ke stejnému cíli je mnohem jednodušší.")
                $ mc.say("Ty pro každého, kdo věří v tvého boha, hledáš jeho vlastní cestu?")
                $ sabri.say("Samozřejmě. Každého provázím na cestě, kterou potřebuje projít on sám.")
                $ mc.say("To můžeš jen proto, že tady nemáš skoro žádné věřící.")
                $ sabri.say("Jestli jejich počet někdy přeroste moje síly, seženu pro ně další kněze.")
                $ sabri.say("Jaká je tvá zkušenost z kněžími Olwena? Podporují tě na té cestě, která je správná přímo pro tebe?")
                show mcPic at menuImage
                menu:
                    "Jdu stejnou cestou jako každý, tedy ano.":
                        hide mcPic
                        $ cultistMaterial -= 1
                        $ sabri.say("A je ta cesta opravdu tvá, nebo jsi jen přejal[a] cizí představu, protože ti chybí odvaha vytyčit si vlastní?")
                    "Samozřejmě, a to i přesto, že je oproti cestám ostatních odlišná.":
                        hide mcPic
                        $ sabri.say("A jsou ti kněží opravdu tak schopní, nebo jen nežádáš nijak mnoho?")
                    "Moc ne, ale to přece nemůžu čekat, když si razím cestu vlastní.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("Možná to od nich nemůžeš čekat, ale rozhodně to můžeš požadovat. Pokud kněz nedokáže věřícího provázet, jaká je tedy jeho úloha?")
                    "Vůbec, mám pocit, že se o mě vůbec nezajímají.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("Pokud pro kněží nic neznamenáš, setrváváš tedy ve víře díky osobnímu spojení přímo s Olwenem, nebo jen ze zvyku?")
                $ sabri.say("Klást si podobné otázky je důležité. Bez toho můžeš místo procházení své osobní cesty snadno ustrnout na místě a ani si to neuvědomit.")

            "Snažím se žít hlavně podle svého svědomí a s úctou ke všem bohům.":
                hide mcPic
                $ personality.append("faith - own conscience")
                $ sabri.say("Svědomí různých lidí se může hodně lišit. Nakolik se to tvé dostává do sporu s očekáváním tvého okolí?")
                show mcPic at menuImage
                menu:
                    "Málokdy. Většinou se s lidmi docela shodnu.":
                        hide mcPic
                        $ cultistMaterial -= 1
                        $ sabri.say("Pak máš buď velké štěstí, nebo nad slovy svého svědomí příliš nepřemýšlíš.")
                    "Velmi často. Většina lidí si nevidí na špičku nosu.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("S tím lze souhlasit. To těžké je uvědomit si to, ale nestat se zároveň jedním z nich.")
            "Ve skutečnosti mě neoslovil žádný z bohů, které znám.":
                hide mcPic
                $ personality.append("faith - still searching")
                $ cultistMaterial += 1
                $ sabri.say("Pak jsi možná zatím jen nepotkal[a] toho pravého.")
                $ sabri.say("Není to ale obvyklé. Znamená to, že ti nestačí bůh řemeslníků, bůh zamilovaných, bůh všech, kteří svůj život vidí jako neustálý pohyb vpřed, ani žádný jiný. Co tedy u bohů očekáváš a nenacházíš?")
                show mcPic at menuImage
                menu:
                    "Bohové mi nemůžou dát nic, co si nedokážu opatřit vlastními silami.":
                        hide mcPic
                        $ sabri.say("Víra v sebe sama je také víra. Jen je jí na rozdíl od víry v sílu boha snazší otřást.")
                    "Víra mi připadá příliš svazující.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("Víra omezuje jen tolik, jak jí dovolíš. Pokud na tebe působila jako vězení, možná jsi jen potkal[a] špatné kněze.")
                        $ sabri.say("Ale jestli je pro tebe opravdu svoboda ta nejvyšší hodnota, bohyně volnosti a svobody tu je také. Není to ovšem příliš známé božstvo a já ti cestu k ní neumím ukázat.")
                    "Co vím, žádný z bohů neříká dost jasně, jak se tedy mám správně chovat.":
                        hide mcPic
                        $ cultistMaterial += 1
                        $ sabri.say("To je asi pravda. Hodně nároků mívají kněží nebo obyčejní sousedé, ale často to je jen jejich snaha člověka ovládnout. Ne vedení, které přichází přímo od boha.")
                        $ sabri.say("Takové snahy je potřeba odvrhnout.")
            "To si raději nechám pro sebe.":
                hide mcPic
                $ sabri.say("Většinou si lidé stejně brzy všimnou, do jakých chrámů kdo chodí. Je tvá víra tak neobvyklá, že ji raději tajíš, nebo nemáš odpověď, za kterou si stojíš?")
                $ sabri.say("Ale rozumím, nebudu naléhat.")

    jump sabriOptions

label sabriAboutHayfaPast:
    if "meeting hayfa" in sabri.asked and "hayfa skills" in sabri.asked:
        $ sabri.say("Řekl jsem přece, že o její minulosti nechci mluvit. Zeptej se přímo jí, ona sama se rozhodne, co ti chce sdělit.")
        $ sabri.trust -= 1
    else:
        $ sabri.say("Její minulost patří jen jí a já o ní nebudu nic říkat.")
    return

label einionFollowerWatch:
    hide mcPic
    $ sabri.say("Tedy pro tebe něco znamená hledání cizích bot? Nebo až je najdeš, tak vodění opilců domů a důležité postávání na tržišti?")
    $ mc.say("To vše je součástí udržování pořádku a to je to, co má smysl.")
    $ sabri.say("Pak se jen nezapomeň občas ptát, kdo ten pořádek ustanovil a čemu slouží.")
    return

label zeranInnocentProofSummary:
    $ zeranInnocentProofSummary = "Dostal[a] jsem se k dopisům, které měl Zeran napsat Heinrichově dceři a jsou psané na drahém papíře"
    if "zeran handwriting checked" in status:
        $ zeranInnocentProofSummary += ", navíc písmem, které se tomu Zeranovu ani v nejmenším nepodobá."
    else:
        $ zeranInnocentProofSummary += "."
    if "letters for Ada seen" in status and "Amadis grave" in zeran.asked:
        $ zeranInnocentProofSummary += " V jednom z nich se také mluví o návštěvě hrobu nového Amadise, u kterého Zeran nikdy nemohl být."
    return

label zairisGuiltyProofSummary:
    $ zairisGuiltyProofSummary = ""
    if "Zairis handwriting checked" in status or ("Zairis poem seen" in status or "letters for Ada checked in library" in status):
        $ zairisGuiltyProofSummary += "Je to i poznat"
    if "Zairis handwriting checked" in status:
        $ zairisGuiltyProofSummary += " z jeho písma"
    if "Zairis handwriting checked" in status and ("Zairis poem seen" in status or "letters for Ada checked in library" in status):
        $ zairisGuiltyProofSummary += " a"
    if "Zairis poem seen" in status or "letters for Ada checked in library" in status:
        $ zairisGuiltyProofSummary += " z toho, že píše podobnou poezii, jakou Ada dostávala"
    if "Zairis handwriting checked" in status or ("Zairis poem seen" in status or "letters for Ada checked in library" in status):
        $ zairisGuiltyProofSummary += "."
    return

###

label sabriOptionsRemainingCheck:
    $ sabriOptionsRemaining = 0
    if "place" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "dangerous people" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "people" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "what people do here" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "place" in sabri.asked and "why help" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "what makes hayfa special" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "meeting hayfa" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa" in sabri.asked and "hayfa skills" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "temporary quarter" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if zeranNote.isActive == True and "zeran" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran plans" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran help" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran and ada" not in sabri.asked and "Zeran offense" in clues:
        $ sabriOptionsRemaining += 1
    if "zeran" in sabri.asked and "zeran thief" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "alibi" in zeran.asked and "zeran alibi" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "letters for Ada seen" in status and "zeran cleared" not in status and "zeran innocent" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "Hayfa experienced fire" in globalClues or "Killian encounter" in status and "Hayfa experienced fire" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "hayfa's past" in globalClues and "past crimes" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    if "past crimes" in sabri.asked and "not punished" not in sabri.asked:
        $ sabriOptionsRemaining += 1
    return
