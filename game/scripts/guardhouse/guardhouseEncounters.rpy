# player receives requested info
label suspectListDelivered:
    if "out of office" not in rauvin.status:
        "Jakmile si tě Rauvin všimne, mávne na tebe listem papíru."
        $ rauvin.say("Hostinská Salma ti posílá seznam hostů ze včerejška, prý sis ho vyžádal.[a]")
        $ mc.say("To je pravda. Myslel[a] jsem, že by nám pomohlo vědět, kdo všechno mohl slyšet o dokončených střevících.")
        "Rauvin se mírně zamračí."
        $ rauvin.say("Ta úvaha dává smysl, ale nejsem si jistý, jestli na procházení celého seznamu máme čas. Einionovy slavnosti jsou už za čtyři dny a jen obejít všechny tyhle lidi by mohlo zabrat celý den, možná víc.")
        $ rauvin.say("Zkus se zaměřit na jiné stopy a pokud by žádná z nich nikam nevedla, k seznamu hostů se můžeš vrátit později.")
    else:
        "Dojde k tobě Solian a podá ti list papíru."
        $ solian.say("Tady ti Salma posílá seznam hostů ze včerejška, prý jsi chtěl[a] vědět, kdo mohl slyšet o Heinrichově dokončeném díle. Znamená to, že nemáš žádnou konkrétní stopu?")
        show mcPic at menuImage
        menu:
            "Konkrétní stopy mám, ale chtěl[a] jsem být důkladn[y].":
                hide mcPic
                $ solian.say("Tak se zaměř spíš na ně. Einionovy slavnosti jsou za čtyři dny a už jenom oběhnout celý tenhle seznam může zabrat víc času, než vůbec máš.", "angry")
            "Zatím méně, než by se mi líbilo.":
                hide mcPic
                $ solian.say("Tak zkus co nejrychleji nějaké najít. Einionovy slavnosti jsou za čtyři dny a už jenom oběhnout celý tenhle seznam může zabrat víc času, než vůbec máš.", "angry")
        $ solian.say("A v nejhorším případě na tom seznamu začni u nějakých potulných tovaryšů a jiné pakáže, někdo takový tam určitě bude.")
    $ status.remove("waiting for suspect list")
    $ status.append("suspect list delivered")
    $ time.addMinutes(5)
    return

label AmlMerchantListDelivered:
    if "out of office" not in rauvin.status:
        "Přijde k tobě Rauvin s listem papíru v ruce."
        if "less deals checked" in status:
            $ rauvin.say("Mistr Njal ti tady posílá seznam jmen. Týká se to myslím těch podezřelých obchodů, které jsi prověřoval[a].")
        else:
            $ rauvin.say("Mistr Njal ti tady posílá nějaký seznam jmen.")
        if "AML" in lotte.asked:
            $ mc.say("Už ho možná nebudu potřebovat, ale díky.")
        else:
            $ mc.say("Výborně, díky.")
        if "less deals checked" not in status:
            "Rauvin povytáhne obočí."
            $ rauvin.say("O co vlastně jde?")
            $ mc.say("Mistr Njal má v poslední době zvláštní problémy s nákupy materiálu, tak jsem chtěl[a] prověřit, jestli to není snaha poškodit ševcovský cech jako celek. Njal mi slíbil seznam obchodníků, kteří mu odmítli něco prodat.")
            if "AML" in lotte.asked:
                $ rauvin.say("To rozhodně za prověření stojí. Co jsi zatím zjistil[a]?")
            else:
                $ rauvin.say("To rozhodně za prověření stojí. Můžu ten seznam rovnou předat našim lidem, ať se nezdržuješ obcházením většího množství lidí.")
        else:
            if "AML" in lotte.asked:
                $ rauvin.say("Co jsi zatím zjistil[a]?")
        if "AML" in lotte.asked:
            show mcPic at menuImage
            menu:
                "Podle Karstenovy ženy Lotte šlo o instrukce cechmistra Rumelina.":
                    hide mcPic
                    $ rauvin.say("Zmínila i jeho důvody?")
                    $ mc.say("Prý mělo jít o společné nákupy pro cech, ale moc tomu nevěřím. Vůbec to nesedí dohromady.")
                "Vlastně na tom ještě pracuji.":
                    hide mcPic
                    $ rauvin.say("V téhle věci určitě nedělej nic ukvapeného.")
        $ rauvin.say("Hlavně buď v pátrání diskrétní a informuj mě o pokroku. Nekalé obchody většinou vedou k bohatým a vlivným lidem.")
    else:
        "Přijde k tobě Solian s papírem v ruce."
        if "less deals checked" in status:
            $ solian.say("Chápu správně, že jsi otravoval[a] mistra Njala tím podezřením na změny v obchodech?", "angry")
            if "less deals" in solian.asked:
                $ solian.say("Neříkal jsem ti, že by to měl řešit především cech samotný?", "angry")
            show mcPic at menuImage
            menu:
                "Rauvin by to chtěl vyšetřit." if "less deals" in solian.asked:
                    hide mcPic
                    $ solian.say("Říká někdo, kdo ho zná dva dny. Rauvin by ti hlavně řekl, abys byl[a] opatrn[y] a nešlápnul někomu na kuří oko.", "angry")
                    $ solian.say("A především, Rauvin tu teď není a my ostatní musíme řešit nejdřív ty případy, na kterých záleží někomu důležitému. Jinak bychom taky mohli mít ještě míň lidí a zdrojů, než máme teď.")
                "Rauvin mě pověřil, ať to vyšetřím." if "less deals" not in solian.asked:
                    hide mcPic
                    $ solian.say("To je možné. A také ti určitě řekl, že máš být opatrn[y] a nešlápnout někomu na kuří oko.", "angry")
                    $ solian.say("A především, Rauvin tu teď není a my ostatní musíme řešit nejdřív ty případy, na kterých záleží někomu důležitému. Jinak bychom taky mohli mít ještě míň lidí a zdrojů, než máme teď.")
                "Mistr Njal mne požádal o pomoc.":
                    hide mcPic
                    "Solian se zamračí."
                    $ solian.say("Pak měl radši požádat hlídku jako celek.", "angry")
                    $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrn[y], abys proti hlídce nepoštval[a] někoho důležitého. Nebo abys nezanedbával[a] ztracené dílo mistra Heinricha.", "angry")
        else:
            $ solian.say("Mistr Njal ti tady posílá seznam jmen. Nechápu ale, jak to souvisí s krádeží u mistra Heinricha.", "angry")
            show mcPic at menuImage
            menu:
                "Vyšetřuji podezřelé změny v obchodech týkající se celého ševcovského cechu.":
                    hide mcPic
                    $ mc.say("Je možné, že ta krádež je součástí snahy poškodit celý cech.")
                    $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc. Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.", "angry")
                    show mcPic at menuImage
                    menu:
                        "Budu na to myslet.":
                            hide mcPic
                            "Solian kývne, podá ti list se jmény a vrátí se zas ke své práci."
                        "Pokud tu dochází ke zločinu, budu ho řešit.":
                            hide mcPic
                            $ solian.say("Hlavně buď opatrn[y] a nestrkej do ničeho zbytečně prsty.", "angry")
                "Nejspíš nijak, ale mistr Njal mne požádal o pomoc.":
                    hide mcPic
                    "Solian se zamračí."
                    $ solian.say("Pak měl radši požádat hlídku jako celek.", "angry")
                    $ solian.say("Jestli je to něco, na čem mistru Njalovi záleží, tak prosím. Ale i tak buď opatrn[y], abys proti hlídce nepoštval[a] někoho důležitého. Nebo abys nezanedbával[a] ztracené dílo mistra Heinricha.", "angry")
    $ status.remove("awaiting AML merchant list")
    $ status.append("AML merchant list delivered")
    $ time.addMinutes(5)
    return

