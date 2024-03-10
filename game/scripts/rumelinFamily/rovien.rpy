label rovienController:
    $ origAsked = rovien.asked.copy()
    call rovienHouseInside
    if rovien.alreadyMet == False:
        call rovienFirst
    else:
        call rovienAgain
    call rovienOptions

    # adjust time spent
    $ rovien.alreadyMet = True
    $ time.addMinutes((len(rovien.asked) - len(origAsked)) * 3)
    return

label rovienFirst:
    $ rovien.say("Jak můžu být hlídce nápomocný?")
    return

label rovienAgain:
    $ rovien.say("Můžu pro hlídku ještě něco udělat?")
    return

label rovienOptions:
    call rovienOptionsRemainingCheck
    if rovienOptionsRemaining == 0 and zairisOptionsRemaining == 0:
        $ mc.say("To jsou všechny otázky, děkuji za váš čas.")
        return

    call zairisOptionsRemainingCheck
    show mcPic at menuImage
    menu:
        "Byl jste včera večer se svým bratrem v hospodě U Salmy?" if ("alibi details" in rumelin.asked or "rumelin alibi" in salma.asked) and "rumelin alibi" not in rovien.asked:
            hide mcPic
            $ rovien.asked.append("rumelin alibi")
            $ rovien.say("Jen později večer. Měl jsem předtím ještě vlastní obchodní jednání.")
            $ mc.say("Ale odešli jste spolu?")
            $ rovien.say("To ano. Poté, co se Rumelin uklidnil. Podle toho, co jsem pochopil, se před mým příchodem pohádali s Heinrichem a Heinrich ho napadl.")
            $ rovien.say("Šli jste rovnou domů? Tušíte, kolik mohlo být hodin?")
            $ rovien.say("Ano, rozloučili jsme se u jeho dveří.")
            $ rovien.say("Od Salmy jsme myslím odcházeli něco před půlnocí a vzali jsme to delší cestou, Rumelin si chtěl vyčistit hlavu.")
            $ rovien.say("Jsou to všechny nutné otázky, nebo máte ještě něco?")
        "Máte nějaké neshody s mistrem Njalem?" if "less deals details" in njal.asked and "njal deals" not in rovien.asked:
            hide mcPic
            $ rovien.asked.append("njal deals")
            $ rovien.say("Nic mě nenapadá, proč se ptáte?")
            $ mc.say("Slyšel[a] jsem, že jste mu odmítl prodat materiál na jeho práci.")
            "Rovien se zarazí."
            $ rovien.say("To nebylo... nic osobního. Jen...")
            if "AML" in lotte.asked:
                $ mc.say("Je možné, že to byl nápad vašeho bratra?")
                $ rovien.say("Ano, přesně. Rumelin se rozhodl, že některý luxusní materiál bude lepší nakupovat pro celý cech najednou, do společného skladu. To je všechno.")
            else:
                $ rovien.say("Rumelin se rozhodl, že některý luxusní materiál bude lepší nakupovat pro celý cech najednou, do společného skladu. To je všechno.")
            $ mc.say("Takže mistr Njal není jediný, komu jste přestal materiál dodávat?")
            "Rovien na chvíli zaváhá."
            $ rovien.say("Mistr Njal je jediný, kdo si stěžoval.")
        "Našel si váš syn děvče?" if "Zairis suggested as Ada's boyfriend" in clues and "Zairis and Ada" not in rovien.asked and "Zairis girlfriend" not in rovien.asked:
            hide mcPic
            $ rovien.asked.append("Zairis girlfriend")
            $ rovien.say("Zairis? Vlastně nevím. Pořád píše básně, ale jestli nějaké dívce, nebo třeba měsíci, těžko říct.")
            $ rovien.say("Proč se vlastně ptáte? Můj syn je slušný mladý muž, rozhodně by nedělal žádné nepřístojnosti.")
            show mcPic at menuImage
            menu:
                "Nepřímo to souvisí s případem, na kterém teď pracuji.":
                    hide mcPic
                    $ rovien.say("S botami mistra Heinricha?")
                    if "njal deals" in rovien.asked:
                        $ rovien.say("Nebo s vaším podezřením ohledně mistra Njala, ať už tím míříte kamkoli?")
                        $ mc.say("Jde hlavně o ty boty.")
                    $ mc.say("Snažím se pochopit, kdo se kde pohyboval a kdo s kým mluvil a tím zúžit okruh podezřelých.")
                    $ rovien.say("To zní složitě. Napadlo vás, že možná jen Heinrich slavil předčasně, jeho výrobek měl nějakou vadu a teď se to snaží zakrýt?")
                    $ mc.say("I to je samozřejmě možnost, se kterou pracuji.")
                "Mám podezření, že kvůli jedné dívce způsobil malér.":
                    hide mcPic
                    $ rovien.say("Prosím? Tak to by mě hodně zajímalo, o co se má jednat.", "angry")
                    $ rovien.say("O rvačku určitě nejde, o tom by se mluvilo, a jestli s ním někdo čeká dítě, není to žádný malér, ale dar od bohů. Spousta elfů se o dítě musí snažit mnoho let.")
                    $ mc.say("Je to složitější a možná se také vůbec nic nestalo.")
                    $ rovien.say("A nebylo by potom lepší se věnovat nějaké skutečné práci?")
        "Mohlo by něco být mezi vaším synem a dcerou mistra Heinricha?" if "Zairis suggested as Ada's boyfriend" in clues and "Zairis and Ada" not in rovien.asked:
            hide mcPic
            $ rovien.asked.append("Zairis and Ada")
            $ rovien.say("To by rozhodně nemohlo.", "angry")
            $ rovien.say("Nejenom, že bych něco takového v žádném případě nedovolil, ale Zairis je sice romantik posedlý Amadisem, ale není úplný blázen. A už vůbec ne úplný hlupák. Moc dobře ví, že se od něj bude čekat založení rodiny.", "angry")
            $ rovien.say("A kdyby přeci jen... promluvím si s ním a pak už mezi nimi nic nebude.")
        "Můžu si ještě promluvit s vaším synem?" if zairisOptionsRemaining > 0:
            hide mcPic
            $ rovien.say("Pokud to pomůže vašemu vyšetřování, tak jistě.")
            "Rovien přivede svého syna Zairise a sám se diskrétně vzdálí."
            jump zairisController
        "To jsou všechny otázky, děkuji za váš čas.":
            hide mcPic
            return
    jump rovienOptions

###

label rovienOptionsRemainingCheck:
    $ rovienOptionsRemaining = 0
    if ("alibi details" in rumelin.asked or "rumelin alibi" in salma.asked) and "rumelin alibi" not in rovien.asked:
        $ rovienOptionsRemaining += 1
    if "less deals details" in njal.asked and "njal deals" not in rovien.asked:
        $ rovienOptionsRemaining += 1
    if "Zairis suggested as Ada's boyfriend" in clues and "Zairis and Ada" not in rovien.asked and "Zairis girlfriend" not in rovien.asked:
        $ rovienOptionsRemaining += 1
    if "Zairis suggested as Ada's boyfriend" in clues and "Zairis and Ada" not in rovien.asked:
        $ rovienOptionsRemaining += 1
    return
