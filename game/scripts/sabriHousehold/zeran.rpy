label zeranController:
    $ origAsked = zeran.asked.copy()
    if zeran in cells:
        call zeranCellsIntro
    elif zeran.alreadyMet == False:
        $ zeran.alreadyMet = True
        call zeranFirst
    else:
        call zeranAgain
    if leaveOption != "none" and "arrest in progress" not in status:
        call zeranOptions

    # adjust time spent
    $ lastSpokenWith = "zeran"
    $ time.addMinutes((len(zeran.asked) - len(origAsked)) * 3)
    return

label zeranFirst:
    $ mc.say("Ty jsi Zeran? Bývalý učedník mistra Heinricha?")
    "Elf si tě změří pohledem."
    $ zeran.say("Jo. A ty sem očividně nepatříš. Kdo tě sem poslal a proč?", "angry")
    $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v mistrově dílně.")
    $ zeran.say("Aha, chápu, takže mě teď jdete zatknout.", "angry")

    show mcPic at menuImage
    menu:
        "Přiznáváš se?":
            hide mcPic
            $ zeran.trust -= 1
            $ zeran.say("Ne. Ani pořádně nevím, o co jde. Záleží na tom?")
            $ zeran.say("Můžete mě rovnou sebrat, Heinrich si určitě vzpomene, že mě tam vlastně viděl, a ty budeš mít padla.")
            call zeranMistrust
        "Ne, proč bych tě měl[a] hned zatýkat? Zatím probíhá vyšetřování.":
            call zeranTooSoonToArrest
        "Co kdybys mé úmysly začal soudit po víc než pár větách?":
            hide mcPic
            $ zeran.say("Se spravedlností v tomhle městě mám nějaké zkušenosti. Ale dobře, třeba jsi černá ovce, bílá vrána a člověk bez předsudků. Tak se ptej.")
        "Naopak, doufal[a] jsem, že v tobě najdu korunního svědka proti Heinrichovi." :
            call zeranWitnessAgainstHeinrich
    return

label zeranAgain:
    $ zeran.say("Vida, opět návštěva z hlídky. O Heinrichových botách pořád nic nevím a ten kašpar mě pořád nezajímá, ale jinak jsem k službám.")
    return

label zeranCellsIntro:
    python:
        currentOffense = zeran.arrestReason[-1]

    "Zerana najdeš, jak se vestoje a se založenýma rukama opírá o nejvzdálenější stěnu cely. Když tě uvidí, vrhne na tebe vyzývavý pohled, ale zůstane na místě."
    if "Zeran seen in cells" in status:
        $ zeran.say("Tak co zásadního neseš tentokrát?", "angry")
    else:
        $ zeran.say("Tak co, při[sel] jsi mě pustit, nebo to chceš dotáhnout až k soudu?")
        $ status.append("Zeran seen in cells")

        show mcPic at menuImage
        menu:
            "Tou drzostí si to děláš jenom horší." if currentOffense == "vagrancy":
                hide mcPic
                $ zeran.say("Jaká drzost? Řekl jsem, co si o hlídce myslím, a ty jsi v zápětí dokázal[a], že jsem měl pravdu.")
                $ mc.say("Kdybys měl trochu úcty, nic se ti nestalo.")
                $ zeran.say("Kdyby ses choval[a] jinak, možná bych měl důvod pro trochu úcty.")
            "Co uděláš, aby ses dostal ven?":
                hide mcPic
                $ zeran.say("No ty se překonáváš. A co si myslíš, že nuzák jako já může mít užitečného?")
                show mcPic at menuImage
                menu:
                    "Budeš mi dlužit službičku.":
                        hide mcPic
                        $ zeran.say("Mám protinávrh. Službičku budeš dlužit ty mně, pokud o tomhle návrhu nikomu neřeknu.")
                        $ zeran.say("Nebo můžeš začít vysvětlovat, proč si hlídka zkouší budovat svou vlastní bandu nohsledů, o kterých ani nikomu neříká. Navíc pomocí vydírání.")
                        $ mc.say("A myslíš, že ti to někdo uvěří? S tvojí pověstí?")
                        $ zeran.say("Je tvoje pověst o tolik lepší? Nebo pověst hlídky, po tom, k čemu ji zneužíval Velin a jak dlouho?")
                        $ zeran.say("Volba je na tobě.")
                        "Zeran se otočí zády k tobě, začne si ostentativně pohvizdovat a na další pokusy o komunikaci nereaguje."
                    "Odpros.":
                        hide mcPic
                        $ zeran.say("Poníženě se omlouvám, že jsem hned nepoznal, jaký jste arogantní pitomec. Chápu, že muset to každému dokazovat je pro vás obrovská námaha a oběť.")
                        $ zeran.say("Mohl byste mi prokázat tu obrovskou laskavost a vypadnout?")
                $ leaveOption = "none"
            "Při[sel] jsem ti pomoct.":
                hide mcPic
                $ zeran.say("A to mi tvrdíš poté, co jsi mě zatkl[a] bez pořádného důvodu? Nebuď směšn[y].")
            "Chci se jen na pár věcí zeptat.":
                hide mcPic
                $ zeran.say("Jsem teď velmi zaměstnaný, ale když to musí být, sem s tím.")
    return

