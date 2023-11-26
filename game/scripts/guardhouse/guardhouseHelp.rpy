label guardhouseHelpMenu:
    call guardhouseHelpOptionsAvailable
    if helpOptionsAvailable == 0:
        $ mc.say("Děkuji, to je všechno, co jsem chtěl[a].")
        return

    show mcPic at menuImage
    menu:
        "Mohla by hlídka prověřit nějaké obchody?" if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status:
            hide mcPic
            call helpWithAml
            $ helpAsked += 1
        "Potřeboval bych ověřit, jestli Zeran včera v noci opravdu pracoval." if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status) and gender == "M":
            hide mcPic
            call helpWithZeranWitnesses
            $ helpAsked += 1
        "Potřebovala bych ověřit, jestli Zeran včera v noci opravdu pracoval." if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status) and gender == "F":
            hide mcPic
            call helpWithZeranWitnesses
            $ helpAsked += 1
        "Vyzná se tu někdo v poezii?" if "letters for Ada seen" in status and "asked for literature help" not in status and "poetry style" not in assistant.asked:
            hide mcPic
            call helpWithLiteratureStyle
            $ helpAsked += 1
        "Mistr Heinrich docela ošklivě zmlátil mistra Kaspara. Neměli bychom to nějak řešit?" if kaspar.imageParameter == "beaten" and "asked about Kaspar's beating" not in status:
            hide mcPic
            call helpKasparBeating
            $ helpAsked += 1
        "Vlastně si to ještě nechám projít hlavou." if helpAsked == 0:
            hide mcPic
            return
        "Děkuji, to je všechno, co jsem chtěl." if helpAsked > 0 and gender == "M":
            hide mcPic
            return
        "Děkuji, to je všechno, co jsem chtěla." if helpAsked > 0 and gender == "F":
            hide mcPic
            return
    jump guardhouseHelpMenu

label solianHelpMenu:
    call solianHelpOptionsAvailable
    if solianHelpOptionsAvailable == 0:
        "Vrátíš se zas k jiným záležitostem."
        return

    show mcPic at menuImage
    menu:
        "Jak snadné je dostat se k záznamům o clech? Hodilo by se mi do nich občas nakouknout." if "offered favour" in "lotte asked" and "industrial espionage" not in solian.asked:
            hide mcPic
            call industrialEspionage
        "{i}(Vrátit se k jiným záležitostem.){/i}":
            return
    jump solianHelpMenu

# Responses #

