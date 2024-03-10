label lotteController:
    # check if visit makes sense
    call lotteOptionsRemainingCheck
    if lotteOptionsRemaining == 0:
        "Nenapadá tě, co dalšího se Lotte ještě ptát."
        return
    if currentLocation != "victim street":
        call preludeController

    # walk over
    if currentLocation != "victim house" or currentLocation != "victim street":
        $ time.addMinutes(15)
        $ currentLocation = "victim street"
        scene bg exterior02
    $ origAsked = lotte.asked.copy()

    if lotte.alreadyMet == False:
        if chosenChar == "merchant":
            call merchantFirst
        else:
            call lotteFirst
    else:
        if chosenChar == "merchant":
            "Hledání Karstenova domu tě zavede do stejné ulice, kde žije mistr Heinrich, a pak ke dveřím, kde jsi mluvil[a] s černovlasou sousedkou Lotte."
        call lotteAgain
    call lotteOptions

    $ time.addMinutes((len(lotte.asked) - len(origAsked)) * 3)
    if lotte.alreadyMet == False:
        $ time.addMinutes(10)
        $ lotte.alreadyMet = True
    $ lastSpokenWith = "Lotte"
    if chosenChar == "merchant" and lotteNote.isActive == False:
        $ merchantNote.isActive = False
        $ lotteNote.isActive = True
    return

label lotteFirst:
    "V dalších několika domech buď na klepání nikdo neodpoví, nebo se tam nedozvíš nic nového. Až skoro na konci ulice ti otevře energicky působící černovláska."
    $ lotte.say("Jestli jdete kvůli obchodu, manžel se vrátí až na Einionovy slavnosti.")
    $ mc.say("Jsem z městské hlídky, kvůli krádeži v dílně mistra Heinricha.")
    label lotteTheftRoute:
    "Neunikne ti ženin výraz zájmu."
    $ lotte.say("Ale ne. Co se ztratilo?", "happy")
    show mcPic at menuImage
    menu:
        "Jeho mistrovský výtvor na slavnosti.":
            hide mcPic
            "Ženiny očí se rozšíří překvapením a koutky se jí na moment pohnou směrem nahoru, ale pak zase zvážní."
            $ lotte.say("A myslíte, že to byl záměr? Že chtěl zloděj zabránit v jeho představení na slavnostech?")
            $ mc.say("Zatím to vypadá pravděpodobně. Můžu vám položit pár otázek?")
        "Na tom tak moc nezáleží. Můžu vám položit pár otázek?":
            hide mcPic
    $ lotte.say("Samozřejmě, ráda odpovím.")
    $ mc.say("Nevšimla jste si dnes v noci kolem dílny něčeho podezřelého?")
    label lotteMainInfo:
    $ lotte.say("To jsem si všimla. Heinrich šel včera večer ven, nejspíš k Salmě. Tam on chodí často, to by nebylo nic divného, ale nějakou dobu potom přišel do domu cizí chlap a Lisbeth ho pustila dál.")
    $ mc.say("A vy myslíte, že to byl ten zloděj?")
    $ lotte.say("Nemyslím. Nebo možná byl, ale to není to hlavní. Myslím, že spolu mají poměr. Ten chlap a Lisbeth, ta dokonalá hospodyňka. Ne, že bych se jí divila, její manžel je ožrala a hrubián.", "happy")
    return

label lotteAgain:
    "Když tě paní domu uvidí, rozzáří se jí oči."
    if "secret lover identity" not in lotte.asked:
        $ lotte.say("Jak jde vaše pátrání? Už víte, kdo je ten záhadný milenec?", "happy")
        show mcPic at menuImage
        menu:
            "Zatím ne." if "secret lover" not in nirevia.asked:
                hide mcPic
                $ lotte.say("Škoda.")
            "Zřejmě mistr Kaspar, prý tráví s paní Lisbeth hodně času a rozumí si." if "secret lover" in nirevia.asked and "secret lover identity" not in clues:
                call loverRevealedToLotte
            "Kvůli tomu tady teď nejsem.":
                hide mcPic
                $ lotte.say("Škoda.")
        $ lotte.say("Můžu pro vás udělat něco jiného?")
    else:
        $ lotte.say("Jak vám můžu pomoci tentokrát?", "happy")

    return

