label victimHouseholdController:
    # check if visit makes sense
    if wifeNote.isActive == False:
        pass
    elif chosenChar == "workshop":
        call workshopOptionsRemainingCheck
        if optionsRemaining == 0:
            "" "Nenapadá tě, co dalšího v (mistrově) dílně ještě prohlížet."
            return
    elif chosenChar == "victim":
        call victimOptionsRemainingCheck
        if "carrying key" not in status and optionsRemaining == 0:
            "" "Nenapadá tě, na co dalšího se (okradeného mistra) ještě ptát."
            return
    elif chosenChar == "wife":
        call wifeOptionsRemainingCheck
        if optionsRemaining == 0:
            "" "Nenapadá tě, na co dalšího se (manželky okradeného mistra) ještě ptát."
            return
    elif chosenChar == "son":
        pass
    elif chosenChar == "daughter":
        pass
    elif chosenChar == "apprentice1" or chosenChar == "apprentice2":
        pass

    # walk over
    if currentLocation != "victim house":
        $ time.addMinutes(15)
        $ currentLocation = "victim house"

    # visit itself
    call victimHouseIntro

    # adjust time and status
    if "victim house visited" not in status:
        $ status.append("victim house visited")
    $ wifeNote.isActive = True
    "" "DEBUG: Odcházíme z domu"
    return

label victimHouseIntro:
    scene bg exterior02
    if "victim house visited" not in status:
        "" "Dům (okradeného mistra) najdeš snadno. Je to jeden z nejvýstavnějších v ulici a přiléhá k němu prostorná dílna."
        "" "Zaklepeš na dveře a otevře ti upravená žena s milým úsměvem."
        $ wife.say("Dobrý den, potřebujete něco?")
        $ mc.say("Jsem %(mcName)s z městské hlídky a vyšetřuji krádež výrobku mistra (jméno).")
        $ wife.say("Já jsem (jméno), jeho žena. Můžu vám nějak pomoct?")
    else:
        "" "Cestu k domu (okradeného mistra) už znáš a tak ani nemusíš přemýšlet, který z výstavních domů v ulici je ten správný."
        if wifeNote.isActive == False:
            "" "Zaklepeš na dveře a otevře ti upravená žena s milým úsměvem."
        $ wife.say("Dobrý den… aha, vy jste ten strážný, co hledá manželův výrobek. Můžu vám nějak pomoct?")
    if wifeNote.isActive == False:
        show mcPic at menuImage
        menu:
            "Nesu vašemu muži klíč od jeho dílny." if "carrying key" in status:
                hide mcPic
                if gender == "M":
                    $ wife.say("To jste hodný. Dojdu pro něj, pojďte zatím dál.", "happy")
                else:
                    $ wife.say("To jste hodná. Dojdu pro něj, pojďte zatím dál.", "happy")
                jump returningKey
            "Rád bych ještě jednou mluvil s vaším mužem." if gender == "M":
                hide mcPic
                jump victimIntro
            "Ráda bych ještě jednou mluvila s vaším mužem." if gender == "F":
                hide mcPic
                jump victimIntro
            "Můžu vám položit pár otázek?":
                hide mcPic
                jump wifeIntro
            "Chtěl bych si promluvit s (mistrovými) učedníky." if gender == "M":
                hide mcPic
                jump apprenticesIntro
            "Chtěla bych si promluvit s (mistrovými) učedníky." if gender == "F":
                hide mcPic
                jump apprenticesIntro
            "Můžu mluvit s vaším synem?" if sonNote.isActive == True:
                hide mcPic
                jump sonIntro
            "Můžu mluvit s vaší dcerou?" if daughterNote.isActive == True:
                hide mcPic
                jump daughterIntro
            "Mohl bych se podívat do dílny?" if gender == "M" and "workshop visited" not in status:
                hide mcPic
                jump workshopIntro
            "Mohl bych se ještě jednou podívat do dílny?" if gender == "M" and "workshop visited" in status:
                hide mcPic
                jump workshopIntro
            "Mohla bych se podívat do dílny?" if gender == "F" and "workshop visited" not in status:
                hide mcPic
                jump workshopIntro
            "Mohla bych se ještě jednou podívat do dílny?" if gender == "F" and "workshop visited" in status:
                hide mcPic
                jump workshopIntro

    elif chosenChar == "workshop":
        if "gender" == "M":
            $ mc.say("Mohl bych se (ještě jednou) podívat do dílny?")
        else:
            $ mc.say("Mohla bych se (ještě jednou) podívat do dílny?")
        jump workshopIntro
    elif chosenChar == "victim":
        if gender == "M":
            $ mc.say("Rád bych ještě jednou mluvil s vaším mužem.")
        else:
            $ mc.say("Ráda bych ještě jednou mluvila s vaším mužem.")
        jump victimIntro
    elif chosenChar == "wife":
        $ mc.say("Můžu vám položit pár otázek?")
        jump wifeIntro
    elif chosenChar == "son":
        $ mc.say("Můžu mluvit s vaším synem?")
        jump sonIntro
    elif chosenChar == "daughter":
        $ mc.say("Můžu mluvit s vaší dcerou?")
        jump daughterIntro
    elif chosenChar == "apprentice1" or chosenChar == "apprentice2":
        if "gender" == "M":
            $ mc.say("Chtěl bych si promluvit s (mistrovými) učedníky.")
        else:
            $ mc.say("Chtěla bych si promluvit s (mistrovými) učedníky.")
        jump apprenticesIntro
    return