label helpWithAml:
    $ helpAsked += 1
    $ rauvin.trust += 1
    $ hayfa.trust += 1

    if "out of office" not in rauvin.status: # asking Rauvin
        $ rauvin.say("Pravděpodobně ano, ale teď před slavnostmi je spousta práce. O jaké obchody jde a proč by měly být důležité?")
    else: # asking Solian
        $ solian.say("O jaké obchody jde a jak souvisí se ztracenými botami mistra Heinricha?", "angry")

        if "less deals" in njal.asked:
            $ mc.say("Mistr Njal má v posledních dvou týdnech problém uzavřít obchod na nákup materiálu, který potřebuje na výrobu vlastního díla na Einionovy slavnosti. Několik obchodníků mu potřebné věci odmítlo prodat dost náhle, po slibně působícím rozhovoru.")
            show mcPic at menuImage
            menu:
                "Mistr Njal navíc pracoval na stejném typu bot jako mistr Heinrich." if "police business" in njal.asked:
                    hide mcPic
                "Je to už druhý mistr, kterému někdo brání se na slavnostech prezentovat.":
                    hide mcPic
                    $ mc.say("Mohla by to být snaha poškodit celý cech.")
                "Svoje obchody navíc skrývá nebo přesouvá i cechmistr Rumelin.":
                    hide mcPic
                    $ mc.say("Podle Salmy uzavírá méně smluv na drahý materiál, ale smlouvy na prodej zůstávají stejné.")

            if "out of office" not in rauvin.status: # Rauvin
                $ rauvin.say("Je pravda, že to by mohlo stát za prověření. Nechám někoho zjistit, jestli ti obchodníci odmítají prodávat materiál i jiným ševcovským mistrům. Víš, o které by mělo jít?")
                if "awaiting AML merchant list" in status:
                    $ mc.say("Ano, požádal[a] jsem mistra Njala o seznam.")
                    $ rauvin.say("Výborně, někdo ty obchodníky prověří.")
                else:
                    $ mc.say("Z hlavy si mistr Njal vzpomněl na Karstena a Roviena.")
                    $ rauvin.trust -=1
                    $ hayfa.trust -= 1
                    $ rauvin.say("Kdybychom je znali všechny, usnadnilo by to našim lidem práci, ale dva jsou asi lepší než nic. Nechám někoho, aby se poptal.")
                $ status.append("add investigating less deals")
            else: # Solian
                "Solian se zamračí."
                $ solian.say("A mistr Njal chce, aby to řešila hlídka? Neměl by to spíš řešit cech sám?", "angry")
                show mcPic at menuImage
                menu:
                    "Ano, Njal mne požádal, abychom to prověřili.":
                        hide mcPic
                        $ solian.say("Pak měl ideálně jít za hlídkou jako celkem, ale možná měl takhle před slavnostmi spoustu práce.")
                        $ solian.say("Dobře, zkusím se nějak opatrně poptat. Víš, kteří obchodníci Njala odmítli?")
                    "Já myslím, že bychom to řešit měli.":
                        hide mcPic
                        $ mc.say("Tohle by snadno mohla být cílená snaha Njala poškodit a to je určitě zločin.")

        else:
            $ mc.say("Mistr Njal má podle Salmy najednou problém uzavřít obchody a mistr Rumelin uzavírá méně smluv na drahý materiál. Zajímavé je, že smlouvy na prodej zůstávají stejné.")
            $ mc.say("Tak přemýšlím, jestli to spolu s krádeží výrobku, který chtěl mistr Heinrich představit na slavnostech, nemůže ukazovat na snahu poškodit ševcovský cech jako celek.")

            if "out of office" not in rauvin.status: # Rauvin
                "Rauvin se zamračí a zamyslí."
                $ rauvin.say("To opravdu zní trochu zvláštně. Možná to nic neznamená, ale pro jistotu nechám někoho zjistit, jestli se jen nepřesunuli do jiné hospody. A jestli mistr Rumelin pořád prodává zboží, které drahý materiál potřebuje.")
                $ status.append("add investigating less deals")
            else: # Solian
                "Solian se zamračí."
                $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc.", "angry")
                $ solian.say("Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.")
                show mcPic at menuImage
                menu:
                    "To dává smysl, radši do toho nebudu šťourat.":
                        hide mcPic
                        $ solian.say("Jsem rád, že to chápeš.", "happy")
                    "Pokud tu dochází ke zločinu, měli bychom to řešit.":
                        hide mcPic
                        $ solian.trust -= 1
                        $ solian.say("Já bych měl radši jistotu, že budeme mít možnost řešit zločiny i za měsíc. Mimo jiné proto, že nechci přijít o práci. Samozřejmě nevím, jak to vidíš ty...")
                        show mcPic at menuImage
                        menu:
                            "Máš pravdu, radši to nechám být.":
                                hide mcPic
                                $ solian.say("Výborně, jsem rád, že jsme se shodli.", "happy")
                            "Máš jistotu, že až se vrátí Rauvin, uvidí to stejně?":
                                hide mcPic
                                $ solian.say("Rauvin je občas zatracený...", "angry")
                                $ solian.say("No dobře, nějak to ověřím. Hlavně do té doby neudělej žádnou hloupost, která by někoho naštvala.")
                                $ status.append("add investigating less deals solian")
                    "I tak mi přijde bezpečnější to prověřit.":
                        hide mcPic
                        $ mc.say("Už kvůli tomu, aby to nevypadalo, že jsme něco zanedbali.")
                        $ mc.say("Nebo máš naprostou jistotu, že by to Rauvin nechal být?")
                        $ solian.say("Rauvin je občas zatracený...", "angry")
                        $ solian.say("No dobře, nějak to ověřím. Hlavně do té doby neudělej žádnou hloupost, která by někoho naštvala.")
                        $ status.append("add investigating less deals solian")

    $ time.addMinutes(10)
    return

label helpWithZeranWitnesses:
    $ mc.say("Janis ho prý najal na čištění žump nedaleko západní brány.")
    $ mc.say("A spolu s ním tam měl pracovat ještě Francek.")
    if "out of office" not in rauvin.status:
        $ rauvin.say("To by mělo být snadné ověřit. Pošlu někoho, aby se jich zeptal.")
    else:
        $ solian.say("To nebude problém ověřit, zařídím to.")
    $ status.append("add zeran witnesses")
    $ time.addMinutes(3)
    return