label merchantFirst:
    "Hledání Karstenova domu tě zavede do stejné ulice, kde žije mistr Heinrich. Když zaklepeš na dveře, které ti ukázali, otevře ti energicky působící černovláska."
    $ lotte.say("Jestli jdete kvůli obchodu, manžel se vrátí až na Einionovy slavnosti.")
    $ mc.say("Váš manžel je Karsten?")
    $ lotte.say("Ano, potřebujete od něj něco?")
    if "other fights" in salma.asked or "less deals details" in njal.asked:
        show mcPic at menuImage
        menu:
            "Jsem z městské hlídky, kvůli krádeži v dílně mistra Heinricha.":
                hide mcPic
                jump lotteTheftRoute
            "Váš manžel se nedávno pohádal s mistrem Heinrichem?" if "other fights" in salma.asked:
                hide mcPic
                label lotteArgumentRoute:
                    "Žena se zamračí."
                    $ lotte.say("Kdo se ptá a proč?", "angry")
                    $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v jeho dílně.")
                    $ lotte.say("Znamená to, že ho podezříváte? Můj manžel by nikdy nic neukradl. A navíc ani není ve městě, před dvěma dny odjel pro zboží a vrátí se až na slavnosti.", "angry")
                    $ mc.say("Zajímám se o každou možnou stopu. Můžete mi prosím říct víc o té hádce?")
                    $ lotte.say("Heinrich mého muže neprávem osočil, přišli jsme kvůli tomu i o pár zákazníků. Jako kdyby můj muž mohl za to, že ten ožrala nerozumí svému vlastnímu řemeslu.", "angry")
                    $ mc.say("O co přesně šlo?")
                    $ lotte.say("Heinrich si objednal materiál na nějakou zvláštní zakázku, hodně konkrétní a celkem drahé zboží. Manžel všechno osobně zkontroloval. A Heinrich potom přišel s tím, že jeho boty nedrží tvar a že mu Karsten dodal zmetek.", "angry")
                    $ lotte.say("Protože pana mistra by ani ve snu nenapadlo, že by třeba chybu mohl udělat on.", "angry")
                    $ lotte.say("Seřval manžela v hospodě U Salmy, ten samozřejmě bránil svoje dobré jméno. Ale Heinrich ho stejně pomluvil a pár lidí mu uvěřilo.", "angry")
                    $ lotte.asked.append("husband")
                    $ lotte.asked.append("pub fight")
                    "Uhneš očima před ženiným pronikavým pohledem."
                    $ lotte.say("Je to všechno?")
                    $ mc.say("Děkuji vám za pomoc.")
            "Měl váš manžel nějaký konflikt s mistrem Njalem?" if "less deals details" in njal.asked:
                hide mcPic
                $ lotte.asked.append("AML")
                "Žena se zamračí."
                $ lotte.say("Kdo se ptá a proč?")
                $ mc.say("Jsem z městské hlídky a vyšetřuji krádež v dílně mistra Heinricha.")
                $ lotte.say("A jak s tou krádeží souvisí Njal a jeho obchody?")
                $ mc.say("To zatím nevím, ale pro jistotu sledujeme cokoli neobvyklého pro případ, že by tady souvislost byla.")
                $ mc.say(" Vypadá to, že podobných zrušených obchodů s mistrem Njalem bylo několik a cechmistr Rumelin některé ze svých nákupů materiálu přesunul mimo všechny hospody ve městě. Může to samozřejmě být náhoda, ale také se někdo může snažit poškodit ševcovský cech jako celek.")
                call lotteAML
                call lotteAmlOptions
    $ clues.append("Karsten away")
    "Obrátíš se k odchodu a pohled ti padne na dům mistra Heinricha a dveře vedoucí do jeho dílny. Vlastně odsud není špatný výhled, pokud by se někdo díval ve správnou chvíli. Otočíš se zpět na Lotte."
    $ mc.say("Můžu vás ještě na chvíli zdržet? Nevšimla jste si v noci kolem dílny mistra Heinricha něčeho podezřelého?")
    jump lotteMainInfo
    return

