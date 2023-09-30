label rovienHouseController:
    # check if visit makes sense
    if "Rovien house visited" not in status:
        pass
    elif chosenChar == "rovien":
        if "rovien closed door" in status:
            "Rovien s tebou stále odmítá mluvit."
            return
        call rovienOptionsRemainingCheck
        if rovienOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se Roviena ještě ptát."
            return
    elif chosenChar == "zairis":
        call zairisOptionsRemainingCheck
        if zairisOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se Zairise ještě ptát."
            return
    call preludeController

    # walk over
    if currentLocation != "Rovien house":
        if "Rovien house visited" not in status:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        $ currentLocation = "Rovien house"

    # visit itself
    scene bg rovien outside
    if "rumelin exposed" in status or "rumelin threatened" in status:
        call rovienHouseClosedDoor
    if "Rovien house visited" not in status:
        call rovienHouseFirst
    else:
        call rovienHouseAgain
    call leavingRovienHouse

    # adjust status
    $ zairisNote.isActive = True
    if "Rovien house visited" not in status:
        $ status.append("Rovien house visited")
    return

label rovienHouseFirst:
    "Velmi rychle zjistíš, že Rovien je mladší bratr cechmistra Rumelina a živí se obchodem s kvalitními látkami. Jeho dům stojí v elfí čtvrti, nedaleko domu jeho bratra."
    "Zaklepeš na dveře a ty se otevřou dřív, než stihneš plně stáhnout ruku. Před tebou stojí elfí mladík s dychtivým výrazem."
    $ zairis.say("Neseš mi mou knihu?")
    show mcPic at menuImage
    menu:
        "Jakou knihu?":
            hide mcPic
            $ zairis.say("Jarní Madrigaly... Takže ji nemáš?")
            $ mc.say("Ne, jsem z městské hlídky...")
            $ zairis.asked.append("book")
        "Ne, jsem z městské hlídky...":
            hide mcPic
        "Ty jsi Rovienův syn?" if chosenChar == "rovien":
            hide mcPic
            $ zairis.say("Ano, já jsem Zairis. A čekám na Jarní Madrigaly od Huguese de Harignol. Máš je?")
            $ mc.say("Ne, jsem z městské hlídky...")
            $ zairis.asked.append("book")
        "Ty jsi Zairis?" if chosenChar == "zairis":
            hide mcPic
            $ zairis.say("Ano, to jsem já. A čekám na Jarní Madrigaly od Huguese de Harignol. Máš je?")
            $ mc.say("Ne, jsem z městské hlídky...")
            $ zairis.asked.append("book")
    $ zairis.say("Pak nechápu, kde se ten poslíček mohl tak zdržet. Měl tu být dnes ráno.")
    if "letters for Ada seen" in status:
        show mcPic at menuImage
        menu:
            "Můžu se poptat. Napsal bys mi jméno té knihy a kdo ti ji měl donést?":
                hide mcPic
                $ zairis.trust += 1
                $ zairis.say("S radostí, jenom si dojdu pro kus papíru.")
                "Mladý elf zmizí v domě a po chvilce ti přinese lístek s pár napsanými řádky."
                show sh zairis note at truecenter
                pause
                hide sh zairis note
                $ status.append("Zairis writing sample")
                $ zairis.asked.append("book title")
                $ zairis.say("Tady to máte a děkuji.", "happy")
                if gender == "M":
                    $ zairis.say("Ale vy jste určitě chtěl něco jiného. Říkal jste městská hlídka? Stalo se něco?")
                else:
                    $ zairis.say("Ale vy jste určitě chtěla něco jiného. Říkal jste městská hlídka? Stalo se něco?")
            "Snad dorazí brzy.":
                hide mcPic
                $ zairis.say("Doufám. Dobrá poezie se shání těžko.")
                if gender == "M":
                    $ zairis.say("Počkej, říkal jsi městská hlídka? Stalo se něco?")
                else:
                    $ zairis.say("Počkej, říkala jsi městská hlídka? Stalo se něco?")
    else:
        $ zairis.say("Počkej, říkal jsi městská hlídka? Stalo se něco?")
    label rovienHouseIntroductionMenu:
    show mcPic at menuImage
    menu:
        "Vyšetřuji krádež v dílně mistra Heinricha." if "investigation reason" not in zairis.asked:
            hide mcPic
            $ zairis.asked.append("investigation reason")
            $ zairis.say("Heinricha? To je… jeden z ševcovských mistrů, myslím?")
            $ mc.say("Ano, to je on.")
            $ zairis.say("A jak můžeme pomoci my?")
            jump rovienHouseIntroductionMenu
        "Jen si chci ověřit pár drobností s Rovienem." if chosenChar == "rovien":
            hide mcPic
            $ zairis.say("To je můj otec. Asi pro něj můžu dojít, jestli vám to pomůže.")
            "Přikývneš a mladý elf na chvíli zmizí v domě."
            $ zairis.say("Otec si s vámi promluví, mám vás vzít dál.")
            call rovienHouseInside
            call rovienController
        "Jen si chci ověřit pár drobností. Můžu se tě na pár věcí zeptat?":
            hide mcPic
            $ chosenChar = "zairis"
            $ zairis.say("Samozřejmě, rád pomůžu.")
            if "investigation reason" in zairis.asked:
                $ zairis.say("Ale s mistrem Heinrichem se nijak nestýkám.")
            $ zairis.say("Nepůjdete dál?")
            call rovienHouseInside
            call zairisController
    return

