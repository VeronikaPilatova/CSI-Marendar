label gerdController:
    $ origAsked = gerd.asked.copy()
    if gerd.alreadyMet == False:
        call gerdFirst
    else:
        call gerdAgain
    if gerd.alreadyMet == False:
        $ gerd.alreadyMet = True
    call gerdOptions

    # adjust time spent
    $ time.addMinutes((len(gerd.asked) - len(origAsked)) * 3)
    return

label gerdFirst:
    show mcPic at menuImage
    if gerdNote.isActive == True:
        menu:
            "Byl jsi dřív v učení u mistra Heinricha?" if "fired apprentices" in clues:
                hide mcPic
                $ gerd.say("Bohužel. Myslím, že to byla nešťastná náhoda, můj otec slyšel jenom o jeho práci a ne o jeho povaze. Ale teď jsem u mistra Njala a upřímně jsem se tady za ty dva týdny naučil víc, než u Heinricha za měsíc. Takže jestli si to rozmyslel, tak zpátky nechci.", "happy")
                $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v Heinrichově dílně. Můžu ti položit pár otázek?")
            "Jsem z městské hlídky a vyšetřuji krádež v Heinrichově dílně. Můžu ti položit pár otázek?":
                hide mcPic
    else:
        $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v Heinrichově dílně. Můžu ti položit pár otázek?")
    "Gerd, který byl dosud úplně klidný, na chvilku znervózní, pak ale pokrčí rameny."
    $ gerd.say("Nejspíš. Co se ztratilo?")
    show mcPic at menuImage
    menu:
        "Jeho mistrovský kus na Einionovy slavnosti.":
            hide mcPic
            $ gerd.say("Pak si nejsem jistý, jak vám můžu pomoct. Já ani nevím, kdy přesně ho dokončil.")
            "Gerd znovu pokrčí rameny, zřejmě už zase v naprostém klidu."
        "To teď není důležité.":
            hide mcPic
            $ gerd.say("Pak si nejsem jistý, jak vám můžu pomoct. Ale rád se pokusím.")
            "Gerd se usměje, ale napětí z jeho pohybů úplně nezmizí."
    return

label gerdAgain:
    $ mc.say("Můžu se tě ještě na pár věcí zeptat?")
    "Gerd možná na moment zaváhá, ale pak pokrčí rameny."
    if "cheeky" not in gerd.asked:
        $ gerd.say("Ptejte se, na co chcete, a já, na co chci, odpovím.", "happy")
        menu:
            "Nebuď drzý, tohle je vážná věc.":
                $ gerd.trust -= 1
                $ gerd.asked.append("cheeky")
                $ gerd.say("Rozkaz, pane!", "eyeroll")
            "{i}(Přejít poznámku mlčením){/i}":
                pass
    else:
        $ gerd.say("Rozkaz, pane!")
    return

