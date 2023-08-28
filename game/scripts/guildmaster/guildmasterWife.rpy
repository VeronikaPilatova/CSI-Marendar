label nireviaController:
    # check if visit makes sense
    if "nirevia closed door" in status:
        "Paní Nirevia s tebou stále odmítá mluvit."
        return
    call nireviaOptionsRemainingCheck
    if optionsRemaining == 0:
        "Nenapadá tě, co dalšího se paní Nirevii ještě ptát."
        return
    call preludeController

    # walk over
    if currentLocation != "rumelin home":
        if "rumelin home visited" not in status:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        $ currentLocation = "rumelin home"
    $ origAsked = nirevia.asked.copy()

    # visit itself
    scene bg rumelin outside
    if "rumelin exposed" in status or "rumelin threatened" in status:
        call rumelinHouseClosedDoor
    elif "rumelin home visited" not in status:
        call nireviaFirst
    else:
        call nireviaAgain
    call nireviaOptions

    # adjust time spent and status
    $ time.addMinutes((len(nirevia.asked) - len(origAsked)) * 3)
    if "rumelin home visited" not in status:
        $ status.append("rumelin home visited")
        $ nireviaNote.isActive = True
        $ nirevia.alreadyMet = True
    return

label nireviaFirst:
    scene bg rumelin outside
    "Najdeš krásný dům v elfí čtvrti a zaklepeš na dveře. Otevře ti starší elfka a tázavě se na tebe podívá."
    $ mc.say("Dobrý den. Jsem %(mcName)s z městské hlídky a vyšetřuji krádež v dílně jednoho z ševcovských mistrů.")
    if time.hours < 18:
        $ nirevia.say("Pak asi budete chtít mluvit s mým manželem, ten bude touto dobou pracovat v budově cechu na náměstí.")
    else:
        $ nirevia.say("Pak asi budete chtít mluvit s mým manželem. Touto dobou už ale nepracuje.")
    if gender == "M":
        $ mc.say("Mohl bych položit několik otázek vám?")
        "Paní Nirevia se na moment zamračí, ale pak kývne a pokyne ti, abys šel dál."
    else:
        $ mc.say("Mohla bych položit několik otázek vám?")
        "Paní Nirevia se na moment zamračí, ale pak kývne a pokyne ti, abys šla dál."

    scene bg rumelin inside
    $ nirevia.say("Co se ztratilo a komu?")
    $ mc.say("Mistru Heinrichovi někdo v noci ukradl jeho čerstvě dokončený mistrovský výrobek.")
    $ nirevia.say("Na Einionovy slavnosti? To by pro mistra Heinricha mohl být vážný problém.")
    if gender == "M":
        $ mc.say("Právě proto bych uvítal vaši pomoc při vyšetřování.")
    else:
        $ mc.say("Právě proto bych uvítala vaši pomoc při vyšetřování.")
    $ nirevia.say("Ptejte se a já se pokusím odpovědět.")
    return

label nireviaAgain:
    scene bg rumelin outside
    "Znovu zaklepeš na dveře domu, kde žije cechmistr Rumelin se svou manželkou."
    $ nirevia.say("Dobrý den. Jak pokračuje vaše pátrání? Podařilo se vám najít Heinrichův výrobek a zloděje?")
    if gender == "M":
        $ mc.say("Stále po něm pátrám. Mohl bych vám ještě položit několik otázek?")
    else:
        $ mc.say("Stále po něm pátrám. Mohla bych vám ještě položit několik otázek?")
    $ nirevia.say("Pokud to pomůže, pokusím se odpovědět.")
    scene bg rumelin inside
    return

label rumelinHouseClosedDoor:
    scene bg rumelin outside
    "Po chvíli klepání ti otevře mladá elfka."
    $ laris.say("Můžu vám nějak pomoci? Mistr Rumelin ani paní Nirevia bohužel nejsou doma.")
    label rumelinHouseClosedDoorMenu:
    show mcPic at menuImage
    menu:
        "Víš, kdy se vrátí?":
            hide mcPic
            "Elfka krátce zaváhá."
            $ laris.say("Nejsem si jistá. Ale i potom budou oba velmi zaměstnaní. Nejméně do začátku Einionových slavností.")
        "Kdo jsi vlastně ty?" if "introductions" not in laris.asked:
            hide mcPic
            $ laris.asked.append("introductions")
            $ laris.say("Samozřejmě, omlouvám se.")
            $ laris.say("Jsem Laris, mistr Rumelin a paní Nirevia si mě vzali k sobě, když jsem přišla o domov a rodiče. Snažím se v domě aspoň pomáhat tam, kde můžu.")
            jump rumelinHouseClosedDoorMenu
        "Chápu.":
            hide mcPic
            $ laris.say("Hodně štěstí ve vašem vyšetřování.")
    $ laris.AlreadyMet = True
    if chosenChar == "nirevia":
        $ status.append("nirevia closed door")
    elif chosenChar == "rumelin":
        $ status.append("rumelin closed door")
    $ leaveOption = "none"
    return

