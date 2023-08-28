label hayfaRecruiting:
    scene bg people
    if gender == "M":
        "Na jedné z rušnějších ulic spatříš skupinu lidí zabraných do hovoru, podle oblečení zřejmě bohatších měšťanů. Zabraný do práce jim sotva věnuješ pozornost, když z jejich směru zahlédneš rychlý pohyb a všimneš si Hayfy, jak drží za ruku asi osmileté děvče."
    else:
        "Na jedné z rušnějších ulic spatříš skupinu lidí zabraných do hovoru, podle oblečení zřejmě bohatších měšťanů. Zabraná do práce jim sotva věnuješ pozornost, když z jejich směru zahlédneš rychlý pohyb a všimneš si Hayfy, jak drží za ruku asi osmileté děvče."
    "Měšťani se po nich ohlédnou a znepokojeně si ohledají kapsy, pak se ale uklidněni vrátí zpět k hovoru."
    "Hayfa zatím dítě táhne do postranní uličky. Zvědavě je následuješ."
    scene bg street03
    "Začátek jejich rozhovoru neslyšíš, vidíš jen, že Hayfa dívce domlouvá, ona se nejdřív brání, ale brzy kapituluje a už jen hlídkařku vyděšeně sleduje."
    $ hayfa.say("Takže víš, co jsi udělala špatně?")
    "Holčička na Hayfu chvíli zmateně hledí a potom opatrně přikývne."
    $ hayfa.say("Viděla jsi někdy, jak se tady trestají zloději?")
    "Holčička ještě víc vytřeští oči a začne natahovat. Nepatrně znovu přikývne."
    $ hayfa.say("Tak to jsi ráda, že jsi nic neukradla, že ano? Chytila jsem tvojí ruku dřív, než ses kohokoli z těch lidí jenom dotkla. Nestihla jsi nic provést.")
    $ hayfa.say("A jestli potřebuješ peníze, možná můžeš občas nějaké dostat ode mě.")
    "V Hayfiných prstech se zableskne stříbrná mince. Holčička hlídkařku pozorně sleduje."
    $ hayfa.say("Jestli uvidíš, jak někdo něco krade, nebo jak někoho bijou, nebo jak někdo najednou hodně často brečí, nebo jak se někdo najednou často tajně schází a všechny odtamtud vyhání, chci to vědět, ano?")
    $ hayfa.say("A příště si je tak dlouho neobhlížej. Hned jsem věděla, že něco chystáš.")
    $ hayfa.say("Také si najdi nějaký přirozený důvod, proč se k nim přiblížit, třeba k nim nech utéct obruč nebo se s nimi potkej v hodně úzké uličce. Na tak široké cestě jako tady bys je správně měla obejít, a když to neuděláš, vzbudíš zbytečně pozornost.")
    "Holčička na Hayfu hledí se směsicí zmatku a obdivu, ale když jí hlídkařka podá stříbrňák, schová ho a rychle odběhne. Hayfa ji sleduje a dovolí si mírný úsměv. Potom se otočí na tebe."
    $ hayfa.say("Šikovná holka. Za pár let může být jedna z nás.", "happy")
    show mcPic at menuImage
    menu:
        "Vážně jsi jí právě poradila, jak být lepší zlodějka?":
            $ hayfa.asked.append("pickpocket disapproval")
            hide mcPic
            if hayfa.trust > 8:
                $ hayfa.say("Jistě. Přece nemůžu dopustit, aby můj nový ptáček hned došel k úhoně.", "happy")
                $ hayfa.say("A jestli opravdu do hlídky někdy vstoupí, ať toho umí co nejvíc hned od začátku.")
                if gender == "M":
                    $ mc.say("Přiznám se, že z toho jsem trochu nesvůj. Krádež je pořád zločin, těm by přece měla hlídka bránit, a ne je podporovat.")
                else:
                    $ mc.say("Přiznám se, že z toho jsem trochu nesvá. Krádež je pořád zločin, těm by přece měla hlídka bránit, a ne je podporovat.")
                $ hayfa.say("Kdyby o všechna takováhle děcka bylo postaráno a kdybychom neměli na práci horší věci, tak bych souhlasila. Teď jsem ráda, že holka může svůj osud ovlivnit aspoň tím, že si sežene pár mincí navíc.")
            elif hayfa.trust > 0:
                $ hayfa.say("Jistě. Když už jí platím, tak chci, aby něco uměla.")
                $ mc.say("A je to správně? Krádež je pořád zločin, těm by přece měla hlídka bránit, a ne je podporovat.")
                $ hayfa.say("Až budou dětští kapsáři to nejhorší zlo v Marendaru, možná to správně nebude. Do té doby jsem ráda, že holka může svůj osud ovlivnit aspoň tím, že si sežene pár mincí navíc.")
            else:
                $ hayfa.say("Očividně. Přijde ti to špatně?")
                $ mc.say("Krádež je zločin, těm by přece měla hlídka bránit, a ne je podporovat.")
                $ hayfa.say("Až budou dětští kapsáři to nejhorší zlo v Marendaru, budu ochotná se o tom bavit. Do té doby jsem ráda, že holka může svůj osud ovlivnit aspoň tím, že si sežene pár mincí navíc.", "angry")
            $ mc.say("A co když ty peníze ve skutečnosti nepotřebuje a chce je utratit za zbytečnosti?")
            $ hayfa.say("Jestli se vystavuje nebezpečí, že ji v lepším případě seřežou a v horším ocejchujou, tak pro ni ty peníze asi důležité jsou, ať už za ně koupí jídlo, nebo něco, co nám přijde jako hloupá cetka.")
            $ hayfa.say("Dají jí možnost rozhodovat sama o sobě, jít za tím, co ona sama chce. To má obrovskou cenu.")
        "Páni, to bylo chytré! Kolik takových pomocníků už máš?":
            hide mcPic
            $ hayfa.say("Pár. Většina jich nechodí až tak často.")
            $ mc.say("Ví o nich Rauvin?")
            $ hayfa.say("Jména nezná, ale ví, že se dětí občas ptám.")
            $ mc.say("A ví, že jim za to platíš?")
            $ hayfa.say("Já i Rauvin dostáváme nějaké peníze k platu na vybavení. On si za to kupuje leštidlo na zbroj, já informace. Můžeš se rozhodnout, co ti přijde užitečnější.")
            $ colleaguesAsked.append("Rauvin's armour")
            show mcPic at menuImage
            menu:
                "Rozhodně informace!":
                    hide mcPic
                    if "not sharing" not in status and "not sharing 2" not in status:
                        if gender == "M":
                            $ hayfa.say("Právě. Proto jsem ráda, že jsi ochotný nám s Rauvinem čas od času říct, co zrovna děláš. Hlídka bez informací je hodně smutná, zvlášť když se týkají samotných hlídkařů a jejich práce.")
                        else:
                            $ hayfa.say("Právě. Proto jsem ráda, že jsi ochotná nám s Rauvinem čas od času říct, co zrovna děláš. Hlídka bez informací je hodně smutná, zvlášť když se týkají samotných hlídkařů a jejich práce.")
                    else:
                        $ hayfa.say("Právě. Proto mě mrzí, že se nám s Rauvinem občas snažíš tajit, co zrovna děláš. Hlídka bez informací je hodně smutná, zvlášť když se týkají samotných hlídkařů a jejich práce.")
                        show mcPic at menuImage
                        menu:
                            "Zkusím se zlepšit.":
                                hide mcPic
                                $ status.append("promise to share info")
                                $ hayfa.say("Když někdy zajdeš za Rauvinem s hlášením, bude to dobrý začátek.")
                                $ dailyStatus.append("promised to share")
                            "Nejsem děcko, abych vám hlásil každou hloupost." if gender == "M":
                                hide mcPic
                                $ hayfa.say("Jak už jsem říkala, já to na jednu stranu chápu. Jen si uvědom, že jestli se někdy dostaneš do průšvihu, jsme to my, kdo by ti měl krýt záda, stejně jako ty nám.")
                                $ hayfa.say("Násilím to z tebe páčit nebudu.")
                            "Nejsem děcko, abych vám hlásila každou hloupost." if gender == "F":
                                hide mcPic
                                $ hayfa.say("Jak už jsem říkala, já to na jednu stranu chápu. Jen si uvědom, že jestli se někdy dostaneš do průšvihu, jsme to my, kdo by ti měl krýt záda, stejně jako ty nám.")
                                $ hayfa.say("Násilím to z tebe páčit nebudu.")
                "No, zbroj se musí taky dost hodit...":
                    hide mcPic
                    $ hayfa.say("Na ochranu jsem ji ještě nepotřebovala a Rauvin pokud vím také ne. Ale je pravda, že někteří lidé ho díky zbroji považují za větší autoritu.")
                    "Hayfa pokrčí rameny."
                "Budu peníze na vybavení dostávat taky?":
                    hide mcPic
                    $ hayfa.say("Až se osvědčíš a až přesvědčíš Rauvina, že je dokážeš rozumně využít.")

    $ origAsked = hayfa.asked.copy()
    call hayfaRecruitingMenu
    $ time.addMinutes(15)
    return