label rovienHouseAgain:
    if "promised poetry" in status:
        "Znovu ti otevře Zairis a když tě uvidí, rozzáří se mu oči."
        $ zairis.say("Máte s sebou nějakou vlastní báseň?", "happy")
        if any("poem" in str for str in status):
            show mcPic at menuImage
            menu:
                "Bohužel, jdu si jen krátce promluvit s tvým otcem." if chosenChar == "rovien":
                    hide mcPic
                    $ mc.say("Mé vyšetřování musí mít bohužel přednost před mými zájmy.")
                    $ zairis.say("To je škoda, ale chápu to.", "sad")
                    $ zairis.say("Dojdu tvás u otce ohlásit, ale doufám, že se si na mne s poezií někdy uděláte čas. Opravdu velmi rád bych si nějakou vaši báseň přečetl.")
                    "Zairis na chvíli zmizí v domě a pak tě pozve dál."
                    jump rovienController
                "Samozřejmě, tady je.":
                    hide mcPic
                    call mcPoemReaction
                "Ještě jsem nestihl žádnou vhodnou vybrat." if gender == "M":
                    hide mcPic
                    $ zairis.say("Škoda, opravdu velmi rád bych si nějakou přečetl.", "sad")
                "Ještě jsem nestihla žádnou vhodnou vybrat." if gender == "F":
                    hide mcPic
                    $ zairis.say("Škoda, opravdu velmi rád bych si nějakou přečetl.", "sad")
        elif chosenChar == "rovien":
            $ mc.say("Bohužel, jdu si jen krátce promluvit s tvým otcem.")
            $ mc.say("Mé vyšetřování musí mít bohužel přednost před mými zájmy.")
            $ zairis.say("To je škoda, ale chápu to.", "sad")
            $ zairis.say("Dojdu tvás u otce ohlásit, ale doufám, že se si na mne s poezií někdy uděláte čas. Opravdu velmi rád bych si nějakou vaši báseň přečetl.")
            "Zairis na chvíli zmizí v domě a pak tě pozve dál."
            jump rovienController
        else:
            if gender == "M":
                $ mc.say("Ještě jsem nestihl žádnou vhodnou vybrat.")
            else:
                $ mc.say("Ještě jsem nestihla žádnou vhodnou vybrat.")
            $ zairis.say("Škoda, opravdu velmi rád bych si nějakou přečetl.", "sad")
    else:
        "Znovu ti otevře Zairis a zdvořile se na tebe usměje."

    $ zairis.say("Můžeme ještě nějak pomoct s vaším vyšetřováním?")
    if chosenChar == "rovien":
        if rovien.alreadyMet:
            if gender == "M":
                $ mc.say("Rád bych ještě jednou mluvil s tvým otcem, pokud je to možné.")
            else:
                $ mc.say("Rád bych ještě jednou mluvila s tvým otcem, pokud je to možné.")
        else:
            if gender == "M":
                $ mc.say("Rád bych mluvil s tvým otcem, pokud je to možné.")
            else:
                $ mc.say("Rád bych mluvila s tvým otcem, pokud je to možné.")
        $ zairis.say("Dojdu mu říct.")
        "Zairis na chvíli zmizí v domě a pak tě pozve dál."
        call rovienController
    elif chosenChar == "zairis":
        $ mc.say("Ano, mohl bys mi odpovědět na několik otázek.")
        $ zairis.say("Ale samozřejmě, rád pomůžu.")
        call zairisController
    return

label rovienHouseClosedDoor:
    $ status.append("rovien closed door")
    "Na tvé klepání dlouho nikdo nereaguje. Už to skoro chceš vzdát, když se dveře konečně pootevřou. Mladý elf za nimi tě ale nepustí dovnitř ani sám nevyjde ven."
    $ zairis.say("Otec s vámi nechce mluvit. Velmi výslovně a velmi silně. A vzhledem k tomu, jak moc strýc zuří, se to nijak rychle nezmění.")
    if chosenChar == "zairis":
        $ mc.say("Můžu se na pár věcí zeptat tebe?")
    else:
        show mcPic at menuImage
        menu:
            "Chápu.":
                hide mcPic
                "Zairis pokrčí rameny a zavře mezi vámi dveře."
                return
            "Můžu se na pár věcí zeptat tebe?":
                hide mcPic
        $ zairis.say("Neměl bych, ale...")
        "Mladý elf pokrčí rameny."
        $ zairis.say("...ale jestli je to ve veřejném zájmu, tak se ptejte. Jen to neříkejte otci.")
        "Zairis vyjde ze dveří a odvede tě kus za dům, pravděpodobně mimo dohled většiny oken."
        scene bg rovien wall
        $ zairis.say("S čím můžu hlídce pomoct?")
        call zairisController
    return