label nireviaOptions:
    if leaveOption == "none":
        return
    call nireviaOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Moc vám děkuji, nebudu vás už zdržovat.")
        "Paní Nirevia se usměje a nechá tě doprovodit ke dveřím."
        return

    show mcPic at menuImage
    menu:
        "Kde byl včera v noci váš manžel?" if "rumelin alibi" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("rumelin alibi")
            $ nirevia.say("U Salmy, oslavoval tam dokončení svého výrobku na slavnosti. Odtamtud šel rovnou domů spát.")
            $ mc.say("Kdy se asi vrátil?")
            $ nirevia.say("Hodně pozdě, asi kolem půlnoci. Ale to všechno vám může říct on sám.")
            $ mc.say("Jste si jistá, že po návratu už byl jen doma?")
            $ nirevia.say("Ano, jsem si jistá. Mám lehké spaní, kdyby vstával ze společné postele, všimla bych si toho.")
        "Co víte o vztazích uvnitř cechu?" if "guild relations" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("guild relations")
            $ nirevia.say("Poslední dobou všichni řeší blížící se volbu cechmistra, která vynáší na povrch velké množství emocí.")
            $ nirevia.say("Někteří lidé si přejí změnu, možná jen proto, že se poslední rok mění vše kolem nás. Já myslím, že právě proto je potřeba zachovat jistou míru stability.")
            $ nirevia.say("Navíc si nejsem jistá, jestli je vůbec k dispozici vhodný protikandidát. Heinrich má na jednu stranu uznání, ale na stranu druhou mu mnoho lidí nemůže přijít na jméno a on se nijak nesnaží to změnit.")
            $ nirevia.say("Kaspar se myslím bude o vedení cechu ucházet jen pokud usoudí, že svými sladkými řečmi obludil tolik lidí, že nemůže prohrát.")
            $ nirevia.say("Z dalších mistrů už je výraznější jen Njal, ale ten platí spíš za podivína a od cechovní politiky zůstává stranou.")
        "Změnil váš manžel v poslední době způsob, kterým získává materiál?" if "less deals" in salma.asked and "less deals 1" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("less deals 1")
            $ nirevia.asked.append("less deals husband")
            $ nirevia.say("Je mi líto, do takových detailů nevidím.", "angry")
        "A co mistr Njal, prý má problémy najít dodavatele?" if "less deals husband" in nirevia.asked and "less deals 2" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("less deals 2")
            $ nirevia.say("Všimla jsem si, že tam asi došlo k nějakým neshodám, ale neznám detaily.")
        "Slyšel jsem, že se mistr Njal dostal do nějakých potíží s dodavateli, víte o tom něco?" if "less deals" in salma.asked and "less deals 1" not in nirevia.asked and gender == "M":
            call lessDealsNjal
        "Slyšela jsem, že se mistr Njal dostal do nějakých potíží s dodavateli, víte o tom něco?" if "less deals" in salma.asked and "less deals 1" not in nirevia.asked and gender == "F":
            call lessDealsNjal
        "A co váš manžel, u něj se něco změnilo?" if "less deals njal" in nirevia.asked and "less deals 2" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("less deals 2")
            $ nirevia.say("Nic, o čem bych já věděla.")
        "Tušíte, jaký vztah mezi sebou mají mistr Heinrich a jeho žena?" if lotte.alreadyMet == True and "victim's marriage" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("victim's marriage")
            $ nirevia.say("Myslím, že Heinrich si své ženy jistým způsobem váží, ale neumí to dát najevo.")
            $ nirevia.say("Je to náročný muž, velmi hrdý na své schopnosti a musím přiznat, že právem, to ale nedělá život s ním o nic snazší. Na své učedníky má opravdu velká očekávání a na svou rodinu pravděpodobně ještě větší.")
        "Pokud by měla paní Lisbeth milence, kdo by to mohl být?" if lotte.alreadyMet == True and "secret lover" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("secret lover")
            $ nirevia.say("Proč se vlastně městská hlídka zajímá o podobné věci?", "angry")
            $ mc.say("Je možné, že střevíce mistra Heinricha ukradl právě ten milenec. Měl by motiv i příležitost.")
            "Nirevia se na chvíli zamyslí, ale možná tím jen získává čas."
            $ nirevia.say("Pokud budeme mluvit jen o možnostech a domněnkách, pak myslím, že si Lisbeth velmi rozumí s mistrem Kasparem. Na cechovních slavnostech spolu často hovoří, zatímco Heinrich se věnuje jednodušší zábavě.")
        "Tušíte, kdo by mohl psát poezii pro Heinrichovu dceru Adu?" if "Ada's boyfriend" in lisbeth.asked or "Ada 2" in zeran.asked and "Ada's boyfriend" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("Ada's boyfriend")
            if "Ada relationship" in zeran.asked:
                $ mc.say("Prý by to nejspíš byl romanticky založený elf, nejspíš obdivovatel Amadise nebo někdo zcestovalý.")
            else:
                $ mc.say("Prý by to měl být elf.")
            $ nirevia.say("Myslela jsem, že za dcerou Heinrichovi chodil jeho vlastní učedník.")
            $ mc.say("Je možné, že došlo k omylu a Zeran byl vyhozen neprávem.")
            $ nirevia.say("To by bylo nešťastné, ale nejsem si jistá, jak v té věci můžu pomoci.")
            $ mc.say("Pokud byste věděla o někom jiném...")
            $ nirevia.say("Pak by to byly jen nepodložené spekulace, které by snadno mohly vést k dalšímu omylu, nemyslíte?")
        "Tušíte, jak by město vzalo, kdyby dva mistři předložili na Einionových slavnostech společný výrobek?" if "join forces victim pending" in status and "join forces" not in nirevia.asked:
            hide mcPic
            $ nirevia.asked.append("join forces")
            $ status.append("join forces survey")
            $ nirevia.say("Pravděpodobně velmi dobře. Taková spolupráce umožní mistrům dosáhnout výsledku, na který by sami nikdy nedosáhli.")
            $ nirevia.say("Pamatuji si, jak před mnoha lety tesaři společně vytvořili čtveřici sousoší symbolizujících roční doby. Dohromady je těch soch snad patnáct a všechny viditelně patří jedna k druhé. Myslím, že to bylo snad nejlepší dílo, které toto město vidělo.")
            if race == "elf":
                if gender == "M":
                    $ nirevia.say("Ty sochy jsou pořád v našem chrámu, určitě jste si jich už musel všimnout.")
                else:
                    $ nirevia.say("Ty sochy jsou pořád v našem chrámu, určitě jste si jich už musela všimnout.")
            else:
                $ nirevia.say("Ty sochy jsou pořád v našem chrámu. Tím myslím chrám rovnováhy, samozřejmě. Když slušně požádáte, určitě vás nechají si ty sochy prohlédnout.")
            $ nirevia.say("Je škoda, že v našem cechu nic takového není možné.")
            $ nirevia.say("Pochopte, aby spolupráce dávala smysl, musí to dílo být odpovídajícím způsobem rozsáhlé, aby do něj každý mistr vložil to úsilí a ten um, který se od něj očekává. Mnohem rozsáhlejší než jedny boty.")
            $ nirevia.say("U nás by to nespíš působilo jako popření celého smyslu té tradice.")
        "Moc vám děkuji, nebudu vás už zdržovat.":
            hide mcPic
            "Paní Nirevia se usměje a nechá tě doprovodit ke dveřím."
            return
    jump nireviaOptions

