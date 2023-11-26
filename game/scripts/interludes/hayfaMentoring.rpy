label hayfaMentoring:
    call hayfaMentoringPreparation

    scene bg street01
    "Vyjdeš ze strážnice rychlým krokem a v hlavě si procházíš otázky, které chceš položit, a podrobnosti, na které nesmíš zapomenout. Málem sebou trhneš, když tě náhle někdo osloví."
    $ hayfa.say("Kam vyrážíš?")
    show mcPic at menuImage
    menu:
        "[response!c]":
            hide mcPic
        "Radši bych si to nechal[a] pro sebe.":
            call hayfaMentoringSecrecy
    $ hayfa.say("Vida, zrovna mám pochůzku stejným směrem. Můžu se připojit?")
    "Působí to spíš jako řečnická otázka. Společně vyrazíte ulicí."
    $ hayfa.say("Co si zatím o hlídce myslíš?")
    show mcPic at menuImage
    menu:
        "Čekal[a] jsem, že budeme řešit nějakou vraždu, a ono boty.":
            call hayfaMentoringBoredResponse
        "Čekal[a] jsem, že budeme jen postávat někde na stráži, z toho běhání mě začínají bolet nohy.":
            call hayfaMentoringTiredResponse
        "Čekal[a] jsem, že nejdřív budu muset jen stát někde na stráži nebo něco opisovat, ne že hned dostanu vlastní případ.":
            call hayfaMentoringImportantResponse
        "Přemýšlím, kolik z práce hlídky opravdu pomáhá městu a kolik toho děláme jen proto, že to někdo bohatý požaduje.":
            hide mcPic
            $ hayfa.trust += 1
            $ hayfa.say("To já občas také.")
            $ hayfa.say("Ale říkám si, že musíme být trpěliví. Spousta lidí by byla nejradši, kdyby hlídka nebyla vůbec, nebo kdyby jen postávala u brány a jinak nic nedělala. Zatím děláme málo, postupně toho bude víc a víc.")
    $ hayfa.say("Kolik hlášení už po tobě Rauvin chtěl?")
    if "Rauvin visited" in status:
        $ mc.say("Už dvě. Ptá se takhle lidí pokaždé, kdy je vidí?")
        $ hayfa.say("Jen když mezitím stihli vylézt ze strážnice. Nebo když sice neodešli, ale on na ně mezitím zapomněl.")
    else:
        $ mc.say("Zatím jedno, jakmile jsem se poprvé vrátil[a] na strážnici.")
    $ hayfa.say("Rauvin hlášení miluje. Má rád přehled a z armády je na to zvyklý. Myslím, že i dávání portrétů na zeď všechny učí hlavně proto, aby mohl snáz dohlížet.")
    $ hayfa.say("Jestli si chceš šplhnout, zajdi za ním s hlášením někdy [sam] od sebe.")
    show mcPic at menuImage
    menu:
        "Ty Rauvina asi nemáš moc ráda?":
            hide mcPic
            $ hayfa.say("Na šlechtice ujde.")
            $ hayfa.say("Není hloupý, je zvyklý něco dělat a umí velet. Jen je na můj vkus až moc přesvědčený, že zákony jsou vždycky správné, i když je napíše někdo, kdo nikdy nevytáhl paty z paláce.")
            $ mc.say("Neměla by hlídka hlídat dodržování zákonů?")
            $ hayfa.say("Hlídka by měla hlavně chránit město a lidi v něm.")
        "Jak často mu dáváš hlášení ty?":
            hide mcPic
            $ hayfa.say("Já mu nedávám hlášení, já s ním probírám věci, které je potřeba řešit. Ale trvalo mi pěkných pár měsíců, než jsem ho přesvědčila, že mi může tímhle způsobem důvěřovat.")
            $ mc.say("Jak se ti to nakonec povedlo?")
            $ hayfa.say("Vystopovala jsem podvodníka, který mu dlouho dělal starosti.")
        "Ty portréty na zdi nepoužíváš?":
            hide mcPic
            $ hayfa.say("Ne. Moc pomalé a moc velké nebezpečí, že to někdo omylem rozhází. Ale spoustě hlídkařů to vyhovuje, tak proč ne.")
    $ mc.say("Zdá se mi to, nebo práci v hlídce bereš dost po svém?")
    $ hayfa.say("V některých věcech.")
    $ mc.say("A jak tedy pracuješ?")
    $ hayfa.say("Ve skutečnosti stejně jako všichni. Bavím se s lidmi, všímám si věcí, používám hlavu. Jsem v tom dobrá, ale většinou nedělám nic tak zvláštního.")
    $ hayfa.say("Od Rauvina a ostatních se liším v tom, že oni hrozně dají na lidi, co považují za vážené měšťany. Já se mnohem víc ptám různých žebráků, tichých manželek a podobně. Jeden by nevěřil, kolik špíny na tyhlety vážené měšťany občas vědí.")
    $ mc.say("Díky za radu. Je ještě něco, co bys mi doporučila?")
    $ hayfa.say("Jo. Nikdy nepředpokládej, že už jsi od někoho zjistil[a] všechno. Při prvním rozhovoru většina lidí jednu půlku věcí zapomene a druhou zatají. Často je potřeba k nim přijít znovu a připomenout jim nějaké nové zjištění, které by mohli chtít vysvětlit.")
    $ hayfa.say("Ještě bych ti ráda doporučila, že se může hodit, když co nejméně lidí ví, že patříš k hlídce. Ale to jde hodně těžko, tak to možná ani nemá smysl zkoušet.")
    $ hayfa.say("Přinejmenším mě už zná výrazně víc lidí, než by se mi líbilo.")
    $ mc.say("Aspoň už se nemusíš desetkrát denně prokazovat glejtem?")
    $ hayfa.say("Chabá útěcha, když je pak mnohem těžší někoho nalákat do pasti.")
    $ hayfa.say("Tady se odpojím. Hodně štěstí v případu. A mimochodem, %(advice)s")
    return