label AmlCheckResult:
    if "out of office" not in rauvin.status:
        "Dojde k tobě Rauvin."
        $ rauvin.say("Vypadá to, že se změnou v obchodování ševcovských mistrů jsi měl[a] pravdu. Nechal jsem to prověřit a v ostatních hospodách to vypadá přesně stejně.")
        $ rauvin.say("Mistra Njala několik obchodníků odmítlo i jinde a mistra Rumelina nikdo neviděl nakupovat luxusní materiál, přestože ho podle všeho má a používá.")
        $ mc.say("Pokusím se zjistit, kdo za tím stojí.")
        "Rauvin krátce kývne."
        $ rauvin.say("Postupuj opatrně, a pokud něco zjistíš, určitě mi to nahlaš.")
    else:
        "Přijde k tobě Solian se zamračeným výrazem."
        $ solian.say("Jak jsi řešil[a] ty změny v obchodování...", "angry")
        $ mc.say("Přišlo mi to podezřelé, a tak jsem chtěl[a] vědět, jestli se to změnilo opravdu i v jiných hospodách než u Salmy.")
        $ solian.say("Nechali jsme to prověřit a mistra Njala prý opravdu několik obchodníků odmítlo i jinde. Ale...")
        $ mc.say("A co mistr Rumelin? Viděl ho někdo v poslední době nakupovat luxusní materiál?")
        $ solian.say("Pokud vím, tak ne. Ale souvisí to nějak s tvým případem?", "angry")
        $ mc.say("Mohlo by. Co kdyby krádež Heinrichových střevíců byla součást snahy poškodit nějak celý cech?")
        $ solian.say("Pak by to měl řešit především cech sám, případně požádat hlídku o pomoc. Nechceme vypadat, že se příliš vměšujeme do jejich záležitostí. Příliš ambiciózní hlídka by mohla naštvat vlivné lidi a to tady nemůžeme potřebovat.", "angry")
        show mcPic at menuImage
        menu:
            "Budu na to myslet.":
                hide mcPic
            "Pokud tu dochází ke zločinu, budu ho řešit.":
                hide mcPic
                $ solian.trust -= 1
                $ solian.say("Hlavně buď opatrn[y] a nestrkej do ničeho zbytečně prsty.", "angry")
        $ mc.say("V každém případě díky za ověření, že Salma měla pravdu.")
        "Solian jen kývne a vrátí se k vlastní práci."
        $ solian.asked.append("less deals")
    $ status.remove("investigating less deals")
    $ status.append("less deals checked")
    $ time.addMinutes(5)
    return

label zeranWitnessesChecked:
    if "out of office" not in rauvin.status:
        "Dojde za tebou Rauvin."
        $ rauvin.say("Nechal jsem prověřit Zeranovu práci v noc krádeže a nevidím v jeho výpovědi žádné nesrovnalosti.")
        $ rauvin.say("Janis ho na tu noc skutečně najal na čištění žump a do rána byla práce odvedená. Francek skutečně pracoval nedaleko a matně si vzpomíná, že Zerana v noci potkal, i když spolu nemluvili.")
    else:
        "Dojde za tebou Solian."
        $ solian.say("Jak jsi chtěl[a] prověřit Zeranovy údajné svědky, tak nejsou schopní říct nic konkrétního.")
        $ solian.say("Janis ho na tu noc opravdu najal na čištění žump a do rána byla práce odvedená, nic jiného neví. Francek skutečně pracoval poblíž a prý Zerana možná v noci potkal, ale nemluvili spolu.")
        $ mc.say("Takže jeho výpověď se potvrdila?")
        $ solian.say("Možná. Ale pevný důkaz to není. Francek si není úplně jistý a stejně není dost důvěryhodný, aby jen jeho slovo stačilo.")
        show mcPic at menuImage
        menu:
            "To je dobré vědět, díky.":
                hide mcPic
                "Solian kývne a vrátí se ke své práci."
            "Zajímá mě pravda, ne důvěryhodnost.":
                hide mcPic
                $ solian.trust -= 1
                $ solian.say("Tak zkus nezapomenout, že pravda pak musí ještě obstát u soudu.")
    $ status.remove("zeran witnesses")
    $ status.append("zeran witnesses checked")
    $ time.addMinutes(5)
    return

