

label dinnerWithColleaguesOptions:

    show mcPic at menuImage
    menu:
        "To je nás v hlídce tak málo?" if "watch size" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("watch size")
            $ solian.say("Je nás víc, ale větší část mužstva má na přes den starosti vybírání cla u bran a po službě jde většinou za svou rodinou. Runa taky radši večeří doma.")
            $ hayfa.say("A Melien se nerad váže, ten prý nejradši večeří podle toho, jak má zrovna hlad a chuť. Ale občas se za námi staví Valeran.")
            $ solian.say("Většinou sem chodí hlavně ti, kdo doma nemají nic nebo nikoho lepšího. Nebo kdo hlídku tak milují, že v ní chtějí trávit co nejvíc času.")
            show mcPic at menuImage
            menu:
                "Co velitel?":
                    hide mcPic
                    $ solian.say("Toho jsem tu snad ještě nikdy neviděl.")
                    $ rauvin.say("Má spoustu práce a vlastní rodinu.")
                    $ hayfa.say("Hlavně spoustu práce neudělat nic výrazného, co by mu kdokoli mohl zazlívat.")
                    $ rauvin.say("To je v marendarské hlídce velmi důležité.")
                "Co z toho platí o tobě?":
                    hide mcPic
                    $ solian.say("Z hlídkařské mzdy je možné uživit rodinu jen o málo lépe než z tovaryšské. Zbytek si domysli.")
        "Jak jste se do hlídky vlastně dostali vy?" if "reasons" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("reasons")
            $ hayfa.say("Část je nás tu z lásky k Marendaru a druhá proto, že prostě potřebovali práci. Rozlišit to jistě dokážeš [sam], byť ne všichni ti to sami hned řeknou.")
            $ solian.say("Vynecháváš tu nejzajímavější část.")
            $ hayfa.say("Myslíš tu o zchudlém šlechtici, který potřeboval uplatnit vojenský výcvik v zemi, kde se těsně po jeho příchodu přestalo válčit?", "happy")
            $ rauvin.say("To není nic zvláštního, takových zchudlých zemanů a mladších synů je spousta. Jen v Eichenau nás takových byla celá jednotka.")
            $ solian.say("Myslím to, že jsi sotva před rokem byla veřejně odsouzená za pokus ovládnout město a teď málem velíš celé hlídce a nikomu to asi nevadí.", "angry")
            $ hayfa.say("Tehdy jsem sloužila vládcům Königswiesen. Od té doby oni padli a já si zamilovala Marendar.")
            $ solian.say("Myslíš té hnusné sektě.", "angry")
            $ hayfa.say("Osobně nevidím rozdíl mezi hnusným sektářem a hnusným šlechticem. Oba ti budou tvrdit, že jsou něco lepšího, a když je neposlechneš, pošlou na tebe pohůnky.", "angry")
            $ hayfa.say("Rozdíl je jen v tom, jestli má moc ten nejschopnější, nebo ten, kdo se správně narodí.")
            $ rauvin.say("Dohodli jsme se přece, že o tomhle srovnání se nebudeme bavit.", "angry")
            $ hayfa.say("Jen jsem nechtěla, aby %(mcName)s od Soliana získal[a] špatný dojem. Když už tomu tady skoro velím.")
            $ rauvin.say("Řekl jsem, že se o tom nebudeme dál bavit.", "angry")
            $ rauvin.say("%(mcName)s se nemůže účastnit rozhovoru a to od nás není slušné.")
            $ globalClues.append("hayfa's past")
            call askMc
        "Jak dlouho jste v hlídce?" if "time employed" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("time employed")
            $ solian.say("Já něco přes dva roky, Rauvin tu je necelý rok a Hayfa asi pět měsíců.")
            $ hayfa.say("Šest.")
            $ mc.say("Tak krátce?")
            $ solian.say("Hayfa teprve před rokem vůbec přišla do města a Rauvin se tu sice narodil, ale potom byl dlouho pryč.")
            $ solian.say("Služebně starší bys spočítal na prstech jedné ruky. Většina staré gardy byla až moc spojená s Velinem na to, aby mohla zůstat. Já nastoupil jako jeden z prvních poté, co Velin padl.")
            $ globalClues.append("Hayfa's arrival to Marendar")
        "Rauvine, jestli jsi sloužil v Eichenau, co tě přimělo se vrátit do Marendaru?" if ("reasons" in colleaguesAsked or "origin" in mc.asked) and "Rauvin's return" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("Rauvin's return")
            $ globalClues.append("Luisa arsonist")
            "Rauvin viditelně znejistí způsobem, který jsi u něj ještě nepozoroval[a]."
            $ rauvin.say("To se těžko vysvětluje. Asi se mi začalo stýskat.")
            $ rauvin.say("Pořád jsem tady měl sestru a ani jsem nevěděl, jestli je po požáru v pořádku.")
            $ hayfa.say("Jistě že byla. Přece nebude zakládat požár, co jí samotné ublíží.", "angry")
            $ rauvin.say("Hayfo.", "angry")
            $ hayfa.say("Já vím, já vím. Nemám důkazy a bez důkazů o tom s tebou nemám mluvit. Ale já je jednou najdu.", "angry")
            $ rauvin.say("To jsem zvědavý.", "angry")
            $ solian.say("V každém případě Luise se velmi daří, opravila dům a obnovuje knihovnu a máte si tolik co říct, že většinou radši večeříš s námi než s ní. Tak proč ses do Eichenau nevrátil?")
            $ rauvin.say("Prostě jsem se tak rozhodl, nemůžete mi dát pokoj?", "angry")
            $ rauvin.say("V Eichenau jsem neměl žádné vyhlídky. Jezdit podél hranic a chytat lapky nestojí za moc a nějaké důležitější místo by mi jako cizinci možná nikdy nesvěřili.")
            $ solian.say("Zato tady z tebe nejspíš brzy bude velitel hlídky. To pak není o čem přemýšlet.")
            $ rauvin.say("Tady hlavně dělám něco užitečného. Pojďme konečně řešit něco jiného, tak zajímavý přece nejsem.", "angry")
            call askMc
        "Čekal[a] bych, že svobodný pán bude chtít do lepší hospody..." if "pub choice" not in colleaguesAsked:
            call betterPubForRauvin
        "Jak vlastně vybíráte, do které hospody jít?" if "pub choice" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("pub choice")
            $ solian.say("Pravidelně se chodí sem. Tak to bylo, už když jsem nastoupil já.")
            call pubTraditionOrigin
        "Víte, jak začala ta tradice chodit sem?" if "pub choice" in colleaguesAsked and "pub tradition origin" not in colleaguesAsked:
            hide mcPic
            call pubTraditionOrigin
        "Potřebujeme nosit zbroj? Tady ve městě?" if "Rauvin's armour" in colleaguesAsked and "need for armour" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("need for armour")
            $ hayfa.say("Jen když máš tolik nepřátel jako Rauvin.")
            $ rauvin.say("Prosím? Víš snad něco, co já ne?")
            $ hayfa.say("Já nevím o ničem. Ty jsi ozbrojený, jako bys čekal útočníka v každé tmavší uličce.")
            $ rauvin.say("Být upravený a ve zbroji pomáhá hlídce dodat vážnost.")
            $ solian.say("Já si myslím, že beze zbroje vypadáme přístupněji.")
        "Pořád tady slyším o Velinovi, jak hrozné to tehdy vlastně bylo?" if origin != "born here" and "Velin" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("Velin")
            "Tví spolustolovníci na sebe pohlédnou a krátce zaváhají."
            $ rauvin.say("Hlídka tehdy byla početná a Velin ji používal... a sloužila Velinovi, ne městu.")
            $ hayfa.say("Hodně rozlišoval, že elfové Marendaru vládnou, zatímco lidi mají jen platit daně a být vděční, že je nechá naživu.")
            $ solian.say("Ve skutečnosti spousta lidí se neměla tak špatně. Mohli se třeba stát řemeslnými mistry nebo pokračovat v obchodu.")
            $ hayfa.say("Jen protože to bral pomalu.", "angry")
            $ solian.say("Na začátku nevypadal tak špatně, ale potom mu umřel syn při požáru a stal se z něj prostě krutovládce. Tak jsme ho sesadili.")
            $ rauvin.say("A právě proto, že to byl krutovládce a že hlídku zneužíval, teď musíme dávat takový pozor, aby nikdo nemohl pochybovat, že sloužíme městu jako takovému. Ne jen třeba veliteli nebo městské radě.")
            $ hayfa.say("Zapomněl jsi dodat, že Velin začal právě jako velitel hlídky.")
            $ rauvin.say("Ano. To nám také nepomáhá.")
        "Jaký je vlastně velitel?" if "Galar" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("Galar")
            $ rauvin.say("Zkušený. Zažil tady dva předchozí velitele, dva převraty ve městě, několik povstání...")
            $ hayfa.say("To všechno od stolu.")
            $ hayfa.say("Na můj vkus Galar řeší víc zákony než lidi, ale aspoň sám nemá ambice. Na rozdíl od obou předchozích velitelů. Mohlo by to být horší.")
            $ mc.say("Je normální, že jsem ho ještě nepotkal[a]?")
            $ rauvin.say("Ano, velitel Galar celé dny řeší nutnou administrativu a na moc jiného mu nezbývá čas.")
            $ rauvin.say("Musíme vést podrobné záznamy o výběru cla u bran a o všem ostatním, co má hlídka na starosti. Především pro případ, že by vzniklo jakékoli podezření na nerovné jednání nebo zneužití moci. Na to jsou tady v Marendaru všichni citliví.")
        "Jaký trest toho zloděje čeká, až ho dopadneme?" if "thief punishment" not in colleaguesAsked:
            hide mcPic
            $ colleaguesAsked.append("thief punishment")
            $ solian.say("To záleží na tom, kdo by to byl.")
            $ hayfa.say("Samozřejmě.", "angry")
            $ mc.say("Tak se to liší všude, ale jaký trest hrozí tady v Marendaru?")
            $ rauvin.say("Ještě potom záleží, s jakým úmyslem ten čin byl provedený. Soudci se k tomu teď snaží přihlížet.")
            $ solian.say("Jestli to udělal nějaký špinavý nuzák, protože prostě nezná žádnou slušnost, může ho klidně čekat cejch nebo může přijít o ruku.")
            $ rauvin.say("Jestli ten důvod je nějak omluvitelný, možná by mohl stačit pranýř a povinnost to odpracovat. Když bude soudce mírný.")
            $ solian.say("Ale přiznejme si, tahle lůza se dá omluvit jen málokdy.", "angry")
            $ hayfa.say("Nejsi ty náhodou také špinavá lůza, když ses neuchytil ani jako tovaryš?", "angry")
            $ solian.say("Já jsem v hlídce! A nepáchám zločiny!", "angry")
            $ rauvin.say("No a jestli to udělal třeba nějaký řemeslník, nejspíš bude mít možnost zaplatit odškodné. Ačkoli očekávám, že když jde o výrobek na Einionovy slavnosti, bude ta částka patřičně navýšená.")
            show mcPic at menuImage
            menu:
                "Stejně se mi nelíbí, jak moc záleží na něčím původu.":
                    hide mcPic
                    $ hayfa.say("To nejsi [sam].")
                "To zkoumání důvodů se mi nezdá. Potom může někomu spousta věcí projít jen proto, že umí na soudce udělat nevinné oči.":
                    hide mcPic
                    $ hayfa.say("To i teď. A když někde soudí osobně místní šlechtic, tak obzvlášť.")
                "Tenhle přístup se mi líbí. Je nejpřísnější na ty, kdo mají nejvíc důvodů je porušovat, ale umožní odlišit pachatele, kteří se můžou napravit.":
                    hide mcPic
                    $ solian.say("Nebo si to od něj aspoň všichni slibují.")

    jump dinnerWithColleaguesOptions