label gerdOptions:
    call njalOptionsRemainingCheck
    call gerdOptionsRemainingCheck
    if gerdOptionsRemaining == 0 and njalOptionsRemaining == 0:
        $ mc.say("To jsou všechny otázky.")
        $ gerd.say("Tak já se zase vrátím k práci. Popřál bych hodně štěstí v pátrání, ale Heinrich si ztrapnit zaslouží.")
        return

    show mcPic at menuImage
    menu:
        "Byl jsi včera v dílně mistra Heinricha?" if "fired apprentices" in clues and "which apprentice" in liese.asked and "stolen idea" not in clues:
            hide mcPic
            $ gerd.asked.append("workshop visit")
            call workshopVisitGerd
        "Řekni mi víc o své návštěvě v dílně mistra Heinricha." if "workshop visit" in njal.asked and "workshop visit" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("workshop visit")
            $ gerd.say("Mistr už vám myslím řekl všechno. Heinrich ukradl jeho střih, my si ho vzali zpátky. Teď je zpátky u právoplatného majitele, to by přece hlídka měla schvalovat, ne? O jeden zločin míň, co musíte aktivně napravit.")
        "Měl jsi s tím jít za hlídkou nebo aspoň za svým mistrem." if "workshop visit" in gerd.asked and "workshop visit" not in njal.asked and "told njal" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("told njal")
            $ gerd.say("S mistrem jsem o tom samozřejmě mluvil. Byl rád, že aspoň s jistotou ví, kdo ten střih má, snažil se to nějak řešit, ale neměli jsme žádný důkaz. To jsme to měli nechat být?")
            $ mc.say("A co myslíš, že by tvůj mistr řekl na další krádež?")
            $ gerd.say("No, včera mi řekl ‘Dobrá práce.’ Odemčenou dílnu jsme viděli oba a on mě tam sám poslal. A nebyla to krádež, bylo to vrácení kradené věci.")
        "Ten střih, který jsi v dílně vzal, byl ve vypáčené zásuvce u stolu?" if "workshop visit" in gerd.asked and "table" in workshop.checked and "forced drawer" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("forced drawer")
            $ gerd.say("Jo, přesně tam. Toho šuplíku je mi líto, jestli to bude potřeba, tak ho s mistrem zaplatíme.")
        "Dělal jsi v Heinrichově dílně ještě něco?" if "workshop visit" in gerd.asked and "did anything else" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("did anything else")
            $ gerd.say("Ne, jenom jsem vypáčil ten jeden šuplík, vzal správné papíry a rychle vypadl. Fakt jsem nechtěl, aby mě tam Heinrich našel.")
            $ mc.say("Takže jsi věděl předem, kde přesně ten střih je?")
            $ gerd.say("Jasně. Předtím jsem u Heinricha dělal, samozřejmě, že jsem věděl, kde co má.")
        "Všiml sis Heinrichova mistrovského výrobku?" if "workshop visit" in gerd.asked and "noticed shoes" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("noticed shoes")
            if "shoes description" in clues:
                $ mc.say("Měly to být dámské střevíce, barvené na fialovo, se zlatými stuhami a jemným zdobením.")
            $ gerd.say("Nevšiml jsem si. Ale já jsem chtěl hlavně být co nejrychlejc zase venku, na nic jiného než na ten jeden šuplík jsem nekoukal ani nesahal.")
        "Všiml sis v Heinrichově dílně čehokoli podezřelého?" if "workshop visit" in gerd.asked and "anything suspicious" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("anything suspicious")
            "Gerd se na chvíli zamyslí."
            $ gerd.say("Ne, nic mě nenapadá. Během rychlého páčení šuplíku to tam vypadalo stejně, jako si pamatuju.")
        "Myslím, že bys měl dobrý důvod chtít mistra Heinricha na slavnostech znemožnit." if "fired apprentices" in clues and "motive" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("motive")
            $ gerd.say("Kdyby mi nebyl ukradený celý Heinrich, byl bych mu vlastně vděčný.")
            $ mc.say("Za to, že tě vyhodil a asi ti poškodil pověst?")
            $ gerd.say("Kdo by u něj chtěl být? Všechny jenom sekýruje a jak není přesně po jeho, je zle. I jeho vlastní syn by byl nejradši kdekoli jinde.")
            $ gerd.say("Jenomže změnit mistra normálně stojí peníze a domlouvání. Kdyby mě nepustil Heinrich sám, jen tak bych se od něj nedostal. U mistra Njala jsem šťastný, možná bych se k němu chtěl vrátit i po cestě na zkušenou.")
        "Víš něco o tom, že by měl tvůj nový mistr problémy s nákupem materiálu?" if "less deals" in salma.asked and "less deals" not in gerd.asked:
            hide mcPic
            $ gerd.asked.append("less deals")
            $ gerd.say("Jo, stěžoval si, že mu nikdo nechce prodat materiál na jeho nový mistrovský výrobek.")
        "Chtěl bych si ještě promluvit s tvým mistrem." if njalOptionsRemaining > 0 and gender == "M":
            hide mcPic
            $ gerd.say("Počkejte chvíli, dojdu mu to říct.")
            "Gerd zmizí v domě, ale za pár minut je zpátky a podrží ti dveře."
            $ gerd.say("Mistr říkal, že máte jít rovnou dál.")
            call njalHouseInside
            jump njalController
        "Chtěla bych si ještě promluvit s tvým mistrem." if njalOptionsRemaining > 0 and gender == "F":
            hide mcPic
            if currentLocation != "njal house inside":
                $ gerd.say("Počkejte chvíli, dojdu mu to říct.")
                "Gerd zmizí v domě, ale za pár minut je zpátky a podrží ti dveře."
                $ gerd.say("Mistr říkal, že máte jít rovnou dál.")
                call njalHouseInside
            else:
                "Gerd se beze slova otočí na svého mistra a ten přikývne."
                $ njal.say("Poslouchám.")
            jump njalController
        "To jsou všechny otázky.":
            hide mcPic
            $ gerd.say("Tak já se zase vrátím k práci. Popřál bych hodně štěstí v pátrání, ale Heinrich si ztrapnit zaslouží.")
            return
    jump gerdOptions