label victimIntro:
    $ wife.say("Dojdu pro něj, pojďte zatím dál.")
    "" "(Okradený mistr) vejde do místnosti s výrazem jako by se napil kyselého piva."
    if "burned evidence seen" in workshopChecked:
        $ victim.say("Už víš, kdo se opovážil hodit moje dílo do mého vlastního krbu?")
    else:
        $ victim.say("Neseš mi zpátky můj ztracený výrobek?")
    if "carrying key" in status:
        $ mc.say("Zatím ne, ale nesu vám od (přítele) zpět klíč od vaší dílny.")
        jump returningKey
    else:
        if gender == "M":
            $ mc.say("Zatím ne, ale dělám vše pro to, abych ho našel. Můžu vám ještě položit pár otázek?")
        else:
            $ mc.say("Zatím ne, ale dělám vše pro to, abych ho našla. Můžu vám ještě položit pár otázek?")
    # sent for key and not bringing it
    if "retrieving workshop key" in status:
        $ victim.say("A co ten klíč, který jsi slíbil donést?")
        if gender == "M":
            $ mc.say("Ještě jsem se pro něj nedostal…")
        else:
            $ mc.say("Ještě jsem se pro něj nedostala…")
        if time.days == 1 and time.hours < 17:
            if gender == "M":
                $ victim.say("A to si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co? Kdybys to nesliboval, mohl jsem si za (přítelem) dojít sám.", "angry")
            else:
                $ victim.say("A to si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co? Kdybys to neslibovala, mohl jsem si za (přítelem) dojít sám.", "angry")
            $ victim.trust -= 1
        else:
            $ victim.say("Tak už se neobtěžuj. Už jsem si za (přítelem) došel sám a vyzvedl si ho osobně.", "angry")
            $ victim.say("To si myslíš, že když se ztratil můj mistrovský výrobek, můžu teď nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            $ victim.trust -= 3
            $ status.remove("retrieving workshop key")
        $ mc.say("Těch pár otázek…?")
        $ victim.say("Mám sto chutí tě rovnou vyhodit… ale ptej se.", "angry")
    jump victimMain
    return

label victimMain:
    $ origAsked = victimAsked.copy()
    call victimOptions
    $ time.addMinutes((len(victimAsked) - len(origAsked)) * 3)
    return


label wifeIntro:
    $ wifeNote.isActive = True
    $ wife.say("Mně? Samozřejmě ráda pomůžu, ale já do manželovy dílny nechodím ani uklízet.")

    call wifeOptions
    return

label sonIntro:
    $ sonNote.isActive = True
    $ wife.say("Bude myslím někde s učedníky. Zatím pojďte dál, zavolám vám ho.")
    return

label apprenticesIntro:
    $ apprentice1Note.isActive = True
    $ apprentice2Note.isActive = True
    $ wife.say("Zatím pojďte dál a já vám je zavolám.")
    return

label daughterIntro:
    $ daughterNote.isActive = True
    $ wife.say("Nejsem si jistá, jestli bude zrovna ona něco vědět… ale jak chcete. Pojďte dál a já vám ji zavolám.")
    return

label workshopIntro:
    $ wife.say("Tam vás musí pustit manžel, já tam nesmím ani uklízet. Dojdu mu říct.")
    jump workshopController
    return

label returningKey:
    if "retrieving workshop key" in status:
        # sent for key and on time
        if time.days == 1 and time.hours < 16 and time.minutes < 20:
            $ victim.trust += 1
            "" "(Okradený) si klíč převezme s úsměvem, za kterým je vidět mírné překvapení."
            $ victim.say("Vida, hlídka přeci jen k něčemu je. Za ušetření cesty děkuju, ale teď se vrať ke své práci a najdi toho zloděje.", "happy")
            call guildmasterReminder
        # sent for key and a little late
        elif time.days == 1 and time.hours < 17:
            "" "(Okradený) si klíč převezme, ale jeho výraz se velmi brzy změní zpět na zamračený."
            $ victim.say("No ale že ti to trvalo. A teď se vrať ke své práci a najdi toho zloděje.")
            call guildmasterReminder
        # sent for key and very late
        else:
            $ victim.trust -= 3
            "" "Když vidí klíč v tvé ruce, (okradený) se zamračí ještě víc než předtím."
            if gender == "M":
                $ victim.say("“Kde všude ses s klíčem od mé dílny poflakoval? Když jsem tě pro něj poslal, myslel jsem, že mi ho opravdu přineseš.", "angry")
                $ victim.say("Dokonce jsem za (přítelem) zašel sám, ale ten mi řekl, že už jsi tam byl. A jenom ses neobtěžoval dojít až za mnou. To si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            else:
                $ victim.say("“Kde všude ses s klíčem od mé dílny poflakovala? Když jsem tě pro něj poslal, myslel jsem, že mi ho opravdu přineseš.", "angry")
                $ victim.say("Dokonce jsem za (přítelem) zašel sám, ale ten mi řekl, že už jsi tam byla. A jenom ses neobtěžovala dojít až za mnou. To si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            call apologyForLateness
    else:
        # not sent for key and on time
        if time.days == 1 and time.hours < 17:
            $ victim.trust += 1
            "" "(Okradený) vejde do místnosti s mírně zmateným výrazem, ale jakmile zahlédne klíč, téměř ti ho vytrhne z ruky."
            if gender == "M":
                $ victim.say("To je klíč od mé dílny! Jak ses k němu dostal?")
            else:
                $ victim.say("To je klíč od mé dílny! Jak ses k němu dostala?")
            $ mc.say("Posílá mě s ním (přítel). Prý by přišel sám, ale je mu špatně.")
            $ victim.say("No dobře. Tak děkuju, ale teď se vrať ke své práci a najdi toho zloděje.", "happy")
            call guildmasterReminder
        # not sent for key and very late
        else:
            $ victim.trust -= 2
            "" "(Okradený) ti klíč skoro vytrhne z ruky, ale pak se zamračí ještě víc."
            $ victim.say("Co děláš s klíčem od mojí dílny?", "angry")
            $ mc.say("(Přítel) ho měl u sebe a napadlo mě…")
            $ victim.say("“A kdo se tě prosil o takové nápady? Když jsem konečně našel čas za (přítelem) dojít, řekl mi, že můj klíč předal náhodnému strážnému. Který se očividně neobtěžoval dojít až za mnou.", "angry")
            $ victim.say("To si myslíš, že můžu nechat svou dílnu odemčenou celý den, nebo co?", "angry")
            call apologyForLateness
    # status update
    $ status.remove("carrying key")
    if "retrieving workshop key" in status:
        $ status.remove("retrieving workshop key")
    $ status.append("key delivered")
    # leave or questions
    show mcPic at menuImage
    menu:
        "Vrátím se k případu.":
            $ victim.say("To je to nejlepší, co můžeš udělat.")
            $ time.addMinutes(5)
            return
        "Můžu vám ještě položit pár otázek?":
            if victim.trust > -2:
                $ victim.say("Když to musí být… tak se ptej.")
            else:
                $ victim.say("Mám sto chutí tě rovnou vyhodit… ale ptej se.", "angry")
            jump victimMain
    return

label victimOptions:
    call victimOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Děkuji, to je všechno.")
        $ victim.say("Tak hlavně pohni, slavnosti jsou už za chvíli a já tam pořád nemám co představit.")
        return

    show mcPic at menuImage
    menu:
        "Můžete mi popsat ztracenou věc?" if "shoes description" not in clues:
            hide mcPic
            $ clues.append("shoes description")
            $ victimAsked.append("shoes description")
            $ victim.say("Jsou to nádherné dámské střevíce z nejjemnější kůže. Precizně tvarované, složité šněrování, barvené drahou fialovou barvou. Zlaté stuhy a jemné zdobení. Druhé takové ve městě určitě nejsou.")
        "Máte ve městě s někým spory?" if "enemies" not in victimAsked:
            hide mcPic
            $ victimAsked.append("enemies")
            $ victim.say("S každým, kdo si dostatečně neváží mé práce. (Cechmistr) ví, že ho chci nahradit v čele cechu a bojí se o svoje teplé místečko, (konkurent) si brousí zuby na tu samou židli, i když na to nemá schopnosti… no a potom kdokoli mi hází klacky pod nohy.")
            $ victim.say("Ale největší důvod znemožnit mě na slavnostech mají myslím tihle dva.")
            $ competitorNote.isActive = True
        "Slyšel jsem, že jste vyhodil několik učedníků?" if "enemies" in guildmasterAsked and "fired apprentices" not in victimAsked and gender == "M":
            hide mcPic
            $ victimAsked.append("fired apprentices")
            $ victim.say("A co jiného jsem s nimi měl dělat, když nesplnili ani základní očekávání? Tak dobře mi jejich rodiče nezaplatili.")
        "Slyšela jsem, že jste vyhodil několik učedníků?" if "enemies" in guildmasterAsked and "fired apprentices" not in victimAsked and gender == "F":
            hide mcPic
            $ victimAsked.append("fired apprentices")
            $ victim.say("A co jiného jsem s nimi měl dělat, když nesplnili ani základní očekávání? Tak dobře mi jejich rodiče nezaplatili.")
        "Co konkrétně provedli?" if "fired apprentices" in victimAsked and "fired apprentices offense" not in victimAsked:
            hide mcPic
            $ victimAsked.append("fired apprentices offense")
            "" "DEBUG: TBD"
        "Víte, kde je najít?" if "fired apprentices" in victimAsked and "fired apprentices" not in clues:
            hide mcPic
            $ victimAsked.append("fired apprentices location")
            $ clues.append("fired apprentices")
            $ victim.say("Jednoho si vzal k sobě (vynálezce). Fakt nevím, co z toho má, je dost schopný na to, aby si mohl vybírat.")
            $ victim.say("Ty druhé dva nikdo rozumný nechtěl. Jeden šel pryč z města, teď je myslím v Sehnau, nebo někde tím směrem. Ten třetí… zkuste to v dočasné čtvrti, mezi ostatními budižkničemy.")
            $ firedApprentice1Note.isActive = True
            $ firedApprentice2Note.isActive = True
        "Kde by se vaše ukradené boty daly nejlépe prodat?" if "best sale" not in victimAsked:
            hide mcPic
            $ victimAsked.append("best sale")
            $ victim.say("V jiném městě. Tady mou práci všichni znají, každý kupec by měl otázky.")
            $ victim.say("Ale jsem si dost jistý, že o peníze nešlo. V dílně mám drahý materiál, spoustu dalších bot a jiných věcí a to všechno tam zůstalo.")
        "Děkuji, to je všechno.":
            hide mcPic
            $ victim.say("Tak hlavně pohni, slavnosti jsou už za chvíli a já tam pořád nemám co představit.")
            return
    jump victimOptions

label wifeOptions:
    call wifeOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Děkuji vám za trpělivost.")
        $ wife.say("Pokud to pomůže najít manželův výrobek…")
        return

    show mcPic at menuImage
    menu:
        "Všimla jste si včera v noci něčeho nebo někoho podezřelého?" if "anything suspicious" not in wifeAsked:
            hide mcPic
            $ wifeAsked.append("anything suspicious")
            if gender == "M":
                "" "(Manželka) se nadechne a pak se rozohní víc, než jsi ji měl zatím možnost vidět."
            else:
                "" "(Manželka) se nadechne a pak se rozohní víc, než jsi ji měla zatím možnost vidět."
            $ wife.say("Jediné podezřelé individuum, kterého jsem si všimla, byl manžel.", "angry")
            $ wife.say("Že se z hospody vrátí až někdy nad ránem a vzbudí mě hlukem jako kdyby boural dílnu, to je jedna věc. Ale že mu to nestačí, vypije potom ještě v noci víc než půlku domácího baru, včetně těch opravdu dobrých lahví pro návštěvy, a ještě ty prázdné lahve někam zašantročí, to už je moc.", "angry")
            $ wife.say("A navíc dělá, že si nic nepamatuje, a popírá to, prase jedno.", "angry")
            $ clues.append("lost bottles")
        "Po odchodu vašeho muže v dílně nikdo nebyl?" if "workshop empty" not in wifeAsked:
            hide mcPic
            $ wifeAsked.append("workshop empty")
            $ wife.say("Myslím, že ne. Ale jak jsem říkala, já tam nechodím.")
        "Kdo všechno žije ve vaší domácnosti?" if "family" not in victimAsked and "family" not in wifeAsked:
            hide mcPic
            $ wifeAsked.append("family")
            $ wife.say("Kromě naší rodiny ještě dva učedníci.")
            $ mc.say("A rodina znamená…?")
            $ wife.say("Manžel, já a naše dvě děti, (syn) a (dcera).")
        "Pamatujete si na ty učedníky, které váš mistr propustil?" if "fired apprentices" not in wifeAsked:
            hide mcPic
            $ wifeAsked.append("fired apprentices")
            "" "DEBUG: TBD"
        "Děkuji vám za trpělivost.":
            hide mcPic
            $ wife.say("Pokud to pomůže najít manželův výrobek…")
            return
    jump wifeOptions
    return


label boys:
    "" "DEBUG: Rozhovor se synem a učedníkem"
    if "privacy" in status:
        "" "DEBUG: Máte soukromí."
    else:
        "" "DEBUG: Mistr se na vás mračí."

    if "boys seen" in status:
        $ status.remove("boys seen")
    $ status.append("boys met")
    return

###

label guildmasterReminder:
    if gender == "M":
        $ victim.say("Už jsi vyslechl (cechmistra)?")
    else:
        $ victim.say("Už jsi vyslechl/a (cechmistra)?")
    if "guildmaster met" in status:
        $ mc.say("Ano, ale sleduji všechny stopy, na které narazím.")
    else:
        $ mc.say("Nejdřív se na něj chci pořádně připravit.")
    return

label apologyForLateness:
    if gender == "M":
        $ mc.say("Omlouvám se, zabral jsem se do vyšetřování…")
    else:
        $ mc.say("Omlouvám se, zabrala jsem se do vyšetřování…")
    $ victim.say("Znamená to, že zloděje už máš?", "angry")
    $ mc.say("Ještě ne, ale…")
    $ victim.say("Tak se přestaň flákat a najdi ho.", "angry")
    return

label victimOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "shoes description" not in clues:
        $ optionsRemaining += 1
    if "enemies" not in victimAsked:
        $ optionsRemaining += 1
    if "enemies" in guildmasterAsked and "fired apprentices" not in victimAsked and gender == "M":
        $ optionsRemaining += 1
    if "enemies" in guildmasterAsked and "fired apprentices" not in victimAsked and gender == "F":
        $ optionsRemaining += 1
    if "fired apprentices" in victimAsked and "fired apprentices offense" not in victimAsked:
        $ optionsRemaining += 1
    if "fired apprentices" in victimAsked and "fired apprentices" not in clues:
        $ optionsRemaining += 1
    if "best sale" not in victimAsked:
        $ optionsRemaining += 1
    return

label wifeOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "anything suspicious" not in wifeAsked:
        $ optionsRemaining += 1
    if "workshop empty" not in wifeAsked:
        $ optionsRemaining += 1
    if "family" not in victimAsked and "family" not in wifeAsked:
        $ optionsRemaining += 1
    if "fired apprentices" not in wifeAsked:
        $ optionsRemaining += 1
    return