label lotteOptions:
    call lotteOptionsRemainingCheck
    if lotteOptionsRemaining == 0:
        $ mc.say("Nebudu vás už zdržovat")
        if "secret lover identity" not in lotte.asked:
            $ lotte.say("Nezdržujete. A jestli zjistíte, kdo byl ten milenec, určitě se zastavte.")
        else:
            $ lotte.say("Vůbec nezdržujete. Stavte se, až budete zase něco potřebovat, ráda zkusím pomoct.", "happy")
        return

    show mcPic at menuImage
    menu:
        "Víte, o koho šlo?" if "lover identity" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("lover identity")
            $ lotte.say("Bohužel ne. Byla tma a viděla jsem ho hlavně zezadu.")
        "A jste si opravdu jistá, že to nebyl mistr Heinrich? Mohl se pro něco vrátit." if "lover identity" in lotte.asked and "mistaken" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("mistaken")
            $ lotte.say("Poznám svého souseda. Tenhle chlap byl menší a měl světlejší vlasy než Heinrich, to bylo vidět i takhle večer. A tak, jak ho Lisbeth vítala, jsem ji vítat manžela ještě nikdy neviděla.")
        "Ničeho dalšího jste si nevšimla?" if "anything else" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("anything else")
            "Lotte se zamyslí."
            $ lotte.say("Ten tajemný muž byl myslím dobře oblečený, mohl to být taky obchodník.")
            $ mc.say("Myslím kromě toho muže?")
            $ lotte.say("Ne, to ne. Jinak tam chodili jenom učedníci. A já samozřejmě nesedím celé dny a noci u okna.")
            $ mc.say("To samozřejmě chápu, ptám se jenom kdyby náhodou.")
        "Váš manžel není doma?" if "other fights" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "husband" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("husband")
            $ lotte.say("Jel pro zboží, ale na slavnosti bude určitě zpátky.")
            $ mc.say("A můžu se zeptat, kdy odjel?")
            $ lotte.say("Před dvěma dny.")
            if "pub fight" not in lotte.asked:
                $ lotte.say("Proč? Potřebujete od něj něco?")
                $ mc.say("Jen jsem se ho chtěl[a] zeptat na mistra Heinricha.")
                $ lotte.say("O tom vám můžu dost říct i já.", "angry")
            $ clues.append("Karsten away")
        "Je pravda, že se váš muž s mistrem Heinrichem pohádal?" if "other fights" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "pub fight" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("pub fight")
            $ lotte.say("Heinrich mého muže neprávem osočil, přišli jsme kvůli tomu i o pár zákazníků. Jako kdyby můj muž mohl za to, že ten ožrala nerozumí svému vlastnímu řemeslu.", "angry")
            $ mc.say("O co šlo?")
            $ lotte.say("Heinrich si objednal materiál na nějakou zvláštní zakázku, hodně konkrétní a celkem drahé zboží. Manžel všechno osobně zkontroloval. A Heinrich potom přišel s tím, že jeho boty nedrží tvar a že mu Karsten dodal zmetek.", "angry")
            $ lotte.say("Protože pana mistra by ani ve snu nenapadlo, že by třeba chybu mohl udělat on.", "angry")
            $ lotte.say("Seřval manžela v hospodě U Salmy, ten samozřejmě bránil svoje dobré jméno. Ale Heinrich ho stejně pomluvil a pár lidí mu uvěřilo.", "angry")
        "Kde jste byla včera v noci vy?" if "other fights" in salma.asked and "husband" in lotte.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "alibi" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("alibi")
            $ lotte.say("Doma, samozřejmě.")
            $ mc.say("Žije s vámi ještě někdo další? Máte děti?")
            $ lotte.say("Nemáme. Proč? To jsem podezřelá?", "angry")
            $ mc.say("Ptám se jenom pro úplnost.")
        "Měl váš manžel nějaký konflikt s mistrem Njalem?" if "less deals details" in njal.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "AML" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("AML")
            $ lotte.say("Nevím o tom, proč se ptáte?")
            $ mc.say("Slyšel[a] jsem, že domlouvali nějaký obchod, ze kterého pak sešlo.")
            $ lotte.say("Můžu se asi podívat do účetní knihy nebo jiných poznámek, možná se manžel prostě v něčem spletl. Je nějaký důvod, proč jeden zrušený obchod řeší městská hlídka?")
            if "less deals checked" in status:
                $ mc.say("Sledujeme cokoli neobvyklého pro případ, že by to souviselo s tou krádeží. Vypadá to, že podobných zrušených obchodů s Njalem bylo několik a cechmistr Rumelin některé ze svých nákupů materiálu přesunul mimo všechny hospody ve městě.")
            else:
                $ mc.say("Sledujeme cokoli neobvyklého pro případ, že by to souviselo s tou krádeží. Vypadá to, že podobných zrušených obchodů s Njalem bylo několik a cechmistr Rumelin některé ze svých nákupů materiálu přesunul přinejmenším ze Salmina hostince.")
            $ mc.say("Může to samozřejmě být náhoda, ale také se někdo může snažit poškodit ševcovský cech jako celek.")
            call lotteAML
        "Uzavřel váš manžel v poslední době nějaký obchod s cechmistrem Rumelinem na nákup materiálu?" if "less deals" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "AML" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("AML")
            $ lotte.say("Možné to je, musela bych to ověřit v účetní knize. Proč se ptáte?")
            if "less deals checked" in status:
                $ mc.say("V souvislosti s krádeží u mistra Heinricha se hlídka zajímá o cokoli neobvyklého a zdá se, že mistr Rumelin nákupy dražšího materiálu přesunul mimo všechny hospody ve městě.")
            else:
                $ mc.say("V souvislosti s krádeží u mistra Heinricha se hlídka zajímá o cokoli neobvyklého a zdá se, že mistr Rumelin nákupy dražšího materiálu přesunul přinejmenším ze Salmina hostince.")
            $ lotte.say("Podezříváte ho z něčeho nezákonného?")
            $ mc.say("Spíš se snažím zjistit, jestli se někdo nesnaží poškodit ševcovský cech jako celek. Zvláštní problémy s nákupem materiálu má i mistr Njal.")
            call lotteAML
        "Zdůvodnil to mistr Rumelin nějak?" if "AML" in lotte.asked and "rumelin reasons" not in lotte.asked:
            hide mcPic
            call lotteRumelinReasons
        "Nenapadlo vás jít s tím za hlídkou?" if "rumelin reasons" in lotte.asked and "why not call police" not in lotte.asked:
            hide mcPic
            call lottePoliceBusiness
        "Všimla jste si, jak včera kousek odtud hořelo?" if "fireshow" in status and "fireshow" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("fireshow")
            $ lotte.say("Samozřejmě, to představení jsem viděla a pak jsem pomáhala hasit.")
            $ lotte.say("Ta holka měla docela úspěch, než vytáhla oheň. Kdyby si to takhle hloupě nezkazila, mohla si přes slavnosti pěkně vydělat nebo si najít bohatého patrona.")
            $ lotte.say("Co ale potřebujete ode mě?")
        "Víte, že teď je ve vězení a bude souzena za žhářství?" if "fireshow" in lotte.asked and "dancer arrested" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("dancer arrested")
            $ lotte.say("To je dobře. Nemůžeme přece dovolit, aby si každý ve městě hrál s ohněm, jak ho napadne.")
        "Považujete ji vy sama za žhářku, která zaslouží potrestat?" if "dancer arrested" in lotte.asked and "dancer arrest deserved" not in lotte.asked and "peer pressure" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("dancer arrest deserved")
            $ lotte.say("Vytáhla na ulici oheň a málem způsobila požár. Jestli zaslouží potrestat, to je na soudu, ne na mně, ale nemyslím, že ji městská rada jen tak pustí.")
            if "dancer arsonist" not in lotte.asked:
                call lotteArsonist
        "Byla byste ochotná svědčit v její prospěch?" if "dancer arrested" in lotte.asked and ("dancer arsonist" not in lotte.asked or "dancer innocent" in lotte.asked) and "testify for dancer" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("testify for dancer")
            $ status.append("helping Katrin")
            if "dancer innocent" in lotte.asked:
                "Lotte zaváhá."
                $ lotte.say("Pořád ji za žhářku považuje většina mých sousedů. Jestli se za ni postavím, mohlo by se to obrátit proti mně.")
                $ lotte.asked.append("peer pressure")
            else:
                $ lotte.say("Prosím? Svědčit ve prospěch žhářky?")
                show mcPic at menuImage
                menu:
                    "Třeba to žhářka není.":
                        hide mcPic
                        $ lotte.say("Třeba není, třeba je. To přece právě posoudí ten soud, já to nevím, a tak pro ni těžko můžu svědčit. Můžu říct, co jsem viděla: že chvíli tančila a potom vytáhla zapálený vějíř.")
                        call lotteArsonist
                    "Stačí, když řeknete, co jste viděla.":
                        hide mcPic
                        $ lotte.say("Můžu říct, že chvíli tančila a potom vytáhla zapálený vějíř. Ale nezaručuji, že to soud pochopí jako svědectví v její prospěch.")
                    "Proč myslíte, že to je žhářka?":
                        hide mcPic
                        $ lotte.say("Málem přece způsobila požár.")
                        call lotteArsonist
                if "dancer innocent" in lotte.asked:
                    $ mc.say("A budete tedy v její prospěch svědčit?")
                    "Lotte zaváhá."
                    $ lotte.say("Pořád ji za žhářku považuje většina mých sousedů. Jestli se za ni postavím, mohlo by se to obrátit proti mně.")
                    $ lotte.asked.append("peer pressure")
            if "peer pressure" in lotte.asked and "secret lover identity" in lotte.asked:
                $ lotte.say("Proč je to pro vás tak důležité?")
                label lotteDancerImportantToMc:
                show mcPic at menuImage
                menu:
                    "Hlídka by přece měla bojovat za spravedlnost. Trestat zločince, ale chránit nevinné.":
                        hide mcPic
                        $ lotte.say("Patří do toho i hledání ztracených bot a donášení na bohaté paničky?", "happy")
                        $ lotte.say("Je dobře, že nás chrání někdo, jako vy. Někomu takovému nemůžu odmítnout pomoc. Počítejte se mnou.", "happy")
                    "Prostě mi jí je líto. Měl by se za ni aspoň někdo postavit.":
                        hide mcPic
                        $ lotte.say("Ach tak, chápu. Mladá, hezká, dobře tančí, ta jednoho dokáže velmi snadno okouzlit. A ta vděčnost, jestli ji opravdu zachráníte...", "happy")
                        show mcPic at menuImage
                        menu:
                            "Takhle to není!":
                                hide mcPic
                                $ lotte.say("Vážně ne? Taková škoda. Byla by to romance jako z jarmarečního představení.", "happy")
                                $ lotte.say("Nebojte, u soudu vám pomůžu. A jestli kvůli ní opustíte hlídku a začnete o vašem seznámení hrát divadlo, doufám, že mě pozvete.")
                            "No hezká mi přijde, ale...":
                                hide mcPic
                                $ lotte.say("Ale podobné věci se nesmí uspěchat? To je rozumný přístup.", "happy")
                                $ lotte.say("Nebojte, u soudu vám pomůžu. A vy pak budete mít spoustu času.", "happy")
                            "To soudíte podle sebe?":
                                hide mcPic
                                $ lotte.trust += 1
                                "Lotte se zvonivě zasměje."
                                $ lotte.say("Já mám manžela. Vodit si domů hezkou holku mladší než já by se mi mohlo nepěkně vymstít.", "happy")
                                $ lotte.say("Ale nebojte, u soudu vám pomůžu. Co kdybych někdy změnila názor, že ano.")
                    "Protože i chudina jako ona by měla mít nějaké zastání.":
                        hide mcPic
                        $ lotte.say("Nějaké ano, jen bychom to neměli přehánět. Aby jednoho dne nechtěli třeba mluvit do vlády nad městem. To by nedopadlo dobře.")
                        $ lotte.say("Ale rozumím. Kdyby ta tanečnice byla známá a bohatá, hrozilo by jí popraviště mnohem méně. K tomu soudu půjdu a promluvím tam v její prospěch. Z našeho přátelství.")
                $ lotte.asked.append("testimony promised")
                $ katrin.cluesAgainst += 1
        "Je pro vás názor sousedů tak důležitý?" if "peer pressure" in lotte.asked and "peer pressure important" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("peer pressure important")
            $ lotte.say("Jsme s manželem obchodníci. Jestli se proti nám lidi obrátí, ztratíme výdělek a přijdeme na mizinu.")
            $ lotte.say("Před pár dny navíc manžela pomluvil Heinrich. Ne všichni mu věřili, ale kdyby se k tomu přidalo obhajování domnělého zločince, určitě by to s kdekým pohnulo.")
        "Kdekdo by naopak ocenil vaši odvahu." if "peer pressure" in lotte.asked and "courage" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("courage")
            $ lotte.say("Tady jsme v Marendaru, na cokoli kolem zakládání ohně jsme tu všichni opravdu citliví. Jestli by to vůbec někdo ocenil, bylo by takových hodně málo.")
        "Můžu pro vás něco udělat na oplátku." if "peer pressure" in lotte.asked and "dancer deal" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("dancer deal")
            $ lotte.say("O obchodu mluvit můžeme. Co máte na mysli?")
            call lotteDancerDealOptions
        "Nebudu vás už zdržovat.":
            hide mcPic
            if "secret lover identity" not in lotte.asked:
                $ lotte.say("Nezdržujete. A jestli zjistíte, kdo byl ten milenec, určitě se zastavte.")
            else:
                $ lotte.say("Vůbec nezdržujete. Stavte se, až budete zase něco potřebovat, ráda zkusím pomoct.", "happy")
            return
    jump lotteOptions