###

label hayfaMentoringBoredResponse:
    hide mcPic
    $ personality.append("bored by first case")
    $ hayfa.say("Marendar je poměrně malé město, k vraždám tu naštěstí dochází zřídka.")
    $ hayfa.say("Naštěstí. Vražda znamená aspoň jednoho mrtvého člověka, její vyřešení dalšího a podle mých zkušeností většinou bývá jednoho z nich škoda.")
    $ mc.say("Čekal[a] bych, že tu budou potíže třeba s loupežníky, co si nevšimli, že už skončilo bezvládí, nebo že se občas vynoří spor mezi lidmi a elfy.")
    $ hayfa.say("Loupežníci opravdu občas něco provedou, ale většinou to nekončí smrtí. A sporům mezi rasami se tady všichni ze všech sil vyhýbají. Bojí se, aby to nespustilo další boje v ulicích.")
    return

label hayfaMentoringTiredResponse:
    hide mcPic
    $ personality.append("tired by first case")
    $ hayfa.say("I postávání na stráži si tady užiješ, ale bolí z toho nohy ještě víc a navíc je to dost nuda. Za sebe jsem ráda, že už to po mně nikdo nechce.")
    $ mc.say("A co se po tobě tedy chce?")
    $ hayfa.say("Šmejdit po městě, všímat si věcí a řešit ty, které jsou potřeba. Rauvin naštěstí chápe, že tohle mi jde mnohem lépe než postávání.")
    return