label askMc:
    if "origin" not in mc.asked:
        $ mc.asked.append("origin")
        $ solian.say("Odkud vlastně jsi?")
        if origin == "born here":
            $ mc.say("Narodil[a] jsem se tady v Marendaru, ale chtěl[a] jsem jít do učení, a ne do války. Tak jsem nakonec skončil[a] až v sousedním hrabství.")
            $ rauvin.say("V Eichenau? Tam jsem strávil dost času také. Kde přesně a co ses učil[a]?")
            $ mc.say("V Sonnenstrahlen, chtěl[a] jsem být písař.")
            $ rauvin.say("Církevní? Myslel jsem, že v Sonnenstrahlen je hlavně velký chrám Heulwen.")
            $ mc.say("Spíš to je první město v Eichenau, kam se mi podařilo se dostat.")
        else:
            $ mc.say("Z Hirschendorfu. Ještě pod vládou Anselma jsem se učil[a] na písaře, to by znamenalo dobré místo v jeho správě. Ale úplně do nevyšlo.")
            $ rauvin.say("Myslíš toho žoldáka, který okupoval panství rodu de Périgny?")
            show mcPic at menuImage
            menu:
                "Aspoň se o něj staral.":
                    hide mcPic
                    $ rauvin.trust -= 1
                    $ mc.say("Na rozdíl od de Pérignyho a dalších šlechticů.")
                "Radši bychom někoho jiného, ale vesničani o tom nerozhodují.":
                    hide mcPic
                    $ hayfa.say("Mohli by. Záleží jen na tom, pro co se jeden rozhodne a co mu za to stojí.")
                    $ hayfa.say("Nebyli to zase jen vesničani, kdo potom Anselma porazil?")
                    $ mc.say("Pokud vím, to proti němu bojoval mnohem silnější protivník než jen pár vesničanů. Ale jinak máš pravdu.")
                "Až tak vysoko jsem se nikdy nedíval[a].":
                    hide mcPic
                    $ mc.say("Chtěl[a] jsem jenom slušný život.")
                    $ solian.trust += 1
            $ mc.say("Anselma potom smetlo povstání a já při[sel] o učitele i všechny vyhlídky.")
            if origin == "family":
                $ mc.say("V Marendaru měl žít můj strýček, ale než jsem se sem dostal[a], musel prodat dílnu a odejít z města.")
            else:
                $ mc.say("Tak jsem zkusil[a] nejbližší město.")
        $ hayfa.say("Proč vlastně neděláš někde toho písaře?")
        if origin == "born here":
            $ mc.say("Protože nejsem plně vyučen[y]. V Sonnenstrahlen jsem dělal[a] spíš pomocníka a poslíčka a snažil[a] se toho naučit co nejvíc, ale nikdo mi to nepotvrdí.")
        else:
            $ mc.say("Protože nejsem plně vyučen[y]. U Anselma jsem dělal[a] spíš pomocníka a poslíčka a snažil[a] se toho naučit co nejvíc, ale nikdo mi to nepotvrdí.")
        $ mc.say("Na nic jiného jsem neměl[a] dost peněz. Možná jednou... jestli někdo bude chtít tak starého učedníka.")
        $ solian.say("Učení taky nikam nevede. Aspoň pokud nechceš zůstat jako věčný tovaryš bez naděje na cokoliv lepšího.", "angry")

    if "Heinrich" not in mc.asked:
        $ mc.asked.append("Heinrich")
        $ solian.say("Co si zatím myslíš o mistru Heinrichovi?")
        label askMcHeinrich:
        show mcPic at menuImage
        menu:
            "Po jednom dni moc nemám, jak soudit." if "Heinrich - too soon to judge" not in mc.asked:
                hide mcPic
                $ mc.asked.append("Heinrich - too soon to judge")
                $ solian.say("To po tobě ani nechci. Jen to je člověk, se kterým bychom měli vycházet, tak mě zajímá tvůj názor.")
                jump askMcHeinrich
            "Připadá mi, že je hodně náročný a vždycky musí být po jeho.":
                hide mcPic
                $ hayfa.say("To určitě je. Proto také nemá žádné tovaryše a ani učedníci u něj často nezůstanou dlouho.")
                $ rauvin.say("Nevím, proč je vůbec nabírá, když je potom stejně hned zase vyhodí.")
                $ solian.say("Aby mu v dílně někdo uklízel a podával věci, samozřejmě. To je úloha učedníků.")
                $ solian.say("Tovaryš, to je něco jiného. Ten už umí pracovat samostatně a měl by mít v dílně svoje slovo. Ale učedník by měl znát svoje místo.")
                $ hayfa.say("I když mu mistr neumožňuje se pořádně učit?")
                $ rauvin.say("I když si na něm mistr vylévá zlost?")
                $ solian.say("Učedník si něco takového velmi často myslí, ale málokdy to je pravda. Většinou ten učedník prostě ještě není dost zkušený.")
                show mcPic at menuImage
                menu:
                    "Špatného učitele, co si jen vylévá zlost, určitě pozná každý.":
                        hide mcPic
                    "To je pravda, bez přísnosti se nikdo nic nenaučí.":
                        hide mcPic
                    "Mistr by měl učedníkovi hlavně dát druhou rodinu. Vždyť u něj ty děti bydlí spoustu let.":
                        hide mcPic
            "Je hodně hrdý na svou práci, a jestli to chápu správně, tak právem." if "Heinrich - justly proud" not in mc.asked:
                hide mcPic
                $ mc.asked.append("Heinrich - justly proud")
                $ solian.say("To rozhodně. Takhle schopného mistra nám závidí i v mnohem větších městech.")
                $ hayfa.say("Ale to jsme všichni věděli dávno před tím, než k té krádeži došlo. Co tam máš dalšího?")
                jump askMcHeinrich
            "Moc nerozumím tomu, proč usiluje o místo cechmistra. Vždyť by mu to jen bralo čas na práci.":
                hide mcPic
                $ hayfa.say("Možná zjistil, že nejlepší švec ve městě už je a tohle je něco dalšího, o co usilovat.")
                $ hayfa.say("Kdyby chtěl být ještě lepší řemeslník, asi by se musel přestěhovat do většího města. Ale to by znamenalo opustit Marendar.")
                $ rauvin.say("Pro něj i celou jeho rodinu.")
                show mcPic at menuImage
                menu:
                    "Podle mě by měl být spokojený s tím, co má.":
                        hide mcPic
                    "Tak ať si najde něco jiného než cechmistrování, když na něj nemá předpoklady.":
                        hide mcPic
                    "Dobře, asi rozumím, že nechce ustrnout na místě.":
                        hide mcPic
            "Divím se, že se uchází o místo cechmistra. Připadá mi jako hodně vznětlivý člověk, pro kterého bude obtížné se s někým dohodnout. Proč by ho někdo volil?":
                hide mcPic
                $ solian.say("To je také to hlavní, co proti němu současný cechmistr vytahuje. Určitě je nebezpečí, že s Heinrichem v čele by si ševci leckoho znepřátelili.")
                $ rauvin.say("Mistr Heinrich má ale zároveň pověst přímého a čestného muže, který nestrpí žádnou nepravost.")
                $ rauvin.say("Občas se někdo může bát, že současný cechmistr se stará především o vlastní zájmy a až potom o dobro cechu jako celku. Potom je Heinrich zajímavá volba.")
                $ hayfa.say("A důvody podezřívat Rumelina by byly. Byl cechmistrem už za Velina, zůstal jím i po něm a celou dobu se měl výborně.")
                $ hayfa.say("To se rozhodně o všech ostatních ševcích říct nedá. Těžko říct, jestli pro ně nemohl nic udělat, nebo je obětoval pro vlastní prospěch. To už se asi nedozvíme.")
                show mcPic at menuImage
                menu:
                    "Mistr Heinrich by se rozhodně postavil za každého, kdo je v právu. Z těch dvou bych volil[a] jeho.":
                        hide mcPic
                    "Mistr Heinrich by to svou vznětlivostí jen zhoršil pro všechny. Já bych vybral[a] Rumelina.":
                        hide mcPic
                    "Jestli je jeden nebezpečně vznětlivý a druhému se nedá věřit, tak ševcům jejich výběr vůbec nezávidím.":
                        hide mcPic
                $ solian.say("Není to snadná volba. Oba mají značné přednosti. Vlastně mě těší, že to nemusím řešit.")

    return