###

label lotteArsonist:
    $ lotte.asked.append("dancer arsonist")
    show mcPic at menuImage
    menu:
        "Aby byl někdo považovaný za žháře, musí se o založení požáru pokoušet úmyslně. Myslíte si, že ona takový úmysl měla?":
            hide mcPic
            $ lotte.say("Nevím. Ve skutečnosti asi ne. To by to nedělala před obecenstvem, nemyslíte?")
            $ mc.say("To jako žhářství nezní.")
            $ lotte.say("Ne. Nanejvýš hloupá neopatrnost.")
            $ mc.say("Jak nebezpečné to její vystoupení bylo?")
            $ lotte.say("Těžko soudit, moc z něj nestihla. Ale různými tyčemi a šátky mávala už předtím a vypadalo to, že ví, co dělá. Nemyslím, že by jí zrovna zapálený vějíř měl vyletět z rukou.")
            $ lotte.say("Na zemi také nic hořlavého nebylo, co si pamatuju. Už proto, že už předtím si na tanec musela udělat místo.")
            $ lotte.asked.append("dancer innocent")
        "Není vám jí líto?":
            hide mcPic
            $ lotte.say("Nevím, nepřemýšlela jsem o tom. Určitě má za sebou pohnutý osud, ale ten může v tomhle hrabství vyprávět každý druhý.")
            $ lotte.say("Můžu vám ještě nějak pomoct?")
        "Rozumím, už vás s ní tedy nebudu obtěžovat.":
            hide mcPic
            $ lotte.say("V pořádku. Můžu vám ještě nějak pomoct?")
    return