# player in trouble
label guarhouseHeinrichComplained:
    if "out of office" not in rauvin.status:
        $ status.append("heinrich complained")
        "Rauvin na tebe ještě z dálky mávne a ukáže směrem k té místnosti, ve které jsi dřív mluvil[a] s mistrem Heinrichem. Tváří se ještě vážněji než obvykle a už to samo o sobě tě dokáže znervóznit."
        scene bg interviewroom
        $ rauvin.say("Měl[a] bys vědět, že tady byl mistr Heinrich a stěžoval si na tebe.", "angry")
        $ heinrichComplaint = "Prý se k němu nechováš s dostatečným respektem"

        python:
            if "not reliable" in status:
                heinrichComplaint += ", nedá se na tebe spolehnout"
            if "alcoholic" in eckhard.asked or "alcoholic" in salma.asked or "alcoholic" in lisbeth.asked:
                heinrichComplaint += ", kladeš naprosto zbytečné otázky"
            if "secret lover" in victim.asked or "relationship" in victim.asked:
                heinrichComplaint += ", strkáš nos do věcí, do kterých ti nic není,"
            heinrichComplaint += " a měl[a] by sis víc hledět své práce."

        $ rauvin.say("%(heinrichComplaint)s.")
        if rauvin.trust > 4:
            $ rauvin.say("Já jsem s tebou zatím spokojený, ale i tak bych ti radil mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
        elif hayfa.trust > 4:
            $ rauvin.say("Hayfa je přesvědčená, že pro nás budeš cenná posila, ale tím spíš bych ti radil mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
        elif rauvin.trust < -4:
            $ rauvin.say("A abych byl upřímný, já sám s ním zatím musím spíš souhlasit. Čekal jsem od tebe výrazně lepší práci. Máš ještě čas s tím něco udělat, ale městská hlídka si potřebuje pověst zlepšit a ne ještě zbytečně provokovat vlivné mistry.")
        else:
            $ rauvin.say("Radil bych ti mistra Heinricha neprovokovat. Je to vážený muž a městská hlídka potřebuje dobrou pověst.")
    else:
        "Solian rázným krokem přijde až k tobě, popadne tě za paži a odvede tě do hloubi strážnice. Na krátký okamžik zaváháš, zda to má být zatčení, dojdete však pouze do místnosti, v níž jsi předtím mluvil[a] s Heinrichem."
        scene bg interviewroom
        $ solian.say("Byl tady mistr Heinrich. Jak se to k němu prosím tě chováš?", "angry")
        $ heinrichComplaint = "Prý vůbec nemáš respekt"

        python:
            if "not reliable" in status:
                heinrichComplaint += ", není na tebe spolehnutí"
            if "alcoholic" in eckhard.asked or "alcoholic" in salma.asked or "alcoholic" in lisbeth.asked:
                heinrichComplaint += ", ptáš se na úplné zbytečnosti"
            if "secret lover" in victim.asked or "relationship" in victim.asked:
                heinrichComplaint += ", strkáš nos do věcí, do kterých ti nic není,"
            heinrichComplaint += " a měl[a] by sis víc hledět své práce."

        $ solian.say("%(heinrichComplaint)s.")
        $ solian.say("Uvědomuješ si, že ten člověk si velmi dobře rozumí s purkmistrem a sám se možná za pár dní stane cechmistrem? Vážně chceš, aby zrovna on měl pocit, že nestojíme za nic a přesně tolik by nám město mělo platit?", "angry")
        $ solian.say("Tohle musíš nějak napravit. Zkus se mu omluvit nebo pro něj něco udělat, nebo pokud možno konečně najdi ty zatracené boty nebo aspoň toho, kdo mu je sebral. A hlavně si prosím dávej pořádný pozor na pusu.", "angry")
    $ status.append("victim expects apology")
    $ time.addMinutes(10)
    return

### Morning stand up
label firstStandUp:
    scene bg guardhouse
    $ rauvin.say("Myslím, že naši novou posilu už jste všichni viděli, ale pro pořádek - tohle je [mcName], vítej v hlídce. Chceš nám o sobě něco říct?")
    show mcPic at menuImage
    menu:
        "Jsem písař a tohle je po delší době práce, co vypadá slibně.":
            hide mcPic
            $ solian.say("Vypadá.")
            $ runa.say("Je to takové, jaké si to uděláš.", "happy")
        "Už mám první případ a rozhodně vás nezklamu!":
            hide mcPic
            $ runa.say("Tak ať ti to nadšení vydrží!", "happy")
        "Ani ne.":
            hide mcPic
            $ runa.say("Tak to z tebe budeme muset vytáhnout někdy v hospodě.", "happy")
    $ runa.say("Rádi tě tady vidíme.", "happy")
    $ melien.say("Konečně tu nejsem nejnovější, vítej!", "happy")
    $ solian.say("Hlavně nevymýšlej žádné přehnané novoty a bude to v pořádku.", "happy")
    $ rauvin.say("Další důležitou novinkou je, že po delší době máme ve sklepě vězně. Hayfo, tu holku jsi zatkla ty, o co šlo?")
    $ hayfa.say("Zkusila podpálit město.", "angry")
    $ hayfa.say("Prý komediantka. Prý to bylo bezpečné. To určitě. V každé ruce měla zapálený vějíř, mávala jimi na všechny strany a nakonec podpálila vůz. Musela to pak hasit spousta lidí.", "angry")
    $ rauvin.say("Takže svědků je dostatek?")
    $ hayfa.say("Víc než dost. Během dneška je oběhnu, pak ji předám soudu a co se mě týče, ještě před slavnostmi může viset.")
    $ runa.say("Opravdu je to tak jasné?")
    $ hayfa.say("Viděla jsem, co jsem viděla.", "angry")
    show mcPic at menuImage
    menu:
        "Já to viděl[a] také a tak jasné mi to nepřijde.":
            hide mcPic
            $ hayfa.trust -= 1
            $ rauvin.trust += 1
            $ solian.trust += 1
            $ hayfa.say("Cože? Jak tohle můžeš říct?", "angry")
            $ mc.say("Nejen můžu, ale musím, z víc důvodů.")
            $ rauvin.say("Tady vás zastavím, to nemusíme probírat teď. [callingMc.capitalize()], jestli k tomu máš co říct, je důležité to přednést soudu.")
            $ runa.say("[mcName.capitalize()] ale není z města, [pronounPossessive] slovo nebude mít takovou váhu.")
            $ rauvin.say("Každý svědek se počítá a je pak na městské radě, aby to při přelíčení všechno posoudila.")
            $ runa.say("Já jen připomínám, že bohatí svědci z města se počítají víc.")
            $ rauvin.say("Pravda, to asi bohužel pořád tak je. [callingMc.capitalize()], jestli znáš okolnosti, které mluví ve prospěch té dívky, postarej se, aby se to k soudu dostalo, pokud možno ústy někoho vlivného.")
            $ hayfa.say("Zbytečná práce.", "angry")
            $ rauvin.say("V nejhorším budeme vědět, že jsme nic nezanedbali. Možná pomůžeme někomu, kdo si trest nezaslouží, nebo se naopak ujistíme, že je trest na místě.")
            $ rauvin.say("A [mcName] se na tom zase něco naučí. Jen prosím nezapomínej ani na ty boty.")
            $ status.append("interested in Katrin")
        "Já to viděl[a] také a Hayfa má pravdu, ta holka nemůže vyváznout bez trestu.":
            hide mcPic
            $ hayfa.trust += 1
            "Runa přikývne."
        "{i}(neříct nic){/i}":
            hide mcPic
    $ rauvin.say("Tady jsme tedy dohodnutí a můžeme se pohnout dál.")
    $ rauvin.say("A teď jen rychle úkoly na dnešek, ať se na to můžeme vrhnout. Práce je spousta.")
    $ hayfa.say("Počkej ještě. Nejdřív něco mám.")
    $ rauvin.say("Ano?")
    $ hayfa.say("Potřebovala bych od zítřka na pár dní odjet.")
    $ rauvin.say("Mimo město? To ti přece soud zakázal.", "surprised")
    $ hayfa.say("Jen na rok, teď už zase můžu.")
    $ rauvin.say("To už je to tak dlouho? Nějak to letí.", "surprised")
    $ rauvin.say("Nepočká to až po slavnostech?")
    $ hayfa.say("Většinu jich stihnu a čekalo to už tak moc dlouho. Potřebuju se s někým vidět a dřív to nešlo, právě kvůli tomu soudu.")
    $ solian.say("S někým? Myslíš své zločinecké kamarády?", "angry")
    $ hayfa.say("Myslím lidi, na kterých mi záleží. Zkus si také někoho takového najít.", "angry")
    $ rauvin.say("Na tohle nemáme čas.", "angry")
    $ rauvin.say("Není žádný zákon, který by nám umožňoval tady Hayfu držet. Moc se mi nelíbí, že to volno chceš zrovna teď, ale budiž, napracováno máš.")
    $ rauvin.say("Jak dlouho jsi říkala?")
    $ hayfa.say("Dva nebo tři dny. Víc ne.")
    $ rauvin.say("To nějak zvládneme. Tak už snad můžeme k těm úkolům.")
    $ rauvin.say("Už to znáte. Slavnosti jsou za dva dny, přijíždějí na ně davy a my musíme zajistit, aby z toho nevzešly žádné potyčky.")
    $ rauvin.say("Lidé od bran by všechny měli nasměrovat, ale určitě se najde někdo, kdo si něco nezapamatuje.")
    $ rauvin.say("Hayfo, kromě zajišťování svědků pro soud s tou tanečnicí bych potřeboval, abys večer obešla hospody a zjistila, jestli se někdo nepokouší o falešnou hru. Čím dřív to zatneme, tím méně stížností se sejde. Stihneš to?")
    $ hayfa.say("Samozřejmě.")
    $ rauvin.say("Meliene, pro jistotu prosím obejdi město a připomeň všem zvenčí naše pravidla kolem ohně. Strážní u bran to všem budou po včerejšku klást na srdce obzvlášť důrazně, ale možná někdo přišel už dřív a pořádně si to neuvědomuje.")
    if "investigating less deals added" in status:
        $ rauvin.say("Kolik ti zbývá z toho ověřování ševcovských obchodů, o kterém jsme včera mluvili?")
        $ melien.say("Něco ještě ano, ale během dneška to určitě zvládnu.")
    $ melien.say("Oběhnu město jako blesk!", "happy")
    $ rauvin.say("Soliane, na radnici nás prosili o pomoc s hlídáním, že všichni obchodníci a komedianti najdou nějaké vhodné místo, kde si můžou rozložit věci, a že se u toho neporvou. Prosím, zajdi tam a domluv se, jak si to představují.")
    if "zeran witnesses added" in status:
        $ rauvin.say("A cestou se prosím zeptej Janise, jestli může potvrdit, že Zeran v noci opravdu pracoval. Tuhle noc i tu minulou.")
        $ solian.say("... a Zeran je...?")
        $ rauvin.say("Elf, který možná dělá potíže a možná také ne.")
    $ solian.say("Zajdu tam. Minule jsme slavnosti zvládli celkem bez potíží, teď by to nemělo být horší.")
    $ rauvin.say("Runo, máme tu první stížnost na komedianty - staré Irmtraud se nelíbilo, že jí vyvádějí pod oknem a nenechají ji spát. Sousedi se jí nezastali, a tak přišla za námi. Můžeš tam prosím zajít a zkusit to nějak urovnat?")
    $ runa.say("Chápu, kdo jiný má usměrnit starou ženskou než jiná stará ženská.", "happy")
    $ rauvin.say("Tak jsem to nemyslel… a nejsi stará!")
    $ runa.say("Oproti vám stará jsem a ty se přestaň červenat. Ráda tam zajdu.", "happy")
    if "interested in Katrin" in status:
        $ rauvin.say("A [callingMc], ty zkus najít svědky kolem té tanečnice, jak jsme se bavili. Zároveň ale také pokračuj s hledáním výrobku mistra Heinricha, ať ho na slavnostech můžou všichni ti návštěvníci obdivovat.")
    else:
        $ rauvin.say("A [callingMc], ty pokračuj s hledáním výrobku mistra Heinricha, ať ho na slavnostech můžou všichni ti návštěvníci obdivovat.")
    $ rauvin.say("A já budu tady a budu řešit všechny ty stížnosti, které nevyhnutelně přijdou.")
    $ time.addMinutes(15)
    return

label secondStandup:
    scene bg guardhouse
    "Na strážnici dorazíš s mírným zpožděním a čekáš, že ti to Rauvin určitě vyčte. U jeho stolu ale nikdo nesedí a shromáždění hlídkaři vypadají poměrně ustaraně."
    $ solian.say("No to je dost, že jsi tady. Už jsem se bál, že celé slavnosti budeme hlídat ve třech.", "angry")
    $ runa.say("Já jenom doufám, že se mu nic nestalo. Ten ještě nikdy nezaspal a pracoval, i když tehdy chytil tu chřipku.", "sad")
    $ melien.say("Vzal si vůbec někdy volno?", "surprised")
    $ runa.say("Co já vím, tak ne.")
    $ solian.say("V tom se s Hayfou našli.")
    $ melien.say("Nemám radši zaběhnout k jeho domu? Ať víme, co a jak?")
    $ runa.say("Možná radši ano?")
    $ solian.say("Ale nemusíme čekat, s čím se vrátíš. Přece se celá hlídka nezastaví jen kvůli jednomu šlechtici, co vyspává.")
    "Solian přejde k Rauvinovu stolu a vezme do ruky papíry, které tam zástupce velitele zanechal."
    $ solian.say("O tom, co se děje, mi samozřejmě nic neřekl. Ale předpokládám, že vám zadal podrobné úkoly na několik dní dopředu?")
    $ runa.say("Ne až tak podrobné, ale někde by tam měl být seznam stížností.")
    "Solian trpaslici podá jeden z papírů."
    $ runa.say("To je on. To je asi moje dnešní práce.")
    $ melien.say("Já na dnešek úkol nemám.")
    $ solian.say("Tak se jdi zeptat, jestli Rauvin včera chlastal, nebo co se to stalo, a dál uvidíme, co mezitím najdu v těch jeho lejstrech.", "angry")
    $ solian.say("[callingMc.capitalize()], ty pořád hledáš ty boty?")
    show mcPic at menuImage
    menu:
        "Už to skoro mám.":
            hide mcPic
        "Ano, ale docela se to zamotává.":
            hide mcPic
        "Hlavně jsme se věnoval[a] jiným věcem.":
            hide mcPic
    $ solian.say("Tak s tím pohni. Jestli nikoho nezatkneme zítra během dne, bude už nejspíš pozdě.", "angry")
    if "interested in Katrin" in status:
        $ solian.say("Hlavně se zbytečně nezdržuj nějakým zachraňováním žhářů. Souhlasím sice s tím, že o Hayfě je dobré mít zdravé pochyby, ale v první řadě musíme dát mistru Heinrichovi dobrou odpověď, až se na svoje boty přijde ptát.")
    $ solian.say("Tak do práce!")
    "S tím se Solian posadí za Rauvinův stůl a začne číst dokumenty, které tam našel. Melien vyběhne ze strážnice a Runa si vezme pár věcí a následuje ho."
    $ time.addMinutes(15)
    return

label thirdStandup:
    scene bg street01
    "Cesta na strážnici ti zabere o něco déle než obvykle, protože se musíš neustále někomu vyhýbat. Slavnosti jako takové začnou už večer, návštěvníci i místní obyvatelé tedy dokončují poslední přípravy: rozkládají stánky, nakupují potraviny na slavnostní pokrmy nebo prodávají hotová jídla do ruky."
    scene bg guardhouse
    "Na strážnici se brzy sejdete všichni čtyři - Hayfa je stále mimo město a Rauvin ani dnes nedorazil."
    $ solian.say("Dobré ráno, Rauvin podle všeho pořád vyspává, tak jdeme na to.")
    $ melien.say("Ráno jsem se tam stavil. Prý to je pořád stejné, hodně ho bolí hlava, vadí mu hluk i ostré světlo a bude muset ještě pár dní ležet. Ale aspoň se to snad nezhoršuje.")
    $ melien.say("Dostal na to od léčitele nějaké bylinky.")
    $ solian.say("Takže slavnosti jsou opravdu na nás. Nevadí, Rauvina jsme nepotřebovali před rokem, nepotřebujeme ho ani teď.")
    $ solian.say("Meliene, vezmi si zbroj a jdi se procházet po hlavním tržišti. Touhle dobou už by všichni měli vědět, kde že mají vyhrazené místo, ale stejně to určitě někdo zkazí a bude potřeba to řešit.")
    $ solian.say("A tvař se přitom výhrůžně, ať si nikdo nedovolí krást ani podvádět.")
    $ melien.say("Ale jestli mám chytat zloděje, půjde to mnohem snáz beze zbroje.")
    $ solian.say("S chytáním ti pomůže ta spousta dalších lidí na tržišti, ty tam jsi od dělání dojmu.")
    $ melien.say("No dobře… jen budu muset najít zbroj...", "sad")
    $ runa.say("Já ti s tím pomůžu.", "happy")
    $ melien.say("Děkuju!", "happy")
    $ solian.say("[callingMc.capitalize()], ty už konečně někoho zatkni za ty boty a sepiš podklady pro soud. Potom si taky vezmi zbroj a vystřídej Meliena. Meliene, ty potom přejdi na to Hayfino tajné sledování.")
    $ runa.say("Já myslím, že jsme [pronoun3] ještě žádnou zbroj nestihli dát.")
    $ solian.say("Jak to? To má být ten pořádek, který Rauvin chce ve všem mít?", "angry")
    $ melien.say("[mcName].capitalize()] od první chvíle pracuje na případu.")
    $ solian.say("Panenko skákavá. Tak Runo, až budeš hledat zbroj pro Meliena, připrav ještě jednu a [mcName] si ji tady pak vyzvedne.")
    $ solian.say("potom zajdi do cechu tesařů. Jejich tovaryši se včera poprali se skupinou kupců a je potřeba to urovnat. Cech je důležitý a jsme tu pro něj, ale zároveň nemůžeme působit jako město, kde nejsou obchodníci v bezpečí.")
    $ runa.say("Bez obav. Po hledání Melienovy zbroje tohle bude pohodička.", "happy")
    $ solian.say("Kdybys zjistila, že to je až moc složité a citlivé, dojdeme pro někoho z městské rady, ale nechci je zatěžovat, jestli to nebude nutné.")
    $ solian.say("Já budu muset na pár schůzek s různými úředníky a zástupci cechů, ale kdyby bylo potřeba něco řešit, nejsnáz budu k nalezení tady.")
    $ solian.say("Tak jdeme na to.")
    $ time.addMinutes(15)
    return

# things happening in the watch
label rauvinHealthReport:
    "Když vejdeš do dveří strážnice, málem se srazíš s Melienem, který zrovna vybíhá za nějakým dalším úkolem."
    $ melien.say("Promiň! Už jsi to slyšel[a]?", "surprised")
    $ mc.say("Co jsem měl[a] slyšet?")
    $ melien.say("Rauvin dnes nepřijde a dalších pár dní asi také ne. Je mu hrozně špatně.", "surprised")
    $ melien.say("On se přijít snažil, ale podle paní Luisy, to je jeho sestra, není schopný vstát z postele, a dokonce s tím po nějaké doby sám souhlasil. A tak teď leží a odpočívá.", "surprised")
    $ melien.say("Touhle dobou už by u něj měl být léčitel, ale nebyl u něj, než jsem odešel.")
    $ melien.say("Prý to začalo až během noci. Nebo možná pozdě večer? Včera ho přivedla domů Hayfa, vypadal prý trochu opilý a trochu unavený, ale nic hrozného. Tak ho paní Luisa poslala spát.")
    $ melien.say("A teď tohle. Doufám, že to není nic vážného...", "sad")
    show mcPic at menuImage
    menu:
        "Hayfa teď není ve městě, to je podezřelé.":
            hide mcPic
            $ melien.say("Myslíš… já nevím, to by přece neudělala. Navíc spolu docela vycházejí.", "surprised")
        "Mohl ho někdo otrávit? Velitel hlídky bude mít určitě spoustu nepřátel.":
            hide mcPic
            $ melien.say("Zatím jen zástupce, ale chápu, všichni ho už za velitele vlastně berou.")
            $ melien.say("Já nevím, otrávit někoho nebude tak jednoduché, ne? A jestli, léčitel to určitě pozná.")
            $ melien.say("A pak ať si nás ten travič nepřeje.", "angry")
        "To bude nějaká magie a to je vážné vždycky.":
            hide mcPic
            $ melien.say("Jestli to je magie, tak je Rauvin v těch nejlepších rukách. Paní Luisa je velmi schopný mág. Teda vlastně theurg, prý to je rozdíl.")
        "Nejspíš je jen přepracovaný.":
            hide mcPic
            $ melien.say("To bych se asi nedivil. Vážně si nepamatuju, že by někdy nepracoval, i kdyby jen na chvíli.")
            $ melien.say("Snad se z toho prostě vyspí.")
    $ melien.say("Asi bych tě už neměl zdržovat, máš určitě spoustu práce a já vlastně taky.")
    $ melien.say("Jen se asi připrav na to, že do slavností se budeme muset obejít bez něj. A bez Hayfy, takže tady asi velí Solian.")
    "Elf ti ještě krátce pokyne a odběhne za svými záležitostmi."
    $ status.append("Rauvin's health report")
    $ time.addMinutes(5)
    return

label nervousSolian:
    "Strážnicí prostupuje výrazný pocit nejistoty. Ačkoli se hlídkaři snaží plnit své každodenní povinnosti, často na sebe navzájem vrhají tázavé pohledy a pak je hned odvrací. Znepokojení je znát i z tichých rozhovorů, které občas zaslechneš."
    "Jakmile tě spatří Solian, pokyne ti, abys ho následoval do jedné z menších místností."
    scene bg interviewroom
    "Nesedne si, jen zavře a rovnou se začne vyptávat."
    $ solian.say("Jak postupuje tvůj případ? Slavnosti jsou skoro tady, potřebujeme někoho zatknout nejpozději zítra v poledne. Máme někoho?")

    label nervousSolianOptions:
    show mcPic at menuImage
    menu:
        "Neměl by se mnou tohle řešit Rauvin?" if "nervous - Rauvin" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Rauvin")
            $ solian.say("Měl, ale ten tady není a kdo ví, kdy se zase vrátí. Já ti budu muset stačit.", "angry")
            $ solian.say("Jestli se ti nelíbí, že mi všechno budeš muset vysvětlovat od začátku, můžeš si na něj stěžovat u velitele.", "angry")
            jump nervousSolianOptions
        "Co se stalo s Rauvinem?" if "nervous - Rauvin 2" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Rauvin 2")
            $ solian.say("To pořád ještě nikdo pořádně neví. Prostě tady není.", "angry")
            $ solian.say("Starají se o něj v hospici a je u něj jeho sestra, takže my se můžeme soustředit na naši práci.")
            jump nervousSolianOptions
        "Kam vlastně jela Hayfa?" if "nervous - Hayfa" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - Hayfa")
            $ solian.say("Nevím a nezajímá mě to. Pro mě je důležité zajistit, aby hlídka splnila svoje povinnosti, a to dokážeme i bez ní.", "angry")
            jump nervousSolianOptions
        "Proč to tak spěchá? Nemůžeme vyšetřovat ještě pár dní?" if "nervous - hurry" not in solian.asked:
            hide mcPic
            $ solian.asked.append("nervous - hurry")
            $ solian.trust -= 2
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ solian.say("Proč asi. Jestli začnou slavnosti a mistr Heinrich ani nebude mít výrobek, ani nebude probíhat soud za jeho krádež nebo zničení, bude všem pro smích. A tomu chceme zabránit.", "angry")
            jump nervousSolianOptions
        "Pořád nemám dokonale přesvědčivé důkazy.":
            hide mcpic
            $ solian.asked.append("nervous - no proof")
            $ soliansay("Na přesvědčivé důkazy už nemáme čas. Ty současné budou muset stačit.")
            $ mc.say("Rauvin ale vždycky říkal...")
            $ solian.say("Rauvin tady není. Jsme tady my a my s tím musíme něco provést. Takže koho můžeme zatknout?", "angry")
            $ mc.say("No, jestli ti stačí i částečné důkazy...")
        "Pachatele už naštěstí znám. Věřím, že mám dobré důkazy.":
            hide mcPic
            $ solian.say("No to je skvělá zpráva. Kdo to je?")

    show mcPic at menuImage
    menu:
        "...tak mně tedy ne." if "nervous - no proof" in solian.asked:
            hide mcPic
            $ rauvin.trust += 3
            $ hayfa.trust += 2
            $ solian.trust -= 2
            $ solian.say("A co tedy chceš dělat? Říct mistru Heinrichovi, že jsme to nezvládli?", "angry")
            $ mc.say("Lepší než zatknout někoho, proti komu nemáme dostatečné důkazy.")
            $ solian.say("V tom případě se běž vrátit k případu a koukej ty svoje dostatečné důkazy hodně rychle najít.", "angry")
            $ solian.say("Jestli mi do zítřejšího poledne nedokážeš říct, koho můžeme zatknout, bude to znamenat, že ses neosvědčil[a]. Určitě dokážeš domyslet, co to pro tvoje další působení v hlídce znamená.")
            show mcPic at menuImage
            menu:
                "Vynasnažím se.":
                    hide mcPic
                    $ solian.say("To je dobře. A teď už se nenech zdržovat.")
                "Co když se ty důkazy prostě nedají najít? Nemůžete mě přece vyhodit z hlídky kvůli jednomu případu.":
                    hide mcPic
                    $ solian.say("Věř tomu, že můžeme.", "angry")
                    $ solian.say("A teď už se nenech zdržovat.", "angry")
                "O tom, kdo zůstane v hlídce, ty přece nijak nerozhoduješ.":
                    hide mcPic
                    $ solian.trust -= 1
                    $ solian.say("Já jsem v hlídce dva roky. Ty dva nebo tři dny. Troufám si tvrdit, že rozumím lépe než ty tomu, jak to tady chodí.", "angry")
                    $ solian.say("Přijmi teď tedy mou dobrou radu a nenech se už zdržovat.", "angry")
        "Můžeme zatknout mistra Kaspara." if "confession" in kaspar.asked:
            hide mcPic
            $ solian.say("Jseš si jist[y]? Je to vážený mistr a navíc se možná bude ucházet o místo cechmistra. Musíme si být opravdu jistí, než ho z čehokoli obviníme.")
            $ mc.say("Sám se mi přiznal, že v dílně mistra Heinricha byl a že jeho boty zničit chtěl. Doufal, že ho tím znemožní právě před tou volbou cechmistra, do které se chtěli hlásit oba.")
            $ solian.say("To ale před soudem nezopakuje. Vždyť tím by znemožnil hlavně sám sebe. Je proti němu i jiný důkaz?", "angry")
            $ mc.say("Paní Lisbeth ho do té dílny sama pustila. Namluvil jí, že si boty chce jen prohlédnout.")
            $ solian.say("Tohle ale nemůžeme vzít k soudu. Uvědomuješ si, co by z toho bylo za řeči? To by popudilo nejen Kaspara a Heinricha, ale ve výsledku možná i Rumelina, protože by celý cech byl městu pro smích.", "angry")
            $ solian.say("Trochu času ještě zbývá. Najdi někoho jiného, na kom je dost silné podezření.")
            $ solian.say("Mistra Kaspara zatknout nemůžeme. Ostatně to, že v dílně byl, ještě neznamená, že s botami opravdu něco určitě provedl.", "angry")
        "Můžeme zatknout Gerda." if ("fired apprentices" in clues and "which apprentice" in liese.asked) or "workshop visit" in gerd.asked:
            hide mcPic
            $ mc.say("To je učedník mistra Njala, který byl dřív v učení u mistra Heinricha.")
            if "workshop visit" in gerd.asked:
                $ mc.say("Přiznal se, že v té dílně tu noc byl.")
            else:
                $ mc.say("Mám svědka, že byl tu noc v dílně.")
            $ solian.say("To je dobré! Ale proč by to dělal?", "surprised")
            $ mc.say("Protože ho Heinrich vyhodil. Sice mu k tomu dal na cestu zbytek peněz zaplacených za vyučení, ale stejně kolem toho určitě bylo hodně zlé krve.")
            $ mc.say("Navíc je Gerd pořádný drzoun, který chce mít vždy poslední slovo.")
            $ solian.say("Dobře, to by mělo obstát. Můžeš ho sebrat.", "happy")
            $ solian.say("Mistr Njal se sice bude vztekat, ale všichni ostatní jen mávnou rukou, že to je stejně jen podivínský trpaslík. To nás nemusí trápit.")
        "Můžeme zatknout mistra Njala s jeho učedníkem." if "workshop visit" in gerd.asked and "workshop visit" in njal.asked:
            hide mcPic
            $ solian.say("Mistra Njala? Je to sice podivínský trpaslík, ale na zatčení mistra potřebujeme hodně pádné důkazy.", "surprised")
            $ mc.say("Oba přiznali, že Gerd tu noc šel do Heinrichovy dílny na Njalův příkaz. Tvrdí, že si hlavně chtěli vzít zpátky střih, podle kterého jsou ty kradené boty ušité a které jim mistr Heinrich prý ukradl.")
            $ mc.say("Ale k čemu je brát mistru Heinrichovi střih, když už má hotové boty? Každý bude předpokládat, že ho má, a on ho podle nich může sestavit znovu.")
            $ mc.say("Mysleli si, že si jen zjednávají spravedlnost, kterou jim městské zákony nikdy nedají.")
            $ solian.say("A myslíš, že to samé budou říkat i před soudem?", "surprised")
            $ mc.say("Myslím, že ano. Oba o tom vypadali hodně přesvědčení.")
            $ solian.say("Nu dobrá. Je pravda, že mistru Heinricha to velmi potěší.")
            $ solian.say("Jen ještě poslední otázka, ví o tom cechmistr Rumelin?")
            if "police business" in njal.asked:
                $ mc.say("Částečně. Njal s ním o ukradeném střihu mluvil, ale o vloupání do dílny už ne, pokud vím.")
            else:
                $ mc.say("To nevím. Njal to neříkal a s Rumelinem jsem o tom nemluvil[a].")
            $ solian.say("V tom případě za ním zajdu, aby z toho soudu nebyl překvapený. Mohlo by ho to ukázat ve špatném světle.")
        "Můžeme zatknout Zerana." if zeranNote.isActive == True and zeran.status != "cleared":
            hide mcPic
            $ solian.say("To je kdo?")
            $ mc.say("Bývalý učedník mistra Heinricha. Mistr ho před několika měsíci vyhodil, protože měl podezření, že mu chodí za dcerou.")
            $ solian.say("Jo tenhle! O tom se ve městě hodně mluvilo. Takovéhle zneužití důvěry jsme tady už nějakou dobu neměli.")
            $ solian.say("Ten se určitě chtěl pomstít. Už jednou mistru Heinrichovi zkusil ublížit, taková verbež jako on to ráda zkusí znovu.")
            $ solian.say("To před soudem obstojí a mistr Heinrich bude spokojený.", "happy")
            $ solian.say("Běž ho rovnou zatknout.")
        "Můžeme zatknout žebračku Erle." if "stolen shoes found" in status:
            hide mcPic
            $ solian.say("A uvěří nám to někdo? Ta si nevezme víc peněz než na jídlo na den, i když jí je někdo dává. Proč by něco kradla?", "angry")
            $ mc.say("To nevím, ale měla u sebe lahve s vínem a pálenkou, které se mistru Heinrichovi ztratily také. Možná chtěla ukrást něco k pití a boty vzala z okamžitého nápadu, protože se jí prostě líbily.")
            $ mc.say("Krádež alkoholu si u ní představit dokážu. Co jiného by ji pořád drželo v tak povznesené náladě?")
            $ mc.say("A hlavně věděla, kde ty boty jsou.")
            $ solian.say("No, možná. Pořád se bojím, že by to u soudu mohlo vyvolat podezření. Ale jestli to nemohl udělat nikdo jiný, ona určitě ano.", "angry")
            $ solian.say("Zkus se zamyslet, jestli nenarazíš ještě na něco užitečného. A jestli ne, tak ji zítra seber.")
    $ solian.asked.append("case progress discussed")
    $ time.addMinutes(10)
    return

# people from the outside
label racismEncounter:
    $ racist.say("Kde si tady můžu stěžovat?", "angry")
    "Otočíš se za hlasem a spatříš menšího chlapíka v drahých barevných šatech, který si to rázuje k Rauvinovu stolu."
    $ racist.say("Právě mě okradli u brány! Chci okamžitou nápravu!", "angry")
    "Rauvin muži vyjde naproti a oba se zastaví přibližně uprostřed místnosti."
    $ rauvin.say("Pokud vás okradli, tak to samozřejmě vyšetříme. Co přesně se vám stalo?")
    $ racist.say("Tady to všechno máte sepsané. Naprostá nehoráznost! Co s tím uděláte?", "angry")
    "Rauvin si od druhého muže vezme list papíru a prostuduje ho."
    $ rauvin.say("To je potvrzení o zaplacení cla a vypadá v pořádku. Samozřejmě, pokud...")
    $ racist.say("Vám tohle přijde v pořádku? Vidíte tu částku? Vždyť to je zlodějina!", "angry")
    $ rauvin.say("Ano, takové clo je tu vyměřené.")
    "Muž v barevném oblečení se zamračí a udělá krok blíž k Rauvinovi. Ten zůstane stát na místě."
    $ racist.say("Možná pro lidi. Elfové ho budou mít tak poloviční.")
    # změna hudby
    "Na strážnici se náhle rozhostí napjaté ticho a všechny pohledy se stočí k obchodníkovi."
    $ rauvin.say("Clo je tu pro všechny stejně vysoké.")
    $ racist.say("Tomu tak věřím. Ten elfí parchant se na mně nakapsoval a vy ho teď kryjete. Máte z nich plné kalhoty, všichni lidi v hlídce.", "angry")
    $ rauvin.say("Nevím, co jste nepochopil. Elfové i lidi platí stejné clo a je to přesně tolik, co jste platil vy. Nikdo vás neokradl ani nepodvedl. Jestli se vám naše cla nelíbí, jeďte příště jinam.")
    $ racist.say("Nesmysly! Ale já to všem povím. Jak se nic nezměnilo. Jak se možná tváříte, kolik je v hlídce lidí, ale jak se třesete, aby si vás velitel nepodal. Jak...", "angry")
    $ rauvin.say("Můžu vám zařídit přijetí u Jeho Jasnosti barona.")
    $ racist.say("No to byste měl! Já mu to vyložím!")
    $ rauvin.say("Můžu vám zaručit, že ten to vezme naprosto vážně a že umí soudit velmi přísně.")
    $ racist.say("No to doufám. I když na můj vkus byl na povstalce až moc měkký. Doufám, že tady bude ráznější.", "happy")
    $ rauvin.say("Je velmi rázný. Obzvlášť u křivých obvinění. A ještě víc u křivých obvinění z útlaku jen kvůli tomu, jaké je kdo rasy.")
    $ rauvin.say("Jaký trest si myslíte, že by mohl za něco takového udělit?")
    $ racist.say("To… nevím? Ale… proč mluvíme o křivých obviněních, přece víte, jak to tu chodí.", "surprised")
    $ rauvin.say("Vím to velmi dobře. Sporů mezi lidmi a elfy už tu bylo dost a on je ve svém městě nestrpí. Nikdo z nás tu nestrpí jakékoli takové činy a jakákoli křivá obvinění z nich.")
    $ rauvin.say("Jestli trváte na svém obvinění, napíšu hned Jeho Jasnosti. Je hodně zaměstnaný na vévodském dvoře, ale kvůli tomuto přijede. Důkladně prověří celou hlídku a i vaše svědectví proti ní.")
    $ rauvin.say("A potom bude soudit. Přísně a rázně, jak jste doufal. Tak, aby dal příklad všem ostatním.")
    $ rauvin.say("Trváte na svém obvinění?")
    $ racist.say("No… možná přeci jen Jeho Jasnost barona nemusíme obtěžovat… Máte pravdu, že je hodně zaměstnaný, mělo mi to dojít hned...")
    $ rauvin.say("Dobrá.")
    $ rauvin.say("Pokud se někdy stanete obětí skutečného zločinu, prosím, obraťte se na nás, pokusíme se zjednat nápravu. To je poslání současné hlídky.")
    $ rauvin.say("Nyní už bych vás nerad zdržoval. Věřím, že se potřebujete věnovat svým obchodům.")
    "Obchodník se krátce rozhlédne a velmi rychle se ze strážnice vytratí. Hlídkaři v místnosti mlčky sledují pohledem nejdřív jeho a poté zavřené dveře, jež za ním zapadnou. Trvá několik dlouhých okamžiků, než první odvážlivec prolomí mlčení a ruch v místnosti se postupně obnoví."
    $ status.append("racism encounter")
    $ sceneWitnessed = True
    $ time.addMinutes(15)
    return

label kilianEncounter:
    $ kilian.rename("Kilian")
    "Zvenčí se ozve nesmělé zaklepání na dveře, tak slabé, že možná šlo jen o klam."
    $ rauvin.say("... a už je to tady.")
    "Hayfa dojde otevřít a venku skutečně nalezne asi dvanáctiletého kluka."
    $ hayfa.say("Vítej na strážnici městské hlídky Marendaru. Jsem Hayfa. S čím můžeme pomoct?")
    "Kluk při pohledu na ni ucukne o krok a kousne se do rtu. Pak se nadechne."
    $ kilian.say("Dobrý den. Já… můžu prosím mluvit s panem velitelem?", "surprised")
    $ hayfa.say("Velitel je zaneprázdněný, ale cokoli můžeš řešit rovnou se mnou. Když to bude potřeba, tak mu to předám.")
    $ kilian.say("Ale… a můžu aspoň dovnitř?", "sad")
    "Hayfa ustoupí ze dveří, pokyne mu hlavou a kluk vstoupí do místnosti. Nejistě se rozhlédne a udělá několik kroků směrem k Rauvinovi, ale přímo ho neosloví."
    $ kilian.say("Já... včera se stala taková nehoda. Nedorozumění. Všechno jsme dělali bezpečně, ale někoho to asi vylekalo a...")
    $ hayfa.say("Co kdybys začal od začátku? Jak se jmenuješ? Z které jsi čtvrti?")
    $ kilian.say("Jsem Kilian. Přišli jsme do města na slavnosti, naše stará… tam, kde jsme bydleli předtím, už být nemůžeme. Já a moje sestra. Potřebovali jsme peníze, a tak začala tančit a všem se to moc líbilo a házeli nám mince do čepice.")
    $ hayfa.say("A potom jste se pokusili zapálit město?", "angry")
    $ kilian.say("Ne! Nikdy jsme nic nezapálili!", "surprised")
    $ hayfa.say("Kromě toho vozu, chceš říct.", "angry")
    $ kilian.say("To bylo to nedorozumění! Už jsme takhle byli v jiných městech a nikdy nic nechytlo!", "surprised")
    $ hayfa.say("Tady jsme v Marendaru, shořel vůz a spousta lidí musela hasit.", "angry")
    $ kilian.say("Ale...", "sad")
    "Kluk vrhne prosebný pohled na Rauvina."
    $ rauvin.say("Nošení otevřeného ohně na ulici je v Marendaru zakázané.")
    $ hayfa.say("A žháře tu nikdo nestrpí.", "angry")
    $ kilian.say("To přece nebylo... my jsme jen chtěli potěšit publikum, my jsme nevěděli, že vám oheň tak vadí.", "surprised")
    $ rauvin.say("Jsem si jistý, že to městská rada zohlední.")
    $ rauvin.say("Ale pořád ještě jsi nepřednesl svou žádost nebo stížnost.")
    $ kilian.say("Já... nemůžete nás nechat prostě vypadnout z tohohle města a celého vévodství a už nikdy se nevracet?", "sad")
    $ hayfa.say("To má být vtip?", "angry")
    $ rauvin.say("Obvinění ze žhářství je příliš závažné a musí ho projednat soud, nejspíš ještě před začátkem slavností. Po něm a po provedení případného trestu samozřejmě budete volní.")
    $ kilian.say("Ale...", "sad")
    "Kluk nedopoví, otočí se na místě a vyběhne ven ze strážnice. Hlídkaři ho sledují, dokud se neztratí za nejbližším rohem."
    $ rauvin.say("Zvláštní. Čekal jsem, že ji aspoň bude chtít vidět, když jí hrozí poprava.")
    "Hayfa jen pokrčí rameny a dojde zavřít dveře."
    show mcPic at menuImage
    menu:
        "Poprava? Za tanec s ohněm?":
            hide mcPic
            $ hayfa.say("Co jiného bys dělal[a] se žhářkou?", "angry")
            $ mc.say("Většina komediantů nic podpalovat nechce. Většina z nich jenom předvádí čísla, která vypadají dobře. Kdyby chtěla založit požár, nebude to dělat před obecenstvem.")
            $ hayfa.say("Chtít mohla cokoli, ale ten požár opravdu málem způsobila.", "angry")
            $ rauvin.say("Po tom velkém požáru před dvěma lety jsou tady hodně přísné zákony kolem neopatrného nošení otevřeného ohně. Bojím se, že její představení pod to spadá.")
        "Otravují vás takhle zločinci často?":
            hide mcPic
            $ rauvin.trust -= 1
            $ hayfa.say("Většinou nemají tu drzost.", "angry")
            $ rauvin.say("Ještě o něm přece nevíme, jestli je zločinec. Ani o jeho sestře.")
            $ hayfa.say("Děláš si legraci?", "surprised")
            $ rauvin.say("Vůbec. On ani není z ničeho obviněný a o té komediantce teprve soud posoudí, jestli měla špatné úmysly, nebo jestli je opravdu jenom zdaleka a nic o Marendaru neví.")
            $ rauvin.say("A na tom, že se někdo přijde zeptat na příbuzného, není nic špatného a občas se to děje.")
            $ hayfa.say("... já vím, nemluvit zbytečně o požáru, protože se jinak pohádáme. Ale občas mě štveš.", "angry")
        "Nebyli jste na něj příliš tvrdí?":
            hide mcPic
            $ rauvin.say("Myslíš? Proč?")
            $ mc.say("Vždyť už na začátku byl hrozně vyděšený a teď musí být úplně zoufalý.")
            $ rauvin.say("Řekl jsem mu přece, že jeho důvody soud zohlední.")
            $ hayfa.say("A žháři si tvrdost zaslouží.", "angry")
            $ mc.say("Ale my ještě nevíme, jestli on nebo jeho sestra jsou žháři. Od toho přece bude ten soud.")
            $ mc.say("Ale tohle znělo, že soud bude sloužit jen jako veřejný spektákl, kde si na té holce všichni vylijí zlost.")
            $ rauvin.say("To jsem přece neřekl... vážně ti přijde, že to tak mohl pochopit?")
            $ mc.say("Jinak o tom nezačínám.")
            $ hayfa.say("Nechceme se radši vrátit k práci? Už jsme kvůli té holce ztratili času až moc.")
        "{i}(Neříct nic){/i}":
            hide mcPic
    $ status.append("Killian encounter")
    $ sceneWitnessed = True
    $ time.addMinutes(15)
    return

label hayfasPastEncounter:
    "Rauvin je právě zabraný do hovoru s jakousi dobře oblečenou ženou, kterou neznáš. Zatímco tvůj velitel se snaží působit klidně, jeho společnice ho probodává pohledem a mírně zvyšuje hlas."
    "Jiní hlídkaři se alespoň zdánlivě věnují své práci a do rozhovoru nezasahují, neujde ti ale, že většina z nich dobře poslouchá."
    $ rauvin.say("“Jak říkám, takové rozhodnutí je plně v kompetenci každého člena hlídky a Hayfa jím své pravomoce nijak nepřekročila.")
    $ angryWoman.say("Vy mě pořád nechápete. Když něco rozhodnete vy nebo kdokoli v téhle místnosti, tak dobře. Ale jak něco podobného můžete dovolit zrovna jí?", "angry")
    $ rauvin.say("Je to členka hlídky stejně jako všichni ostatní.")
    $ angryWoman.say("Není! Nikdo z vás ostatních se nepokusil zabít purkmistra!", "angry")
    $ rauvin.say("Za to byla souzená a potrestaná.")
    $ angryWoman.say("Potrestaná? Vždyť vyvázla s tím, že jen pár měsíců opravovala škody po požáru, a teď je najednou zřejmě skoro nejdůležitější v celé hlídce. Copak je tohle trest?", "surprised")
    $ rauvin.say("Pracovat bez nároku na odměnu vám připadá málo?")
    $ angryWoman.say("Kdyby zůstala u stavění domů, budiž. Ale pustit ji do hlídky?", "angry")
    $ angryWoman.say("Nezapomínejte, že přivandrovala kdo ví odkud a uctívá nějakého pochybného boha. Nikdo z nás nemůže tušit, co dalšího ještě plánuje.", "angry")
    $ rauvin.say("Naše zákony vstup do hlídky nikomu nezakazují a Hayfa mnohokrát prokázala jak schopnosti, tak lásku k městu.")
    $ angryWoman.say("A co vaše soudnost, ta vám nic neříká? Co když to všechno jen hraje? Vždyť tu je tak krátce, že ani nezažila požár, co ona o městě ví, aby ho mohla opravdu tak milovat?", "angry")
    $ rauvin.say("Zřejmě dost na to, aby pro hlídku byla neocenitelná.")
    $ rauvin.say("Podívejte, rozhodnutí soudu ani jeden z nás nemůže zvrátit. Hayfina služba městu teď je příkladná. A snad vás může ubezpečit, že vzhledem k její minulosti je vyloučené, aby v hlídce získala výrazně vyšší postavení, než má teď.")
    $ rauvin.say("Nicméně aby mohla městu co nejlépe sloužit, potřebuji pomoc i od vás.")
    $ rauvin.say("Jestli se začne podezřele, potřebuji to hned vědět. A dokud dělá přesně to, co se od hlídkařů očekává, potřebuji naopak, abyste to od ní přijímala stejně jako od libovolného jiného hlídkaře.")
    $ angryWoman.say("... já jen doufám, že neděláte chybu, které budeme všichni litovat.", "sad")
    $ rauvin.say("“Já věřím tomu, že kdyby měla opravdu nekalé úmysly, odešla by do města, kde ji nikdo nezná, a nezůstala by tady, kde už byla souzená a kde všichni znají její tvář.")
    $ rauvin.say("Je tu ještě něco, s čím vám může hlídka pomoci?")
    "Žena si povzdychne."
    $ angryWoman.say("... asi ne. Budu spoléhat na váš úsudek. Ostatně město vám věří, že hlídku dokážete vést správně. Snad víte, co děláte.")
    "S tím se žena rozloučí a vyjde ven ze strážnice. Rauvin jí otevře dveře a chvíli za ní hledí."
    "Když se otočí zpět do místnosti, zůstává na jeho tváři stále stopa zmatení a možná únavy, kterou ale brzy opět vystřídá věcná přímost, na kterou jste od něj zvyklí."
    $ rauvin.say("Kde jsme to byli. Jak pokračujete se svojí prací? Objevilo se mezitím něco, co se mnou někdo potřebujete probrat?")
    $ globalClues.append("hayfa's past")
    $ globalClues.append("Hayfa's arrival to Marendar")
    $ status.append("Hayfa's past encounter")
    $ sceneWitnessed = True
    $ time.addMinutes(15)
    return