label zeranOptions:
    call zeranOptionsRemainingCheck
    if zeranOptionsRemaining == 0:
        $ mc.say("To jsou všechny moje otázky.")
        if zeran.status == "got money":
            $ zeran.say("V tom případě hodně štěstí v pátrání. Kdybys mě tu příště nena[sel], nejspíš jsem na cestě do Eppenhahnu. Nebo do Seewachtu. Prostě někam daleko.", "happy")
        else:
            $ zeran.say("V tom případě přeji hodně štěstí ve tvém náročném pátrání. Jestli budeš mít štěstí, možná s tebou Heinrich ani nevytře podlahu, jak má ve zvyku.")
        return

    show mcPic at menuImage
    menu:
        "S tebou se nedá bavit, zase půjdu." if zeran in cells:
            hide mcPic
            return
        "Víš vůbec, co ti hrozí za trest?" if zeran in cells and punishment not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("punishment")
            if currentOffense == "vagrancy":
                $ zeran.say("Za potulku se, pokud vím, dává pranýř. Na to se docela těším. Budu moct všem povědět, že se hlídka v ničem nezměnila.")
                $ mc.say("Nezapomeň ještě na znevažování hlídky a překážení v její práci.")
                $ zeran.say("Pravda. Ještě přidám, co hlídka dělá, místo aby vyšetřovala skutečný zločin.")
                $ zeran.say("Jestli tedy to, že Heinrich někde ztratil boty, vůbec byl zločin, a ne jenom vrchol hlouposti.")
            else:
                $ zeran.say("Za něco, co jsem neudělal?")
                $ mc.say("A neříkal jsi snad, že tě mám rovnou sebrat, protože u tebe se nikdo nebude na nic ptát?")
                $ zeran.say("...")
                $ zeran.say("Možná jsem trochu přeháněl. Teď se tady všichni ohání spravedlností a novými zákony, on by se snad někdo trochu víc zajímal.")
                if currentOffense == "stolen shoes":
                    $ mc.say("A k čemu podle tebe dojdou?")
                    $ mc.say("Máš důvod se Heinrichovi mstít, znáš jeho dílnu, klíč jsi klidně mohl sebrat už dávno, potřebuješ peníze a tyhle boty půjdou dobře prodat.")
                    $ zeran.say("... neříkej, že si vážně myslíš, že jsem to udělal.", "surprised")
                    $ mc.say("Proč bych si to neměl[a] myslet?")
                    $ zeran.say("Protože jsem byl celou noc úplně jinde? Vydělával jsem si aspoň na placku k obědu.")
                    if "alibi" in zeran.asked:
                        $ zeran.say("Jak už jsem ti říkal.", "angry")
                    if "work" not in zeran.asked:
                        $ mc.say("A co to bylo za práci?")
                        $ zeran.say("Vybíral jsem žumpy. Co jiného by mě tak asi nechali dělat.")
                    show mcPic at menuImage
                    menu:
                        "To mi nenamluvíš.":
                            hide mcPic
                            $ zeran.say("Tak se zeptej Sabriho. Nebo Janise, který mě na to najal.")
                        "Dobře, nechám to ověřit.":
                            hide mcPic
                            $ zeran.say("To ti žádný čas nezabere, stačí zajít za Sabrim a ten to potvrdí. Nebo Janis, který mě na to najal.")
        "Napadá tě, kdo by mohl chtít mistra Heinricha poškodit?" if "Heinrich enemies" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("Heinrich enemies")
            $ zeran.say("Jeho? Kdokoli soudný, kdo s ním kdy přišel do styku. Ale opravdu by to udělal spíš někdo s jeho postavením nebo výš, nikomu jinému by to neprošlo.")
        "Jaký byl tvůj vztah s Heinrichovou dcerou?" if "Ada" not in zeran.asked and "Zeran offense" in clues:
            hide mcPic
            $ zeran.asked.append("Ada")
            $ zeran.say("Rozhodně ne takový, jak si Heinrich a všichni kolem něj myslí. Ale komukoli to vysvětlovat je ztráta času, tak si asi myslete, co chcete.")
            $ clues.append("Zeran innocent")
        "Nechci si na tvůj vztah s Adou dělat názor, dokud si neposlechnu tvou stranu." if "Ada" in zeran.asked and "Ada 2" not in zeran.asked:
            hide mcPic
            call zeranRelationshipWithAda
        "Ada taky říkala, že ji nikdo neposlouchá. Já si vás oba poslechnout chci." if "Ada" in zeran.asked and "Zeran" in ada.asked and "Ada 2" not in zeran.asked:
            hide mcPic
            $ zeran.say("Tak to jsi první. Heinrich ani Lisbeth to nikdy pořádně nezkoušeli.")
            call zeranRelationshipWithAda
        "Tušíš, s kým jiným mohla mít Ada vztah?" if "Ada 2" in zeran.asked and "Ada relationship" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("Ada relationship")
            $ zeran.say("To mohl být kdekdo. Asi nějaký elf a asi ne moc starý.")
            $ zeran.say("Rád bych řekl, že ji může okouzlit jen někdo chytrý a dobře vychovaný, ale trochu se bojím, že stačí říct “Amadis” a ona půjde do mdlob.")
            $ zeran.say("Takže nejspíš nějaký romantický pozér.")
            $ zeran.say("Co mě napadá, občas byla hodně otrávená z toho, k jak nudnému životu se ji rodiče snaží dotlačit. Asi by mohla skočit i po někom, kdo jí dá představu dobrodružství nebo jenom změny. Nebo vlastní volby.")
            $ zeran.say("Ale komedianti by jí spíš nepsali dlouhodobě dopisy, takže jsme zpátky u těch romantických pozérů.")
        "Chtěl bych tě očistit. Víš, jak to udělat?" if "clear your name" not in zeran.asked and gender == "M":
            call clearZeransName
        "Chtěla bych tě očistit. Víš, jak to udělat?" if "clear your name" not in zeran.asked and gender == "F":
            call clearZeransName
        "Kdy jsi naposledy viděl mistra Heinricha?" if "last seen Heinrich" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("last seen Heinrich")
            $ zeran.say("Zkusil jsem za ním zajít krátce po tom, co mě vyhodil. On ale zrovna něco řešil s Eckhardem, bavili se o nějakém střihu a kdo to zvládne ušít nejlíp. Heinrich se rozčiloval, jak on to má ve zvyku. Že přece nebude dělat cizí střih. Tak ať nedělá, ne? Kdo ho nutil?")
            $ zeran.say("Tak jsem aspoň našel Lisbeth, ale ta mě jenom seřvala a vyhodila z domu.")
            $ zeran.say("Znova už jsem tam jít nezkoušel a dělat to nebudu.", "angry")
        "Kde jsi byl včera v noci?" if "alibi" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("alibi")
            $ zeran.say("Nedaleko západní brány, tak nějak mezi ulicemi provazníků a brašnářů.")
            $ mc.say("Celou noc?")
            $ zeran.say("Většinu. Spát jsem šel nad ránem.")
            $ mc.say("Co jsi tam dělal?")
            $ zeran.say("Pracoval.")
        "Co to bylo za práci, takhle v noci?" if "alibi" in zeran.asked and "work" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("work")
            $ zeran.say("Čistil jsem žumpy, aby řádní měšťani měli pocit, že v jejich domově nic nesmrdí.")
            $ zeran.say("Práce snů, ale nikde jinde mě nezaměstnají a aspoň při tom jeden nikoho nepotká.")
        "Může ti to někdo dosvědčit?" if "alibi" in zeran.asked and "alibi witnesses" not in zeran.asked and zeran not in cells:
            hide mcPic
            $ zeran.asked.append("alibi witnesses")
            $ zeran.say("Určitě Sabri. Nebo Janis, ten mě na tu práci najal. A potom Francek, samozřejmě, ten pracoval od provaznické ulice na druhou stranu.")
            $ mc.say("Potkali jste se přímo při práci? A je někdo další, kdo tě tam přímo v noci viděl?")
            $ zeran.say("Čas od času jsme na sebe narazili. A pak se pár lidí vracelo z hospody a tak, ale ti se vždy jenom ujistili, že je nechci přepadnout, a pak si mě nevšímali. To je pro tuhle práci dost výrazný znak, že si vás nikdo radši nevšímá.")
        "Kdo na tebe během práce dohlíží?" if "alibi" in zeran.asked and "alibi witnesses" not in zeran.asked and zeran in cells:
            hide mcPic
            $ zeran.asked.append("alibi witnesses")
            $ zeran.say("Kdybych ráno nebylo všechno v pořádku, někdo by byl hodně naštvaný a Janis by si to se mnou pěkně rychle vyřídil. To je ten nejlepší možný dohled.", "angry")
            $ mc.say("Ale přímo v noci tam s tebou není nikdo, kdo by dosvědčil, že sis na hodinu neodskočil a nedokončil to potom?")
            $ zeran.say("Jestli se ptáte, jestli za mnou pan ctihodný městský úředník celou noc běhá, tak kupodivu ne.")
            $ zeran.say("Občas se potkávám s Franckem, ten pracuje na tom samém v ulicích vedle.")
            $ mc.say("Dost často na to, aby dosvědčil, že jsi návštěvu v dílně nemohl stihnout?")
            $ zeran.say("Nevím, možná? Co to je vůbec za otázku? Kdo dosvědčí tobě, že jsi tam nebyl ty? Kdo to dosvědčí vašemu veliteli nebo náhodnému spratkovi z protější ulice? Jestli sis nevšiml, v noci většinou všichni spí a to se pak svědčí těžko.", "angry")
            show mcPic at menuImage
            menu:
                "Oni neměli důvod se Heinrichovi mstít. Ty ano.":
                    hide mcPic
                    $ zeran.say("Důvod mstít se Heinrichovi má půlka města, s tím, kolik si o sobě myslí a jak se za všechno hned naštve.", "angry")
                "Nerozčiluj se, jen sbírám vodítka.":
                    hide mcPic
                    $ zeran.say("Tak je jdi sbírat k někomu, kdo Heinricha v posledním měsíci aspoň viděl.", "angry")
            $ zeran.say("To vám nedochází, že mě ten hlupák nezajímá a chci od něj mít pokoj?", "angry")
            $ zeran.say("Jeden by myslel, že když mě vyhodil a okradl, bude to stačit, ale ne, on mi musí pořád kazit život jenom tím, že jsem ho dřív znal.", "angry")
            $ zeran.asked.append("theft mention")
        "Počkej, co tím myslíš, že tě okradl?" if "theft mention" in zeran.asked and "victim of theft" not in zeran.asked:
            hide mcPic
            $ zeran.say("Byl[a] jsi někdy v učení?")
            $ mc.say("No... vlastně ne. Jít do učení bez peněz se nedá a ty já neměl[a].")
            $ zeran.say("Jo. Přesně. A jestli si myslíš, že zrovna Heinrich mě přijal jen z dobroty srdce, tak ne.", "angry")
            $ zeran.say("Stálo mě to v podstatě všechny peníze, co mi zbyly po rodičích.", "sad")
            $ zeran.say("A můžeš hádat, jestli mi něco z toho vrátil, jak by správně měl. Takže teď ani nejsem vyučený, ani nemám peníze. Ale zajímá to někoho?", "angry")
            label zeranVictimOfTheftReaction:
            show mcPic at menuImage
            menu:
                "To by rozhodně mělo!" if "theft should matter" in zeran.asked:
                    hide mcPic
                    $ zeran.asked.append("theft should matter")
                    $ zeran.say("Mělo, ale očividně nezajímá.", "angry")
                    jump zeranVictimOfTheftReaction
                "Byl jsi s tím za hlídkou?" if "asked watch for help" not in zeran.asked:
                    hide mcPic
                    $ zeran.asked.append("asked watch for help")
                    $ zeran.say("Byl jsem s tím za pár lidmi a všichni se mi vysmáli, že si za to můžu sám. U soudu by mě nikdo neposlouchal a jen by mi přišili trest navíc.", "angry")
                    jump zeranVictimOfTheftReaction
                "Mě to rozhodně zajímá.":
                    hide mcPic
                    $ zeran.say("A co s tím uděláš?")
                    if "asked watch for help" not in zeran.asked:
                        $ zeran.say("Jestli s tím půjdeš za Heinrichem, tak se ti jen vysměje, a soud by mi jen přišil trest navíc.", "sad")
                    show mcPic at menuImage
                    menu:
                        "Máš pravdu, asi s tím nic nezmůžu.":
                            hide mcPic
                            $ zeran.say("Tak se vraťme k tomu opravdu důležitému zločinu, ať odtud můžeš vypadnout.", "angry")
                        "Pokusím se něco vymyslet.":
                            hide mcPic
                            $ zeran.say("No to jsem teda zvědavý.")
                            $ globalStatus.append("promised Zeran help")
                "S tím asi nic neuděláme.":
                    hide mcPic
                    $ zeran.say("Neuděláme. Přeci jen, jsi jenom z hlídky, řešení zločinů není tvoje práce.", "angry")
                "Jsou důležitější zločiny, kterým je potřeba se věnovat.":
                    hide mcPic
                    $ zeran.say("Samozřejmě, jako třeba ukradené boty.", "angry")
                    $ mc.say("Mistrovský výrobek na Einionovy slavnosti je přece důležitý.")
                    $ zeran.say("A hlavně je důležitý Heinrich a jeho uražená ješitnost. Mnohem víc než to, jestli já budu mít, co jíst.", "angry")
        "Napsal bys mi jména těch, za kým můžu dojít?" if "alibi witnesses" in zeran.asked and "letters for Ada seen" in status and "Zeran writing sample" not in status:
            hide mcPic
            $ zeran.say("To si nezvládnete zapamatovat tři jména? Vlastně dvě, Sabriho si asi pamatovat musíte, když jste sem zvládl[a] dojít.")
            $ mc.say("Nejsi jediný, s kým mluvím. Podobných ověřování mám spoustu.")
            "Zeran pokrčí rameny, nechá si podat psací potřeby a napíše na něj dvě jména."
            show sh zeran note at truecenter
            pause
            hide sh zeran note
            $ status.append("Zeran writing sample")
        "Mohl bys mi něco napsat, jen jako ukázku, jak píšeš?" if "letters for Ada seen" in status and "Zeran writing sample" not in status and "writing sample" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("writing sample")
            $ zeran.say("Cože? K čemu by ti to bylo?", "surprised")
            show mcPic at menuImage
            menu:
                "Potřebuji ověřit, jestli jsi autorem nějakých textů.":
                    hide mcPic
                    $ zeran.say("Jenom podle písma? Tomu někdo uvěří?", "surprised")
                    $ zeran.say("Nebo chceš to písmo napodobit a pak na mě něco hodit?", "angry")
                    $ zeran.say("Ale pro mě za mě... Těžko tím můžu něco ztratit.")
                    "Zeran si nechá podat psací potřeby, napíše pár slov a vše ti opět vrátí."
                    show expression "sh zeran sample [gender].png"
                    pause
                    hide expression "sh zeran sample [gender].png"
                    $ status.append("Zeran writing sample")
                "Jsem původně písař a baví mě sbírat rukopisy.":
                    $ zeran.asked.append("writing sample refused")
                    hide mcpic
                    $ zeran.trust -= 1
                    $ zeran.say("To se mi snažíš vysmívat, nebo co? Nemáš náhodou spoustu nesmírně důležité práce?", "angry")
                    $ zeran.say("Jestli potřebuješ vědět něco souvisejícího s vyšetřováním, tak to vyklop. Jinak nás oba prosím přestaň zdržovat.", "angry")
        "Potřebuji ověřit, jestli jsi autorem nějakých textů." if "writing sample refused" in zeran.asked and "Zeran writing sample" not in status:
            hide mcPic
            $ zeran.say("Jenom podle písma? Tomu někdo uvěří?", "surprised")
            $ zeran.say("Nebo chceš to písmo napodobit a pak na mě něco hodit?", "angry")
            $ zeran.say("Ale pro mě za mě... Těžko tím můžu něco ztratit.")
            "Zeran si nechá podat psací potřeby, napíše pár slov a vše ti opět vrátí."
            show expression "sh zeran sample [gender].png"
            pause
            hide expression "sh zeran sample [gender].png"
            $ status.append("Zeran writing sample")
        "Myslím, že bys měl dobrý důvod chtít mistra Heinricha na slavnostech znemožnit." if "motive" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("motive")
            $ zeran.say("Ten se znemožňuje každodenně jen tím, jak se chová.", "angry")
            $ zeran.say("Ale teď trochu nechápu, měl jsem ho znemožnit, nebo okrást?")
            $ mc.say("Znemožnit krádeží jeho výrobku na Einionovy slavnosti.")
            $ zeran.say("Jo ono se ztratilo… no páni. To jsem nečekal.", "surprised")
            $ zeran.say("Úplně vidím Heinrichův výraz. Ten musí tak krásně zuřit.", "happy")
            $ zeran.say("Jak to ten zloděj vlastně poznal, že z té spousty bot bere zrovna ty pro Einiona?")
            show mcPic at menuImage
            menu:
                "Mistr Heinrich se prý všude chlubil, jak jsou tyhle boty zvláštní.":
                    hide mcPic
                    $ zeran.say("Všude možná, ale ne přede mnou.")
                "To je součást vyšetřování.":
                    hide mcPic
                    $ zeran.say("Aha… s tím bohužel nemůžu pomoct, o Heinrichově výrobku nic nevím.")
            $ zeran.say("Se mnou se teď skoro nikdo nestýká, tak se ke mně tyhle drby nemají jak dostat. Ne že by mi to chybělo.")
            $ zeran.say("Takže kdokoli jiný z cechu a širokého okolí mohl vědět, jaké boty ukrást a kdy, ale já opravdu ne.")
        "Jak to vypadá v Heinrichově domácnosti?" if "Heinrich household" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("Heinrich household")
            $ zeran.say("Proč se na tohle ptáte mě? Jestli jsme si nevšiml[a], já v tom domě už měsíc nežiju.")
            $ mc.say("Právě proto. Můžeš mi říct skutečné dojmy a nebát se, že někoho urazíš.")
            "Zeran pokrčí rameny."
            $ zeran.say("To je pravda. Co mi teď ještě může Heinrich udělat?")
            $ zeran.say("Všichni v jeho domě se před ním třesou. Myslím, že Aachim nejvíc, i malá Ada má víc odvahy než on. Ale o Adu se Heinrich vlastně nezajímá, zatímco v Aachimovi vidí budoucnost svého jména a své dílny.")
            $ zeran.say("My učedníci jsme vždycky byli jenom pracovní síla, která si ještě platí za to privilegium. Rudimu to snad i vyhovovalo.")
            $ zeran.say("A Lisbeth se možná tváří, že jí na nás záleží, ale že by se za nás i postavila, to zase ne. Hlavně aby si mohla myslet, jak má dokonalou domácnost.")
        "Proč sis nenašel jiného mistra a nedokončil učení?" if "why not finish apprenticeship" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("why not finish apprenticeship")
            $ zeran.say("Protože mě řemeslo omrzelo a tady mi je očividně líp. Proč asi?")
            $ zeran.say("Heinrich si nechal peníze, které jsem mu tehdy zaplatil, a zadarmo ani kuře nehrabe a ani švec neučí. Ale když krade pan mistr Heinrich, je to podle hlídky samozřejmě v pořádku, bez ohledu na následky.")
        "A to ti nikdo nepomohl? Ani rodina?" if "why not finish apprenticeship" in zeran.asked and "why nobody help" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("why nobody help")
            $ zeran.say("Rodiče nebyli místní, mysleli si, že v elfím městě jim bude líp. Jejich dílně se nějakou dobu dost dařilo. A potom umřeli během požáru a všichni ostatní se na mě vykašlali.")
            $ zeran.say("Ještě nějaké chytré otázky o mém soukromém životě?", "angry")
            "Zeran se asi snaží znít lhostejně, ale úplně se mu to nedaří."
        "Možná kdybys zašel za Einionovým knězem..." if "help from priest" in zeran.asked and "why nobody help 2" not in zeran.asked and race == "human":
            hide mcPic
            $ mc.say("Nebo možná nějakým knězem elfí víry? Nedrží elfí komunita pohromadě?")
            call zeranHelpFromPriest
        "Nemohla by ti pomoct elfí komunita?" if "why nobody help" in zeran.asked and "help from priest" not in zeran.asked and race != "human":
            hide mcPic
            $ mc.say("Jednotlivé komunity přece drží pohromadě.")
            $ mc.say("Nebo možná Einionův kněz, pokud jsi u Heinricha změnil víru?")
            call zeranHelpFromPriest
        "Takže kdybys sehnal peníze, mohl by ses k řemeslu vrátit?" if "why not finish apprenticeship" in zeran.asked and "money" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("money")
            $ zeran.say("Peníze a mistra, u kterého mě Heinrich ještě nestihl pomluvit. Takže asi v nějakém jiném městě a to jsme zpátky u těch peněz...")
            $ zeran.say("Takže asi jo. Proč? To mi chcete nějaké dát, nebo se jenom ptáte, aby řeč nestála?", "angry")
        "Tohle by ti mohlo s novým začátkem pomoct. {i}(Dát mu část peněz od Rumelina){/i}" if "money" in zeran.asked and "Rumelin's money" in status and zeran.status != "got money" and "false offer" not in zeran.asked:
            hide mcPic
            $ zeran.say("... kde jsi tolik peněz vzal[a]? Nejsou doufám kradené?", "surprised")
            show mcPic at menuImage
            menu:
                "Nejsou, neboj se.":
                    hide mcPic
                    $ zeran.asked.append("money safe")
                    $ zeran.say("A kde jsi je tedy vzal[a]?")
                    $ mc.say("Znám ve městě pár lidí.")
                    $ zeran.say("Nevypadáš jako někdo, kdo zná bohaté lidi. Proč ti dávno nesehnali lepší boty?")
                    $ mc.say("Snažím se je žádat o laskavosti, jen když na tom opravdu záleží.")
                "Ne, Rumelin mi je dal naprosto dobrovolně.":
                    hide mcPic
                    $ zeran.asked.append("Rumelin's money")
                    $ zeran.say("Vážně? To jsi musel[a] být hodně přesvědčiv[y].", "surprised")
                    $ mc.say("Stačilo na něj vyhrabat dost velkou špínu.")
                "Záleží na tom?":
                    hide mcPic
                    $ zeran.asked.append("money doesn't matter")
                    $ zeran.say("Jestli hrozí, že je u mě někdo najde, bude mě kvůli tomu považovat za zloděje a já zase schytám trest za cizí průšvih, tak docela jo.", "angry")
                    $ mc.say("Jsem si dost jist[y], že je nikdo hledat nebude. Pak by se mohly roznést po městě zprávy, které by se podle mínění některých bohatých osob roznést neměly.")
            $ zeran.say("Dobře... dejme tomu, že z těch peněz nekouká okamžitá cesta do šatlavy.")
            $ zeran.say("Pořád ale nechápu, co tě vede k tomu mi takovou fůru peněz jen tak dát. To je nedokážeš využít nijak jinak?")
            show mcPic at menuImage
            menu:
                "Trochu se v tobě vidím.":
                    hide mcPic
                    $ mc.say("Také byla doba, kdy jsem neměl[a] nic kromě pocitu, že mi celý svět schválně ubližuje.")
                    $ zeran.say("Ale pak ses z toho dostal[a] díky víře, práci a spoustě dalších ctností, co?", "angry")
                    $ mc.say("Ve skutečnosti hlavně díky úplně hloupému štěstí.")
                    $ mc.say("A napadlo mě, že mít také jednou štěstí by sis zasloužil i ty. Třeba v tom, že potkáš blázna, co ti jen tak dá peníze.")
                "Stala se ti nespravedlnost a já ji chci aspoň trochu napravit.":
                    hide mcPic
                    $ zeran.say("Nespravedlnosti se v tomhle městě dějí pořád.", "angry")
                    $ mc.say("Možná, ale na tuhle jsem zrovna narazil[a].")
                    $ zeran.say("A co ty, přímo tobě se nic nestalo?")
                    $ mc.say("To zůstalo daleko, v jiných městech a vesnicích. Nemá význam se k tomu vracet.")
                    $ mc.say("Místo v hlídce není to nejlepší, co mě mohlo potkat, ale ani to nejhorší. Ty potřebuješ peníze víc.")
                "Je to bezpečnější.":
                    hide mcPic
                    $ mc.say("Kdybych je použil[a] pro sebe, mohli by se lidi zajímat, kde jsem k nim při[sel], a ještě bych z toho měl[a] malér. Ty můžeš zmizet z města, to nikoho nepřekvapí, a víc se nikdo nedozví.")
                    $ zeran.say("Můžeš zmizet z města ty.")
                    $ mc.say("Já už se toho nacestoval[a] až dost. Nechci už zase začínat znova. Na vyučení by mi peníze nestačily, na obchodování se necítím... Tady mám aspoň to místo v hlídce.")
                    $ mc.say("Jestli se někdy vzmůžeš, můžeš mi pak ty peníze poslat zpátky.")
                    $ zeran.say("Nevím, nakolik v to můžu doufat... ale rozhodně mám v úmyslu se dostat k něčemu lepšímu, než mám teď. To by nemělo být tak těžké.")
                "Prostě mi přijde vtipné využít Rumelinovy peníze zrovna takto.":
                    hide mcPic
                    $ mc.say("On určitě čeká, že je utratím za něco drahého nebo s nimi zkusím dělat dojem na známé. Tímhle ho dokonale převezu.")
                    if "money safe" in zeran.asked:
                        $ zeran.say("Ještě před chvílí ses tvářil[a], že to byl dárek od obzvlášť hodných přátel. Ne od někoho, z koho si chceš podobným způsobem tropit žerty.")
                    else:
                        if "money doesn't matter" in zeran.asked:
                            $ zeran.say("Jo tak Rumelin. Náš příkladný cechmistr a nechá se vydírat. No asi by mě to v tomhle městě nemělo překvapovat.","happy")
                        $ zeran.say("To je docela draze koupený pocit zadostiučinění, ne?")
                        $ zeran.say("Určitě jsou i jiné způsoby, jak ho převézt. Co já vím, pláchnout s penězi a pak o té jeho špíně někomu napsat dopis.")
                    $ zeran.say("Co máš doopravdy v plánu? K čemu mě chceš využít?", "angry")
                    $ mc.say("Nechci tě k ničemu využít. Prostě mám možnost pomoct, tak chci pomoct. Já se nějak protluču a tobě ty peníze z mých známých pomůžou nejvíc. Vážně je to tak divné?")
                    $ zeran.say("V tomhle městě? To rozhodně je.")
            "Zeran se zamračí, krátce povzdechne a zavrtí hlavou."
            $ zeran.say("Možná mě jenom zkazili a jsem zbytečně podezřívavý. Jestli mi chceš pomoct, jistě že to neodmítnu.")
            show mcPic at menuImage
            menu:
                "V tom případě vítej mezi boháče!":
                    hide mcPic
                    $ zeran.trust += 2
                    $ zeran.say("Díky. To budu moct hned zmizet z města a přesunout se někam, kde mě ještě žádný Heinrich nepomluvil.", "happy")
                    $ zeran.say("Takže jestli ode mě potřebuješ ještě něco, radši se ptej hned. Nevím, kdy přesně budu odcházet, ale bude to brzy.")
                    $ zeran.status = "got money"
                "Vlastně jsem si to rozmyslel[a].":
                    call zeranFalseOffer
        "Byl jsi někdy u Amadisova hrobu?" if ("letters for Ada seen" in status or "letters topic" in ada.asked) and "Amadis grave" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("Amadis grave")
            $ zeran.say("Myslel jsem, že ten je někde v hlavním městě?")
            $ mc.say("A co u hrobu toho druhého Amadise? Toho, který před rokem ukončil Hansovo povstání?")
            $ zeran.say("Poslední dva roky jsem nevytáhl paty z města. Heinrich by mě nepustil, a i kdyby, na cestování jsou potřeba peníze.", "angry")
            $ mc.say("Takže jsi ten hrob nikdy nenavštívil?")
            $ zeran.say("No předtím, než ten druhý Amadis umřel, jsem u jeho hrobu také nebyl, jestli se ptáš na tohle.", "angry")
        "Tušíš, co by Aachim dělal sám v noci v dílně?" if "aachim in workshop" in clues and "aachim in workshop" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("aachim in workshop")
            if zeran.trust < 2:
                $ zeran.say("To vážně netuším. Asi pracoval? Nebo si tam přivedl nějakou holku?")
                $ zeran.say("Kdybych uměl lidem vidět do hlavy, navíc na takovou dálku, netrčel bych tady.", "angry")
            else:
                $ zeran.say("Možná se snažil dokázat tatínkovi, že není úplně ztracený případ?")
                $ zeran.say("Heinrich nemůže snést, že by jeho syn nebyl jako on sám, jenom mladší. Hrozně toho kluka cepuje, ale co je to platné, když Aachim prostě nemá talent. A podle všeho ani zájem.")
                $ zeran.say("Bylo by mi ho skoro líto… ale jak říká Sabri, když člověk něco chce, musí pro to taky něco udělat.")
        "Zatýkám tě za krádež díla mistra Heinricha." (badge="handcuffs") if "stolen shoes" not in zeran.arrestReason:
            hide mcPic
            $ zeran.say("No vždyť jsem to říkal.")
            if len(zeran.asked) < 6:
                $ zeran.say("Ale že pracujete rychle. Žádné zbytečné cavyky. Osoba na svém místě.")
            else:
                $ zeran.say("Ale proč kolem toho bylo potřeba tolik cavyků, když bylo od začátku jasné, jak to dopadne? Takového ztraceného času...")
            $ mc.say("Být tebou držím zobák. Tyhle řeči ti nijak nepomůžou.")
            if "stolen shoes" not in persistent.zeranArrestReasons:
                $ persistent.zeranArrestReasons.append("stolen shoes")
                call universalCulpritAchievementCheck
            $ zeran.arrestReason.append("stolen shoes")
            $ newlyArrested.append(zeran)
            $ status.append("arrest in progress")
            return
        "Zatýkám tě za krádež střihu mistra Njala." (badge="handcuffs") if "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason:
            hide mcPic
            $ zeran.say("Ehm... cože? Ne Heinrichových bot?", "surprised")
            $ zeran.say("Chci říct, samozřejmě, jako pachatel libovolného zločinu jsem hlídce vždy k mání, ale on někdo krade střihy? Proč si ho prostě nepůjčil a neobkreslil, jako všichni?")
            $ mc.say("Ukradl jsi mistru Njalovi střih, podle kterého mistr Heinrich šil ty boty na slavnosti. Jen se neboj, však si vzpomeneš.")
            $ zeran.say("Aha… chápu. Chtěl jsem pomoci svému skvělému příteli. Brzy budou slavnosti, nechceš to místo v hlídce radši zkusit u komediantů?", "angry")
            $ mc.say("Dost řečí, prostě půjdeš se mnou.")
            if "stolen idea" not in persistent.zeranArrestReasons:
                $ persistent.zeranArrestReasons.append("stolen idea")
                call universalCulpritAchievementCheck
            $ zeran.arrestReason.append("stolen idea")
            $ newlyArrested.append(zeran)
            $ status.append("arrest in progress")
            return
        "To jsou všechny moje otázky.":
            hide mcPic
            if zeran.status == "got money":
                $ zeran.say("V tom případě hodně štěstí v pátrání. Kdybys mě tu příště nena[sel], nejspíš jsem na cestě do Eppenhahnu. Nebo do Seewachtu. Prostě někam daleko.", "happy")
            else:
                $ zeran.say("V tom případě přeji hodně štěstí ve tvém náročném pátrání. Jestli budeš mít štěstí, možná s tebou Heinrich ani nevytře podlahu, jak má ve zvyku.")
            return

    jump zeranOptions