label rovienHouseInside:
    scene bg rovien inside
    "Rovienův dům je zařízený velmi elegantně. Na stěnách visí obrazy a mapy a místnosti, do které tě mladý elf zavede, vévodí zdobený krb."
    return

label leavingRovienHouse:
    scene bg rovien outside
    if "promised poetry" in status and not any("poem" in str for str in status):
        $ libraryNote.isActive = True
        menu:
            "{i}(Napsat vlastní báseň){/i}":
                call writingComparisonZairis
                call writePoetry
            "{i}(“Půjčit” si vhodnou báseň v knihovně){/i}":
                call writingComparisonZairis
                $ chosenTopic = "stealPoetry"
                call libraryController
            "{i}(Vrátit se na strážnici){i}":
                call writingComparisonZairis
    return

label writingComparisonZairis:
    scene bg street02
    if "Zairis writing sample" in status and "letters for Ada seen" in status:
        if ("all love letters kept" in status or "one love letter kept" in status):
            if "book title" in zairis.asked or "writing sample" in zairis.asked:
                "Cestou z Rovienova domu vytáhneš jeden z dopisů pro Adu a porovnáš písmo na něm s lístkem od Zairise."
                "Zairisova poznámka je psaná viditelně ve spěchu. Přesto se podle tvaru písmen a způsobu vedení jednotlivých tahů zdá, aspoň co dokážeš posoudit, že oba texty psala stejná ruka."
                "Neujde ti také, že papír je v obou případech identický."
            elif "Zairis sonnet kept" in status:
                "Cestou z Rovienova domu vytáhneš jeden z dopisů pro Adu a porovnáš písmo na něm se Zairisovou básní."
                "Co dokážeš posoudit, tvar písmen i způsob vedení tahů se velmi dobře shoduje a je velmi pravděpodobné, že oba texty psala stejná ruka."
            elif "Zairis sonnet seen" in status:
                "Cestou z Rovienova domu vytáhneš jeden z dopisů pro Adu a pokusíš se co nejpřesněji vybavit Zairisův sonet."
                "Aspoň co si pamatuješ a dokážeš posoudit, tvar písmen i způsob vedení tahů se velmi dobře shoduje a je velmi pravděpodobné, že oba texty psala stejná ruka."
        else:
            if "book title" in zairis.asked or "writing sample" in zairis.asked:
                "Cestou z Rovienova domu se pokusíš co nejpřesněji si vybavit písmo na dopisech pro Adu."
                "Zairisova poznámka je psaná viditelně ve spěchu. Přesto se podle tvaru písmen a způsobu vedení jednotlivých tahů zdá, aspoň co si pamatuješ a dokážeš posoudit, že oba texty psala stejná ruka."
                if gender == "M":
                    "Navíc jsi přesvědčený, že dopisy jsou napsané na stejný druh papíru, který teď držíš v ruce."
                else:
                    "Navíc jsi přesvědčená, že dopisy jsou napsané na stejný druh papíru, který teď držíš v ruce."
            elif "Zairis sonnet kept" in status:
                "Cestou z Rovienova domu se pokusíš co nejpřesněji si vybavit písmo na dopisech pro Adu a porovnat ho se Zairisovým sonetem."
                "Aspoň co si pamatuješ a dokážeš posoudit, tvar písmen i způsob vedení tahů se velmi dobře shoduje a je velmi pravděpodobné, že oba texty psala stejná ruka."
            elif "Zairis sonnet seen" in status:
                "Cestou z Rovienova domu se pokusíš v duchu srovnat písmo Zairisovy básně s dopisy pro Adu. Aspoň co si pamatuješ a dokážeš posoudit, tvar písmen i způsob vedení tahů se velmi dobře shoduje a je velmi pravděpodobné, že oba texty psala stejná ruka."
        $ status.remove("Zairis writing sample")
        $ status.append("Zairis handwriting checked")
    return

label writePoetry:
    scene bg writing table
    show sh blank papers
    if gender == "M":
        "Na psaní poezie jsi nikdy neměl moc času a zvlášť v posledních letech ses nedostal k ničemu lepšímu, než jednoduchým rýmovačkám o nudné nebo příliš těžké práci. Ale možná tím spíš to teď stojí za to zkusit pro úspěch tvého vyšetřování."
    else:
        "Na psaní poezie jsi nikdy neměla moc času a zvlášť v posledních letech ses nedostala k ničemu lepšímu, než jednoduchým rýmovačkám o nudné nebo příliš těžké práci. Ale možná tím spíš to teď stojí za to zkusit pro úspěch tvého vyšetřování."
    "Na strážnici najdeš klidný kout, vytáhneš pár papírů a inkoust a zamyslíš se, jak začít."
    menu:
        "Zločinče, třes se, neb jsem teď v městské stráži!":
            $ status.append("poem watch")
            show expression "sh poem watch [race].png"
        "Hle, z včerejší naděje se rodí světlý zítřek!":
            $ status.append("poem hope")
            show expression "sh poem hope [race].png"
    pause
    if not achievement.has(achievement_name['poet'].name):
        $ Achievement.add(achievement_name['poet'])
    return