label loverRevealedToLotte:
    hide mcPic
    $ lotte.asked.append("secret lover identity")
    $ lotte.say("Kaspar? To je opravdu úžasná… chci říct, to vlastně dává smysl.", "happy")
    $ lotte.say("Co na to říkal Heinrich?")
    show mcPic at menuImage
    menu:
        "Zatím nic, ještě jsem se k němu nedostal[a]" if "secret lover identity" not in victim.asked:
            hide mcPic
            "Lotte trochu zklamaně pokrčí rameny."
            $ lotte.say("Chápu, hlídka musí mít spoustu práce.", "sad")
        "Že si to s Kasparem vyřídí." if "secret lover identity" in victim.asked:
            hide mcPic
            $ lotte.say("To se mu vůbec nedivím.")
            $ lotte.say("Mistr Kaspar má odvahu, konkurovat Heinrichovi v řemesle i v jeho vlastní posteli...", "happy")
        "Nevidím důvod se do toho vměšovat.":
            hide mcPic
            "Lotte trochu zklamaně pokrčí rameny."
            $ lotte.say("Chápu, hlídka musí mít spoustu práce.", "sad")
    return

label lotteAML:
    $ lotte.say("Myslíte, že mistr Rumelin by chtěl poškodit svůj vlastní cech?")
    $ mc.say("Za těmi zrušenými obchody stojí on?")
    $ lotte.say("Ano, skoupil veškeré zásoby některých druhů materiálu a požádal, aby manžel odmítl přesně tyhle věci komukoliv jinému před slavnostmi dovézt.")
    $ lotte.say("Zdálo se nám to s manželem trochu zvláštní, ale je to vlivný muž, manžel se neodvažoval otevřeně nesouhlasit.")
    return