label helpWithLiteratureStyle:
    $ status.append("asked for literature help")
    if "out of office" not in rauvin.status:
        $ rauvin.say("Proč zrovna v poezii? Je to důležité pro případ?", "angry")
        $ mc.say("Je to možné. Při vyšetřování se mi na nějaké básně podařilo narazit a hodil by se mi názor znalce.")
        $ rauvin.say("To jsem zvědavý, ale dobrá.")
        $ rauvin.say("Z hlídky asi Valeran, ale ten má hodně jiné práce. Jestli je to opravdu důležité, zajdi do knihovny, Luisa její obnovou tráví hodně času a prý tam má některé zajímavé kousky.")
    else:
        $ solian.say("To už se s lidmi z města bavíš o poezii? To se asi dá počítat jako pokrok!", "happy")
        $ solian.say("Něco by měl znát Rauvin, ale ten na hovory o umění nebude mít moc čas. Jeho sestra ale obnovuje knihovnu, zkus zajít tam. Buď ti pomůže ona, nebo někdo, kdo si tam zrovna bude číst.")
    $ libraryNote.isActive = True
    return

label helpKasparBeating:
    $ status.append("asked about Kaspar's beating")
    if "out of office" not in rauvin.status:
        $ rauvin.say("O té události jsem už slyšel. Pokud vím, nebylo to tak zlé, aby bylo nutné zasahovat.")
        $ mc.say("A co by tedy bylo dost zlé?")
        $ rauvin.say("Kdyby mistr Kaspar nedokázal odejít po svých nebo kdyby utrpěl nějaké větší zranění, které by mu zůstalo natrvalo nebo které by ho na delší dobu omezilo v práci.")
        show mcPic at menuImage
        menu:
            "Chápu.":
                hide mcPic
                $ rauvin.say("Samozřejmě jiná věc je, jak se k tomu postaví lidé z města. Jestli Heinrichův čin neschválí, ublíží to jeho pověsti a to je víc, než kdyby musel platit odškodné.")
            "Přesně to jsem si myslel[a]":
                hide mcpic
                $ rauvin.say("Přesto jsem rád, že sis to ověřil[a]. Unáhlenost v podobných věcech by se nám mohla snadno vymstít.")
            "Mistr Kaspar ale o náš zásah velmi stojí.":
                hide mcPic
                $ rauvin.say("Tomu rozumím, ale kdybychom se do podobných záležitostí začali vkládat, lidé by nás mohli začít používat pro vyřizování osobních účtů. Ostatně nerad bych se pokoušel rozklíčovat, kdo z těch dvou je v tak osobním sporu v právu.")
                $ rauvin.say("Navíc velitel Galar se snaží být s našimi zásahy velmi střídmý, už kvůli tomu, jak hlídka fungovala pod Velinovou vládou.")
            "Takže to Heinrichovi projde bez trestu?":
                $ rauvin.say("Z naší strany ano.")
                $ rauvin.say("V těchto věcech je ale důležitější, jak se k věci postaví lidé z města. Jestli Heinrichův čin neschválí, ublíží to jeho pověsti a to je víc, než kdyby musel platit odškodné.")
    else:
        $ solian.say("V žádném případě. To je osobní spor jich dvou.")
        show mcPic at menuImage
        menu:
            "Přesně to jsem si myslel[a].":
                hide mcPic
                $ solian.say("Pak máš správný přístup a šanci to tady někam dotáhnout.", "happy")
            "Mistr Kaspar ale o náš zásah velmi stojí.":
                hide mcPic
                $ solian.say("Tomu rozumím, ale stejně tak o něj mistr Heinrich nejspíš vůbec nestojí. Nechci se dostat mezi ty dva.", "angry")
                $ solian.say("Zvlášť když z jednoho z nich se může za pár dní stát nový cechmistr.")
            "Takže to Heinrichovi projde bez trestu?":
                hide mcPic
                $ solian.say("O té rvačce se brzy dozví celé město. Dost možná se potrestal sám tím, co to udělá s jeho pověstí. Zvlášť když zbývá jen pár dní do volby nového cechmistra.")
                $ solian.say("To je významnější než cokoli, co bychom směli nebo chtěli udělat my.")
    return

