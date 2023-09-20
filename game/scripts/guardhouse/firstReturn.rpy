label guardhouseFirst:
    #play music audio.guardhouse
    $ time.addMinutes(15)
    $ currentLocation = "guardhouse"

    scene bg street01
    if gender == "M":
        "Vrátíš se zpět na strážnici, s nejistou představou, že bys možná měl podat hlášení. Nebo si aspoň ujasnit své současné postavení. Vyšetřuješ případ, tak tě asi přijali, ale zatím ti nikdo nic neřekl, nic jsi nepodepsal…"
    else:
        "Vrátíš se zpět na strážnici, s nejistou představou, že bys možná měla podat hlášení. Nebo si aspoň ujasnit své současné postavení. Vyšetřuješ případ, tak tě asi přijali, ale zatím ti nikdo nic neřekl, nic jsi nepodepsala…"
    scene bg guardhouse
    "Uvnitř skoro nikoho nenajdeš, zřejmě mají všichni povinnosti ve městě. Spatříš pouze Rauvina, jak zadává nějaký úkol starší trpaslici. Po chvíli i ona odejde a Rauvin se otočí k tobě."
    $ rauvin.say("Dobře, že jsi zpátky. Původně jsem se chtěl vyptat na víc věcí o tobě, ale když už vyšetřuješ případ, řekni mi spíš nejslibnější stopu, kterou zatím máš.")
    call reportingBack from _call_reportingBack
    if "no clue" in status or "not sharing" in status:
        $ rauvin.say("Normálně bych to řešil víc, ale velitel řekl, že teď před slavnostmi bereme každého.", "angry")
    else:
        $ rauvin.say("Dobře, vypadá to, že děláš zhruba to, co se od tebe očekává.")
    if gender == "M":
        $ rauvin.say("Jsi přijat na zkoušku, a až vyřešíš tenhle případ a skončí Einionovy slavnosti, promluvíme si, co dál.")
    else:
        $ rauvin.say("Jsi přijata na zkoušku, a až vyřešíš tenhle případ a skončí Einionovy slavnosti, promluvíme si, co dál.")
    $ rauvin.say("Tohle podepiš pro pana velitele a tady pak máš pověření člena hlídky.")
    scene bg guardhouse
    show sh contract at truecenter
    pause
    if race == "human":
        show text "{color=#000}{font=fonts/GreatVibes-Regular.ttf}{size=+10}[mcName]{/size}{/font}{/color}" at signature
    elif race == "elf":
        show text "{color=#000}{font=fonts/Allura-Regular.ttf}{size=+10}[mcName]{/size}{/font}{/color}" at signature
    elif race == "hobbit":
        show text "{color=#000}{font=fonts/ClickerScript-Regular.ttf}{size=+10}[mcName]{/size}{/font}{/color}" at signature
    elif race == "dwarf":
        show text "{color=#000}{font=fonts/Devonshire-Regular.ttf}{size=+10}[mcName]{/size}{/font}{/color}" at signature
    pause
    hide text
    hide sh contract
    show sh parchment sealed at truecenter
    show text "{color=#000}{font=fonts/JimNightshade-Regular.ttf}{size=+10}[mcName]{/size}{/font}{/color}" at sealedParchmentName
    pause
    hide text
    hide sh parchment sealed
    $ status.append("provisional watchman")

    $ rauvin.say("A zpátky k tvému případu: kdyby to začalo být až moc složité, můžeš použít zeď na poznámky. Někomu se pak lépe orientuje v lidech a místech, co souvisí s nějakým případem.")
    if gender == "M":
        $ rauvin.say("A taky se tam dají psát adresy, pokud by sis je nepamatoval. Jak dobře se vlastně v Maredaru vyznáš?")
    else:
        $ rauvin.say("A taky se tam dají psát adresy, pokud by sis je nepamatovala. Jak dobře se vlastně v Maredaru vyznáš?")
    show mcPic at menuImage
    menu:
        "Po požáru se toho tady hodně změnilo…" if origin == "born here":
            hide mcPic
            $ rauvin.say("Myslím, že se do toho dostaneš snadno. Pořád tady máme jedno hlavní náměstí a dvě brány a všechno ostatní je někde mezi tím.")
        "Ještě pořád se tady rozkoukávám…" if origin != "born here":
            hide mcPic
            $ rauvin.say("Myslím, že se do toho dostaneš snadno. Máme tady jedno hlavní náměstí a dvě brány a všechno ostatní je někde mezi tím.")
        "Včera jsem se ztratil při hledání Olwenova chrámu, ale hospody už znám všechny." if gender == "M":
            hide mcPic
            "Rauvin pozvedne obočí."
            $ rauvin.say("Tak jen doufám, že nejsi ten typ, co v hospodách působí pozdvižení. Nedělalo by to hlídce dobrou pověst.")
        "Včera jsem se ztratila při hledání Olwenova chrámu, ale hospody už znám všechny." if gender == "F":
            hide mcPic
            "Rauvin pozvedne obočí."
            $ rauvin.say("Tak jen doufám, že nejsi ten typ, co v hospodách působí pozdvižení. Nedělalo by to hlídce dobrou pověst.")
        "Lepší se to, dneska jsem se ještě nemusel ptát na cestu." if gender == "M":
            hide mcPic
            $ rauvin.say("To je dobře. A kdybys chtěl poznat ulice a zákoutí, co často neznají ani místní, řekni někdy Hayfě.")
        "Lepší se to, dneska jsem se ještě nemusela ptát na cestu." if gender == "F":
            hide mcPic
            $ rauvin.say("To je dobře. A kdybys chtěla poznat ulice a zákoutí, co často neznají ani místní, řekni někdy Hayfě.")
        "Je to jako kdybych nikdy neodešel" if origin == "born here" and gender == "M":
            hide mcPic
            $ rauvin.say("To je dobře, na slavnosti přijedou i lidé z okolí, co se budou potřebovat ptát na cestu.")
        "Je to jako kdybych nikdy neodešla" if origin == "born here" and gender == "F":
            hide mcPic
            $ rauvin.say("To je dobře, na slavnosti přijedou i lidé z okolí, co se budou potřebovat ptát na cestu.")
        "Už se tady cítím jako doma." if origin != "born here":
            hide mcPic
            $ rauvin.say("To je dobře, na slavnosti přijedou i lidé z okolí, co se budou potřebovat ptát na cestu.")
    $ rauvin.say("V každém případě, tu metodu se zdí tady používají i největší mazáci.")
    $ rauvin.say("Zkus si dát dohromady svoje poznámky k případu a všechny adresy a rozmysli si, kde budeš pokračovat s vyšetřováním.")

    $ time.addMinutes(10)
    jump evidenceWall