###

label lessDealsNjal:
    hide mcPic
    $ nirevia.asked.append("less deals 1")
    $ nirevia.asked.append("less deals njal")
    $ nirevia.say("Všimla jsem si, že poslední dva týdny má s dodavateli problémy, nevím, kvůli čemu se nepohodli. Myslíte, že to souvisí s případem? Že by z toho mohl vinit Heinricha?")
    $ mc.say("Zatím nevím, co si o tom myslet. Možné je v tuhle chvíli cokoli.")
    return

label nireviaOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "rumelin alibi" not in nirevia.asked:
        $ optionsRemaining += 1
    if "guild relations" not in nirevia.asked:
        $ optionsRemaining += 1
    if "less deals" in salma.asked and "less deals 1" not in nirevia.asked:
        $ optionsRemaining += 1
    if "less deals husband" in nirevia.asked and "less deals 2" not in nirevia.asked:
        $ optionsRemaining += 1
    if "less deals" in salma.asked and "less deals 1" not in nirevia.asked:
        $ optionsRemaining += 1
    if "less deals njal" in nirevia.asked and "less deals 2" not in nirevia.asked:
        $ optionsRemaining += 1
    if lotte.alreadyMet == True and "victim's marriage" not in nirevia.asked:
        $ optionsRemaining += 1
    if lotte.alreadyMet == True and "secret lover" not in nirevia.asked:
        $ optionsRemaining += 1
    if "join forces victim pending" in status and "join forces" not in nirevia.asked:
        $ optionsRemaining += 1
    if "Ada's boyfriend" in lisbeth.asked or "Ada 2" in zeran.asked and "Ada's boyfriend" not in nirevia.asked:
        $ optionsRemaining += 1
    return