label lotteAmlOptions:
    call lotteAmlOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Děkuji vám za pomoc.")
        return
    show mcPic at menuImage
    menu:
        "Zdůvodnil to mistr Rumelin nějak?" if "AML" in lotte.asked and "rumelin reasons" not in lotte.asked:
            hide mcPic
            call lotteRumelinReasons
        "Nenapadlo vás jít s tím za hlídkou?" if "rumelin reasons" in lotte.asked and "why not call police" not in lotte.asked:
            hide mcPic
            call lottePoliceBusiness
        "Děkuji vám za pomoc.":
            hide mcPic
    jump lotteAmlOptions

label lotteRumelinReasons:
    $ lotte.asked.append("rumelin reasons")
    $ rumelin.cluesAgainst += 1
    $ lotte.say("Prý chce zavést něco jako společný sklad na věci, které většina ševců potřebuje jen občas.")
    $ mc.say("A ten zákaz dovozu nového materiálu?")
    $ lotte.say("Tady si to spíš domýšlím, ale možná chtěl, aby ten sklad byl hned užitečný?")
    $ lotte.say("V každém případě nás mistr Rumelin prosil, ať celý plán udržíme v tajnosti až do slavností, kdy ho představí sám. Předpokládám, že tam to všem podrobně vysvětlí.")
    return

