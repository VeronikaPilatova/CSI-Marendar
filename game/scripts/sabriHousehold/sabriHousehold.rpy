label sabriHouseholdController:
    # check if visit makes sense
    if "sabri's house visited" not in status:
        pass
    elif chosenChar == "zeran":
        call zeranOptionsRemainingCheck
        if zeranOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se Zerana ještě ptát."
            return
    elif chosenChar == "sabri":
        call sabriOptionsRemainingCheck
        if sabriOptionsRemaining == 0:
            "Nenapadá tě, co dalšího se Sabriho ještě ptát."
            return
    call preludeController

    # walk over
    if currentLocation != "sabri's house" and currentLocation != "cells":
        if "sabri's house visited" not in status:
            $ time.addMinutes(30)
        else:
            $ time.addMinutes(15)
        $ currentLocation = "sabri's house"

    # visit itself
    if "sabri's house visited" not in status:
        call sabriHouseFirst
    else:
        call sabriHouseAgain
    # if Zeran already met, skip Sabri
    if chosenChar == "zeran" and zeran.alreadyMet == True:
        jump zeranController
    else:
        call sabriController

    # adjust status
    if "sabri's house visited" not in status:
        $ status.append("sabri's house visited")
    return

label sabriHouseFirst:
    scene bg temporary quarter
    "Vydat se do dočasné čtvrti působí trochu jako návrat v čase. Během velkého požáru jsi sice ve městě nebyl[a], ale když procházíš kolem sežehnutých kamenných základů a zuhelnatělých trosek, dokážeš si zničující oheň představit až příliš živě."
    "Jiné části města jsou nově přestavěné, ale tady to vypadá, jakoby se nikdo nenamáhal ani opravami nebo stržením neobyvatelných budov. Až po chvíli si všimneš, že část obydlí je zřejmě nová a provizorně působící. To by tě možná mělo naplnit nadějí jako příslib lepší budoucnosti, ale přítomnost to nedělá méně bezútěšnou."
    "Místní sem obvykle nechodí, pokud opravdu nemusí a na lidech kolem tebe je znát, že nemají kam jinam jít."
    "Dotazy na Sabriho ubytovnu tě nakonec zavedou k většímu domu, který sice působí zanedbaně, ale je celý a vypadá stabilně."
    scene bg sabri outside
    return

label sabriHouseAgain:
    scene bg temporary quarter
    "Víš, co v dočasné čtvrti čekat, ale bezútěšné atmosféře místa bez přítomnosti se i tak brání těžko. Daleko víc než stav domů na tebe působí tváře lidí, kteří zřejmě nemají kam jinam jít."
    "Po chvíli konečně znovu stojíš přede dveřmi Sabriho ubytovny."
    scene bg sabri outside
    return