label zeranTooSoonToArrest:
    hide mcPic
    $ zeran.trust += 1
    $ zeran.say("Takže ještě nevíte, komu to přišít? Zbytečné obavy, seberte kohokoli z téhle čtvrti, on to nikdo zpochybňovat nebude.")
    call zeranMistrust
    return

label zeranWitnessAgainstHeinrich:
    hide mcPic
    $ zeran.trust -= 2
    "Zeran se na tebe dlouze zadívá. V jeho pohledu není stopa ani po pobavení, ani po nadšení."
    $ zeran.say("Jo, takže mám dosvědčit, že mistr, u kterého už nějakou dobu nepracuju, sám sebe okradl. K popukání.")
    $ zeran.say("Co takhle přestat zdržovat nás oba a pohnout s tím vaším vyšetřováním?")
    return

label zeranRelationshipWithAda:
    hide mcPic
    $ zeran.asked.append("Ada 2")
    $ zeran.say("Ono moc není, o čem mluvit. Občas jsme si s Adou povídali. Je to překvapivě chytrá holka, když se zrovna rozhodne použít hlavu.")
    $ zeran.say("Samozřejmě mnohem častěji se jí chce vzdychat po Amadisovi, bláznit po nové pentli nebo se něčemu hrozně hihňat. Holt bohatá holka.")
    $ zeran.say("Trochu mi připomíná sestru.", "sad")
    $ mc.say("Ty máš sestru?")
    $ zeran.say("Ne. Už ne.", "sad")
    $ zeran.say("To s případem nesouvisí, neměl jsem to vůbec zmiňovat.")
    return