label lottePoliceBusiness:
    $ lotte.asked.append("why not call police")
    $ lotte.say("Kvůli tajnému projektu, kterým si chce mistr Rumelin pojistit znovuzvolení?","surprised")
    $ mc.say("Pořád tím zabránil jednomu ze členů svého cechu získat materiál, který potřeboval. To by mělo stát alespoň za prověření.")
    $ lotte.say("Upřímně řečeno nás nenapadlo, že by výpadek v dovážení materiálu mohl někomu tolik vadit. Vždyť šlo jen o pár dní do slavností.")
    $ lotte.say("A jestli to mistru Njalovi opravdu výrazně zkřížilo plány, určitě to řekne, až mistr Rumelin bude svůj plán představovat, a dost možná tím jeho naděje na znovuzvolení hodně utrpí.")
    $ lotte.say("Vy si myslíte, že by se hlídka o podobné věci měla zajímat?")
    show mcPic att menuImage
    menu:
        "Vlastně spíš ne. O obchodech by si měli měšťané rozhodovat sami.":
            hide mcPic
            $ solian.trust += 1
            $ watchScores["solian"] += 1
            $ lotte.say("Tak vidíte.")
        "Určitě. Hlídka by se měla zajímat o vše, v čem může vězet nějaká špinavost.":
            hide mcPic
            $ hayfa.trust += 1
            $ watchScores["hayfa"] += 1
            $ lotte.say("To by ovšem měla hlídka najmout mnohem víc členů a já nevím, z čeho je všechny budeme platit.")
        "Nevím. Nelíbí se mi to, ale zákon proti tomu asi není.":
            hide mcPic
            $ rauvin.trust += 1
            $ watchScores["rauvin"] += 1
            $ lotte.say("Není a asi máme důležitější věci, kterými by se rada měla zabývat. Tohle si opravdu nejlépe vyřídí ševci sami mezi sebou.")
    return

label lotteDancerDealOptions:
    call lotteDancerDealOptionsRemainingCheck
    if optionsRemaining == 0:
        $ mc.say("Nechme to pro tuto chvíli být.")
        $ lotte.say("Škoda, začínalo to vypadat, že se možná dostaneme k něčemu zajímavému.")
        return

    show mcPic at menuImage
    menu:
        "Prozradím vám, kdo byl ten tajemný milenec, který šel předevčírem k paní Lisbeth." if "offered gossip" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("offer gossip")
            if "secret lover identity" in victim.asked:
                $ lotte.say("Předpokládám, že to byl mistr Kaspar?")
                $ mc.say("Ano...")
                $ lotte.say("To teď ví už celé město. Když se Heinrich vzteká, je to obvykle dost slyšet.", "happy")
            else:
                "Lotte se krátce rozzáří oči, potom se ale vrátí k napjatému výrazu."
                $ lotte.say("Nebudu přece riskovat svou a manželovu pověst jen kvůli drbu, jakkoli zajímavému.")
        "Ten drb by právě mohl vaši pověst podpořit." if "offered gossip" in lotte.asked and "gossip worth" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("gossip worth")
            $ mc.say("Mistr Heinrich by tím ztratil na vážnosti a s tím i cokoli, co řekl o vašem muži. Když si nedokáže ohlídat ani vlastní manželku...")
            $ mc.say("A teď si představte, co kdyby se k němu doneslo, co se šušká, a on udělal něco unáhleného.")
            $ lotte.say("To by nejspíš udělal, to je pravda. Přemýšlení nikdy nebyla jeho silná stránka, natož předtím, než něco udělá.")
        "Milenec paní Lisbeth je zřejmě mistr Kaspar, prý tráví s paní Lisbeth hodně času a rozumí si." if "gossip worth" in lotte.asked and "secret lover" in nirevia.asked and "secret lover identity" not in clues:
            call lotteDealLoverRevealed
        "Milenec paní Lisbeth je mistr Kaspar, dokonce to i přiznal." if "gossip worth" in lotte.asked and "confession" in kaspar.asked and "confession" not in lisbeth.asked:
            call lotteDealLoverRevealed
        "Milenec paní Lisbeth je mistr Kaspar, Lisbeth to dokonce přiznala." if "gossip worth" in lotte.asked and "confession" not in kaspar.asked and "confession" in lisbeth.asked:
            call lotteDealLoverRevealed
        "Milenec paní Lisbeth je mistr Kaspar, dokonce to oba přiznali." if "gossip worth" in lotte.asked and "confession" in kaspar.asked and "confession" in lisbeth.asked:
            call lotteDealLoverRevealed
        "Co by tak pomohlo vašemu obchodu?" if "offered favour" not in lotte.asked:
            hide mcPic
            $ lotte.asked.append("offered favour")
            "Lotte povytáhne obočí."
            $ lotte.say("Nejdůležitější jsou známosti, ale těch předpokládám moc mít nebudete. Ne mezi obchodníky, se kterými bychom s manželem mohli spolupracovat.")
            $ lotte.say("Pak se ale také hodí vědět, jaké známosti mají ostatní. Jaké zboží přesně kdo dováží z jiných měst a za jakou cenu. A to byste už možná zjistit mohl[a].")
            $ lotte.say("Samozřejmě vás nenabádám, abyste pro mě opisoval[a] záznamy o vybraných clech. To by byl zločin. Ale jestli mi informace sdělíte, protože jsme přátelé a protože je náhodou víte od svých známých mimo město, budu velmi ráda.")
            $ lotte.say("Chci říct, rád bude hlavně manžel. On je tady ten obchodník.")
            label lotteDancerFavourOptions:
            show mcPic at menuImage
            menu:
                "Za to by mě Rauvin okamžitě vyrazil!" if "favour too risky" not in lotte.asked:
                    hide mcPic
                    $ lotte.asked.append("favour too risky")
                    $ lotte.say("Mít dobré známé mimo město snad není nic špatného? Ale ano, zrovna on by se o tom asi neměl dozvědět. Zbytečně by do toho šťoural a má určitě mnohem důležitější práci, jako třeba hledat Heinrichovo smetí.")
                "Nejsem si jist[y], jestli mám k těm... známým... přístup." if "favour hard" not in lotte.asked:
                    hide mcPic
                    $ lotte.say("Můžete se zkusit poptat i jiných hlídkařů. Pán de Vito to asi nepochopí, ale někdo jiný třeba ano.")
                "Dohodnuto. Zjistím, co potřebujete.":
                    hide mcPic
                    $ lotte.say("Výborně! Přijďte prosím s první várkou novinek ještě před soudem. Pochopte, potřebujeme se podle toho připravit na slavnosti.")
                    return
                "To bohužel nemůžu riskovat.":
                    hide mcPic
                    $ lotte.say("Škoda. Máte tedy něco jiného, na čem se můžeme dohodnout?")
                    jump lotteDancerDealOptions
            jump lotteDancerFavourOptions
        "Nechme to pro tuto chvíli být.":
            hide mcPic
            $ lotte.say("Škoda, začínalo to vypadat, že se možná dostaneme k něčemu zajímavému.")
            return
    jump lotteDancerDealOptions