label industrialEspionage:
    $ solian.asked.append("industrial espionage")
    $ solian.say("Záznamy se pečlivě uchovávají. Ale není dovolené si je jen tak prohlížet, někomu by mohlo vadit, kdybychom jen tak pro zábavu štourali do jeho obchodů. Proč se o ně zajímáš?")
    show mcPic at menuImage
    menu:
        "Kvůli dobrým vztahům s jednou osobou, se kterou jsem se seznámil[a].":
            call industrialEspionageGoodRelations
        "Požádala mě o to Lotte, žena obchodníka Karstena.":
            hide mcPic
            $ solian.say("S tou je určitě dobré se přátelit. Dobře, zjistím, co potřebuje, a předám jí to.")
            $ solian.say("Ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "Potřebuji to, abych dokázal[a] pomoct té tanečnici s ohněm.":
            call industrialEspionageHelpKatrin
    $ time.addMinutes(10)
    return

label industrialEspionageGoodRelations:
    hide mcPic
    $ solian.say("Chápu. O koho jde?")
    show mcPic at menuImage
    menu:
        "O Lotte, ženu obchodníka Karstena.":
            hide mcPic
            $ solian.say("S tou je určitě dobré se přátelit. Dobře, zjistím, co potřebuje, a předám jí to.")
            $ solian.say("Ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "To bych si radši nechal[a] pro sebe.":
            hide mcPic
            $ solian.say("Jak myslíš. V tom případě ale nemám důvod ti s něčím takhle nebezpečným pomáhat.", "angry")
    return

label industrialEspionageHelpKatrin:
    hide mcPic
    $ solian.say("Vážně chceš kvůli ní dělat něco podobně nebezpečného? Jestli se na to přijde, velitel Galar tě okamžitě vyhodí z hlídky a nejspíš skončíš přinejmenším na pranýři. On velitel nebývá moc vidět, ale zrovna překračování pravomocí opravdu nestrpí.", "angry")
    $ solian.say("A jak jí to vůbec pomůže? Chceš tím někoho uplatit, aby se jí zastal?", "angry")
    show mcPic at menuImage
    menu:
        "Ano, Lotte z ulice, kde bydlí mistr Heinrich.":
            hide mcPic
            $ solian.trust += 1
            $ solian.say("No dobře, zrovna ta to snad vezme spíš jako začátek přátelského vztahu, než aby zůstala u té jedné pomoci a pak nás už nechtěla znát.")
            $ solian.say("Zjistím, co potřebuje, a předám jí to. A ty se u ní klidně zastav také, až budeš mít chvíli. Jestli jste si naposled tak dobře popovídali, byla by škoda na to nenavázat.")
            $ katrin.cluesAgainst += 1
            $ status.append("industrial espionage")
        "Do toho ti nic není.":
            hide mcPic
            $ solian.trust -= 2
            $ solian.say("Jak myslíš. V tom případě ale nemám důvod ti s něčím takhle nebezpečným pomáhat.", "angry")
        "Máš pravdu, nestojí to za to.":
            hide mcPic
            $ solian.trust += 1
            $ solian.say("Těší mě, že to tak vidíš. Když už podstupovat podobné nebezpečí, mělo by to být pro něco odpovídajícího.")
            $ solian.say("Nemůžeme pomoct každému, kdo to potřebuje. Na to nás není dost a příliš pozorně nás hlídají.")
    return

# Options available check #

label guardhouseHelpOptionsAvailable:
    $ helpOptionsAvailable = 0
    if "less deals" in salma.asked and not any("investigating less deals" in str for str in status) and "less deals checked" not in status:
        $ helpOptionsAvailable += 1
    if "alibi witnesses" in zeran.asked and not any("zeran witnesses" in str for str in status):
        $ helpOptionsAvailable += 1
    if "letters for Ada seen" in status and "asked for literature help" not in status and "poetry style" not in assistant.asked:
        $ helpOptionsAvailable += 1
    if kaspar.imageParameter == "beaten" and "asked about Kaspar's beating" not in status:
        $ helpOptionsAvailable += 1
    return

label solianHelpOptionsAvailable:
    $ solianHelpOptionsAvailable = 0
    if "offered favour" in "lotte asked" and "industrial espionage" not in solian.asked:
        $ solianHelpOptionsAvailable += 1
    return