label hayfaRecruitingMenu:
    call hayfaRecruitingOptionsRemainingCheck
    if optionsRemaining == 0:
        if gender == "M":
            $ mc.say("Asi bych se měl vrátit ke svému případu...")
        else:
            $ mc.say("Asi bych se měla vrátit ke svému případu...")
        call hayfaRecruitingPlayerLeaves
        return
    if len(hayfa.asked) - len(origAsked) >= 2:
        $ hayfa.say("Támhle jde Amrin. Musím jít.")
        if gender == "M":
            $ mc.say("...prosím? Něco, o čem bych měl vědět?")
        else:
            $ mc.say("...prosím? Něco, o čem bych měla vědět?")
        $ hayfa.say("Ani ne, aspoň zatím. Soustřeď se na svůj případ.")
        return

    show mcPic at menuImage
    menu:
        "Takže nebude nijak potrestaná?" if "pickpocket disapproval" in hayfa.asked and "pickpocket punishment" not in hayfa.asked:
            hide mcPic
            $ hayfa.asked.append("pickpocket punishment")
            if gender == "M":
                $ hayfa.say("Ty bys pro nějaký trest byl?")
            else:
                $ hayfa.say("Ty bys pro nějaký trest byla?")
            show mcPic at menuImage
            menu:
                "Ani ne, k čemu? Jen by pak považovala hlídku za další z té řady dospělých a bohatých, před kterými se musí schovávat.":
                    hide mcPic
                    $ hayfa.say("Právě. K čemu je hlídka, když se na ni lidé nebudou chtít obrátit?")
                    $ hayfa.say("Jsem ráda, že se shodneme.")
                "Jistě, musí se přece naučit, že pravidla platí vždy. Neříkám jí hned sekat ruku, ale výprask by zasloužila.":
                    hide mcPic
                    $ hayfa.say("A čemu to pomůže? Krást kvůli tomu nepřestane, jen se utvrdí v tom, že hlídka tady je jenom pro ty bohaté.")
        "Opravdu myslíš, že bychom ji mohli někdy najmout? Vždyť jsi jí právě řekla, že to celé provedla úplně špatně." if "pickpocket recruit" not in hayfa.asked:
            hide mcPic
            $ hayfa.asked.append("pickpocket recruit")
            $ hayfa.say("Tak zlé to nebylo. Kdyby to provedla celé úplně špatně, řekla bych jí, ať už to radši nikdy nezkouší, jestli se má jenom trochu ráda.")
        "Myslíš, že se od ní dozvíš něco užitečného?" if "pickpocket information" not in hayfa.asked:
            hide mcPic
            $ hayfa.asked.append("pickpocket information")
            $ hayfa.say("Myslím, že se dozvím spoustu drbů, kdo se s kým tajně líbá ve starém sklepě a kdo krade med ze spíže. Ale někde mezi tím může být i něco užitečného.")
            $ mc.say("Dost na to, aby to stálo za to?")
            $ hayfa.say("Jinak bych to nedělala. Navíc se to pak mezi podobnými dětmi rozkřikne a je snazší za nimi přijít.")
        "Asi bych se měl vrátit ke svému případu..." if gender == "M":
            call hayfaRecruitingPlayerLeaves
            return
        "Asi bych se měla vrátit ke svému případu..." if gender == "F":
            call hayfaRecruitingPlayerLeaves
            return
    jump hayfaRecruitingMenu