###

label workshopVisitGerd:
    $ gerd.say("Co bych tam dělal? Heinrich mi tím vyhazovem udělal obrovskou laskavost, doufám, že do jeho dílny už nikdy nevkročím. A jak bych se tam vůbec dostal?")
    if "workshop unlocked" in clues:
        $ mc.say("Dílna byla většinu noci odemčená. Jedna ze sousedek tě tam viděla v noci jít, popsala tě dost přesně.")
        "Gerd se zamračí, ale po chvilce pokrčí rameny."
        $ gerd.say("Tak fajn, byl jsem tam. Asi celých deset minut, když jsem viděl, že Eckhard za sebou po odchodu nezamkl.")
    else:
        $ mc.say("Doufal jsem, že to mi řekneš ty. Ale jedna ze sousedek tě tam viděla v noci jít, popsala tě dost přesně.")
        "Gerd se zamračí, ale po chvilce pokrčí rameny."
        $ gerd.say("Tak fajn, byl jsem tam. Asi celých deset minut. Ale nebylo to vloupání, Heinrich s Eckhardem se asi vraceli z hospody a nechali dílnu odemčenou.")
        if "Eckhard" not in clues:
            $ clues.append("Eckhard")
    $ mc.say("Co jsi tam dělal?")
    $ gerd.say("Bral zpátky věc, která Heinrichovi nepatřila.")
    if "workshop visit" in njal.asked:
        $ mc.say("Ten střih, který vymyslel a zdokonalil tvůj současný mistr?")
        $ gerd.say("Přesně ten. Teď je zpátky u právoplatného majitele, to by přece hlídka měla schvalovat? O jeden zločin míň, co musíte aktivně napravit.")
    else:
        $ mc.say("To asi budeš muset vysvětlit.")
        $ gerd.say("Heinrich se nějak dostal ke střihu, který vymyslel mistr Njal. Nějak mu ho ukradl, netuším jak, přišel jsem na to až tady, když jsem u svého nového mistra viděl ty stejné vylepšení.")
        $ gerd.say("Zeptal jsem se ho na ně a on mi řekl o té krádeži. Tak když jsem měl příležitost, přišlo mi jenom fér vrátit ten střih právoplatnému majiteli.")
    $ clues.append("stolen idea")
    return

label gerdOptionsRemainingCheck:
    $ gerdOptionsRemaining = 0
    if "fired apprentices" in clues and "which apprentice" in liese.asked and "stolen idea" not in clues:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in njal.asked and "workshop visit" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in gerd.asked and "workshop visit" not in njal.asked and "told njal" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in gerd.asked and "table" in workshop.checked and "forced drawer" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in gerd.asked and "did anything else" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in gerd.asked and "noticed shoes" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "workshop visit" in gerd.asked and "anything suspicious" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "fired apprentices" in clues and "motive" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    if "less deals" in salma.asked and "less deals" not in gerd.asked:
        $ gerdOptionsRemaining += 1
    return