label zeranHelpFromPriest:
    $ zeran.append("help from priest")
    $ zeran.say("To se říká. Ctihodný Molin mi sdělil, že to mám z toho, že se tahám s lidmi, a ať si to pěkně užiju a že si pomoc nezasloužím.", "angry")
    $ mc.say("Kdo to je ctihodný Molin?")
    $ zeran.say("Ále. Kněz, vážená osoba, hrozný suchar a hlavně nejchytřejší na světě. Pořád ještě se nesmířil s tím, že musí žít v jednom městě s lidmi, i když se přesně do toho narodil.")
    $ zeran.say("A oba Einionovi kněží ve městě mají Heinricha hrozně rádi, jak je to ten obdivovaný řemeslník, tak to jsem ani nezkoušel.")
    return

label zeranFalseOffer:
    hide mcPic
    $ zeran.trust -= 3
    $ zeran.asked.append("false offer")
    $ zeran.say("Aha. Chápu. Jak jinak.", "angry")
    $ zeran.say("V tom případě děkuji za napínavý rozhovor.", "angry")
    $ zeran.say("Ještě něco, s čím mohu naši skvělou hlídku podpořit v její důležité práci pro blaho města?", "angry")
    return

label zeranMistrust:
    show mcPic at menuImage
    menu:
        "Proč tolik nedůvěry k hlídce?" if "mistrust" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("mistrust")
            $ zeran.say("Už jsem si stihl všimnout, jak se hlídka chová v téhle čtvrti. Nebo kdekoli jinde ke každému, ke komu si to může dovolit. Chrání akorát tak bohatství a pohodlí smetánky a všichni ostatní jsou jim ukradení.")
        "Ne všichni hlídkaři jsou takoví." if "mistrust" in zeran.asked and "not all cops" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("not all cops")
            $ zeran.say("Jo, ale Hayfa tu není.")
            show mcPic at menuImage
            menu:
                "Vy dva se znáte?":
                    hide mcPic
                    $ zeran.say("Potkali jsme se. S ukradenými botami to nijak nesouvisí.")
                "Rauvin je také slušný člověk. Nikdy by nedovolil, aby hlídka někoho zatkla bez důkazů.":
                    hide mcPic
                    $ zeran.trust += 1
                    $ zeran.say("Možná. Na mě působí jako někdo, kdo za důkaz bude považovat prostě slovo nějakého boháče, ale asi ho znáš líp.")
                "Hayfu hodně obdivuju, doufám, že jednou dokážu být jako ona.":
                    hide mcPic
                    $ zeran.trust -= 1
                    $ zeran.say("Nebo se ještě můžeš rozhodnout být takový ten hlídkař, co jenom sedí na strážnici a nic nedělá. Je to méně práce a nepotřebuješ pro to žádné nadání.")
                "Hayfa nejsem, ale snad tohle nebude tak náročný případ, abych jí dokázal udělat ostudu.":
                    hide mcPic
                    $ zeran.say("Buď bez obav, veškerá ostuda bude jen a pouze tvoje.")
        "Tohle si vyprošuji! Hlídka je vážená instituce!" if "respect me" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("respect me")
            $ zeran.trust -= 1
            $ zeran.say("Ach promiň, zapomněl jsem, že znevažovat hlídku je už od Velinových dob trestné.")
            $ zeran.say("To víte, takový pochybný živel jako já to nikdy nemůže plně docenit. Jste všichni samozřejmě skvělí strážci pořádku a všech ctností.")
        "Uvědomuješ si, že za tohle tě můžu zatknout?" if "respect me" in zeran.asked and "can arrest for disrespect" not in zeran.asked:
            hide mcPic
            $ zeran.asked.append("can arrest for disrespect")
            $ zeran.say("Jistě. Doporučuju potulku, na tu narozdíl od urážek opravdu zákony jsou.")
            "Zeran se významně rozhlédne po pevných stěnách ubytovny kolem vás a pak se vrátí pohledem k tobě."
        "Zatýkám tě za potulku!" (badge="handcuffs") if "can arrest for disrespect" in zeran.asked and "vagrancy" not in zeran.arrestReason:
            hide mcPic
            $ zeran.trust -= 3
            $ sabri.trust -= 3
            $ rauvin.trust -= 5
            $ hayfa.trust -= 10
            $ zeran.say("Je tak povznášející pozorovat naši hlídku při práci!")
            if "vagrancy" not in persistent.zeranArrestReasons:
                $ persistent.zeranArrestReasons.append("vagrancy")
                call universalCulpritAchievementCheck
            $ zeran.arrestReason.append("vagrancy")
            $ newlyArrested.append(zeran)
            $ status.append("arrest in progress")
            return
        "Pojďme se raději vrátit k případu.":
            hide mcPic
            $ zeran.say("Skvělý nápad.")
            return
    jump zeranMistrust

