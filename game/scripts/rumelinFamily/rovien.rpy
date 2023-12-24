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
                $ rovien.say("Ano, přesně. Rumelin se rozhodl, že některý luxusní materiál bude lepší nakupovat pro celý cech najednou. To je všechno.")
            else:
                $ rovien.say("Rumelin se rozhodl, že některý luxusní materiál bude lepší nakupovat pro celý cech najednou. To je všechno.")
            $ mc.say("Takže mistr Njal není jediný, komu jste přestal materiál dodávat?")
            "Rovien na chvíli zaváhá."
            $ rovien.say("Mistr Njal je jediný, kdo si stěžoval.")
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
    return