###

label betterPubForRauvin:
    hide mcPic
    $ colleaguesAsked.append("pub choice")
    $ colleaguesAsked.append("Rauvin's armour")
    $ rauvin.say("Už nás tady znají, chodilo se sem vždycky.")
    $ solian.say("Rozhodně už když jsem nastoupil já, rok před tady svobodným pánem.")
    $ rauvin.say("A vaří tady dobře. Je to mnohem lepší než vojenské příděly a ani do toho nepotřebují dávat žádná divná koření.")
    $ hayfa.say("Nejdůležitější ale je, že do dražší hospody bychom s ním nemohli, zatímco tady nás má všechny na očích.")
    $ rauvin.say("Zrovna ty si stěžuj. Většinu dne nikdo neví, co děláš.")
    $ hayfa.say("A potom také musí šetřit. Leštidlo na zbroj je dnes drahé.")
    $ solian.say("Já myslel, že na to dostává ten velitelský příplatek.")
    $ hayfa.say("Ano, ale viděl jsi jeho zbroj. Na Rauvinovu spotřebu těch pár mincí zdaleka nestačí.")
    $ rauvin.say("Ty víš, kolik dostávám jako velitelský příplatek?")
    $ hayfa.say("Opravdu mám odpovídat?", "happy")
    $ rauvin.say("Nemusíš. Stačí, když mi řekneš, jestli si můžu dovolit ještě jednu placku.", "happy")
    $ hayfa.say("Jednu ano. Malou. Bez škvarků.")
    return

label pubTraditionOrigin:
    $ colleaguesAsked.append("pub tradition origin")
    $ solian.say("Manžel Teliven, které to tu patří, býval člen hlídky a padl během povstání proti Velinovi. Tak nová hlídka tuhle hospodu vzala za svoji, na jeho památku.")
    $ rauvin.say("A jako symbol toho, o co se tady snažíme. Bránit nevinné proti bezpráví.")
    return