label hayfaRecruitingPlayerLeaves:
    hide mcPic
    if "bored by first case" in personality:
        $ mc.say("Kdyby se boty nenašly včas, asi by se město celé propadlo do bezvládí nebo něco podobného. To nemůžu dopustit.")
    elif "tired by first case" in personality:
        $ mc.say("Chci už mít dnešek za sebou a konečně se někde posadit.")
    elif "flattered by first case" in personality or "nervous of first case" in personality:
        $ mc.say("Když už mám vlastní případ, tak nechci zklamat vaši důvěru.")
    $ hayfa.say("Hodně štěstí v pátrání. Já si tady ještě počkám na Amrin, poslední dobou se chová divně.")
    if gender == "M":
        $ mc.say("...prosím? Něco, o čem bych měl vědět?")
    else:
        $ mc.say("...prosím? Něco, o čem bych měla vědět?")
    $ hayfa.say("Ani ne, aspoň zatím. Soustřeď se na svůj případ.")
    return

label hayfaRecruitingOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "pickpocket disapproval" in hayfa.asked and "pickpocket punishment" not in hayfa.asked:
        $ optionsRemaining += 1
    if "pickpocket recruit" not in hayfa.asked:
        $ optionsRemaining += 1
    if "pickpocket information" not in hayfa.asked:
        $ optionsRemaining += 1
    return