label clearZeransName:
    hide mcPic
    $ zeran.asked.append("clear your name")
    $ zeran.say("To kdybych věděl, tak už dávno netrčím tady.")
    $ zeran.say("Asi nějak přesvědčit Heinricha, že nejsem jediný elf se jménem na Z a že jsem ty zatracené dopisy opravdu nepsal já. Ale když si Heinrich něco vezme do palice, tak s ním nehne ani pár volů.")
    $ zeran.say("Takže hodně štěstí.")
    return

###

label zeranOptionsRemainingCheck:
    $ zeranOptionsRemaining = 0
    if "Heinrich enemies" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "Ada" not in zeran.asked and "Zeran offense" in clues:
        $ zeranOptionsRemaining += 1
    if "Ada" in zeran.asked and "Ada 2" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "Ada 2" in zeran.asked and "Ada relationship" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "clear your name" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "last seen Heinrich" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "alibi" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "alibi" in zeran.asked and "work" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "alibi" in zeran.asked and "alibi witnesses" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "alibi witnesses" in zeran.asked and "letters for Ada seen" in status and "Zeran writing sample" not in status:
        $ zeranOptionsRemaining += 1
    if "motive" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "Heinrich household" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "why not finish apprenticeship" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "why not finish apprenticeship" in zeran.asked and "why nobody help" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "help from priest" in zeran.asked and "why nobody help 2" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "why not finish apprenticeship" in zeran.asked and "money" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "money" in zeran.asked and "Rumelin's money" in status and zeran.status != "got money" and "false offer" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if ("letters for Ada seen" in status or "letters topic" in ada.asked) and "Amadis grave" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "aachim in workshop" in clues and "aachim in workshop" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "stolen shoes" not in zeran.arrestReason:
        $ zeranOptionsRemaining += 1
    if "join forces njal pending" in status and "stolen idea" not in zeran.arrestReason:
        $ zeranOptionsRemaining += 1
    if "letters for Ada seen" in status and "Zeran writing sample" not in status and "writing sample" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    if "writing sample refused" in zeran.asked and "Zeran writing sample" not in status:
        $ zeranOptionsRemaining += 1
    if "theft mention" in zeran.asked and "victim of theft" not in zeran.asked:
        $ zeranOptionsRemaining += 1
    return
