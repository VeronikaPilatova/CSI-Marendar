label reportingBack:
    call cluesOptionsRemainingCheck
    if optionsRemaining == 0 and "provisional watchman" not in status:
        $ mc.say("Vlastně zatím nic, co by mi přišlo dostatečně důležité.")
        $ rauvin.trust -= 2
        $ hayfa.trust -= 2
        $ status.append("no clue")
        $ rauvin.say("V tom případě bys měl[a] s pátráním co nejdřív začít, Einionovy slavnosti začínají už za čtyři dny.")
        return

    show mcPic at menuImage
    menu:
        # workshop
        "Dílna mistra Heinricha byla zřejmě celou noc odemčená." if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("workshop unlocked")
            $ rauvin.say("Takže přístup mohl mít aspoň teoreticky kdokoli… budeš muset zjistit, kdo všechno měl důvod tu věc ukrást.")
        "Žádné dveře do dílny mistra Heinricha nejsou vypáčené, zloděje musel někdo pustit dovnitř." if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("no forced entry")
            $ rauvin.say("To by mohlo zjednodušit pátrání. Stačí zjistit, kdo tam měl přístup, a okruh podezřelých se tím zúží.")
        "Jedna ze zásuvek u stolu v dílně mistra Heinricha byla násilím vylomená, ale prý z ní nic nechybí." if "break-in" in clues and "missing stuff1" in workshop.checked and "break-in2" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("break-in")
            $ rauvin.say("A myslíš, že to souvisí s tvým případem? Boty by se myslím do zásuvky nevešly, nemohlo se to stát někdy dřív?")
            $ mc.say("Mistr Heinrich o tom nevěděl, dokud jsem na to neupozornil[a]. Víc zatím nevím.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "Jedna ze zásuvek v dílně mistra Heinricha byla násilím vylomená." if "break-in" in clues and "missing stuff1" not in workshop.checked and "break-in1" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("break-in")
            $ rauvin.say("Boty by se myslím do zásuvky nevešly, znamená to, že zloděj hledal ještě něco jiného? Ztratilo se z té zásuky něco?")
            $ mc.say("Nevím, neptal[a] jsem se.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
        "V krbu v dílně mistra Heinricha jsem našel stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "M":
            hide mcPic
            $ rauvin.asked.append("burned evidence")
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistý, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1
        "V krbu v dílně mistra Heinricha jsem našla stužku, která odpovídala popisu ztracených střevíců." if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported and gender == "F":
            hide mcPic
            $ rauvin.asked.append("burned evidence")
            $ rauvin.say("Takže tvoje teorie není krádež, ale zničení toho výrobku?")
            $ mc.say("Zatím si nejsem jistá, ale je to možnost.")
            $ rauvin.trust += 1
            $ hayfa.trust += 1

        # Heinrich household
        "Myslím, že učedníci mistra Heinricha něco skrývají." if "boys met" in status and "boys" not in cluesReported:
            hide mcPic
            $ rauvin.say("To bych se vůbec nedivil, ale snadno to může být i úplná drobnost. Mistr Heinrich je prý náročný člověk, můžou z něj prostě mít strach.")

        # neighbours
        "Paní Lisbeth má pravděpodobně milence." if lotte.alreadyMet == True and "confession" not in kaspar.asked and "confession" not in lisbeth.asked and "possible lover" not in cluesReported:
            hide mcPic
            "Rauvin se zamračí."
            $ rauvin.say("A jak to souvisí s tvým případem? Hlídka tady není od špehování záletníků nebo řešení manželských problémů.")
            $ mc.say("Ten milenec byl včera v noci u ní doma, zatímco mistr Heinrich pil U Salmy. Mohl mít přístup i do jeho dílny.")
            $ rauvin.say("Ale jistě to nevíš. Víš aspoň, kdo to je, nebo to jsou jenom nepodložené drby?")
            if "secret lover" in nirevia.asked:
                $ mc.say("Mohl by to být mistr Kaspar, podle Nirevie si s paní Lisbeth velmi dobře rozumí.")
                if "ambitions" in kaspar.asked:
                    $ mc.say("Mistr Kaspar navíc také usiluje o pozici cechmistra, mohl by chtít mistra Heinricha zdiskreditovat.")
                $ rauvin.say("Pak možná dává smysl si s ním promluvit. Ale buď diskrétní a nedělej žádné ukvapené kroky, všechno to jsou vážení lidé.")
            else:
                $ mc.say("Zatím se mi ho nepodařilo najít.")
                $ rauvin.say("Hlavně v tom směru nedělej žádné ukvapené kroky. Mistr Heinrich i jeho žena jsou vážení lidé.")
            $ rauvin.asked.append("careful of the rich - lover")
        "Myslím, že za těmi podezřelými obchody by mohl stát cechmistr Rumelin." if "AML" in rauvin.asked and "AML" in lotte.asked and "confession" not in rumelin.asked and "AML" not in cluesReported:
            hide mcPic
            $ mc.say("Podle Karstenovy manželky Lotte se jednalo o jeho instrukce.")
            $ rauvin.say("Jaké by k tomu měl důvody?")
            $ mc.say("To nevím, zatím jsem s ním nemluvil[a].")
        "Za podezřelými obchody stojí cechmistr Rumelin, dokonce se mi i přiznal." if "AML" in rauvin.asked and "confession" in rumelin.asked and "AML solved" not in cluesReported:
            hide mcPic
            $ mc.say("Cechmistr chtěl zabránit mistru Njalovi, aby dokončil své dílo na Einionovy slavnosti. Celé to souviselo s ukradeným střihem, podle kterého šil svoje boty mistr Heinrich.")
            $ rauvin.say("K tomu budu později chtít podrobné hlášení se všemi souvislostmi.")

        # Rumelin
        "Mistr Heinrich se rozhádal s polovinou cechu a většinou obchodníků, od kterých bere materiál." if "enemies" in rumelin.asked and "enemies everywhere" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("enemies everywhere")
            $ rauvin.say("To by mohlo být až příliš mnoho podezřelých. Ale měl někdo z nich příležitost se k té věci dostat?")
            if "workshop unlocked" in clues:
                $ mc.say("Dílna byla zřejmě celou noc odemčená, takže bohužel v podstatě kdokoli.")
            elif "doors" in workshop.checked:
                $ mc.say("Na dveřích do dílny jsem neviděl[a] žádné stopy násilí, takže zřejmě jen někdo, koho tam pustil někdo zevnitř. Nebo komu by se podařilo získat klíč.")
        "Mistr Heinrich vyhodil tři učedníky a jeden z nich se prý dostal do špatné společnosti." if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("fired apprentices")
            $ rauvin.say("Pak by rozhodně mohl být dobrý nápad si s nimi promluvit. Víš, kde je najít?")
            $ mc.say("Jeden z nich se přestěhoval do Sehnau, ale ty zbylé dva najdu.")
        "Mistr Heinrich má špatné vztahy i ve své vlastní dílně a tři učedníky už vyhodil." if "enemies" in rumelin.asked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("fired apprentices")
            $ rauvin.say("Pak by mohl být dobrý nápad si se všemi učedníky promluvit. Víš, kde najít ty, co u něj už nejsou?")
            $ mc.say("Jeden z nich se přestěhoval do Sehnau, druzí dva budou někde ve městě. Nejsem si jist[y], kde přesně.")
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1

        # Kaspar
        "Mistr Heinrich má problémy s alkoholem." if kaspar.alreadyMet == True and "alcoholic" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("alcoholic")
            call alcoholicResponse
        "Mistr Kaspar se mi nelíbí. Snažil se mi vlichotit a nevím, nakolik mu můžu věřit." if kaspar.alreadyMet == True in status and "kaspar suspicious" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("kaspar suspicious")
            $ rauvin.trust += 1
            $ hayfa.trust += 2
            $ rauvin.say("Zajímavé. Bylo to jen lichocení, nebo se ti snažil něco podsunout?")
            $ mc.say("Říkal, že mistr Heinrich pije tak moc a je tak vzteklý, že ty boty klidně mohl zničit sám. A naznačoval, že cechmistr by ho právě kvůli tomu mohl chtít znemožnit.")

        # Salma's pub
        "Cechmistr Rumelin včera mistru Heinrichovi vyhrožoval." if "pub fight" in salma.asked and "pub fight" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("pub fight")
            $ mc.say("Prý se osobně postará, aby se nikdy nedostal do čela cechu. To mi zní jako silný motiv.")
            $ rauvin.say("Mistra Rumelina znám spíš jako vyjednavače. Čekal bych, že mistra Heinricha třeba pomluví a poštve proti němu další mistry, ne že by se vloupal do jeho dílny. Ani že by tam někoho poslal.")
            $ rauvin.say("Ukazuje na cechmistra ještě něco dalšího?")
            $ mc.say("Zatím nic, o čem bych věděl[a].")
            if "rumelin alibi" in salma.asked:
                $ mc.say("Navíc od Salmy odešel o hodně později, než Heinrich.")
            $ rauvin.say("Rozumím. Asi ho nemůžeme zcela vyloučit, ale zaměřil bych se hlavně na jiné podezřelé.")
        "Další podezřelý může být Karsten, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu." if "other fights" in salma.asked and "husband" not in lotte.asked and "karsten" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("karsten")
        "Další podezřelá může být manželka obchodníka, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu. Karsten sám není ve městě, ale jeho žena ano." if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" not in lotte.asked and "Lotte" not in cluesReported:
            hide mcPic
            $ rauvin.asked.appemd("lotte")
        "Další podezřelá může být manželka obchodníka, kterému mistr Heinrich vyčítal dodávku nekvalitního materiálu. Karsten sám není ve městě, ale jeho žena prý byla sama doma." if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" in lotte.asked and "Lotte" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("lotte")
        "S případem to možná nesouvisí, ale ševcovští mistři poslední dobou obchodují jinak než dřív." if "less deals" in salma.asked and "less deals" not in cluesReported:
            hide mcPic
            $ rauvin.asked.append("AML")
            $ mc.say("Mistr Njal má podle Salmy najednou problém uzavřít obchody a mistr Rumelin uzavírá méně smluv na drahý materiál. Zajímavé je, že smlouvy na prodej zůstávají stejné.")
            "Rauvin se zamračí a zamyslí."
            $ rauvin.say("To opravdu zní trochu zvláštně. Možná to nic neznamená, ale pro jistotu nechám někoho zjistit, jestli se jen nepřesunuli do jiné hospody. A jestli cechmistr pořád prodává zboží, které drahý materiál potřebuje.")
            $ status.append("add investigating less deals")
        "Žebračka Erle dnes ráno donesla do hospody lahve se stejným popisem, jaké se ztratily z domu mistra Heinricha." if "lost bottles" in clues and "lost bottles" not in cluesReported:
            hide mcPic
            $ rauvin.say("Hm. Předpokládám, že to jsou nějaké drahé lahve, které jdou snadno poznat?")
            $ mc.say("Ano, je to drahé pití, které si mistr Heinrich schovává pro dobré přátele nebo vážené hosty.")
            $ rauvin.say("A kde je získala?")
            show mcPic at menuImage
            menu:
                "To nevím, Salma se jí neptala a já s ní ještě nemluvil." if erle.alreadyMet == False and gender == "M":
                    hide mcPic
                    $ rauvin.say("Tak se jí zeptej. Nevím, jestli to s krádeží bot souvisí, ale jestli chceš tuhle stopu sledovat, je to přirozený krok.")
                "To nevím, Salma se jí neptala a já s ní ještě nemluvila." if erle.alreadyMet == False and gender == "M":
                    hide mcPic
                    $ rauvin.say("Tak se jí zeptej. Nevím, jestli to s krádeží bot souvisí, ale jestli chceš tuhle stopu sledovat, je to přirozený krok.")
                "Tvrdí, že je našla v blátě u řeky." if "bottles 2" in erle.asked:
                    hide mcPic
                    $ rauvin.say("To se takhle v blátě u řeky přehrabuje často?")
                    $ mc.say("Mluvil[a] jsem s ní pod mostem, kde asi tráví většinu času. Tak bych se vlastně nedivil[a].")
                    $ rauvin.say("Potom potřebujeme zjistit, jestli si vymýšlí, nebo jakou zvláštní cestou se lahve mistra Heinricha do té řeky dostaly.")
                    $ mc.say("To mám přesně v úmyslu.")
                "Kde jinde, než v té dílně?":
                    hide mcPic
                    $ rauvin.trust -= 1
                    $ hayfa.trust -= 1
                    $ rauvin.say("Takže tvoje domněnka je, že se Erle vloupala do Heinrichovy dílny, ukradla tam lahve, přes noc je vypila, ráno je donesla Salmě a doufala, že si to nikdo nespojí dohromady?")
                    $ mc.say("Vypít je mohl i někdo spolu s ní. Nebo mohla obsah někam přelít.")
                    $ rauvin.say("Pořád by to pro ni byl dost nebezpečný podnik. A neříká Erle, že je jako žebračka spokojená? Prý občas dokonce odmítá almužny, že má v danou chvíli dost. Aspoň myslím, že to je ona.")
                    $ mc.say("To možná říká, ale buď lže a pak klidně mohla krást, nebo říká pravdu a pak to nemá v hlavě v pořádku a kdo ví, co všechno mohla udělat.")
                    $ rauvin.say("Možná. Kde tvrdí ona sama, že ty lahve našla?")
                    if "bottles 2" in erle.asked:
                        $ mc.say("Prý v blátě u řeky, ale to nedává smysl. Jak by se tam dostaly?")
                        $ rauvin.say("Jak by se Erle dostala do dílny a kam zmizel obsah těch lahví? Nemyslím, že v tuto chvíli můžeme dělat jakékoli závěry.")
                    else:
                        $ mc.say("Na to jsem se ještě nestihl[a] zeptat.")
                        $ rauvin.say("Tak to udělej, třeba nás to na něco navede.")
                "Asi někde na smetišti?":
                    hide mcPic
                    $ rauvin.say("A proč to považuješ za zajímavou stopu?")
                    $ mc.say("Zloděj je zřejmě neprodal, ale rovnou vypil.")
                    show mcPic at menuImage
                    menu:
                        "A protože těch lahví je víc, asi na to nebyl sám.":
                            hide mcPic
                            $ rauvin.say("To ale nemusí znamenat, že měl komplice přímo při krádeži. Mohl prostě nabídnout pití nějakému kamarádovi, který netušil, odkud to je.")
                            $ rauvin.say("Jak s tím chceš pracovat? Nemůžeme přece chodit od domu k domu a všech se ptát, jestli náhodou nepili z těchto lahví.")
                            $ mc.say("Tohle je drahé pití. Někdo bohatý by ho nekradl, ten by si ho sám koupil, a pro někoho chudého by to byla moc velká vzácnost na to, aby ji vypil jen tak s někým.")
                            $ mc.say("Myslím, že zloděj byl spíš chudší, a že jestli neměl komplice, přinesl to někomu, kdo je mu blízký nebo na koho chtěl udělat dojem.")
                            $ rauvin.say("“Dobře, to asi ano. Pořád mi není jasné, jestli nás to někam posouvá, ale ve spojitosti s něčím dalším to možná může být užitečné.")
                        "To mu muselo způsobit dost ošklivou kocovinu, to by ho mohlo pomoct prozradit.":
                            hide mcPic
                            $ rauvin.say("Dobře, to asi může být nějaká stopa.")
                            $ rauvin.say("Ale spousta lidí se týž večer opila jinde, na někom kocovina nemusí být poznat a mistru Heinrichovi pořád jde hlavně o ty boty. Na tuhle stopu bych se nesoustředil až příliš.")
                        "Možná potom v opilosti ukradl ty boty.":
                            hide mcPic
                            $ rauvin.say("Nemusel by potom pít přímo v dílně?")
                            $ mc.say("Přesně. Takže jestli ten zloděj nebyl obzvlášť drzý, musel to být někdo z Heinrichovy rodiny.")
                            $ rauvin.say("Kdo z Heinrichovy rodiny by měl zájem na tom krást Heinrichův mistrovský výrobek? Není přirozenější předpokládat, že spolu ty dvě krádeže nesouvisí?")
                            $ mc.say("Dvě nesouvisející krádeže v jeden den, to by také byla velká náhoda.")
                            $ rauvin.say("Nebo tam může být souvislost, kterou teď nevidíme.")
                            $ rauvin.say("Jen chci říct, neupínej se na to, že se někdo opil v dílně a poté ukradl boty. Je to určitě možné, ale není to jediné možné vysvětlení.")
                        "Těžko se mi představuje, že by někdo kradl jen kvůli tomu, aby se mohl rovnou zpít. Myslím, že to vypil přímo mistr Heinrich.":
                            hide mcPic
                            $ rauvin.trust -= 1
                            $ rauvin.say("A kdo potom donesl ty lahve na smetiště?")
                            $ mc.say("Možná on, aby mu na to nepřišla manželka?")
                            $ rauvin.say("Záleží mu na tom? Na mě tak nepůsobí.")
                            $ rauvin.say("Asi bych se zkusil zamyslet ještě nad jiným vysvětlením.")

        # Zeran
        "Myslím, že mistr Heinrich vyhodil jednoho ze svých učedníků neprávem." if "Zeran innocent" in clues and "Zeran innocent" not in cluesReported:
            hide mcPic
            $ rauvin.say("A myslíš, že to nějak souvisí s tvým současným případem?")
            $ mc.say("Nejspíš ne, ale chci jeho nevinu dokázat.")
            show mcPic at menuImage
            menu:
                "Spravedlnost je přece to, od čeho tady hlídka je.":
                    hide mcPic
                    $ rauvin.say("Především je tady hlídka od udržování pořádku a vynucování zákonů.")
                "Hlídka je tady přece od toho, aby chránila lidi.":
                    hide mcPic
                    $ hayfa.trust += 1
                    $ rauvin.say("Zníš jako Hayfa.")
            $ rauvin.say("Ne, že bych tě nechápal nebo s tebou vlastně nesouhlasil, ale před jakou dobou byl ten učedník vyhozený?")
            $ mc.say("Asi před dvěma měsíci, nevím úplně přesně.")
            $ rauvin.say("Pak může určitě na očištění počkat ještě týden. Střevíce mistra Heinricha nebo aspoň zloděje je nutné najít do začátku Einionových slavností.")

        # nothing
        "Raději bych si to nechal pro sebe." if "provisional watchman" not in status and gender == "M":
            hide mcPic
            $ rauvin.trust -= 2
            $ status.append("not sharing")
            "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
            jump leaveReporting
        "Raději bych si to nechala pro sebe." if "provisional watchman" not in status and gender == "F":
            hide mcPic
            $ status.append("not sharing")
            $ rauvin.trust -= 2
            "Rauvin pozdvihne obočí."
            $ rauvin.say("Nejsem si jistý, že tomu rozhodnutí rozumím, ale beru to tak, že se chceš prokázat až vyřešeným případem.")
            jump leaveReporting
        "Vlastně radši počkám, až budu mít víc stop." if "provisional watchman" in status:
            hide mcPic
            jump leaveReporting

    if "provisional watchman" in status and "report given" not in dailyStatus:
        $ dailyStatus.append("report given")
    if "promised to share" in dailyStatus:
        $ hayfa.trust += 1
        $ dailyStatus.remove("promised to share")
    $ cluesReported.extend(cluesAvailable)

    label leaveReporting:
    if "provisional watchman" in status and "Rauvin visited" not in status:
        $ status.append("Rauvin visited")
    return

label alcoholicResponse:
    $ rauvin.say("To je zajímavé. Vím, že se napije rád, ale nikdy jsem neslyšel o žádných výtržnostech. Odkud tu stopu máš?")
    show mcPic at menuImage
    menu:
        "Říkal to mistr Kaspar. Vypadal, že mluví ze zkušenosti.":
            hide mcPic
            $ rauvin.trust -= 1
            $ hayfa.trust -= 1
            $ rauvin.say("Dobrá, nemuselo se ke mně asi donést všechno. Nicméně jestli s tou informací máme pracovat, potřebujeme ji ověřit ještě z dalšího zdroje.")
        "Velmi se mě o tom snažil přesvědčit mistr Kaspar.":
            hide mcPic
            $ mc.say("Když nad tím tak přemýšlím, žádné důkazy nebo zážitky nezmiňoval, jen ho hodně očerňoval. Možná doufal, že mu to pomůže dostat se do čela cechu.")
            $ rauvin.say("Tomu bych klidně věřil. Ale s případem to vůbec nemusí souviset.")
        "Radši si to nechám pro sebe.":
            hide mcPic
            $ rauvin.trust -= 2
            $ hayfa.trust -= 2
            $ rauvin.say("Protože je tvůj zdroj tak tajný, nebo tak málo důvěryhodný? V každém případě myslím, že je na čase, aby ses vrátil[a] k případu.")
    return
###

label cluesOptionsRemainingCheck:
    $ optionsRemaining = 0
    $ cluesAvailable = []
    if "workshop unlocked" in clues and "workshop unlocked" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("workshop unlocked")
    if "no forced entry" in clues and "workshop unlocked" not in clues and "no forced entry" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("no forced entry")
    if "break-in" in clues and "missing stuff1" in workshop.checked and "break-in2" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in2")
    if "break-in" in clues and "missing stuff1" not in workshop.checked and "break-in1" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("break-in1")
    if "burned evidence" in clues and "shoes description" in clues and "burned evidence" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("burned evidence")
    if "enemies" in rumelin.asked and "enemies everywhere" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies everywhere")
    if "fired apprentices" in clues and "fired apprentices" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("fired apprentices")
    if "enemies" in rumelin.asked and "fired apprentices" not in clues and "enemies at home" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("enemies at home")
    if kaspar.alreadyMet == True and "alcoholic" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("alcoholic")
    if kaspar.alreadyMet == True and "kaspar suspicious" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("kaspar suspicious")
    if "pub fight" in salma.asked and "pub fight" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("pub fight")
    if "other fights" in salma.asked and "husband" not in lotte.asked and "merchant" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("merchant")
    if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" not in lotte.asked and "Lotte" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Lotte")
    if "other fights" in salma.asked and "husband" in lotte.asked and "alibi" in lotte.asked and "Lotte" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Lotte")
    if "less deals" in salma.asked and "less deals" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("less deals")
    if "lost bottles" in clues and "lost bottles" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("lost bottles")
    if lotte.alreadyMet == True and "confession" not in kaspar.asked and "confession" not in lisbeth.asked and "possible lover" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("possible lover")
    if "AML" in rauvin.asked and "AML" in lotte.asked and "confession" not in rumelin.asked and "AML" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("AML")
    if "AML" in rauvin.asked and "confession" in rumelin.asked and "AML solved" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("AML solved")
    if "Zeran innocent" in clues and "Zeran innocent" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Zeran innocent")
    if "boys met" in status and "boys" not in cluesReported:
        $ optionsRemaining += 1
        $ cluesAvailable.append("Zeran innocent")
    return