label hayfaMentoringImportantResponse:
    hide mcPic
    $ hayfa.say("A je to příjemné překvapení, nebo ani ne?")
    show mcPic at menuImage
    menu:
        "Cítím se polichoceně, beru to jako výraz důvěry!":
            hide mcPic
            $ personality.append("flattered by first case")
            $ hayfa.trust -= 1
            $ hayfa.say("Důvěry, že to nezkazíš tolik, aby to Rauvin nedokázal urovnat, ano. A také je to výraz toho, že nikoho jiného jsme stejně neměli.")
            $ mc.say("Jak to? Na strážnici přece věčně někdo je, mohl to vzít někdo z nich. Kdyby to zvládnul.")
            $ hayfa.say("To nudné postávání a opisování bohužel má svůj smysl. Hlídka postává u brány, sepisuje, co který obchodník veze za zboží, vybírá cla a potom to všechno pečlivě zanáší do účetních knih, aby si někdo nemyslel, že si hrabeme pro sebe nebo někoho utlačujeme.")
            $ hayfa.say("Nemyslím, že v porovnání s výběrem cla by městu přišly ztracené boty tak podstatné.")
            $ mc.say("A to si myslí celá hlídka?")
            "Hayfa pokrčí rameny."
            $ hayfa.say("Nemůžu mluvit za ostatní. Co se mě týče, z něčeho se ty nové domy v Dočasné čtvrti platit musí. A když nás město zruší, ničemu tím nepomůžeme.")
        "Ani nevím, ve skutečnosti se trochu bojím, jestli to zvládnu.":
            hide mcPic
            $ personality.append("nervous of first case")
            $ hayfa.say("To Rauvin také.")
            $ mc.say("A ty?")
            $ hayfa.say("Já ne. Buď se osvědčíš a získáme dalšího schopného hlídkaře, nebo se neosvědčíš a my to aspoň zjistíme rychle. Mistr Heinrich to nějak zvládne.")
            $ mc.say("To není moc uklidňující.")
            $ hayfa.say("Čemu by pomohlo tě uklidňovat? Máš svoje schopnosti, máš touhu to dokázat a to je všechno, co potřebuješ. Buď to bude stačit, nebo ne.")
            $ hayfa.say("Když budeš potřebovat pomoc, pomůžeme, ale to hlavní je na tobě.")
        "Asi by to bylo příjemnější, kdyby to nevypadalo, že tím Rauvinovi i mistru Heinrichovi zároveň děláš nějaký naschvál.":
            hide mcPic
            $ personality.append("unsure of first case politics")
            $ hayfa.say("Trochu ho to překvapilo, to je pravda. Na některé věci si ještě nezvykl.", "happy")
            $ hayfa.say("Ale ve skutečnosti to je pomoc pro vás oba. Hlídka vybírá cla u bran, a tak každý z nás musí být dokonale bezúhonný. Jak by to u tebe Rauvin ověřoval? Nevypadáš, že by se za tebe někdo mohl zaručit.")
            $ hayfa.say("Možná by tě přijal jako postávače, který ve skutečnosti nic nesmí. Na případu se můžeš rychle osvědčit.")
            $ mc.say("Takže je to pomoc, nebo zkouška?")
            $ hayfa.say("Obojí, pochopitelně.", "happy")
    return

label hayfaMentoringSecrecy:
    hide mcPic
    "Hayfa se na tebe dlouze podívá."
    if "not sharing" in status:
        $ hayfa.say("Pořád karty pevně u těla.")
        $ hayfa.say("Rauvinovi to dost vadilo. Já tě na jednu stranu chápu, ale na druhou, tady hrajeme jako tým. A my všichni ostatní známe město a lidi v něm daleko líp.")
    else:
        $ hayfa.say("Karty pevně u těla. Na jednu stranu tě chápu, ale na druhou, tady hrajeme jako tým. A my všichni ostatní známe město a lidi v něm daleko líp.")
    $ status.append("not sharing 2")
    $ mc.say("Jdu %(response)s")
    return