label lotteDealLoverRevealed:
    call loverRevealedToLotte
    $ lotte.say("Hm, tohle je věc, kterou byste neřekl[a] jen tak někomu, že ne?", "happy")
    $ lotte.say("Přátelé si mají pomáhat vzájemně. Ale řekněte mi nejdřív, proč je pro vás vůbec tak důležitá", "happy")
    call lotteDancerImportantToMc
    return

###

label lotteOptionsRemainingCheck:
    $ lotteOptionsRemaining = 0
    if "lover identity" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "lover identity" in lotte.asked and "mistaken" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "anything else" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "other fights" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "husband" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "other fights" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "pub fight" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "other fights" in salma.asked and "husband" in lotte.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "alibi" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "less deals details" in njal.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "AML" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "less deals" in salma.asked and (chosenChar == "merchant" or lotteNote.isActive == True) and "AML" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "AML" in lotte.asked and "rumelin reasons" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "rumelin reasons" in lotte.asked and "why not call police" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "fireshow" in status and "fireshow" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "fireshow" in lotte.asked and "dancer arrested" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "dancer arrested" in lotte.asked and "dancer arrest deserved" not in lotte.asked and "peer pressure" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "dancer arrested" in lotte.asked and ("dancer arsonist" not in lotte.asked or "dancer innocent" in lotte.asked) and "testify for dancer" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "peer pressure" in lotte.asked and "peer pressure important" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "peer pressure" in lotte.asked and "courage" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    if "peer pressure" in lotte.asked and "dancer deal" not in lotte.asked and "secret lover identity" not in lotte.asked and "testimony promised" not in lotte.asked:
        $ lotteOptionsRemaining += 1
    return

label lotteAmlOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "AML" in lotte.asked and "rumelin reasons" not in lotte.asked:
        $ optionsRemaining += 1
    if "rumelin reasons" in lotte.asked and "why not call police" not in lotte.asked:
        $ optionsRemaining += 1
    return

label lotteDancerDealOptionsRemainingCheck:
    $ optionsRemaining = 0
    if "offered gossip" not in lotte.asked:
        $ optionsRemaining += 1
    if "offered gossip" in lotte.asked and "gossip worth" not in lotte.asked:
        $ optionsRemaining += 1
    if "gossip worth" in lotte.asked and "secret lover" in nirevia.asked and "secret lover identity" not in clues:
        $ optionsRemaining += 1
    if "offered favour" not in lotte.asked:
        $ optionsRemaining += 1
    return
