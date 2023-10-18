label guardhouseArrestMenu:
    show mcPic at menuImage
    menu:
        "Chci zatknout mistra Kaspara, za krádež Heinrichova výrobku." if "confession" in kaspar.asked and kaspar not in arrested:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for theft")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            if gender == "M":
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčený, že lže a buď je zničil, nebo odnesl a někde schoval.")
            else:
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčená, že lže a buď je zničil, nebo odnesl a někde schoval.")
            $ rauvin.say("Máš na to důkazy?")
            $ mc.say("Mistr Kaspar se v podstatě přiznal…")
            $ rauvin.say("Potřebujeme buď plné přiznání nebo nezvratný důkaz.")
            $ rauvin.say("Neříkám, že nemáš pravdu, ale pokračuj v pátrání, dokud toho nebudeš mít v rukou víc.")
            if gender == "M":
                $ rauvin.say("A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Kaspara, za zničení Heinrichova výrobku." if "confession" in kaspar.asked and kaspar not in arrested and "burned evidence" in clues:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for sabotage")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            if gender == "M":
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčený, že lže. Navíc mám důkaz, že se někdo pokusil Heinrichovy střevíce spálit v jeho vlastním krbu.")
            else:
                $ mc.say("Tvrdí, že tam střevíce nenašel, ale jsem přesvědčená, že lže. Navíc mám důkaz, že se někdo pokusil Heinrichovy střevíce spálit v jeho vlastním krbu.")
            $ rauvin.say("Máš na to důkaz, který by ukazoval přímo na mistra Kaspara?")
            $ mc.say("V podstatě se přiznal.")
            $ rauvin.say("Potřebujeme buď plné přiznání nebo nezvratný důkaz.")
            $ rauvin.say("Neříkám, že nemáš pravdu, ale pokračuj v pátrání, dokud toho nebudeš mít v rukou víc.")
            if gender == "M":
                $ rauvin.say("A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Kaspara, za úmysl poškodit Heinrichův výrobek." if "confession" in kaspar.asked and kaspar not in arrested and "burned evidence" in clues:
            hide mcPic
            $ rauvin.asked.append("arrest Kaspar for intentions")
            "Rauvin se zamračí."
            $ rauvin.say("Co myslíš tím úmyslem?")
            $ mc.say("Mistr Kaspar se přiznal, že byl v Heinrichově dílně, a naznačil, že ho chtěl znemožnit na slavnostech.")
            $ rauvin.say("Ale neudělal to?")
            $ mc.say("Tvrdí, že ty střevíce nenašel, a já mu spíš věřím.")
            $ rauvin.say("Nemyslím si, že je možné zatknout váženého mistra jen za úmysl něco udělat, i kdybychom pro ten úmysl měli naprosto nezvratný důkaz. A já si moc nedokážu představit, jak by takový důkaz mohl vypadat, Kaspar může kdykoli všechno popřít.")
            $ rauvin.say("Kdyby něco skutečně udělal, třeba se do té dílny vloupal nebo si na to ničení aspoň přinesl nějaké nástroje, mělo by to větší pádnost, ale ani potom by se tím soudce nemusel chtít vůbec zabývat.")
            if gender == "M":
                $ rauvin.say("Pokračuj tedy prosím v pátrání, jestli najdeš něco dalšího, co proti mistru Kasparovi směřuje. A buď prosím opatrný, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
            else:
                $ rauvin.say("Pokračuj tedy prosím v pátrání, jestli najdeš něco dalšího, co proti mistru Kasparovi směřuje. A buď prosím opatrná, aby se to podezření nedostalo nejen ke Kasparovi, ale ani k mistru Heinrichovi. Nechceme vztahy v cechu zhoršit ještě víc.")
        "Chci zatknout mistra Rumelina, za podvod a snahu poškodit jiného mistra jeho cechu." if "confession" in rumelin.asked and rumelin not in arrested:
            hide mcPic
            $ rauvin.asked.append("arrest Rumelin")
        "Chci zatknout Zerana, za krádež střihu mistra Njala." if zeranNote.isActive and "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason:
            hide mcPic
            $ rauvin.asked.append("arrest Zeran for stolen idea")
            if "stolen idea" in rauvin.asked:
                $ rauvin.say("Zerana? Takže ten střih mistru Heinrichovi donesl on?")
                $ mc.say("Ano, pravděpodobně aby ho mistr Heinrich vzal zpátky.")
            else:
                $ rauvin.say("O jaký střih se jedná?")
                $ mc.say("O střih na ukradené boty mistra Heinricha. Původně ho vytvořil mistr Njal a Zeran mu ho ukradl. Pravděpodobně doufal, že ho pak mistr Heinrich vezme zpátky.")
            $ rauvin.say("A máš na to důkazy?")
            show mcPic at menuImage
            menu:
                "Ne, ale jsem si jistý, že to udělal." if gender == "M":
                    call arrestZeranStolenIdeaConvinced
                "Ne, ale jsem si jistá, že to udělal." if gender == "F":
                    call arrestZeranStolenIdeaConvinced
                "Ne, ale Njal požaduje, abychom někoho zatkli.":
                    hide mcPic
                "Ve skutečnosti ne, možná to není dobrý nápad.":
                    hide mcPic
                    $ rauvin.say("Zatýkat někoho bez důkazů rozhodně dobrý nápad není.")
                    if gender == "M":
                        $ rauvin.say("Vrať se k pátrání a stav se, kdybys potřeboval s něčím pomoct.")
                    else:
                        $ rauvin.say("Vrať se k pátrání a stav se, kdybys potřeboval s něčím pomoct.")
    return

label arrestZeranStolenIdeaConvinced:
    hide mcPic
    $ rauvin.trust -= 3
    $ mc.cluesAgainst += 1
    "Rauvin se zamračí."
    $ rauvin.say("A to ti připadá jako dostatečný důvod?", "angry")
    if gender == "M":
        $ rauvin.say("Jestli nemáš důkazy, proč si jsi tak jistý?")
    else:
        $ rauvin.say("Jestli nemáš důkazy, proč si jsi tak jistá?")
    $ mc.say("Kdo jiný by to udělal? Zeran měl důvod si Heinricha chtít udobřit a neměl moc jiných možností, jak to udělat.")
    $ mc.say("Navíc jeho noví kamarádi mu něco podobného klidně mohli vnuknout.")
    $ rauvin.say("Jací noví kamarádi?")
    $ mc.say("No vždyť víte. V dočasné čtvrti je určitě spousta pochybných osob.")
    $ mc.say("My víme, že Zeran přijal útočiště u Sabriho, který na něj podle všeho má velký vliv. Ten říká, že když člověk něco chce, má si to prostě vzít.")
    $ rauvin.say("To říká i Hayfa.")
    $ mc.say("No ano, ale u ní to hlavně znamenalo dostat se do hlídky a získat si její důvěru. Ale Zeran hlídce každým slovem nadává. Od toho těžko můžeme čekat, že najde zápal pro nějakou dobrou věc.")
    $ rauvin.say("A jak vysvětluješ, že Heinrich měl střih v rukou, ale Zerana zpátky nepřijal?")
    $ mc.say("Jednoduše, je na Zerana opravdu naštvaný, dceru chce ze všech sil chránit.")
    $ rauvin.say("Takže když to shrnu, chceš zatknout Zerana, protože se ti nelíbí, kdo mu jako jediný nabídl střechu nad hlavou. Důkazy nemáš, ale předpokládáš, že mu po dvou letech v Heinrichově učení nedošlo, jestli pro něj bude důležitější ukradený střih, nebo bezpečí jeho dcery.")
    $ rauvin.say("Pochopil jsem to správně?")
    $ mc.say("No, ano. My nad tím můžeme uvažovat s chladnou hlavou, ale Zeran je na to příliš v zajetí pocitu, jak mu všichni ublížili.")
    $ rauvin.say("Chápu.")
    $ rauvin.say("Aby tedy bylo jasno, my tu nejsme od toho, abychom posílali lidi k soudu jen na základě pocitů nebo domněnek. Potřebujeme pořádné důkazy. Ty tvoje by nám soud smetl se stolu, a jestli ne, bylo by to jeho selhání a jeho ostuda úplně stejně jako naše.", "angry")
    $ rauvin.say("Už vůbec potom nikoho neposíláme k soudu za to, že někdo má určitě podezřelé kamarády. To není důkaz, to by bylo souzení ostatních jen proto, že se nám na nich něco nelíbí. A toho už v Marendaru bylo dost.", "angry")
    if mc.cluesAgainst > 1:
        $ rauvin.say("O něčem podobném už jsme ale mluvili. Doufal jsem, že se poučíš, ale nestalo se. Někoho takového si v hlídce nemůžu dovolit držet.")
        $ rauvin.say("Prosím, vrať svůj glejt.")
        $ rauvin.say("Hodně štěstí při hledání jiné práce.")
        jump thrownOut
    $ rauvin.say("Ve skutečnosti nemám radost z toho, že to vůbec navrhuješ. Uvědom si, že by to mělo následky. V lepším případě by se u soudu ukázalo, že se nám nedá důvěřovat a nejsme o nic lepší než hlídka za Velina, a v horším by to Zeranovi zničilo život ještě víc.", "angry")
    $ rauvin.say("Podobného způsobu přemýšlení se musíš co nejdřív zbavit. Ten do hlídky nepatří.", "angry")
    show mcPic at menuImage
    menu:
        "Díky za vysvětlení. Polepším se.":
            hide mcPic
            $ rauvin.say("O tom nepochybuji.")
        "Připadá mi, že si toho o sobě nějak moc myslíš.":
            hide mcPic
            $ rauvin.trust -= 3
            $ rauvin.say("Myslím si o sobě, že jsem tvůj velitel. Můžeš to přijmout, nebo odejít.")
            show mcPic at menuImage
            menu:
                "Jistě, omlouvám se.":
                    hide mcPic
                    $ rauvin.say("V pořádku.")
                "S takovýmto velitelem v jedné hlídce být nechci.":
                    hide mcPic
                    $ rauvin.say("Dobrá, v tom případě prosím vrať glejt a já ti popřeji hodně štěstí při hledání jiné práce.")
                    jump thrownOut
    if gender == "M":
        $ rauvin.say("Samozřejmě ale oceňuji, že ses nejdřív přišel zeptat, jestli zatknout Zerana je dobrý nápad. To je správný postup.")
    else:
        $ rauvin.say("Samozřejmě ale oceňuji, že ses nejdřív přišla zeptat, jestli zatknout Zerana je dobrý nápad. To je správný postup.")
    $ rauvin.say("Potřebujeme ještě něco probrat, nebo se teď vrátíš k případu?")
    return

label arrestZeranStolenNjalInsists:
    hide mcPic
    $ rauvin.trust -= 3
    $ mc.cluesAgainst += 1
    "Rauvin se zamračí."
    $ rauvin.say("A to ti připadá jako dostatečný důvod?", "angry")
    $ mc.say("Ne u každého, ale tady mluvíme o řemeslnickém mistru a Zeran to klidně mohl udělat. Dost pochybuji, že bude mít nějaké důkazy o své nevině.")
    $ rauvin.say("A právě proto nikoho nezatýkáme bez důkazů!", "angry")
    show mcPic at menuImage
    menu:
        "Proč ne? Tak se to přece dělá všude.":
            hide mcPic
            $ rauvin.say("Ale ne tady! A jestli to tak bylo vždycky, tak teď už ne. Teď platí rovnost před zákonem!", "angry")
            if gender == "M":
                $ mc.say("Tomu nerozumím. Všiml jsem si, jak moc je pro vás důležité dobré jméno u vážených osob. Už jenom ten rozdíl, jak jste hned první den mluvil se mnou a potom s mistrem Heinrichem, byl opravdu výrazný.")
            else:
                $ mc.say("Tomu nerozumím. Všimla jsem si, jak moc je pro vás důležité dobré jméno u vážených osob. Už jenom ten rozdíl, jak jste hned první den mluvil se mnou a potom s mistrem Heinrichem, byl opravdu výrazný.")
            $ rauvin.say("Ctít něčí společenské postavení přece neznamená ohýbat kvůli nim zákony!", "angry")

            if any("careful of the rich" in str for str in status):
                if "careful of the rich - lover" in status:
                    $ mc.say("Když jsme ale mluvili o možném milenci paní Lisbeth, kladl jste mi na srdce, že mám na jejich postavení brát ohled. U nikoho jiného jste po mně takovou opatrnost nechtěl.")
                $ mc.say("Jestli mám někoho vyšetřovat obzvlášť opatrně a u jiného to je jedno, tak to přece jasně říká, že na každého platí zákony jinak.")
                $ rauvin.say("Neříká! Vždycky chceme případ pochopit tak do hloubky, jak to jen jde. Jediný rozdíl je v tom, že bohatší lidé mají víc možností, jak nám v tom překážet.", "angry")

            $ rauvin.say("Zatýkat lidi jen proto, že to klidně mohli udělat, to si nemůžeme dovolit. A nemůžeme si dovolit hlídkaře, kteří to navrhují.", "angry")
            $ rauvin.say("“Prosím, vrať svůj glejt.")
            $ rauvin.say("Zkus štěstí v nějaké práci, kde nerozhoduješ o ostatních.")
            jump thrownOut
        "Chápu. Asi bych měl jít hledat důkazy." if gender == "M":
            call goFindEvidence
        "Chápu. Asi bych měla jít hledat důkazy." if gender == "F":
            call goFindEvidence

    return

label goFindEvidence:
    hide mcPic
    if mc.cluesAgainst < 2:
        if gender == "M":
            $ rauvin.say("To bys měl. Opravdové důkazy, ne to, že někdo nebude nikomu chybět nebo se ti nelíbí.", "angry")
        else:
            $ rauvin.say("To bys měla. Opravdové důkazy, ne to, že někdo nebude nikomu chybět nebo se ti nelíbí.", "angry")
        $ rauvin.say("A prosím, přemýšlej příště nad tím, jestli tvůj návrh nemůže ublížit někomu, kdo je možná nevinný. My nejsme utlačovatelská hlídka. A nemůžeme si tu dovolit nikoho, kdo jako utlačovatel přemýšlí.")
    else:
        $ rauvin.say("Ve skutečnosti ne.", "angry")
        $ rauvin.say("Tohle není první případ, kdy spolu o něčem podobném mluvíme. Doufal jsem, že si z toho napoprvé něco vezmeš, ale nestalo se. Někoho takového si v hlídce nemůžeme dovolit mít.", "angry")
        $ rauvin.say("“Prosím, vrať svůj glejt.")
        $ rauvin.say("Hodně štěstí při hledání nové práce.")
        jump thrownOut
    return