label hayfaMentoringPreparation:
    if chosenChar == "apprentice1" or chosenChar == "apprentice2":
        $ response = "položit pár otázek Heinrichovým učedníkům."
        $ advice = "zamysli se, jestli s učedníky chceš mluvit v Heinrichově přítomnosti. Myslím, že se ho dost bojí a neřeknou nic, s čím by mohl nesouhlasit. Na druhou stranu kdybys s nimi měl[a] mít problémy, vyhrožovat Heinrichem by mělo zabrat."
    elif chosenChar == "erle":
        $ response = "položit pár otázek žebračce Erle."
        $ advice = "s Erle jsem párkrát mluvila a pořád si nejsem jistá, jestli je tak hrdá, že nechce přijmout pomoc, nebo jestli jí současný život opravdu vyhovuje. Asi by mě pak zajímal i tvůj názor."
    elif chosenChar == "kaspar":
        $ response = "položit pár otázek mistru Kasparovi"
        $ advice = "o mistru Kasparovi jsem slyšela od každého něco jiného. Jiným mistrům a váženým obchodníkům většinou připadá jako úžasně příjemný a galantní člověk, zatímco různí pomocníci a sloužící ho moc v lásce nemívají. Můžeš si vybrat, komu věřit víc."
    elif chosenChar == "ada":
        $ response = "položit pár otázek Heinrichově dceři."
        $ advice = "myslím, že Ada má dobrý důvod si myslet, že ji nikdo dospělý nebere vážně. To může být způsob, jak si ji získat."
    elif chosenChar == "zeran":
        $ response = "položit pár otázek Zeranovi."
        $ advice = "jsem si jistá, že ten kluk je nevinný. Zároveň v tom domě dost dlouho žil, možná ví něco, co ti ostatní neřeknou."
    elif chosenChar == "eckhard":
        $ response = "Promluvit si s Eckhardem."
        $ advice = "Eckhard a Heinrich spolu byli v učení a ještě teď jsou jedna ruka. Vůbec bych se nedivila, kdyby na sebe navzájem věděli zajímavé věci."
    elif chosenChar == "gerd":
        $ response = "položit pár otázek Gerdovi."
        $ advice = "jestli byl ten kluk opravdu vyhozený za odporování, tak se očividně nebojí říct svůj názor. To by mohl být někdo, komu se dá v dost věcech věřit."
    elif chosenChar == "rumelin":
        $ response = "za cechmistrem Rumelinem."
        $ advice = "cechmistr Rumelin často říká, že vždy jedná jen v zájmu cechu. Já si ale nejsem jistá, jestli je to vždycky i v zájmu lidí v něm."
    elif chosenChar == "rovien":
        $ response = "položit pár otázek Rovienovi."
        $ advice = "pokud vím, Rovien a Rumelin si jsou dost blízko a ve všem se podporují. Jestli má cechmistr nějaká tajemství, myslím, že jeho bratr je bude znát."
    elif chosenChar == "zairis":
        $ response = "položit pár otázek Rovienovu synovi."
        $ advice = "Zairis je možná romantik nadšený do poezie a Amadise, ale na obchody má překvapivě dobrou hlavu."
    elif chosenChar == "nirevia":
        $ response = "za paní Nirevií."
        $ advice = "dobrá volba. Paní Nirevia může vypadat jako tichá voda, ale doporučuji brát ji vážně. Máloco jí unikne, zvlášť, když jde o vztahy mezi lidmi."
    elif chosenChar == "njal":
        $ response = "položit pár otázek mistru Njalovi."
        $ advice = "mistr Njal přišel do Marendaru teprve nedávno a většina cechu ho má za výstředního novátora. Rozhodně lépe rozumí ševcovským technikám než lidem. Přesto si myslím, že by si zasloužil brát víc vážně. "
    elif chosenChar == "merchant":
        $ response = "položit pár otázek Karstenovi."
        $ advice = "vůbec bych se nedivila, kdyby za Karstena dělala velkou část rozhodnutí jeho žena Lotte."
    elif chosenChar == "merchant" and "Karsten away" in clues:
        $ response = "položit pár otázek Karstenově ženě Lotte."
        $ advice = "Lotte je rozhodně lepší volba než její manžel. Mám podezření, že většinu rozhodnutí za něj stejně dělá ona."
    elif chosenChar == "pub":
        $ response = "ke Splašenému koni, zeptat se na pár věcí hostinské Salmy."
        $ advice = "u Salmy se uzavírá velká část důležitých obchodů, nedivila bych se, kdyby měla Salma hodně dobrý přehled o fungování cechů a různých vztazích."
    elif chosenChar == "son":
        $ response = "položit pár otázek Heinrichovu synovi."
        $ advice = "mistr Heinrich je prý na své učedníky hodně náročný. Myslím, že tlak na jeho syna bude ještě mnohem horší."
    elif chosenChar == "victim":
        $ response = "položit ještě pár otázek mistru Heinrichovi."
        $ advice = "mistr Heinrich ve městě rozhodně není oblíbený, ale nevím o tom, že by měl vážné nepřátele. Za tou krádeží myslím bude něco jiného než běžné spory nebo nevraživost uvnitř cechu."
    elif chosenChar == "lisbeth":
        $ response = "za paní Lisbeth, položit jí pár otázek."
        $ advice = "paní Lisbeth je schopná hospodyně, ale myslím, že má sklon vidět v lidech jen to dobré."
    elif chosenChar == "workshop":
        $ response = "do Heinrichovy dílny, prohlédnout si místo činu."
        $ advice = "touhle dobou už může být velká část stop pryč, ale občas stojí za to všímat si i věcí, které chybí oproti očekávání."
    else:
        $ response = "pokračovat v pátrání."
        $ advice = "dost lidí má nějaké tajemství, ale většina z nich nemusí s touhle krádeží vůbec souviset. Ale zase... hlídka je tady od toho, aby pomáhala lidem a řešila problémy."
    return
